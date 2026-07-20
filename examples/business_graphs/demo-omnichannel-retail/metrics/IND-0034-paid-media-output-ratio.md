---
type: metric
id: IND-0034
name: 付费投放产出比
status: demo
updated_at: 2026-07-18
---

# IND-0034 付费投放产出比

## 节点定位

- 用途: 付费营销产出效率指标，用于比较可归因净销售额与营销费用。
- 计算属性: 比率派生指标；不可加、不可直接平均。

## 定义或计算公式

可归因净销售额 / 可归因营销费用。

## 可拆解为

### 结构拆解

- 可按区域、城市、渠道和可归因流量来源观察。

### 公式拆解

- 可归因净销售额 / 可归因营销费用

### 条件性拆解

- 仅适用于具有明确归因边界的付费投放。
- 分母为 0 时不可计算。

## 适用范围

是经营归因口径，不等同于严格因果 ROI，也不扣除商品和履约成本。

## 拆分维度

- [DIM-0001 月份](../dimensions/DIM-0001-month.md)
- [DIM-0002 区域](../dimensions/DIM-0002-region.md)
- [DIM-0003 城市](../dimensions/DIM-0003-city.md)
- [DIM-0004 销售渠道](../dimensions/DIM-0004-sales-channel.md)
- [DIM-0005 流量来源](../dimensions/DIM-0005-traffic-source.md)

## 数据源

- [SRC-0006](../sources/SRC-0006-marketing-campaigns.md)
- 取数规则: 只使用可归因净销售额与可归因营销费用。

## 业务事实

- [FACT-0008 自营App低意向投放扩张](../facts/FACT-0008-app-low-intent-paid-traffic.md)

## 关系备注

- 汇总时从基础分子分母重算。
- 不能用全渠道净销售额作分子，也不能据此单独判断投放增量因果。
