---
type: metric
id: IND-0028
name: 购买频次
status: demo
updated_at: 2026-07-18
---

# IND-0028 购买频次

## 节点定位

- 用途: 客户购买深度效率指标，用于解释订单增长是否来自复购或单客多单。
- 计算属性: 人均派生指标；不可加、不可直接平均。

## 定义或计算公式

[支付订单数](IND-0026-paid-orders.md) / [支付客户数](IND-0016-paying-customers.md)。

## 可拆解为

### 结构拆解

- 可按区域、城市、渠道、主品类和客户类型观察。

### 公式拆解

- [支付订单数](IND-0026-paid-orders.md) / [支付客户数](IND-0016-paying-customers.md)

### 条件性拆解

- 分母为 0 时不可计算。
- 支付客户数必须使用与订单数一致的去重边界。

## 适用范围

统计月内平均每位支付客户的支付订单数。

## 拆分维度

- [DIM-0001 月份](../dimensions/DIM-0001-month.md)
- [DIM-0002 区域](../dimensions/DIM-0002-region.md)
- [DIM-0003 城市](../dimensions/DIM-0003-city.md)
- [DIM-0004 销售渠道](../dimensions/DIM-0004-sales-channel.md)
- [DIM-0006 一级品类](../dimensions/DIM-0006-category-l1.md)
- [DIM-0009 客户类型](../dimensions/DIM-0009-customer-type.md)

## 数据源

- [SRC-0003](../sources/SRC-0003-order-transactions.md)
- 取数规则: 由支付订单数与支付客户数计算。

## 业务事实

- [FACT-0001 南区老客分层触达](../facts/FACT-0001-south-repeat-operation.md)
- [FACT-0004 全渠道大促](../facts/FACT-0004-omnichannel-sale.md)

## 关系备注

- 汇总时先汇总订单数并取得目标口径去重客户数，再相除。
- 不得平均城市或客户类型购买频次。
