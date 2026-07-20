---
type: metric
id: IND-0021
name: 新支付客户数
status: demo
updated_at: 2026-07-18
---

# IND-0021 新支付客户数

## 节点定位

- 用途: 新客获取结果，用于衡量首次成交客户规模。
- 计算属性: 去重客户基础量；在主归属口径内可加。

## 定义或计算公式

首次成功支付发生在统计月的客户数。

## 可拆解为

### 结构拆解

- 与 [老支付客户数](IND-0022-returning-paying-customers.md) 共同构成 [支付客户数](IND-0016-paying-customers.md)。
- 可按区域、城市、渠道和主流量来源拆分。

### 公式拆解

- 这是基础量；[支付客户数](IND-0016-paying-customers.md) = 新支付客户数 + [老支付客户数](IND-0022-returning-paying-customers.md)。

### 条件性拆解

- 只有可归因付费来源的新支付客户可以进入 [新客获客成本](IND-0033-new-customer-acquisition-cost.md)。

## 适用范围

观察窗口内首次支付；受窗口前历史不可见的左截断限制。

## 拆分维度

- [DIM-0001 月份](../dimensions/DIM-0001-month.md)
- [DIM-0002 区域](../dimensions/DIM-0002-region.md)
- [DIM-0003 城市](../dimensions/DIM-0003-city.md)
- [DIM-0004 销售渠道](../dimensions/DIM-0004-sales-channel.md)
- [DIM-0005 流量来源](../dimensions/DIM-0005-traffic-source.md)
- [DIM-0006 一级品类](../dimensions/DIM-0006-category-l1.md)
- [DIM-0009 客户类型](../dimensions/DIM-0009-customer-type.md)

## 数据源

- [SRC-0001](../sources/SRC-0001-channel-traffic-funnel.md)
- [SRC-0006](../sources/SRC-0006-marketing-campaigns.md)
- 取数规则: 渠道漏斗为新客总量权威；投放表只提供可归因新客子集。

## 业务事实

- [FACT-0008 自营App低意向投放扩张](../facts/FACT-0008-app-low-intent-paid-traffic.md)

## 关系备注

- 不得把全部新支付客户都归因给付费营销。
- 必须与老支付客户闭合为支付客户总数。
