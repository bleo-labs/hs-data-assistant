---
type: metric
id: IND-0019
name: 加购提交转化率
status: demo
updated_at: 2026-07-18
---

# IND-0019 加购提交转化率

## 节点定位

- 用途: 购物车到提交订单的流程效率指标。
- 计算属性: 比率派生指标；不可加、不可直接平均。

## 定义或计算公式

[提交订单用户数](IND-0015-order-submit-users.md) / [加购用户数](IND-0014-add-to-cart-users.md)。

## 可拆解为

### 结构拆解

- 可按区域、城市、渠道、一级品类和客户类型观察。

### 公式拆解

- [提交订单用户数](IND-0015-order-submit-users.md) / [加购用户数](IND-0014-add-to-cart-users.md)

### 条件性拆解

- 分母为 0 时不可计算。
- 仅使用同一商品行为漏斗口径。

## 适用范围

用于识别购物车到下单环节的摩擦，不等于支付成功率。

## 拆分维度

- [DIM-0001 月份](../dimensions/DIM-0001-month.md)
- [DIM-0002 区域](../dimensions/DIM-0002-region.md)
- [DIM-0003 城市](../dimensions/DIM-0003-city.md)
- [DIM-0004 销售渠道](../dimensions/DIM-0004-sales-channel.md)
- [DIM-0006 一级品类](../dimensions/DIM-0006-category-l1.md)
- [DIM-0009 客户类型](../dimensions/DIM-0009-customer-type.md)

## 数据源

- [SRC-0002](../sources/SRC-0002-product-behavior-funnel.md)
- 取数规则: 由加购用户与提交订单用户计算。

## 业务事实

- [FACT-0004 全渠道大促](../facts/FACT-0004-omnichannel-sale.md)
- [FACT-0007 小家电补货暂停](../facts/FACT-0007-small-appliance-supply-pause.md)

## 关系备注

- 汇总时从基础用户数重算。
- 不得用订单数代替用户数。
