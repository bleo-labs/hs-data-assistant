---
type: hierarchy
id: HIER-0002
name: 一级品类-二级类目-SKU
status: demo
updated_at: 2026-07-18
---

# HIER-0002 一级品类-二级类目-SKU

## 层级目的

统一维护商品类目与 SKU 的时间有效归属，避免在多个维度文件中重复复制映射。

## 参与维度

- [一级品类](../dimensions/DIM-0006-category-l1.md)
- [二级类目](../dimensions/DIM-0007-category-l2.md)
- [SKU](../dimensions/DIM-0008-sku.md)

## 映射关系

| 一级品类 | 二级类目 | SKU 编码范围 |
|---|---|---|
| 厨房用品 | 烹饪器具 | `KIT-COOK-01` 至 `KIT-COOK-08` |
| 厨房用品 | 餐厨工具 | `KIT-TOOLS-01` 至 `KIT-TOOLS-08` |
| 收纳用品 | 衣物收纳 | `STO-CLOTH-01` 至 `STO-CLOTH-08` |
| 收纳用品 | 空间整理 | `STO-SPACE-01` 至 `STO-SPACE-08` |
| 清洁用品 | 清洁工具 | `CLN-TOOLS-01` 至 `CLN-TOOLS-08` |
| 清洁用品 | 家居耗材 | `CLN-CONSUM-01` 至 `CLN-CONSUM-08` |
| 小家电 | 厨房小电 | `AP-KITCH-01` 至 `AP-KITCH-08` |
| 小家电 | 生活电器 | `AP-LIFE-01` 至 `AP-LIFE-08` |

## 适用范围

适用于商品行为、订单、库存、财务与履约的品类下钻。

## 例外规则

- `AP-LIFE-08` 在 2026-01 起从“生活电器”调整至“厨房小电”。
- 跨期二级类目比较必须使用当期映射，并披露 [FACT-0005](../facts/FACT-0005-category-reclassification.md)。
- 一级品类口径不受该调整影响。

## 支撑数据源

- [SRC-0008](../sources/SRC-0008-dimension-mappings.md)
- [SRC-0003](../sources/SRC-0003-order-transactions.md)
- [SRC-0004](../sources/SRC-0004-product-inventory.md)
- 取数规则: 映射表为关系权威；交易与库存必须按当期映射闭合。

## 影响指标

- [GMV](../metrics/IND-0001-gmv.md)
- [净销售额](../metrics/IND-0003-net-sales.md)
- [有货率](../metrics/IND-0025-in-stock-rate.md)
- [详情加购转化率](../metrics/IND-0018-detail-to-cart-rate.md)
- [平均销售单价](../metrics/IND-0030-average-selling-price.md)
