---
type: dimension
id: DIM-0006
name: 一级品类
status: demo
updated_at: 2026-07-18
---

# DIM-0006 一级品类

## 维度定义

商品经营的一级分类口径。

## 可取值或取值来源

- 厨房用品
- 收纳用品
- 清洁用品
- 小家电

## 适用指标

适用于商品行为、交易、库存、财务和履约指标，包括 [详情加购转化率](../metrics/IND-0018-detail-to-cart-rate.md)、[GMV](../metrics/IND-0001-gmv.md)、[有货率](../metrics/IND-0025-in-stock-rate.md)、[净销售额](../metrics/IND-0003-net-sales.md)、[毛利率](../metrics/IND-0006-gross-margin.md)、[准时履约率](../metrics/IND-0032-on-time-fulfillment-rate.md)。

## 数据源字段

- [SRC-0002](../sources/SRC-0002-product-behavior-funnel.md)
- [SRC-0003](../sources/SRC-0003-order-transactions.md)
- [SRC-0005](../sources/SRC-0005-financial-results.md)
- [SRC-0007](../sources/SRC-0007-fulfillment.md)
- [SRC-0008](../sources/SRC-0008-dimension-mappings.md)
- 取数规则: 字段名为 `category_l1`，层级关系由映射表校验。

## 相关 hierarchy

- [HIER-0002 一级品类-二级类目-SKU](../hierarchies/HIER-0002-category-sku.md)

## 注意事项

- 一级品类间互斥完整时，可加指标才能汇总。
- 比率和单价必须由品类基础量重算。
