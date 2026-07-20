---
type: fact
id: FACT-0007
name: 小家电核心供应商补货暂停
status: synthetic_ground_truth
updated_at: 2026-07-18
---

# FACT-0007 小家电核心供应商补货暂停

## 事实陈述

2026-04 至 2026-05，小家电核心供应商因质检暂停补货，东区受影响最明显。

## 适用范围

- 时间: 2026-04 至 2026-05。
- 区域: [东区](../dimensions/DIM-0002-region.md) 为主要影响区。
- 品类: [小家电](../dimensions/DIM-0006-category-l1.md)。

## 影响对象

- [有货SKU数](../metrics/IND-0024-in-stock-sku-count.md)
- [有货率](../metrics/IND-0025-in-stock-rate.md)
- [详情加购转化率](../metrics/IND-0018-detail-to-cart-rate.md)
- [支付订单数](../metrics/IND-0026-paid-orders.md)
- [净销售额](../metrics/IND-0003-net-sales.md)
- [贡献利润](../metrics/IND-0010-contribution-profit.md)

## 证据来源

- 已确认的合成供给冲击事实，来自 [演示命题与标准答案](../design/scenario-ground-truth.md)。

## 分析影响

2026-05 收入下滑分析应优先检查东区小家电供给链；仍需用其他区域和品类作对照，量化主因贡献。
