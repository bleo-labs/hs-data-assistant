#!/usr/bin/env python3
"""Build deterministic evidence snapshots for the five retail demo tasks."""

from __future__ import annotations

import csv
import json
from collections import defaultdict
from decimal import Decimal
from pathlib import Path


DEMO_ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = DEMO_ROOT / "datasets" / "raw"
EVIDENCE_DIR = DEMO_ROOT / "tasks" / "evidence"


def read_rows(filename: str) -> list[dict[str, str]]:
    with (RAW_DIR / filename).open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def dec(value: str) -> Decimal:
    return Decimal(value)


def sum_decimal(rows: list[dict[str, str]], field: str) -> Decimal:
    return sum((dec(row[field]) for row in rows), Decimal(0))


def sum_integer(rows: list[dict[str, str]], field: str) -> int:
    return sum(int(row[field]) for row in rows)


def ratio(numerator: Decimal | int, denominator: Decimal | int) -> Decimal:
    if not denominator:
        return Decimal(0)
    return Decimal(numerator) / Decimal(denominator)


def growth(current: Decimal, prior: Decimal) -> Decimal:
    return ratio(current, prior) - Decimal(1)


def amount(value: Decimal) -> float:
    return float(value.quantize(Decimal("0.01")))


def rate(value: Decimal) -> float:
    return float(value.quantize(Decimal("0.000001")))


def comparison(rows, month_a, month_b, key_fn, value_field):
    values = defaultdict(lambda: [Decimal(0), Decimal(0)])
    for row in rows:
        if row["month"] not in {month_a, month_b}:
            continue
        slot = 0 if row["month"] == month_a else 1
        values[key_fn(row)][slot] += dec(row[value_field])
    return {
        key: {
            month_a: amount(prior),
            month_b: amount(current),
            "delta": amount(current - prior),
            "growth": rate(growth(current, prior)),
        }
        for key, (prior, current) in sorted(values.items())
    }


