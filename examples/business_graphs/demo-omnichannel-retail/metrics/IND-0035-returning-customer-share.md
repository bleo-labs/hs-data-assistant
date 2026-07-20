---
type: metric
id: IND-0035
name: 老客占比
status: demo
updated_at: 2026-07-18
---

# IND-0035 老客占比

## 节点定位

- 用途: 客户结构指标，用于观察支付客户中老客户的贡献程度。
- 计算属性: 比率派生指标；不可加、不可直接平均。

## 定义或计算公式

[老支付客户数](IND-0022-returning-paying-customers.md) / [支付客户数](IND-0016-paying-customers.md)。

## 可拆解为

### 结构拆解

- 可按区域、城市、渠道和主品类观察。

### 公式拆解

- [老支付客户数](IND-0022-returning-paying-customers.md) / [支付客户数](IND-0016-paying-customers.md)

### 条件性拆解

- 分母为 0 时不可计算。
- 依赖一致的新老客户定义和历史观察窗口。

## 适用范围

描述客户结构，不直接代表老客绝对规模或复购率。

## 拆分维度

- [DIM-0001 月份](../dimensions/DIM-0001-month.md)
- [DIM-0002 区域](../dimensions/DIM-0002-region.md)
- [DIM-0003 城市](../dimensions/DIM-0003-city.md)
- [DIM-0004 销售渠道](../dimensions/DIM-0004-sales-channel.md)
- [DIM-0006 一级品类](../dimensions/DIM-0006-category-l1.md)

## 数据源

- [SRC-0001](../sources/SRC-0001-channel-traffic-funnel.md)
- 取数规则: 由老支付客户与全部支付客户计算。

## 业务事实

- [FACT-0001 南区老客分层触达](../facts/FACT-0001-south-repeat-operation.md)

## 关系备注

- 汇总时从基础客户数重算。
- 占比上升可能来自老客增长，也可能来自新客下降，必须同时查看绝对量。
