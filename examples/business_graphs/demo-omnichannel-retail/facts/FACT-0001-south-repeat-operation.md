---
type: fact
id: FACT-0001
name: 南区上线老客分层触达策略
status: synthetic_ground_truth
updated_at: 2026-07-18
---

# FACT-0001 南区上线老客分层触达策略

## 事实陈述

自 2025-03 起，南区持续运行老客分层触达策略。

## 适用范围

- 时间: 2025-03 起。
- 区域: [南区](../dimensions/DIM-0002-region.md)。
- 客户: [老客户](../dimensions/DIM-0009-customer-type.md)。

## 影响对象

- [老支付客户数](../metrics/IND-0022-returning-paying-customers.md)
- [购买频次](../metrics/IND-0028-purchase-frequency.md)
- [老客占比](../metrics/IND-0035-returning-customer-share.md)
- [净销售额](../metrics/IND-0003-net-sales.md)
- [贡献利润](../metrics/IND-0010-contribution-profit.md)

## 证据来源

- 已确认的合成业务事实，来自 [演示命题与标准答案](../design/scenario-ground-truth.md)。
- 实际数据证据待数据生成阶段写入对应 Source。

## 分析影响

南区复购与频次改善时，应把本事实作为候选机制；仍需用南区与其他区域的前后趋势验证，不能仅凭事实存在就确定因果强度。
