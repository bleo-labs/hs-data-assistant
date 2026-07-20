---
type: fact
id: FACT-0003
name: 小家电统一提价
status: synthetic_ground_truth
updated_at: 2026-07-18
---

# FACT-0003 小家电统一提价

## 事实陈述

2025-09，小家电品类实施一次统一提价。

## 适用范围

- 时间: 2025-09 起观察价格影响。
- 品类: [小家电](../dimensions/DIM-0006-category-l1.md)。

## 影响对象

- [平均销售单价](../metrics/IND-0030-average-selling-price.md)
- [客单价](../metrics/IND-0029-aov.md)
- [详情加购转化率](../metrics/IND-0018-detail-to-cart-rate.md)
- [毛利率](../metrics/IND-0006-gross-margin.md)
- [GMV](../metrics/IND-0001-gmv.md)

## 证据来源

- 已确认的合成价格实验事实，来自 [演示命题与标准答案](../design/scenario-ground-truth.md)。

## 分析影响

应同时观察价格、件数、转化和毛利，不能把平均销售单价上升自动解释为经营质量提升。
