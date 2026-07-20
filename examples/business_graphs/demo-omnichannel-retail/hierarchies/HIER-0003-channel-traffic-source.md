---
type: hierarchy
id: HIER-0003
name: 渠道-流量来源适用关系
status: demo
updated_at: 2026-07-18
---

# HIER-0003 渠道-流量来源适用关系

## 层级目的

销售渠道与流量来源不是严格父子层级，但存在稳定的可用组合和归因边界，需要集中约束。

## 参与维度

- [销售渠道](../dimensions/DIM-0004-sales-channel.md)
- [流量来源](../dimensions/DIM-0005-traffic-source.md)

## 映射关系

| 销售渠道 | 自然流量 | 付费投放 | 私域触达 | 内容合作 |
|---|---:|---:|---:|---:|
| 自营App | 适用 | 适用 | 适用 | 适用 |
| 自营小程序 | 适用 | 适用 | 适用 | 不完整，不进入归因效率 |
| 第三方平台 | 适用 | 适用 | 不适用 | 适用 |

## 适用范围

用于流量漏斗、付费获客与营销归因分析。

## 例外规则

- 不适用组合不生成记录。
- “不完整”来源可以用于规模观察，但不能进入获客成本或投放产出计算。
- 只有明确标记为可归因的付费投放进入 [新客获客成本](../metrics/IND-0033-new-customer-acquisition-cost.md) 与 [付费投放产出比](../metrics/IND-0034-paid-media-output-ratio.md)。

## 支撑数据源

- [SRC-0008](../sources/SRC-0008-dimension-mappings.md)
- [SRC-0001](../sources/SRC-0001-channel-traffic-funnel.md)
- [SRC-0006](../sources/SRC-0006-marketing-campaigns.md)
- 取数规则: 映射表为适用关系权威；漏斗与投放表用于检验实际组合。

## 影响指标

- [访问用户数](../metrics/IND-0012-visit-users.md)
- [访问详情转化率](../metrics/IND-0017-visit-to-detail-rate.md)
- [新客获客成本](../metrics/IND-0033-new-customer-acquisition-cost.md)
- [付费投放产出比](../metrics/IND-0034-paid-media-output-ratio.md)
