---
type: dimension
id: DIM-0008
name: SKU
status: demo
updated_at: 2026-07-18
---

# DIM-0008 SKU

## 维度定义

可独立维护库存和销售状态的最小商品单元。

## 可取值或取值来源

- 共 64 个虚构 SKU，每个二级类目 8 个。
- 编码由品类前缀、类目标识与序号组成，完整映射未来由 `SRC-0008` 提供。

## 适用指标

- [在售SKU数](../metrics/IND-0023-active-sku-count.md)
- [有货SKU数](../metrics/IND-0024-in-stock-sku-count.md)
- [有货率](../metrics/IND-0025-in-stock-rate.md)
- [销售件数](../metrics/IND-0027-units-sold.md)

## 数据源字段

- [SRC-0004](../sources/SRC-0004-product-inventory.md)
- [SRC-0008](../sources/SRC-0008-dimension-mappings.md)
- 取数规则: 库存字段为 `sku`，类目归属使用当期有效映射。

## 相关 hierarchy

- [HIER-0002 一级品类-二级类目-SKU](../hierarchies/HIER-0002-category-sku.md)

## 注意事项

- SKU 只属于一个当期有效二级类目。
- 有货率按 SKU 状态计算，不能用库存件数替代。
