#!/usr/bin/env python3
"""Independently validate closure and scenario signals in the retail demo."""

from __future__ import annotations

import csv
import sys
from collections import defaultdict
from decimal import Decimal
from pathlib import Path


DEMO_ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = DEMO_ROOT / "datasets" / "raw"
AUDIT_DIR = DEMO_ROOT / "datasets" / "audit"

FILES = {
    "SRC-0001": "channel_traffic_funnel_monthly.csv",
    "SRC-0002": "product_behavior_funnel_monthly.csv",
    "SRC-0003": "order_transactions_monthly.csv",
    "SRC-0004": "product_inventory_monthly.csv",
    "SRC-0005": "financial_results_monthly.csv",
    "SRC-0006": "marketing_campaigns_monthly.csv",
    "SRC-0007": "fulfillment_monthly.csv",
    "SRC-0008": "dimension_mappings.csv",
}

KEYS = {
    "SRC-0001": ["month", "city", "sales_channel", "traffic_source", "customer_type"],
    "SRC-0002": ["month", "city", "sales_channel", "category_l1", "customer_type"],
    "SRC-0003": ["month", "city", "sales_channel", "category_l1", "category_l2", "customer_type", "promotion_type"],
    "SRC-0004": ["month", "city", "warehouse", "sku"],
    "SRC-0005": ["month", "city", "sales_channel", "category_l1"],
    "SRC-0006": ["month", "city", "sales_channel", "traffic_source", "campaign"],
    "SRC-0007": ["month", "city", "warehouse", "category_l1"],
    "SRC-0008": ["mapping_type", "parent_value", "child_value", "effective_start", "effective_end"],
}

AMOUNT_FIELDS = {
    "SRC-0003": ["gmv", "refund_amount"],
    "SRC-0005": ["gmv", "refund_amount", "net_sales", "cogs", "gross_profit", "marketing_expense", "fulfillment_expense", "channel_fee", "contribution_profit"],
    "SRC-0006": ["marketing_expense", "attributable_net_sales"],
}

COUNT_FIELDS = {
    "SRC-0001": ["visit_users", "product_detail_users", "paying_customers"],
    "SRC-0002": ["product_detail_users", "add_to_cart_users", "order_submit_users", "paying_customers"],
    "SRC-0003": ["paying_customers", "paid_orders", "units_sold"],
    "SRC-0004": ["active_flag", "in_stock_flag", "opening_inventory_units", "inbound_units", "units_sold", "ending_inventory_units"],
    "SRC-0006": ["attributable_visit_users", "attributable_new_paying_customers"],
    "SRC-0007": ["completed_orders", "on_time_completed_orders", "canceled_orders"],
}


def read_rows(source_id: str):
    path = RAW_DIR / FILES[source_id]
    if not path.exists():
        raise AssertionError(f"missing {path.relative_to(DEMO_ROOT)}")
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def dec(value: str) -> Decimal:
    return Decimal(value)


def key(row, fields):
    return tuple(row[field] for field in fields)


def sum_by(rows, group_fields, value_field, caster=int):
    result = defaultdict(lambda: Decimal(0) if caster is dec else 0)
    for row in rows:
        result[key(row, group_fields)] += caster(row[value_field])
    return result


