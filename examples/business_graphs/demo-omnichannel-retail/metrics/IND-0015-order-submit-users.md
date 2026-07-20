---
type: metric
id: IND-0015
name: 提交订单用户数
status: demo
updated_at: 2026-07-18
---

# IND-0015 提交订单用户数

## 节点定位

- 用途: 接近支付的购买意向过程指标。
- 计算属性: 去重用户基础量；按主品类契约可向上汇总。

## 定义或计算公式

统计月内成功提交至少一笔订单的去重用户数。

## 可拆解为

### 结构拆解

- 可按区域、城市、渠道、一级品类和客户类型拆分。

### 公式拆解

- 这是基础量，是 [加购提交转化率](IND-0019-cart-to-submit-rate.md) 的分子和 [提交支付转化率](IND-0020-submit-to-pay-rate.md) 的分母。

### 条件性拆解

- 必须小于或等于同粒度 [加购用户数](IND-0014-add-to-cart-users.md)。

## 适用范围

不代表支付成功；支付失败和取消可能发生在其后。

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

- [FACT-0004 全渠道大促](../facts/FACT-0004-omnichannel-sale.md)
- [FACT-0007 小家电补货暂停](../facts/FACT-0007-small-appliance-supply-pause.md)

## 关系备注

- 数据生成必须满足加购用户数 >= 提交订单用户数。
- 不得用支付订单数替代提交订单用户数。
