---
type: fact
id: FACT-0009
name: 小家电恢复补货
status: synthetic_ground_truth
updated_at: 2026-07-18
---

# FACT-0009 小家电恢复补货

## 事实陈述

2026-06，小家电核心供应商恢复补货。

## 适用范围

- 时间: 2026-06 起。
- 品类: [小家电](../dimensions/DIM-0006-category-l1.md)。
- 区域: [东区](../dimensions/DIM-0002-region.md) 的恢复最明显。

## 影响对象

- [有货SKU数](../metrics/IND-0024-in-stock-sku-count.md)
- [有货率](../metrics/IND-0025-in-stock-rate.md)
- [详情加购转化率](../metrics/IND-0018-detail-to-cart-rate.md)
- [支付订单数](../metrics/IND-0026-paid-orders.md)
- [净销售额](../metrics/IND-0003-net-sales.md)

## 证据来源

- 已确认的合成供给恢复事实，来自 [演示命题与标准答案](../design/scenario-ground-truth.md)。

## 分析影响

用于验证 2026-04 至 05 的供给冲击是否具有恢复证据；如果有货率恢复但交易未恢复，需要继续检查需求和转化路径。
