---
type: dimension
id: DIM-0001
name: 月份
status: demo
updated_at: 2026-07-18
---

# DIM-0001 月份

## 维度定义

指标发生或归属的自然月，格式为 `YYYY-MM`。

## 可取值或取值来源

- 2024-01 至 2026-06，共 30 个完整自然月。
- 未来由所有月度 Source 的 `month` 字段取得。

## 适用指标

适用于全部 [指标资产](../indexes/METRIC_INDEX.md)，用于同比、环比、季度和年度聚合。

## 数据源字段

- [SRC-0001](../sources/SRC-0001-channel-traffic-funnel.md)
- [SRC-0002](../sources/SRC-0002-product-behavior-funnel.md)
- [SRC-0003](../sources/SRC-0003-order-transactions.md)
- [SRC-0004](../sources/SRC-0004-product-inventory.md)
- [SRC-0005](../sources/SRC-0005-financial-results.md)
- [SRC-0006](../sources/SRC-0006-marketing-campaigns.md)
- [SRC-0007](../sources/SRC-0007-fulfillment.md)
- [SRC-0008](../sources/SRC-0008-dimension-mappings.md)
- 取数规则: 月度表使用 `month`，映射表使用生效与失效日期。

## 相关 hierarchy

- 不需要单独 hierarchy。

## 注意事项

- 同比需要上年同期完整数据。
- 2026-01 的品类映射变化必须结合 [品类层级](../hierarchies/HIER-0002-category-sku.md) 使用当期有效映射。
