---
type: dimension
id: DIM-0011
name: 仓库
status: demo
updated_at: 2026-07-18
---

# DIM-0011 仓库

## 维度定义

承担库存和履约责任的区域仓。

## 可取值或取值来源

- 北区仓
- 东区仓
- 南区仓

## 适用指标

适用于 [在售SKU数](../metrics/IND-0023-active-sku-count.md)、[有货SKU数](../metrics/IND-0024-in-stock-sku-count.md)、[有货率](../metrics/IND-0025-in-stock-rate.md)、[履约费用](../metrics/IND-0008-fulfillment-expense.md) 和 [准时履约率](../metrics/IND-0032-on-time-fulfillment-rate.md)。

## 数据源字段

- [SRC-0004](../sources/SRC-0004-product-inventory.md)
- [SRC-0007](../sources/SRC-0007-fulfillment.md)
- [SRC-0008](../sources/SRC-0008-dimension-mappings.md)
- 取数规则: 库存与履约字段为 `warehouse`，城市服务仓由映射表校验。

## 相关 hierarchy

- [HIER-0001 区域-城市-仓库](../hierarchies/HIER-0001-region-city-warehouse.md)

## 注意事项

- 城市归属区域稳定，但实际服务仓允许随时间调整。
- 不得把仓库映射硬编码进城市维度。
