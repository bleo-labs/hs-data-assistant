#!/usr/bin/env python3
"""Generate reproducible, internally closed synthetic retail demo data."""

from __future__ import annotations

import csv
import hashlib
import math
import shutil
from collections import defaultdict
from datetime import date
from pathlib import Path


SEED = 20260718
DEMO_ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = DEMO_ROOT / "datasets" / "raw"
BAD_DIR = DEMO_ROOT / "datasets" / "bad_samples"

MONTHS = [f"{year}-{month:02d}" for year in (2024, 2025, 2026) for month in range(1, 13)]
MONTHS = [m for m in MONTHS if "2024-01" <= m <= "2026-06"]

CITIES = {
    "北辰市": ("北区", "北区仓", 0.92),
    "云岭市": ("北区", "北区仓", 0.78),
    "东澜市": ("东区", "东区仓", 1.30),
    "海岳市": ("东区", "东区仓", 1.12),
    "南浦市": ("南区", "南区仓", 1.04),
    "榕川市": ("南区", "南区仓", 0.88),
}

CHANNELS = ["自营App", "自营小程序", "第三方平台"]
SOURCES_BY_CHANNEL = {
    "自营App": ["自然流量", "付费投放", "私域触达", "内容合作"],
    "自营小程序": ["自然流量", "付费投放", "私域触达"],
    "第三方平台": ["自然流量", "付费投放", "内容合作"],
}
CUSTOMER_TYPES = ["新客户", "老客户"]
CATEGORIES = {
    "厨房用品": ["烹饪器具", "餐厨工具"],
    "收纳用品": ["衣物收纳", "空间整理"],
    "清洁用品": ["清洁工具", "家居耗材"],
    "小家电": ["厨房小电", "生活电器"],
}
PROMOTIONS = ["无促销", "优惠券", "平台大促", "会员优惠"]

SKU_PREFIX = {
    "烹饪器具": "KIT-COOK",
    "餐厨工具": "KIT-TOOLS",
    "衣物收纳": "STO-CLOTH",
    "空间整理": "STO-SPACE",
    "清洁工具": "CLN-TOOLS",
    "家居耗材": "CLN-CONSUM",
    "厨房小电": "AP-KITCH",
    "生活电器": "AP-LIFE",
}

BASE_PRICE_CENTS = {
    "烹饪器具": 6900,
    "餐厨工具": 3300,
    "衣物收纳": 4200,
    "空间整理": 5600,
    "清洁工具": 3800,
    "家居耗材": 2500,
    "厨房小电": 21900,
    "生活电器": 16900,
}

COST_RATES = {
    "厨房用品": 0.58,
    "收纳用品": 0.52,
    "清洁用品": 0.55,
    "小家电": 0.66,
}


def stable_unit(*parts: object) -> float:
    payload = "|".join(str(p) for p in (SEED, *parts)).encode("utf-8")
    digest = hashlib.sha256(payload).digest()
    return int.from_bytes(digest[:8], "big") / float(2**64 - 1)


def noise(amplitude: float, *parts: object) -> float:
    return 1.0 + (stable_unit(*parts) * 2.0 - 1.0) * amplitude


def month_index(month: str) -> int:
    return MONTHS.index(month)


def seasonality(month: str) -> float:
    month_num = int(month[-2:])
    return {
        1: 0.90,
        2: 0.82,
        3: 1.02,
        4: 1.00,
        5: 1.04,
        6: 1.02,
        7: 1.00,
        8: 1.03,
        9: 1.05,
        10: 1.08,
        11: 1.32,
        12: 1.15,
    }[month_num]


