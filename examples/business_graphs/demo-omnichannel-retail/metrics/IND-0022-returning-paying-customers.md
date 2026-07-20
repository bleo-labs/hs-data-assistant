---
type: metric
id: IND-0022
name: 老支付客户数
status: demo
updated_at: 2026-07-18
---

# IND-0022 老支付客户数

## 节点定位

- 用途: 复购结果，用于衡量历史客户在本期再次成交的规模。
- 计算属性: 去重客户基础量；在主归属口径内可加。

## 定义或计算公式

统计月前已有成功支付记录、并在统计月再次支付的客户数。

## 可拆解为

### 结构拆解

- 与 [新支付客户数](IND-0021-new-paying-customers.md) 共同构成 [支付客户数](IND-0016-paying-customers.md)。

### 公式拆解

- 这是基础量；[老客占比](IND-0035-returning-customer-share.md) = 老支付客户数 / [支付客户数](IND-0016-paying-customers.md)。

### 条件性拆解

- 需要稳定客户标识和历史观察窗口。

## 适用范围

用于复购和客户结构分析，不等于全部存量客户。

## 拆分维度

- [DIM-0001 月份](../dimensions/DIM-0001-month.md)
- [DIM-0002 区域](../dimensions/DIM-0002-region.md)
- [DIM-0003 城市](../dimensions/DIM-0003-city.md)
- [DIM-0004 销售渠道](../dimensions/DIM-0004-sales-channel.md)
- [DIM-0006 一级品类](../dimensions/DIM-0006-category-l1.md)
- [DIM-0009 客户类型](../dimensions/DIM-0009-customer-type.md)

## 数据源

- [SRC-0001](../sources/SRC-0001-channel-traffic-funnel.md)
- [SRC-0003](../sources/SRC-0003-order-transactions.md)
- 取数规则: 渠道漏斗为老客总量权威；交易表提供主品类和促销切片。

## 业务事实

- [FACT-0001 南区老客分层触达](../facts/FACT-0001-south-repeat-operation.md)

## 关系备注

- 老支付客户增长与购买频次提升需要分别观察。
- 不能用老客占比上升自动推断客户规模增长。