def main() -> None:
    traffic = read_rows("channel_traffic_funnel_monthly.csv")
    behavior = read_rows("product_behavior_funnel_monthly.csv")
    transactions = read_rows("order_transactions_monthly.csv")
    inventory = read_rows("product_inventory_monthly.csv")
    financial = read_rows("financial_results_monthly.csv")
    campaigns = read_rows("marketing_campaigns_monthly.csv")
    fulfillment = read_rows("fulfillment_monthly.csv")
    mappings = read_rows("dimension_mappings.csv")

    city_region = {
        row["child_value"]: row["parent_value"]
        for row in mappings
        if row["mapping_type"] == "区域-城市"
    }

    april_finance = [row for row in financial if row["month"] == "2026-04"]
    may_finance = [row for row in financial if row["month"] == "2026-05"]
    april_net = sum_decimal(april_finance, "net_sales")
    may_net = sum_decimal(may_finance, "net_sales")

    region_change = comparison(
        financial,
        "2026-04",
        "2026-05",
        lambda row: city_region[row["city"]],
        "net_sales",
    )
    category_change = comparison(
        financial,
        "2026-04",
        "2026-05",
        lambda row: row["category_l1"],
        "net_sales",
    )
    channel_change = comparison(
        financial,
        "2026-04",
        "2026-05",
        lambda row: row["sales_channel"],
        "net_sales",
    )
    region_category_change = comparison(
        financial,
        "2026-04",
        "2026-05",
        lambda row: f"{city_region[row['city']]} / {row['category_l1']}",
        "net_sales",
    )

    paid_app = [
        row
        for row in traffic
        if row["sales_channel"] == "自营App" and row["traffic_source"] == "付费投放"
    ]
    paid_app_month = {}
    for month in ("2026-04", "2026-05"):
        sample = [row for row in paid_app if row["month"] == month]
        visits = sum_integer(sample, "visit_users")
        details = sum_integer(sample, "product_detail_users")
        paid_app_month[month] = {
            "visit_users": visits,
            "product_detail_users": details,
            "visit_to_detail_rate": rate(ratio(details, visits)),
        }

    south_cities = {city for city, region in city_region.items() if region == "南区"}
    south_old_frequency = {}
    for month in ("2026-04", "2026-05"):
        sample = [
            row
            for row in transactions
            if row["month"] == month
            and row["city"] in south_cities
            and row["customer_type"] == "老客户"
        ]
        south_old_frequency[month] = rate(
            ratio(sum_integer(sample, "paid_orders"), sum_integer(sample, "paying_customers"))
        )

    case_01 = {
        "period": "2026-04 vs 2026-05",
        "net_sales": {
            "2026-04": amount(april_net),
            "2026-05": amount(may_net),
            "delta": amount(may_net - april_net),
            "growth": rate(growth(may_net, april_net)),
        },
        "region_change": region_change,
        "category_change": category_change,
        "channel_change": channel_change,
        "east_small_appliance": region_category_change["东区 / 小家电"],
        "paid_app_traffic": paid_app_month,
        "south_returning_purchase_frequency": south_old_frequency,
    }

    regions = sorted(set(city_region.values()))
    region_stats = {}
    for region in regions:
        cities = {city for city, mapped_region in city_region.items() if mapped_region == region}
        finance_2025_h1 = [
            row for row in financial if "2025-01" <= row["month"] <= "2025-06" and row["city"] in cities
        ]
        finance_2026_h1 = [
            row for row in financial if "2026-01" <= row["month"] <= "2026-06" and row["city"] in cities
        ]
        finance_period = [row for row in financial if row["month"] >= "2025-01" and row["city"] in cities]
        campaign_period = [row for row in campaigns if row["month"] >= "2025-01" and row["city"] in cities]
        transaction_period = [row for row in transactions if row["month"] >= "2025-01" and row["city"] in cities]
        fulfillment_period = [row for row in fulfillment if row["month"] >= "2025-01" and row["city"] in cities]

        h1_2025_net = sum_decimal(finance_2025_h1, "net_sales")
        h1_2026_net = sum_decimal(finance_2026_h1, "net_sales")
        net_sales = sum_decimal(finance_period, "net_sales")
        gmv = sum_decimal(finance_period, "gmv")
        refund_amount = sum_decimal(finance_period, "refund_amount")
        contribution_profit = sum_decimal(finance_period, "contribution_profit")
        attributable_new_customers = sum_integer(campaign_period, "attributable_new_paying_customers")
        attributable_marketing = sum_decimal(campaign_period, "marketing_expense")
        completed_orders = sum_integer(fulfillment_period, "completed_orders")
        on_time_orders = sum_integer(fulfillment_period, "on_time_completed_orders")
        old_rows = [row for row in transaction_period if row["customer_type"] == "老客户"]
        all_customers = sum_integer(transaction_period, "paying_customers")
        old_customers = sum_integer(old_rows, "paying_customers")

        region_stats[region] = {
            "net_sales_2025_to_2026_06": amount(net_sales),
            "h1_net_sales_growth": rate(growth(h1_2026_net, h1_2025_net)),
            "contribution_margin": rate(ratio(contribution_profit, net_sales)),
            "refund_rate": rate(ratio(refund_amount, gmv)),
            "new_customer_acquisition_cost": amount(ratio(attributable_marketing, attributable_new_customers)),
            "on_time_fulfillment_rate": rate(ratio(on_time_orders, completed_orders)),
            "returning_customer_share": rate(ratio(old_customers, all_customers)),
            "returning_purchase_frequency": rate(
                ratio(sum_integer(old_rows, "paid_orders"), old_customers)
            ),
        }

    case_02 = {
        "period": "2025-01 to 2026-06",
        "growth_comparison": "2026H1 vs 2025H1",
        "regions": region_stats,
    }

    q2_filter = lambda row: "2026-04" <= row["month"] <= "2026-06"
    q2_finance = [row for row in financial if q2_filter(row)]
    q2_traffic = [row for row in traffic if q2_filter(row)]
    q2_transactions = [row for row in transactions if q2_filter(row)]
    q2_campaigns = [row for row in campaigns if q2_filter(row)]
    q2_fulfillment = [row for row in fulfillment if q2_filter(row)]
    q2_inventory = [row for row in inventory if q2_filter(row)]

    q2_net = sum_decimal(q2_finance, "net_sales")
    q2_gmv = sum_decimal(q2_finance, "gmv")
    q2_refund = sum_decimal(q2_finance, "refund_amount")
    q2_cp = sum_decimal(q2_finance, "contribution_profit")
    q2_visits = sum_integer(q2_traffic, "visit_users")
    q2_details = sum_integer(q2_traffic, "product_detail_users")
    q2_paying = sum_integer(q2_traffic, "paying_customers")
    q2_orders = sum_integer(q2_transactions, "paid_orders")
    old_rows = [row for row in q2_transactions if row["customer_type"] == "老客户"]
    old_customers = sum_integer(old_rows, "paying_customers")
    old_orders = sum_integer(old_rows, "paid_orders")
    q2_aov = ratio(q2_gmv, q2_orders)
    q2_old_frequency = ratio(old_orders, old_customers)
    target_multiplier = Decimal("1.12")
    target_net = q2_net * target_multiplier
    required_old_frequency = ratio(
        Decimal(q2_orders) * target_multiplier - Decimal(q2_orders - old_orders),
        old_customers,
    )

    q2_completed = sum_integer(q2_fulfillment, "completed_orders")
    q2_on_time = sum_integer(q2_fulfillment, "on_time_completed_orders")
    q2_active_sku = sum_integer(q2_inventory, "active_flag")
    q2_in_stock_sku = sum_integer(q2_inventory, "in_stock_flag")
    q2_attributable_new = sum_integer(q2_campaigns, "attributable_new_paying_customers")
    q2_attributable_marketing = sum_decimal(q2_campaigns, "marketing_expense")

    case_03 = {
        "baseline_period": "2026Q2",
        "target_uplift": 0.12,
        "baseline_net_sales": amount(q2_net),
        "target_net_sales": amount(target_net),
        "target_gap": amount(target_net - q2_net),
        "baseline": {
            "visit_users": q2_visits,
            "visit_to_detail_rate": rate(ratio(q2_details, q2_visits)),
            "pay_per_detail_rate": rate(ratio(q2_paying, q2_details)),
            "purchase_frequency": rate(ratio(q2_orders, q2_paying)),
            "average_order_value": amount(q2_aov),
            "returning_purchase_frequency": rate(q2_old_frequency),
            "refund_rate": rate(ratio(q2_refund, q2_gmv)),
            "contribution_margin": rate(ratio(q2_cp, q2_net)),
            "on_time_fulfillment_rate": rate(ratio(q2_on_time, q2_completed)),
            "in_stock_rate": rate(ratio(q2_in_stock_sku, q2_active_sku)),
            "new_customer_acquisition_cost": amount(
                ratio(q2_attributable_marketing, q2_attributable_new)
            ),
        },
        "single_lever_pressure": {
            "traffic_only_visit_users": int(round(q2_visits * 1.12)),
            "conversion_only_pay_per_detail_rate": rate(
                ratio(q2_paying, q2_details) * target_multiplier
            ),
            "aov_only_average_order_value": amount(q2_aov * target_multiplier),
            "repeat_only_returning_purchase_frequency": rate(required_old_frequency),
            "repeat_only_uplift": rate(growth(required_old_frequency, q2_old_frequency)),
        },
        "balanced_path": {
            "visit_users_uplift": 0.03,
            "pay_per_detail_uplift": 0.03,
            "purchase_frequency_uplift": 0.03,
            "average_order_value_uplift": 0.025,
            "combined_uplift": rate(
                Decimal("1.03") * Decimal("1.03") * Decimal("1.03") * Decimal("1.025") - Decimal(1)
            ),
        },
    }

    evidence = {
        "metadata": {
            "demo_id": "demo-omnichannel-retail",
            "synthetic": True,
            "generator_seed": 20260718,
            "source_count": 8,
        },
        "case_01": case_01,
        "case_02": case_02,
        "case_03": case_03,
    }

    EVIDENCE_DIR.mkdir(parents=True, exist_ok=True)
    (EVIDENCE_DIR / "task_evidence.json").write_text(
        json.dumps(evidence, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    lines = [
        "# 演示任务证据快照",
        "",
        "> 本文件由八份虚构 Source 自动计算，不能手工修改。全部金额单位为元。",
        "",
        "## Case 01：2026 年 5 月净销售额下滑",
        "",
        f"- 净销售额：{april_net:,.2f} -> {may_net:,.2f}，变化 {may_net - april_net:,.2f}（{growth(may_net, april_net):.1%}）。",
        f"- 东区小家电：{Decimal(str(case_01['east_small_appliance']['2026-04'])):,.2f} -> {Decimal(str(case_01['east_small_appliance']['2026-05'])):,.2f}，变化 {Decimal(str(case_01['east_small_appliance']['delta'])):,.2f}。",
        f"- 自营 App 付费流量访问：{paid_app_month['2026-04']['visit_users']:,} -> {paid_app_month['2026-05']['visit_users']:,}；访问详情率 {Decimal(str(paid_app_month['2026-04']['visit_to_detail_rate'])):.1%} -> {Decimal(str(paid_app_month['2026-05']['visit_to_detail_rate'])):.1%}。",
        f"- 南区老客购买频次：{Decimal(str(south_old_frequency['2026-04'])):.3f} -> {Decimal(str(south_old_frequency['2026-05'])):.3f}。",
        "",
        "## Case 02：区域综合表现",
        "",
        "| 区域 | 18个月净销售额 | H1同比 | 贡献利润率 | 退款率 | 新客CAC | 准时履约率 | 老客占比 | 老客购买频次 |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for region, stats in region_stats.items():
        lines.append(
            f"| {region} | {stats['net_sales_2025_to_2026_06']:,.2f} | {stats['h1_net_sales_growth']:.1%} | "
            f"{stats['contribution_margin']:.1%} | {stats['refund_rate']:.1%} | {stats['new_customer_acquisition_cost']:,.2f} | "
            f"{stats['on_time_fulfillment_rate']:.1%} | {stats['returning_customer_share']:.1%} | {stats['returning_purchase_frequency']:.3f} |"
        )
    lines.extend([
        "",
        "## Case 03：目标压力测算",
        "",
        f"- 2026Q2 净销售额：{q2_net:,.2f}；+12% 目标：{target_net:,.2f}；缺口：{target_net - q2_net:,.2f}。",
        f"- 单靠流量：访问用户需从 {q2_visits:,} 增至 {int(round(q2_visits * 1.12)):,}。",
        f"- 单靠详情到支付效率：{ratio(q2_paying, q2_details):.2%} -> {ratio(q2_paying, q2_details) * target_multiplier:.2%}。",
        f"- 单靠客单价：{q2_aov:,.2f} -> {q2_aov * target_multiplier:,.2f}。",
        f"- 单靠老客购买频次：{q2_old_frequency:.3f} -> {required_old_frequency:.3f}（+{growth(required_old_frequency, q2_old_frequency):.1%}）。",
        "- 平衡路径：访问、详情到支付效率、购买频次各 +3%，客单价 +2.5%，乘积约 +12.0%。",
        f"- 质量护栏基线：退款率 {ratio(q2_refund, q2_gmv):.1%}，贡献利润率 {ratio(q2_cp, q2_net):.1%}，准时履约率 {ratio(q2_on_time, q2_completed):.1%}。",
        "",
    ])
    (EVIDENCE_DIR / "task_evidence.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {EVIDENCE_DIR / 'task_evidence.json'}")
    print(f"Wrote {EVIDENCE_DIR / 'task_evidence.md'}")


if __name__ == "__main__":
    main()
