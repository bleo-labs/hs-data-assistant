---
type: metric
id: IND-0013
name: 商品详情用户数
status: demo
updated_at: 2026-07-18
---

# IND-0013 商品详情用户数

## 节点定位

- 用途: 用户表达具体商品兴趣的漏斗过程指标。
- 计算属性: 去重用户基础量；是否可加取决于主品类与主渠道归属契约。

## 定义或计算公式

统计月内浏览至少一个商品详情页的去重用户数。

## 可拆解为

### 结构拆解

- 渠道流量视角按区域、城市、渠道、来源和客户类型拆分。
- 商品行为视角按一级品类和客户类型拆分。

### 公式拆解

- 这是基础量，是 [访问详情转化率](IND-0017-visit-to-detail-rate.md) 的分子和 [详情加购转化率](IND-0018-detail-to-cart-rate.md) 的分母。

### 条件性拆解

- 商品行为表使用每位用户一个主浏览品类的合成口径，才能与渠道总量闭合。

## 适用范围

不等于商品曝光；第一版不含独立曝光指标。

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
- [SRC-0002](../sources/SRC-0002-product-behavior-funnel.md)
- 取数规则: 渠道总量与主品类切片必须在共同粒度闭合。

## 业务事实

- [FACT-0003 小家电提价](../facts/FACT-0003-small-appliance-price-rise.md)
- [FACT-0007 小家电补货暂停](../facts/FACT-0007-small-appliance-supply-pause.md)
- [FACT-0008 自营App低意向投放扩张](../facts/FACT-0008-app-low-intent-paid-traffic.md)
- [FACT-0009 小家电恢复补货](../facts/FACT-0009-small-appliance-restock.md)

## 关系备注

- 同一用户在真实业务可能浏览多个品类，本 Demo 通过主品类契约保证可审计。
- 不得跨来源表重复相加。
