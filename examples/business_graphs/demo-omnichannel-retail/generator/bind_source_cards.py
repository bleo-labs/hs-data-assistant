#!/usr/bin/env python3
"""Bind generated Source cards back to graph assets in a repeatable way."""

from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE_FILES = {
    "SRC-0001": "SRC-0001-channel-traffic-funnel.md",
    "SRC-0002": "SRC-0002-product-behavior-funnel.md",
    "SRC-0003": "SRC-0003-order-transactions.md",
    "SRC-0004": "SRC-0004-product-inventory.md",
    "SRC-0005": "SRC-0005-financial-results.md",
    "SRC-0006": "SRC-0006-marketing-campaigns.md",
    "SRC-0007": "SRC-0007-fulfillment.md",
    "SRC-0008": "SRC-0008-dimension-mappings.md",
}

METRIC_BINDINGS = {
    "IND-0001": (["SRC-0003", "SRC-0005"], "交易表为明细权威；财务表用于聚合一致性校验。"),
    "IND-0002": (["SRC-0003", "SRC-0005"], "交易表为明细权威；财务表必须逐分闭合。"),
    "IND-0003": (["SRC-0005", "SRC-0003"], "财务表为结果权威；必须由交易表的 GMV 与退款金额回算。"),
    "IND-0004": (["SRC-0005"], "商品成本以财务结果月表为权威。"),
    "IND-0005": (["SRC-0005"], "由净销售额与商品成本逐分回算。"),
    "IND-0006": (["SRC-0005"], "聚合毛利润与净销售额后重算，不平均明细毛利率。"),
    "IND-0007": (["SRC-0005", "SRC-0006"], "财务表记录总营销费用；投放表只记录可归因子集。"),
    "IND-0008": (["SRC-0005"], "履约费用以财务结果月表为权威；履约表不记录费用。"),
    "IND-0009": (["SRC-0005"], "渠道费用以财务结果月表为权威。"),
    "IND-0010": (["SRC-0005"], "由毛利润减营销、履约和渠道费用逐分回算。"),
    "IND-0011": (["SRC-0005"], "聚合贡献利润与净销售额后重算。"),
    "IND-0012": (["SRC-0001", "SRC-0006"], "渠道漏斗为总量权威；投放表只提供可归因访问子集。"),
    "IND-0013": (["SRC-0001", "SRC-0002"], "渠道总量与主品类切片必须在共同粒度闭合。"),
    "IND-0014": (["SRC-0002"], "商品行为漏斗为权威。"),
    "IND-0015": (["SRC-0002"], "商品行为漏斗为权威。"),
    "IND-0016": (["SRC-0001", "SRC-0002", "SRC-0003"], "渠道总量、主品类切片和交易归因必须逐层闭合。"),
    "IND-0017": (["SRC-0001"], "由访问用户与商品详情用户计算。"),
    "IND-0018": (["SRC-0002"], "由商品详情用户与加购用户计算。"),
    "IND-0019": (["SRC-0002"], "由加购用户与提交订单用户计算。"),
    "IND-0020": (["SRC-0002"], "由提交订单用户与支付客户计算。"),
    "IND-0021": (["SRC-0001", "SRC-0006"], "渠道漏斗为新客总量权威；投放表只提供可归因新客子集。"),
    "IND-0022": (["SRC-0001", "SRC-0003"], "渠道漏斗为老客总量权威；交易表提供主品类和促销切片。"),
    "IND-0023": (["SRC-0004", "SRC-0008"], "库存表提供状态；类目归属使用当期有效映射。"),
    "IND-0024": (["SRC-0004", "SRC-0008"], "库存表提供状态；类目归属使用当期有效映射。"),
    "IND-0025": (["SRC-0004", "SRC-0008"], "聚合有货 SKU 与在售 SKU 后重算，类目归属使用当期映射。"),
    "IND-0026": (["SRC-0003", "SRC-0007"], "交易表为权威；履约表的完成与取消订单用于闭合校验。"),
    "IND-0027": (["SRC-0003", "SRC-0004"], "交易类目汇总与库存 SKU 底数必须通过有效映射闭合。"),
    "IND-0028": (["SRC-0003"], "由支付订单数与支付客户数计算。"),
    "IND-0029": (["SRC-0003"], "由 GMV 与支付订单数计算。"),
    "IND-0030": (["SRC-0003"], "由 GMV 与销售件数计算。"),
    "IND-0031": (["SRC-0003", "SRC-0005"], "退款金额与 GMV 先聚合再计算，交易与财务必须闭合。"),
    "IND-0032": (["SRC-0007"], "由准时完成订单与已完成订单计算，取消订单不进入分母。"),
    "IND-0033": (["SRC-0006"], "只使用可归因营销费用与可归因新支付客户。"),
    "IND-0034": (["SRC-0006"], "只使用可归因净销售额与可归因营销费用。"),
    "IND-0035": (["SRC-0001"], "由老支付客户与全部支付客户计算。"),
}

