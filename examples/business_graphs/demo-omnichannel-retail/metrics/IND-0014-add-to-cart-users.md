---
type: metric
id: IND-0014
name: 加购用户数
status: demo
updated_at: 2026-07-18
---

# IND-0014 加购用户数

## 节点定位

- 用途: 商品兴趣与交易意向的漏斗过程指标。
- 计算属性: 去重用户基础量；按主品类契约可向上汇总。

## 定义或计算公式

统计月内将至少一个商品加入购物车的去重用户数。

## 可拆解为

### 结构拆解

- 可按区域、城市、渠道、一级品类和客户类型拆分。

### 公式拆解

- 这是基础量，是 [详情加购转化率](IND-0018-detail-to-cart-rate.md) 的分子和 [加购提交转化率](IND-0019-cart-to-submit-rate.md) 的分母。

### 条件性拆解

- 必须小于或等于同粒度 [商品详情用户数](IND-0013-product-detail-users.md)。

## 适用范围

适用于商品行为漏斗；不代表已下单或支付。

## 拆分维度

- [DIM-0001 月份](../dimensions/DIM-0001-month.md)
- [DIM-0002 区域](../dimensions/DIM-0002-region.md)
- [DIM-0003 城市](../dimensions/DIM-0003-city.md)
- [DIM-0004 销售渠道](../dimensions/DIM-0004-sales-channel.md)
- [DIM-0006 一级品类](../dimensions/DIM-0006-category-l1.md)
- [DIM-0009 客户类型](../dimensions/DIM-0009-customer-type.md)

## 数据源

- [SRC-0002](../sources/SRC-0002-product-behavior-funnel.md)
- 取数规则: 商品行为漏斗为权威。

## 业务事实

- [FACT-0003 小家电提价](../facts/FACT-0003-small-appliance-price-rise.md)
- [FACT-0007 小家电补货暂停](../facts/FACT-0007-small-appliance-supply-pause.md)
- [FACT-0009 小家电恢复补货](../facts/FACT-0009-small-appliance-restock.md)

## 关系备注

- 数据生成必须满足详情用户数 >= 加购用户数。
- 缺货影响可以通过品类有货率与本指标共同观察，但同步变化不自动证明因果。
