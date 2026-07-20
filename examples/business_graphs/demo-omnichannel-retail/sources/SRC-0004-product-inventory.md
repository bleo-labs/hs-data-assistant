---
id: SRC-0004
type: source
status: demo_ready
updated_at: 2026-07-18
---

# SRC-0004 商品库存月表

## 数据源定义

- 文件或表名: `product_inventory_monthly.csv`
- 存放位置: [datasets/raw/product_inventory_monthly.csv](../datasets/raw/product_inventory_monthly.csv)
- 数据截止时间: 2026-06-30
- 更新频率: 固定种子合成数据，可由生成器完整重建
- 数据性质: synthetic demo

## 数据粒度与字段

- 粒度: 月份 × 城市 × 仓库 × SKU。
- 唯一键: `month`、`city`、`warehouse`、`sku`。
- 基础字段: `active_flag`、`in_stock_flag`、`opening_inventory_units`、`inbound_units`、`units_sold`、`ending_inventory_units`。
- 闭合关系: 月末库存 = 月初库存 + 入库件数 - 销售件数。

## 支持的指标

- [在售SKU数](../metrics/IND-0023-active-sku-count.md)
- [有货SKU数](../metrics/IND-0024-in-stock-sku-count.md)
- [有货率](../metrics/IND-0025-in-stock-rate.md)
- [销售件数](../metrics/IND-0027-units-sold.md)

## 支持的维度

- 月份、城市、仓库、SKU；区域和品类必须通过 [SRC-0008](SRC-0008-dimension-mappings.md) 的当期有效关系取得。

## 口径限制

- 有货率按 SKU 状态计算，不以库存件数替代。
- `in_stock_flag = 0` 可以表示质检暂停等不可售状态，不等于物理库存必然为 0。
- 销售件数必须与 [SRC-0003](SRC-0003-order-transactions.md) 按有效 SKU 类目映射闭合。