DIMENSION_BINDINGS = {
    "DIM-0001": (["SRC-0001", "SRC-0002", "SRC-0003", "SRC-0004", "SRC-0005", "SRC-0006", "SRC-0007", "SRC-0008"], "月度表使用 `month`，映射表使用生效与失效日期。"),
    "DIM-0002": (["SRC-0008"], "区域由区域-城市时间有效映射取得，不在事实表重复生成。"),
    "DIM-0003": (["SRC-0001", "SRC-0002", "SRC-0003", "SRC-0004", "SRC-0005", "SRC-0006", "SRC-0007", "SRC-0008"], "事实表使用 `city`，区域和仓库关系由映射表校验。"),
    "DIM-0004": (["SRC-0001", "SRC-0002", "SRC-0003", "SRC-0005", "SRC-0006"], "字段名为 `sales_channel`。"),
    "DIM-0005": (["SRC-0001", "SRC-0006", "SRC-0008"], "事实表字段为 `traffic_source`，适用组合由映射表冻结。"),
    "DIM-0006": (["SRC-0002", "SRC-0003", "SRC-0005", "SRC-0007", "SRC-0008"], "字段名为 `category_l1`，层级关系由映射表校验。"),
    "DIM-0007": (["SRC-0003", "SRC-0008"], "交易字段为 `category_l2`，SKU 归属使用当期有效映射。"),
    "DIM-0008": (["SRC-0004", "SRC-0008"], "库存字段为 `sku`，类目归属使用当期有效映射。"),
    "DIM-0009": (["SRC-0001", "SRC-0002", "SRC-0003"], "字段名为 `customer_type`。"),
    "DIM-0010": (["SRC-0003"], "字段名为 `promotion_type`。"),
    "DIM-0011": (["SRC-0004", "SRC-0007", "SRC-0008"], "库存与履约字段为 `warehouse`，城市服务仓由映射表校验。"),
}

HIERARCHY_BINDINGS = {
    "HIER-0001": (["SRC-0008", "SRC-0004", "SRC-0007"], "映射表为关系权威；库存与履约表用于检验实际组合。"),
    "HIER-0002": (["SRC-0008", "SRC-0003", "SRC-0004"], "映射表为关系权威；交易与库存必须按当期映射闭合。"),
    "HIER-0003": (["SRC-0008", "SRC-0001", "SRC-0006"], "映射表为适用关系权威；漏斗与投放表用于检验实际组合。"),
}


def links(source_ids):
    return "\n".join(f"- [{source_id}](../sources/{SOURCE_FILES[source_id]})" for source_id in source_ids)


def replace_section(path: Path, heading: str, source_ids, rule: str):
    text = path.read_text(encoding="utf-8")
    replacement = f"{heading}\n\n{links(source_ids)}\n- 取数规则: {rule}\n\n"
    pattern = re.compile(rf"^{re.escape(heading)}\n.*?(?=^## |\Z)", re.MULTILINE | re.DOTALL)
    if not pattern.search(text):
        raise RuntimeError(f"missing section {heading}: {path}")
    path.write_text(pattern.sub(replacement, text), encoding="utf-8")


def apply_bindings(folder: str, heading: str, bindings):
    for path in sorted((ROOT / folder).glob("*.md")):
        text = path.read_text(encoding="utf-8")
        match = re.search(r"^id:\s*([^\n]+)", text, re.MULTILINE)
        if not match:
            raise RuntimeError(f"missing id: {path}")
        asset_id = match.group(1).strip()
        if asset_id not in bindings:
            raise RuntimeError(f"missing binding for {asset_id}")
        source_ids, rule = bindings[asset_id]
        replace_section(path, heading, source_ids, rule)


if __name__ == "__main__":
    apply_bindings("metrics", "## 数据源", METRIC_BINDINGS)
    apply_bindings("dimensions", "## 数据源字段", DIMENSION_BINDINGS)
    apply_bindings("hierarchies", "## 支撑数据源", HIERARCHY_BINDINGS)
    print("Bound Source cards to 35 metrics, 11 dimensions, and 3 hierarchies")
