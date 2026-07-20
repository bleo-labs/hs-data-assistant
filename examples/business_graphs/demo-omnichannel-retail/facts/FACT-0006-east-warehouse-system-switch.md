---
type: fact
id: FACT-0006
name: 东区仓切换履约系统
status: synthetic_ground_truth
updated_at: 2026-07-18
---

# FACT-0006 东区仓切换履约系统

## 事实陈述

2026-03，东区仓切换履约系统，造成当月准时履约短期下降，次月恢复。

## 适用范围

- 时间: 2026-03，恢复观察延伸至 2026-04。
- 区域: [东区](../dimensions/DIM-0002-region.md)。
- 仓库: [东区仓](../dimensions/DIM-0011-warehouse.md)。

## 影响对象

- [准时履约率](../metrics/IND-0032-on-time-fulfillment-rate.md)
- [退款金额](../metrics/IND-0002-refund-amount.md)
- [退款率](../metrics/IND-0031-refund-rate.md)
- [贡献利润](../metrics/IND-0010-contribution-profit.md)

## 证据来源

- 已确认的合成系统事件，来自 [演示命题与标准答案](../design/scenario-ground-truth.md)。

## 分析影响

该事实用于区分短期系统扰动与长期履约能力变化；如果次月未恢复，应继续寻找其他机制。