def allocate_integer(total: int, weighted_keys, capacities=None):
    """Largest-remainder allocation with optional integer capacities."""
    keys = [key for key, _ in weighted_keys]
    weights = {key: max(float(weight), 0.0) for key, weight in weighted_keys}
    capacities = capacities or {key: total for key in keys}
    if total < 0 or total > sum(capacities.get(key, total) for key in keys):
        raise ValueError("allocation target exceeds capacity")
    weight_sum = sum(weights.values()) or float(len(keys))
    raw = {key: total * (weights[key] if sum(weights.values()) else 1.0) / weight_sum for key in keys}
    result = {key: min(int(math.floor(raw[key])), capacities.get(key, total)) for key in keys}
    remaining = total - sum(result.values())
    order = sorted(keys, key=lambda key: (raw[key] - math.floor(raw[key]), stable_unit("alloc", key)), reverse=True)
    while remaining:
        progressed = False
        for key in order:
            if result[key] < capacities.get(key, total):
                result[key] += 1
                remaining -= 1
                progressed = True
                if not remaining:
                    break
        if not progressed:
            raise ValueError("allocation could not satisfy target")
    return result


def money(cents: int) -> str:
    return f"{cents / 100:.2f}"


def write_csv(path: Path, fieldnames, rows) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def sku_catalog():
    rows = []
    for category, subcategories in CATEGORIES.items():
        for subcategory in subcategories:
            for index in range(1, 9):
                rows.append({
                    "category_l1": category,
                    "category_l2": subcategory,
                    "sku": f"{SKU_PREFIX[subcategory]}-{index:02d}",
                })
    return rows


def effective_l2(sku: str, month: str) -> str:
    if sku == "AP-LIFE-08" and month >= "2026-01":
        return "厨房小电"
    for row in sku_catalog():
        if row["sku"] == sku:
            return row["category_l2"]
    raise KeyError(sku)


def category_for_l2(category_l2: str) -> str:
    return next(category for category, values in CATEGORIES.items() if category_l2 in values)


def availability(month: str, city: str, sku: str) -> int:
    region = CITIES[city][0]
    category = category_for_l2(effective_l2(sku, month))
    if region == "东区" and category == "小家电" and month in {"2026-04", "2026-05"}:
        return 0 if int(sku[-2:]) in {1, 2, 3, 4} else 1
    if stable_unit("stockout", month, city, sku) < 0.025:
        return 0
    return 1


