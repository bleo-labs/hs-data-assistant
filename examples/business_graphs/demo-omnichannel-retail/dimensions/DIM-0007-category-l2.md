---
type: dimension
id: DIM-0007
name: 二级类目
status: demo
updated_at: 2026-07-18
---

# DIM-0007 二级类目

## 维度定义

一级品类下的商品细分类目。

## 可取值或取值来源

- 厨房用品: 烹饪器具、餐厨工具
- 收纳用品: 衣物收纳、空间整理
- 清洁用品: 清洁工具、家居耗材
- 小家电: 厨房小电、生活电器

## 适用指标

适用于 [GMV](../metrics/IND-0001-gmv.md)、[退款金额](../metrics/IND-0002-refund-amount.md)、[支付订单数](../metrics/IND-0026-paid-orders.md)、[销售件数](../metrics/IND-0027-units-sold.md)、[客单价](../metrics/IND-0029-aov.md) 和 [平均销售单价](../metrics/IND-0030-average-selling-price.md)。

## 数据源字段

- [SRC-0003](../sources/SRC-0003-order-transactions.md)
- [SRC-0008](../sources/SRC-0008-dimension-mappings.md)
- 取数规则: 交易字段为 `category_l2`，SKU 归属使用当期有效映射。

## 相关 hierarchy

- [HIER-0002 一级品类-二级类目-SKU](../hierarchies/HIER-0002-category-sku.md)

## 注意事项

- 2026-01 存在 SKU 二级类目归属调整，跨期比较必须使用当期有效映射。
