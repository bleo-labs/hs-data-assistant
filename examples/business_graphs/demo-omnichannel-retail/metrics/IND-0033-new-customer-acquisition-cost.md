---
type: metric
id: IND-0033
name: 新客获客成本
status: demo
updated_at: 2026-07-18
---

# IND-0033 新客获客成本

## 节点定位

- 用途: 付费获客效率指标，用于衡量获得一个可归因新支付客户的营销成本。
- 计算属性: 单均派生指标；不可加、不可直接平均。

## 定义或计算公式

可归因营销费用 / 可归因新支付客户数。

## 可拆解为

### 结构拆解

- 可按区域、城市、渠道和可归因流量来源观察。

### 公式拆解

- 可归因营销费用 / 可归因新支付客户数

### 条件性拆解

- 仅适用于明确可归因的付费营销。
- 分母为 0 时不可计算。
- 自然流量客户不进入。

## 适用范围

衡量付费新客获取效率，不代表全业务平均获客成本。

## 拆分维度

- [DIM-0001 月份](../dimensions/DIM-0001-month.md)
- [DIM-0002 区域](../dimensions/DIM-0002-region.md)
- [DIM-0003 城市](../dimensions/DIM-0003-city.md)
- [DIM-0004 销售渠道](../dimensions/DIM-0004-sales-channel.md)
- [DIM-0005 流量来源](../dimensions/DIM-0005-traffic-source.md)

## 数据源

- [SRC-0006](../sources/SRC-0006-marketing-campaigns.md)
- 取数规则: 只使用可归因营销费用与可归因新支付客户。

## 业务事实

- [FACT-0008 自营App低意向投放扩张](../facts/FACT-0008-app-low-intent-paid-traffic.md)

## 关系备注

- 汇总时从费用和新客基础量重算。
- 不得把总营销费用或全部新客代入。