def generate():
    if RAW_DIR.exists():
        shutil.rmtree(RAW_DIR)
    if BAD_DIR.exists():
        shutil.rmtree(BAD_DIR)
    RAW_DIR.mkdir(parents=True)
    BAD_DIR.mkdir(parents=True)

    source1 = []
    source1_index = {}
    source2 = []
    source2_pay = {}

    source_share = {
        "自然流量": 0.43,
        "付费投放": 0.28,
        "私域触达": 0.18,
        "内容合作": 0.11,
    }
    source_detail_rate = {
        "自然流量": 0.64,
        "付费投放": 0.48,
        "私域触达": 0.68,
        "内容合作": 0.57,
    }
    channel_factor = {"自营App": 1.00, "自营小程序": 0.67, "第三方平台": 0.54}

    # SRC-0001 starts the authoritative user chain.
    for month in MONTHS:
        trend = 1.0 + month_index(month) * 0.009
        for city, (region, _, city_factor) in CITIES.items():
            for channel in CHANNELS:
                allowed_sources = SOURCES_BY_CHANNEL[channel]
                normalizer = sum(source_share[source] for source in allowed_sources)
                for customer_type in CUSTOMER_TYPES:
                    customer_factor = 1.0 if customer_type == "新客户" else 0.72
                    if region == "南区" and customer_type == "老客户" and month >= "2025-03":
                        months_since = month_index(month) - month_index("2025-03")
                        customer_factor *= 1.0 + min(0.22, 0.012 * (months_since + 1))
                    total_visits = round(
                        23500 * city_factor * channel_factor[channel] * customer_factor
                        * trend * seasonality(month) * noise(0.035, "visits", month, city, channel, customer_type)
                    )
                    allocations = allocate_integer(
                        total_visits,
                        [(source, source_share[source] / normalizer) for source in allowed_sources],
                    )
                    if month == "2026-05" and channel == "自营App":
                        paid_base = allocations.get("付费投放", 0)
                        extra = round(paid_base * 0.58)
                        allocations["付费投放"] += extra
                    for source in allowed_sources:
                        visits = allocations[source]
                        detail_rate = source_detail_rate[source]
                        if customer_type == "老客户":
                            detail_rate += 0.04
                        if month == "2026-05" and channel == "自营App" and source == "付费投放":
                            detail_rate *= 0.42
                        detail_users = min(visits, round(visits * detail_rate * noise(0.025, "detail", month, city, channel, source, customer_type)))
                        row = {
                            "month": month,
                            "city": city,
                            "sales_channel": channel,
                            "traffic_source": source,
                            "customer_type": customer_type,
                            "visit_users": visits,
                            "product_detail_users": detail_users,
                            "paying_customers": 0,
                        }
                        source1_index[(month, city, channel, customer_type, source)] = row
                        source1.append(row)

    # SRC-0002 inherits the same detail users and adds one primary browsing category.
    category_weights = {"厨房用品": 0.28, "收纳用品": 0.24, "清洁用品": 0.25, "小家电": 0.23}
    category_cart_rate = {"厨房用品": 0.35, "收纳用品": 0.32, "清洁用品": 0.37, "小家电": 0.29}
    for month in MONTHS:
        for city, (region, _, _) in CITIES.items():
            for channel in CHANNELS:
                for customer_type in CUSTOMER_TYPES:
                    source_rows = [source1_index[(month, city, channel, customer_type, source)] for source in SOURCES_BY_CHANNEL[channel]]
                    detail_total = sum(int(row["product_detail_users"]) for row in source_rows)
                    weights = []
                    for category, weight in category_weights.items():
                        adjusted = weight
                        weights.append((category, adjusted))
                    detail_by_category = allocate_integer(detail_total, weights)
                    total_pay = 0
                    for category in CATEGORIES:
                        details = detail_by_category[category]
                        cart_rate = category_cart_rate[category]
                        if customer_type == "老客户":
                            cart_rate += 0.035
                        if category == "小家电" and month >= "2025-09":
                            cart_rate *= 0.94
                        if region == "东区" and category == "小家电" and month == "2026-04":
                            cart_rate *= 0.55
                        if region == "东区" and category == "小家电" and month == "2026-05":
                            cart_rate *= 0.08
                        cart = min(details, round(details * cart_rate * noise(0.025, "cart", month, city, channel, category, customer_type)))
                        submit = min(cart, round(cart * 0.69 * noise(0.018, "submit", month, city, channel, category, customer_type)))
                        pay_rate = 0.75 if customer_type == "老客户" else 0.68
                        pay = min(submit, round(submit * pay_rate * noise(0.018, "pay", month, city, channel, category, customer_type)))
                        total_pay += pay
                        source2_pay[(month, city, channel, category, customer_type)] = pay
                        source2.append({
                            "month": month,
                            "city": city,
                            "sales_channel": channel,
                            "category_l1": category,
                            "customer_type": customer_type,
                            "product_detail_users": details,
                            "add_to_cart_users": cart,
                            "order_submit_users": submit,
                            "paying_customers": pay,
                        })
                    pay_alloc = allocate_integer(
                        total_pay,
                        [(row["traffic_source"], int(row["product_detail_users"]) * ({"自然流量": 1.0, "付费投放": 0.72, "私域触达": 1.18, "内容合作": 0.88}[row["traffic_source"]])) for row in source_rows],
                        {row["traffic_source"]: int(row["product_detail_users"]) for row in source_rows},
                    )
                    for row in source_rows:
                        row["paying_customers"] = pay_alloc[row["traffic_source"]]

    # Availability is decided before transaction units are allocated to SKUs.
    sku_rows = sku_catalog()
    available_skus = defaultdict(list)
    for month in MONTHS:
        for city in CITIES:
            for sku_row in sku_rows:
                sku = sku_row["sku"]
                if availability(month, city, sku):
                    available_skus[(month, city, effective_l2(sku, month))].append(sku)

    source3 = []
    tx_totals = defaultdict(lambda: defaultdict(int))
    units_by_l2 = defaultdict(int)
    promo_weights_default = {"无促销": 0.61, "优惠券": 0.18, "平台大促": 0.10, "会员优惠": 0.11}
    for month in MONTHS:
        for city, (region, _, _) in CITIES.items():
            for channel in CHANNELS:
                for category, l2_values in CATEGORIES.items():
                    for customer_type in CUSTOMER_TYPES:
                        paying = source2_pay[(month, city, channel, category, customer_type)]
                        active_l2 = list(l2_values)
                        combo_weights = []
                        for l2 in active_l2:
                            l2_weight = 0.53 if l2 == active_l2[0] else 0.47
                            for promo in PROMOTIONS:
                                promo_weight = promo_weights_default[promo]
                                if month == "2025-11":
                                    promo_weight = {"无促销": 0.28, "优惠券": 0.20, "平台大促": 0.40, "会员优惠": 0.12}[promo]
                                if customer_type == "老客户" and promo == "会员优惠":
                                    promo_weight *= 1.65
                                combo_weights.append(((l2, promo), l2_weight * promo_weight))
                        allocated = allocate_integer(paying, combo_weights)
                        for (l2, promo), customers in allocated.items():
                            frequency = 1.10 if customer_type == "新客户" else 1.31
                            if region == "南区" and customer_type == "老客户" and month >= "2025-03":
                                frequency *= 1.0 + min(0.17, 0.009 * (month_index(month) - month_index("2025-03") + 1))
                            orders = max(customers, round(customers * frequency * noise(0.018, "orders", month, city, channel, l2, customer_type, promo)))
                            items_per_order = {"厨房用品": 1.42, "收纳用品": 1.55, "清洁用品": 1.68, "小家电": 1.12}[category]
                            units = max(orders, round(orders * items_per_order * noise(0.018, "units", month, city, channel, l2, customer_type, promo)))
                            price = BASE_PRICE_CENTS[l2]
                            price = round(price * {"自营App": 1.00, "自营小程序": 0.98, "第三方平台": 1.03}[channel])
                            if category == "小家电" and month >= "2025-09":
                                price = round(price * 1.09)
                            promo_factor = {"无促销": 1.00, "优惠券": 0.93, "平台大促": 0.84, "会员优惠": 0.91}[promo]
                            price = max(100, round(price * promo_factor * noise(0.012, "price", month, city, channel, l2, promo)))
                            gmv_cents = units * price
                            refund_rate = {"厨房用品": 0.052, "收纳用品": 0.061, "清洁用品": 0.043, "小家电": 0.082}[category]
                            if region == "北区":
                                refund_rate *= 1.20
                            if month == "2025-11":
                                refund_rate *= 1.48
                            refund_cents = round(gmv_cents * refund_rate * noise(0.035, "refund", month, city, channel, l2, promo))
                            base_price = BASE_PRICE_CENTS[l2]
                            cogs_cents = round(units * base_price * COST_RATES[category] * noise(0.012, "cogs", month, city, l2))
                            row = {
                                "month": month,
                                "city": city,
                                "sales_channel": channel,
                                "category_l1": category,
                                "category_l2": l2,
                                "customer_type": customer_type,
                                "promotion_type": promo,
                                "paying_customers": customers,
                                "paid_orders": orders,
                                "units_sold": units,
                                "gmv": money(gmv_cents),
                                "refund_amount": money(refund_cents),
                            }
                            source3.append(row)
                            key = (month, city, channel, category)
                            tx_totals[key]["gmv_cents"] += gmv_cents
                            tx_totals[key]["refund_cents"] += refund_cents
                            tx_totals[key]["cogs_cents"] += cogs_cents
                            tx_totals[key]["orders"] += orders
                            units_by_l2[(month, city, l2)] += units

    # SRC-0004 receives the exact same units, allocated to currently valid SKUs.
    sold_by_sku = defaultdict(int)
    for key, units in units_by_l2.items():
        month, city, l2 = key
        skus = available_skus[(month, city, l2)]
        if not skus:
            raise RuntimeError(f"no available SKU for {key}")
        allocation = allocate_integer(units, [(sku, noise(0.20, "sku-share", month, city, sku)) for sku in skus])
        for sku, value in allocation.items():
            sold_by_sku[(month, city, sku)] = value

    source4 = []
    ending_inventory = {}
    for month in MONTHS:
        for city, (_, warehouse, _) in CITIES.items():
            for sku_row in sku_rows:
                sku = sku_row["sku"]
                active = 1
                in_stock = availability(month, city, sku)
                sold = sold_by_sku[(month, city, sku)]
                previous = ending_inventory.get((city, sku), round(160 * noise(0.35, "opening", city, sku)))
                if in_stock:
                    target = round(max(35, sold * 1.25) * noise(0.10, "target-stock", month, city, sku))
                    inbound = max(0, sold + target - previous)
                else:
                    inbound = 0
                ending = previous + inbound - sold
                if ending < 0:
                    raise RuntimeError("negative inventory")
                ending_inventory[(city, sku)] = ending
                source4.append({
                    "month": month,
                    "city": city,
                    "warehouse": warehouse,
                    "sku": sku,
                    "active_flag": active,
                    "in_stock_flag": in_stock,
                    "opening_inventory_units": previous,
                    "inbound_units": inbound,
                    "units_sold": sold,
                    "ending_inventory_units": ending,
                })

    # SRC-0006 is the attributable paid subset.
    source6 = []
    marketing_by_channel = defaultdict(int)
    attributable_net_by_channel = defaultdict(int)
    channel_net_before_marketing = defaultdict(int)
    paying_by_channel = defaultdict(int)
    for key, totals in tx_totals.items():
        month, city, channel, _ = key
        channel_net_before_marketing[(month, city, channel)] += totals["gmv_cents"] - totals["refund_cents"]
    for row in source2:
        paying_by_channel[(row["month"], row["city"], row["sales_channel"])] += int(row["paying_customers"])
    for month in MONTHS:
        for city in CITIES:
            for channel in CHANNELS:
                paid_rows = [source1_index[(month, city, channel, customer_type, "付费投放")] for customer_type in CUSTOMER_TYPES]
                visits = sum(int(row["visit_users"]) for row in paid_rows)
                new_paying = int(source1_index[(month, city, channel, "新客户", "付费投放")]["paying_customers"])
                cpc_cents = {"自营App": 122, "自营小程序": 92, "第三方平台": 78}[channel]
                if CITIES[city][0] == "北区":
                    cpc_cents = round(cpc_cents * 0.84)
                if month == "2026-05" and channel == "自营App":
                    cpc_cents = round(cpc_cents * 1.22)
                spend = visits * cpc_cents
                total_net = channel_net_before_marketing[(month, city, channel)]
                total_paying = max(1, paying_by_channel[(month, city, channel)])
                attributed_net = min(total_net, round(new_paying * total_net / total_paying * 0.92))
                campaign_alloc = allocate_integer(spend, [("常规拉新", 0.62), ("场景兴趣", 0.38)])
                visit_alloc = allocate_integer(visits, [("常规拉新", 0.62), ("场景兴趣", 0.38)])
                pay_alloc = allocate_integer(new_paying, [("常规拉新", 0.58), ("场景兴趣", 0.42)])
                net_alloc = allocate_integer(attributed_net, [("常规拉新", 0.60), ("场景兴趣", 0.40)])
                for campaign in ("常规拉新", "场景兴趣"):
                    source6.append({
                        "month": month,
                        "city": city,
                        "sales_channel": channel,
                        "traffic_source": "付费投放",
                        "campaign": campaign,
                        "marketing_expense": money(campaign_alloc[campaign]),
                        "attributable_visit_users": visit_alloc[campaign],
                        "attributable_new_paying_customers": pay_alloc[campaign],
                        "attributable_net_sales": money(net_alloc[campaign]),
                    })
                marketing_by_channel[(month, city, channel)] = spend
                attributable_net_by_channel[(month, city, channel)] = attributed_net

    # SRC-0005 aggregates transaction truth and adds explicit cost primitives.
    source5 = []
    for month in MONTHS:
        for city, (region, _, _) in CITIES.items():
            for channel in CHANNELS:
                keys = [(month, city, channel, category) for category in CATEGORIES]
                total_gmv = sum(tx_totals[key]["gmv_cents"] for key in keys)
                spend_total = round(marketing_by_channel[(month, city, channel)] * 1.16)
                spend_alloc = allocate_integer(spend_total, [(key[3], tx_totals[key]["gmv_cents"]) for key in keys])
                for key in keys:
                    category = key[3]
                    totals = tx_totals[key]
                    gmv_cents = totals["gmv_cents"]
                    refund_cents = totals["refund_cents"]
                    net_cents = gmv_cents - refund_cents
                    cogs_cents = totals["cogs_cents"]
                    marketing_cents = spend_alloc[category]
                    fulfillment_rate = {"北区": 560, "东区": 505, "南区": 485}[region]
                    fulfillment_cents = totals["orders"] * fulfillment_rate
                    channel_fee_cents = round(gmv_cents * {"自营App": 0.012, "自营小程序": 0.010, "第三方平台": 0.082}[channel])
                    gross_profit_cents = net_cents - cogs_cents
                    contribution_profit_cents = gross_profit_cents - marketing_cents - fulfillment_cents - channel_fee_cents
                    source5.append({
                        "month": month,
                        "city": city,
                        "sales_channel": channel,
                        "category_l1": category,
                        "gmv": money(gmv_cents),
                        "refund_amount": money(refund_cents),
                        "net_sales": money(net_cents),
                        "cogs": money(cogs_cents),
                        "gross_profit": money(gross_profit_cents),
                        "marketing_expense": money(marketing_cents),
                        "fulfillment_expense": money(fulfillment_cents),
                        "channel_fee": money(channel_fee_cents),
                        "contribution_profit": money(contribution_profit_cents),
                    })

    # SRC-0007 closes exactly to paid orders.
    source7 = []
    orders_by_fulfillment = defaultdict(int)
    for key, totals in tx_totals.items():
        month, city, _, category = key
        orders_by_fulfillment[(month, city, category)] += totals["orders"]
    for month in MONTHS:
        for city, (region, warehouse, _) in CITIES.items():
            for category in CATEGORIES:
                orders = orders_by_fulfillment[(month, city, category)]
                cancel_rate = 0.025 if category != "小家电" else 0.036
                if month == "2025-11":
                    cancel_rate *= 1.35
                canceled = min(orders, round(orders * cancel_rate * noise(0.04, "cancel", month, city, category)))
                completed = orders - canceled
                on_time_rate = {"北区": 0.91, "东区": 0.90, "南区": 0.94}[region]
                if region == "东区" and month >= "2025-06":
                    on_time_rate += 0.045
                if region == "东区" and month == "2026-03":
                    on_time_rate -= 0.14
                if region == "东区" and category == "小家电" and month in {"2026-04", "2026-05"}:
                    on_time_rate -= 0.025
                on_time = min(completed, round(completed * on_time_rate * noise(0.008, "ontime", month, city, category)))
                duration = (36.0 - on_time_rate * 18.0) * noise(0.035, "duration", month, city, category)
                source7.append({
                    "month": month,
                    "city": city,
                    "warehouse": warehouse,
                    "category_l1": category,
                    "completed_orders": completed,
                    "on_time_completed_orders": on_time,
                    "canceled_orders": canceled,
                    "average_fulfillment_hours": f"{duration:.2f}",
                })

    # SRC-0008 is the only effective-dated mapping authority.
    source8 = []
    for city, (region, warehouse, _) in CITIES.items():
        source8.extend([
            {"mapping_type": "区域-城市", "parent_value": region, "child_value": city, "effective_start": "2024-01-01", "effective_end": ""},
            {"mapping_type": "城市-仓库", "parent_value": city, "child_value": warehouse, "effective_start": "2024-01-01", "effective_end": ""},
        ])
    for category, subcategories in CATEGORIES.items():
        for subcategory in subcategories:
            source8.append({"mapping_type": "一级品类-二级类目", "parent_value": category, "child_value": subcategory, "effective_start": "2024-01-01", "effective_end": ""})
    for row in sku_rows:
        sku = row["sku"]
        l2 = row["category_l2"]
        if sku == "AP-LIFE-08":
            source8.append({"mapping_type": "二级类目-SKU", "parent_value": "生活电器", "child_value": sku, "effective_start": "2024-01-01", "effective_end": "2025-12-31"})
            source8.append({"mapping_type": "二级类目-SKU", "parent_value": "厨房小电", "child_value": sku, "effective_start": "2026-01-01", "effective_end": ""})
        else:
            source8.append({"mapping_type": "二级类目-SKU", "parent_value": l2, "child_value": sku, "effective_start": "2024-01-01", "effective_end": ""})
    for channel, sources in SOURCES_BY_CHANNEL.items():
        for source in sources:
            source8.append({"mapping_type": "渠道-流量来源", "parent_value": channel, "child_value": source, "effective_start": "2024-01-01", "effective_end": ""})

    write_csv(RAW_DIR / "channel_traffic_funnel_monthly.csv", list(source1[0]), source1)
    write_csv(RAW_DIR / "product_behavior_funnel_monthly.csv", list(source2[0]), source2)
    write_csv(RAW_DIR / "order_transactions_monthly.csv", list(source3[0]), source3)
    write_csv(RAW_DIR / "product_inventory_monthly.csv", list(source4[0]), source4)
    write_csv(RAW_DIR / "financial_results_monthly.csv", list(source5[0]), source5)
    write_csv(RAW_DIR / "marketing_campaigns_monthly.csv", list(source6[0]), source6)
    write_csv(RAW_DIR / "fulfillment_monthly.csv", list(source7[0]), source7)
    write_csv(RAW_DIR / "dimension_mappings.csv", list(source8[0]), source8)

    bad_path = BAD_DIR / "order_transactions_missing_refund_amount.csv"
    bad_fields = [field for field in source3[0] if field != "refund_amount"]
    write_csv(bad_path, bad_fields, [{field: row[field] for field in bad_fields} for row in source3])
    (BAD_DIR / "README.md").write_text(
        "# 隔离坏样本\n\n"
        "> 全部数据均为虚构演示数据。此目录不属于正常 Source 范围。\n\n"
        "`order_transactions_missing_refund_amount.csv` 故意删除 `refund_amount`，"
        "用于验证数据契约能否阻断净销售额、退款率和利润分析。\n",
        encoding="utf-8",
    )

    return {
        "SRC-0001": len(source1),
        "SRC-0002": len(source2),
        "SRC-0003": len(source3),
        "SRC-0004": len(source4),
        "SRC-0005": len(source5),
        "SRC-0006": len(source6),
        "SRC-0007": len(source7),
        "SRC-0008": len(source8),
    }


if __name__ == "__main__":
    counts = generate()
    print(f"Generated synthetic demo data with seed {SEED}")
    for source_id, count in counts.items():
        print(f"{source_id}: {count} rows")
