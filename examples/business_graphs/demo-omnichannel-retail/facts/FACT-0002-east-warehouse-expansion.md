---
type: fact
id: FACT-0002
name: 东区仓完成容量扩充
status: synthetic_ground_truth
updated_at: 2026-07-18
---

# FACT-0002 东区仓完成容量扩充

## 事实陈述

自 2025-06 起，东区仓完成容量扩充并进入稳定运行。

## 适用范围

- 时间: 2025-06 起。
- 区域: [东区](../dimensions/DIM-0002-region.md)。
- 仓库: [东区仓](../dimensions/DIM-0011-warehouse.md)。

## 影响对象

- [有货SKU数](../metrics/IND-0024-in-stock-sku-count.md)
- [有货率](../metrics/IND-0025-in-stock-rate.md)
- [准时履约率](../metrics/IND-0032-on-time-fulfillment-rate.md)
- [区域-城市-仓库](../hierarchies/HIER-0001-region-city-warehouse.md)

## 证据来源

- 已确认的合成业务事实，来自 [演示命题与标准答案](../design/scenario-ground-truth.md)。

## 分析影响

解释东区长期供给和履约改善时应考虑扩容；2026-03 的系统切换是另一个短期事件，不能把当月波动误判为扩容失效。
