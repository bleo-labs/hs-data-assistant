---
type: fact
id: FACT-0004
name: 全渠道大促清理慢销库存
status: synthetic_ground_truth
updated_at: 2026-07-18
---

# FACT-0004 全渠道大促清理慢销库存

## 事实陈述

2025-11，全渠道执行一次以清理部分慢销库存为目的的大促。

## 适用范围

- 时间: 2025-11。
- 渠道: 全部 [销售渠道](../dimensions/DIM-0004-sales-channel.md)。
- 促销: [平台大促](../dimensions/DIM-0010-promotion-type.md)。

## 影响对象

- [GMV](../metrics/IND-0001-gmv.md)
- [支付订单数](../metrics/IND-0026-paid-orders.md)
- [毛利率](../metrics/IND-0006-gross-margin.md)
- [退款率](../metrics/IND-0031-refund-rate.md)
- [贡献利润率](../metrics/IND-0011-contribution-margin.md)

## 证据来源

- 已确认的合成活动事实，来自 [演示命题与标准答案](../design/scenario-ground-truth.md)。

## 分析影响

该月规模增长需同时检查利润率和退款率；不能把短期活动峰值外推成自然经营趋势。