class Audit:
    def __init__(self):
        self.items = []

    def check(self, name, condition, evidence, impact="主数据闭合", warning=False):
        status = "pass" if condition else ("warning" if warning else "fail")
        self.items.append((name, status, evidence, impact, "无需处理" if condition else "返回生成规则修正"))

    def equal_maps(self, name, left, right, impact):
        differing = sorted(set(left) | set(right))
        bad = [item for item in differing if left.get(item, 0) != right.get(item, 0)]
        self.check(name, not bad, f"比较键 {len(differing)} 个；差异键 {len(bad)} 个" + (f"；首个 {bad[0]}" if bad else ""), impact)

    def write(self, row_counts):
        AUDIT_DIR.mkdir(parents=True, exist_ok=True)
        lines = [
            "# 合成数据生成审计",
            "",
            "> 全部数据均为虚构演示数据。本报告由独立审计脚本从 CSV 基础字段重新计算。",
            "",
            "## 数据规模",
            "",
            "| Source | 行数 |",
            "|---|---:|",
        ]
        lines.extend(f"| `{source_id}` | {count:,} |" for source_id, count in row_counts.items())
        lines.extend([
            "",
            "## 审计结果",
            "",
            "| 检查项 | 结果 | 证据 | 影响 | 处置 |",
            "|---|---|---|---|---|",
        ])
        for item in self.items:
            lines.append("| " + " | ".join(str(value).replace("|", "\\|") for value in item) + " |")
        failures = sum(1 for _, status, *_ in self.items if status == "fail")
        warnings = sum(1 for _, status, *_ in self.items if status == "warning")
        lines.extend([
            "",
            "## 发布状态",
            "",
            f"- fail: {failures}",
            f"- warning: {warnings}",
            f"- release_ready: {'yes' if failures == 0 else 'no'}",
            "",
            "正常 Source 卡只能在 `release_ready: yes` 后创建。",
        ])
        (AUDIT_DIR / "data_generation_audit.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
        return failures


def main():
    rows = {source_id: read_rows(source_id) for source_id in FILES}
    audit = Audit()

    for source_id, source_rows in rows.items():
        keys = [key(row, KEYS[source_id]) for row in source_rows]
        audit.check(f"{source_id} 唯一键", len(keys) == len(set(keys)), f"{len(keys):,} 行，重复 {len(keys)-len(set(keys))} 行")
        numeric_fields = COUNT_FIELDS.get(source_id, []) + AMOUNT_FIELDS.get(source_id, [])
        negative = sum(1 for row in source_rows for field in numeric_fields if dec(row[field]) < 0)
        # Contribution profit is allowed to be negative at a detailed grain.
        if source_id == "SRC-0005":
            negative -= sum(1 for row in source_rows if dec(row["contribution_profit"]) < 0)
        audit.check(f"{source_id} 基础值非负", negative == 0, f"发现不允许的负值 {negative} 个")

    bad_funnel1 = [row for row in rows["SRC-0001"] if not (int(row["visit_users"]) >= int(row["product_detail_users"]) >= int(row["paying_customers"]))]
    bad_funnel2 = [row for row in rows["SRC-0002"] if not (int(row["product_detail_users"]) >= int(row["add_to_cart_users"]) >= int(row["order_submit_users"]) >= int(row["paying_customers"]))]
    audit.check("渠道漏斗逐层不增", not bad_funnel1, f"异常行 {len(bad_funnel1)}")
    audit.check("商品漏斗逐层不增", not bad_funnel2, f"异常行 {len(bad_funnel2)}")

    group12 = ["month", "city", "sales_channel", "customer_type"]
    for field in ("product_detail_users", "paying_customers"):
        audit.equal_maps(
            f"SRC-0001 与 SRC-0002 的 {field} 闭合",
            sum_by(rows["SRC-0001"], group12, field),
            sum_by(rows["SRC-0002"], group12, field),
            "渠道与品类漏斗共享同一用户底数",
        )

    group23 = ["month", "city", "sales_channel", "category_l1", "customer_type"]
    audit.equal_maps(
        "SRC-0002 与 SRC-0003 的支付客户闭合",
        sum_by(rows["SRC-0002"], group23, "paying_customers"),
        sum_by(rows["SRC-0003"], group23, "paying_customers"),
        "支付客户按主品类和主促销归因",
    )

    mappings = rows["SRC-0008"]
    sku_map = []
    for row in mappings:
        if row["mapping_type"] == "二级类目-SKU":
            sku_map.append(row)

    def active_l2(sku, month):
        point = f"{month}-01"
        valid = [row for row in sku_map if row["child_value"] == sku and row["effective_start"] <= point and (not row["effective_end"] or point <= row["effective_end"])]
        if len(valid) != 1:
            raise AssertionError(f"invalid effective mapping for {sku} at {month}")
        return valid[0]["parent_value"]

    tx_units = sum_by(rows["SRC-0003"], ["month", "city", "category_l2"], "units_sold")
    inv_units = defaultdict(int)
    for row in rows["SRC-0004"]:
        inv_units[(row["month"], row["city"], active_l2(row["sku"], row["month"]))] += int(row["units_sold"])
    audit.equal_maps("交易与库存销售件数闭合", tx_units, inv_units, "库存与交易引用同一 SKU 销售底数")

    inventory_bad = [row for row in rows["SRC-0004"] if int(row["ending_inventory_units"]) != int(row["opening_inventory_units"]) + int(row["inbound_units"]) - int(row["units_sold"])]
    audit.check("库存流转公式闭合", not inventory_bad, f"异常行 {len(inventory_bad)}")

    group35 = ["month", "city", "sales_channel", "category_l1"]
    for field in ("gmv", "refund_amount"):
        audit.equal_maps(
            f"交易与财务的 {field} 闭合",
            sum_by(rows["SRC-0003"], group35, field, dec),
            sum_by(rows["SRC-0005"], group35, field, dec),
            "财务聚合必须逐分回算交易",
        )
    financial_bad = []
    for row in rows["SRC-0005"]:
        if dec(row["net_sales"]) != dec(row["gmv"]) - dec(row["refund_amount"]):
            financial_bad.append(row)
        if dec(row["gross_profit"]) != dec(row["net_sales"]) - dec(row["cogs"]):
            financial_bad.append(row)
        expected_cp = dec(row["gross_profit"]) - dec(row["marketing_expense"]) - dec(row["fulfillment_expense"]) - dec(row["channel_fee"])
        if dec(row["contribution_profit"]) != expected_cp:
            financial_bad.append(row)
    audit.check("财务派生结果逐分回算", not financial_bad, f"异常记录 {len(financial_bad)}")

    tx_orders = sum_by(rows["SRC-0003"], ["month", "city", "category_l1"], "paid_orders")
    fulfillment_orders = defaultdict(int)
    fulfillment_bad = []
    for row in rows["SRC-0007"]:
        completed = int(row["completed_orders"])
        canceled = int(row["canceled_orders"])
        on_time = int(row["on_time_completed_orders"])
        fulfillment_orders[(row["month"], row["city"], row["category_l1"])] += completed + canceled
        if on_time > completed:
            fulfillment_bad.append(row)
    audit.equal_maps("交易与履约订单闭合", tx_orders, fulfillment_orders, "支付订单等于完成加取消")
    audit.check("准时订单分母合法", not fulfillment_bad, f"准时数大于完成数的记录 {len(fulfillment_bad)}")

    finance_marketing = sum_by(rows["SRC-0005"], ["month", "city", "sales_channel"], "marketing_expense", dec)
    campaign_marketing = sum_by(rows["SRC-0006"], ["month", "city", "sales_channel"], "marketing_expense", dec)
    marketing_bad = [item for item, value in campaign_marketing.items() if value > finance_marketing[item]]
    audit.check("可归因投放费用不超过财务营销费用", not marketing_bad, f"异常组合 {len(marketing_bad)}")

    # Scenario signal checks.
    south_cities = {"南浦市", "榕川市"}
    north_cities = {"北辰市", "云岭市"}
    east_cities = {"东澜市", "海岳市"}

    def orders_per_customer(months, cities, customer_type):
        sample = [row for row in rows["SRC-0003"] if row["month"] in months and row["city"] in cities and row["customer_type"] == customer_type]
        customers = sum(int(row["paying_customers"]) for row in sample)
        return Decimal(sum(int(row["paid_orders"]) for row in sample)) / Decimal(customers)

    south_pre_frequency = orders_per_customer({"2024-10", "2024-11", "2024-12", "2025-01", "2025-02"}, south_cities, "老客户")
    south_post_frequency = orders_per_customer({"2025-08", "2025-09", "2025-10", "2025-11", "2025-12"}, south_cities, "老客户")
    audit.check("FACT-0001 南区老客运营改善", south_post_frequency > south_pre_frequency, f"老客频次 {south_pre_frequency:.3f}->{south_post_frequency:.3f}", "持续经营机制")

    def in_stock_rate_for(months, cities, sku_prefix=None):
        sample = [row for row in rows["SRC-0004"] if row["month"] in months and row["city"] in cities and (not sku_prefix or row["sku"].startswith(sku_prefix))]
        return Decimal(sum(int(row["in_stock_flag"]) for row in sample)) / Decimal(sum(int(row["active_flag"]) for row in sample))

    def on_time_rate_for(months, cities):
        sample = [row for row in rows["SRC-0007"] if row["month"] in months and row["city"] in cities]
        completed = sum(int(row["completed_orders"]) for row in sample)
        return Decimal(sum(int(row["on_time_completed_orders"]) for row in sample)) / Decimal(completed)

    east_pre_stock = in_stock_rate_for({"2025-03", "2025-04", "2025-05"}, east_cities)
    east_post_stock = in_stock_rate_for({"2025-07", "2025-08", "2025-09"}, east_cities)
    east_pre_ot = on_time_rate_for({"2025-03", "2025-04", "2025-05"}, east_cities)
    east_post_ot = on_time_rate_for({"2025-07", "2025-08", "2025-09"}, east_cities)
    audit.check("FACT-0002 东区仓扩容改善", east_post_stock > east_pre_stock and east_post_ot > east_pre_ot, f"有货率 {east_pre_stock:.1%}->{east_post_stock:.1%}；准时率 {east_pre_ot:.1%}->{east_post_ot:.1%}", "持续供给与履约改善")

    def small_appliance_asp(month):
        sample = [row for row in rows["SRC-0003"] if row["month"] == month and row["category_l1"] == "小家电"]
        return sum(dec(row["gmv"]) for row in sample) / Decimal(sum(int(row["units_sold"]) for row in sample))

    def small_appliance_cart_rate(month):
        sample = [row for row in rows["SRC-0002"] if row["month"] == month and row["category_l1"] == "小家电"]
        return Decimal(sum(int(row["add_to_cart_users"]) for row in sample)) / Decimal(sum(int(row["product_detail_users"]) for row in sample))

    aug_asp, sep_asp = small_appliance_asp("2025-08"), small_appliance_asp("2025-09")
    aug_cart, sep_cart = small_appliance_cart_rate("2025-08"), small_appliance_cart_rate("2025-09")
    audit.check("FACT-0003 小家电提价", sep_asp > aug_asp and sep_cart < aug_cart, f"均价 {aug_asp:.2f}->{sep_asp:.2f}；详情加购率 {aug_cart:.1%}->{sep_cart:.1%}", "价格实验")

    def monthly_finance(month):
        sample = [row for row in rows["SRC-0005"] if row["month"] == month]
        gmv = sum(dec(row["gmv"]) for row in sample)
        net = sum(dec(row["net_sales"]) for row in sample)
        refund = sum(dec(row["refund_amount"]) for row in sample)
        gross = sum(dec(row["gross_profit"]) for row in sample)
        return gmv, refund / gmv, gross / net

    oct_fin, nov_fin = monthly_finance("2025-10"), monthly_finance("2025-11")
    audit.check("FACT-0004 全渠道大促", nov_fin[0] > oct_fin[0] and nov_fin[1] > oct_fin[1] and nov_fin[2] < oct_fin[2], f"GMV {oct_fin[0]:,.0f}->{nov_fin[0]:,.0f}；退款率 {oct_fin[1]:.1%}->{nov_fin[1]:.1%}；毛利率 {oct_fin[2]:.1%}->{nov_fin[2]:.1%}", "短期活动")

    remap_rows = [row for row in rows["SRC-0008"] if row["child_value"] == "AP-LIFE-08" and row["mapping_type"] == "二级类目-SKU"]
    audit.check("FACT-0005 SKU 跨期归属调整", len(remap_rows) == 2 and {row["parent_value"] for row in remap_rows} == {"生活电器", "厨房小电"}, f"有效期映射记录 {len(remap_rows)} 条", "口径变化")

    finance_month = sum_by(rows["SRC-0005"], ["month"], "net_sales", dec)
    audit.check("Case01 2026-05 净销售额环比下降", finance_month[("2026-05",)] < finance_month[("2026-04",)], f"4月 {finance_month[('2026-04',)]:,.2f}；5月 {finance_month[('2026-05',)]:,.2f}", "预设标准答案")

    east_small = sum_by([row for row in rows["SRC-0005"] if row["city"] in east_cities and row["category_l1"] == "小家电"], ["month"], "net_sales", dec)
    audit.check("FACT-0007 东区小家电供给冲击", east_small[("2026-05",)] < east_small[("2026-04",)] * Decimal("0.5"), f"4月 {east_small[('2026-04',)]:,.2f}；5月 {east_small[('2026-05',)]:,.2f}", "Case01 主因")

    paid_app = [row for row in rows["SRC-0001"] if row["sales_channel"] == "自营App" and row["traffic_source"] == "付费投放"]
    paid_visits = sum_by(paid_app, ["month"], "visit_users")
    paid_details = sum_by(paid_app, ["month"], "product_detail_users")
    april_rate = Decimal(paid_details[("2026-04",)]) / Decimal(paid_visits[("2026-04",)])
    may_rate = Decimal(paid_details[("2026-05",)]) / Decimal(paid_visits[("2026-05",)])
    audit.check("FACT-0008 App 付费流量增量低意向", paid_visits[("2026-05",)] > paid_visits[("2026-04",)] and may_rate < april_rate, f"访问 {paid_visits[('2026-04',)]:,}->{paid_visits[('2026-05',)]:,}；访问详情率 {april_rate:.1%}->{may_rate:.1%}", "Case01 次因")

    stock_rows = rows["SRC-0004"]
    def in_stock_rate(month, cities=None, sku_prefix=None):
        sample = [row for row in stock_rows if row["month"] == month and (not cities or row["city"] in cities) and (not sku_prefix or row["sku"].startswith(sku_prefix))]
        return Decimal(sum(int(row["in_stock_flag"]) for row in sample)) / Decimal(len(sample))
    march_stock = in_stock_rate("2026-03", east_cities, "AP-")
    may_stock = in_stock_rate("2026-05", east_cities, "AP-")
    june_stock = in_stock_rate("2026-06", east_cities, "AP-")
    audit.check("FACT-0009 小家电补货恢复", may_stock < march_stock and june_stock > may_stock, f"3月 {march_stock:.1%}；5月 {may_stock:.1%}；6月 {june_stock:.1%}", "供给冲击与恢复")

    on_time = rows["SRC-0007"]
    def on_time_rate(month, cities):
        sample = [row for row in on_time if row["month"] == month and row["city"] in cities]
        completed = sum(int(row["completed_orders"]) for row in sample)
        return Decimal(sum(int(row["on_time_completed_orders"]) for row in sample)) / Decimal(completed)
    feb_ot = on_time_rate("2026-02", east_cities)
    mar_ot = on_time_rate("2026-03", east_cities)
    apr_ot = on_time_rate("2026-04", east_cities)
    audit.check("FACT-0006 东区履约系统切换", mar_ot < feb_ot and apr_ot > mar_ot, f"2月 {feb_ot:.1%}；3月 {mar_ot:.1%}；4月 {apr_ot:.1%}", "短期事件信号")

    # Case02 checks the intended ranking dimensions without collapsing them into one score.
    regions = {"北区": north_cities, "东区": east_cities, "南区": south_cities}
    region_stats = {}
    for region, cities in regions.items():
        finance_sample = [row for row in rows["SRC-0005"] if row["month"] >= "2025-01" and row["city"] in cities]
        campaign_sample = [row for row in rows["SRC-0006"] if row["month"] >= "2025-01" and row["city"] in cities]
        net = sum(dec(row["net_sales"]) for row in finance_sample)
        gmv = sum(dec(row["gmv"]) for row in finance_sample)
        refund = sum(dec(row["refund_amount"]) for row in finance_sample)
        cp = sum(dec(row["contribution_profit"]) for row in finance_sample)
        spend = sum(dec(row["marketing_expense"]) for row in campaign_sample)
        new_pay = sum(int(row["attributable_new_paying_customers"]) for row in campaign_sample)
        region_stats[region] = {"net": net, "refund_rate": refund / gmv, "cp_margin": cp / net, "cac": spend / Decimal(new_pay)}
    ranking_ok = (
        region_stats["东区"]["net"] == max(value["net"] for value in region_stats.values())
        and region_stats["南区"]["cp_margin"] == max(value["cp_margin"] for value in region_stats.values())
        and region_stats["北区"]["cac"] == min(value["cac"] for value in region_stats.values())
        and region_stats["北区"]["refund_rate"] == max(value["refund_rate"] for value in region_stats.values())
    )
    audit.check("Case02 区域差异信号", ranking_ok, "东区规模最大；南区贡献利润率最高；北区 CAC 最低但退款率最高", "预设标准答案")

    failures = audit.write({source_id: len(source_rows) for source_id, source_rows in rows.items()})
    report = AUDIT_DIR / "data_generation_audit.md"
    print(report.relative_to(DEMO_ROOT))
    print(f"checks={len(audit.items)} failures={failures}")
    if failures:
        sys.exit(1)


if __name__ == "__main__":
    main()
