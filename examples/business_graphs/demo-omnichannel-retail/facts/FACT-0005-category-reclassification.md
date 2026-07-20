---
type: fact
id: FACT-0005
name: 商品分类口径调整
status: synthetic_ground_truth
updated_at: 2026-07-18
---

# FACT-0005 商品分类口径调整

## 事实陈述

2026-01 起，SKU `AP-LIFE-08` 从“生活电器”调整至“厨房小电”。

## 适用范围

- 时间: 2026-01 起使用新映射。
- 层级: [一级品类-二级类目-SKU](../hierarchies/HIER-0002-category-sku.md)。
- 影响层级: 二级类目；一级品类“小家电”不变。

## 影响对象

- [二级类目](../dimensions/DIM-0007-category-l2.md)
- [SKU](../dimensions/DIM-0008-sku.md)
- [GMV](../metrics/IND-0001-gmv.md)
- [净销售额](../metrics/IND-0003-net-sales.md)
- [有货率](../metrics/IND-0025-in-stock-rate.md)

## 证据来源

- 已确认的合成口径事实，来自 [演示命题与标准答案](../design/scenario-ground-truth.md)。

## 分析影响

二级类目同比和趋势必须按当期有效映射处理并披露口径变化；不得把重分类造成的转移解释成业务增长或下滑。
