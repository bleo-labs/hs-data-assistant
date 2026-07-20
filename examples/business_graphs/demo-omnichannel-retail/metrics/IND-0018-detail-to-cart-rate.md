---
type: metric
id: IND-0018
name: 详情加购转化率
status: demo
updated_at: 2026-07-18
---

# IND-0018 详情加购转化率

## 节点定位

- 用途: 商品吸引力与供给可用性的漏斗效率指标。
- 计算属性: 比率派生指标；不可加、不可直接平均。

## 定义或计算公式

[加购用户数](IND-0014-add-to-cart-users.md) / [商品详情用户数](IND-0013-product-detail-users.md)。

## 可拆解为

### 结构拆解

- 可按区域、城市、渠道、一级品类和客户类型观察。

### 公式拆解

- [加购用户数](IND-0014-add-to-cart-users.md) / [商品详情用户数](IND-0013-product-detail-users.md)

### 条件性拆解

- 仅使用商品行为漏斗的主品类口径。
- 分母为 0 时不可计算。

## 适用范围

用于详情后的商品兴趣与供给影响诊断；不直接等于支付转化。

## 拆分维度

- [DIM-0001 月份](../dimensions/DIM-0001-month.md)
- [DIM-0002 区域](../dimensions/DIM-0002-region.md)
- [DIM-0003 城市](../dimensions/DIM-0003-city.md)
- [DIM-0004 销售渠道](../dimensions/DIM-0004-sales-channel.md)
- [DIM-0006 一级品类](../dimensions/DIM-0006-category-l1.md)
- [DIM-0009 客户类型](../dimensions/DIM-0009-customer-type.md)

## 数据源

- [SRC-0002](../sources/SRC-0002-product-behavior-funnel.md)
- 取数规则: 由商品详情用户与加购用户计算。

## 业务事实

- [FACT-0003 小家电提价](../facts/FACT-0003-small-appliance-price-rise.md)
- [FACT-0007 小家电补货暂停](../facts/FACT-0007-small-appliance-supply-pause.md)
- [FACT-0009 小家电恢复补货](../facts/FACT-0009-small-appliance-restock.md)

## 关系备注

- 汇总时必须从基础用户数重算。
- 有货率、价格与本指标的同步变化需要结合业务事实和对照组解释。
