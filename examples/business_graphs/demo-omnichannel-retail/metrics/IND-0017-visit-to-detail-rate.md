---
type: metric
id: IND-0017
name: 访问详情转化率
status: demo
updated_at: 2026-07-18
---

# IND-0017 访问详情转化率

## 节点定位

- 用途: 流量与商品兴趣匹配效率，用于识别流量质量。
- 计算属性: 比率派生指标；不可加、不可直接平均。

## 定义或计算公式

[商品详情用户数](IND-0013-product-detail-users.md) / [访问用户数](IND-0012-visit-users.md)。

## 可拆解为

### 结构拆解

- 可按区域、城市、渠道、流量来源和客户类型观察。

### 公式拆解

- [商品详情用户数](IND-0013-product-detail-users.md) / [访问用户数](IND-0012-visit-users.md)

### 条件性拆解

- 只在渠道流量粒度计算，不按品类拆分。
- 分母为 0 时不可计算。

## 适用范围

用于渠道入口流量质量，不代表商品详情到加购效率。

## 拆分维度

- [DIM-0001 月份](../dimensions/DIM-0001-month.md)
- [DIM-0002 区域](../dimensions/DIM-0002-region.md)
- [DIM-0003 城市](../dimensions/DIM-0003-city.md)
- [DIM-0004 销售渠道](../dimensions/DIM-0004-sales-channel.md)
- [DIM-0005 流量来源](../dimensions/DIM-0005-traffic-source.md)
- [DIM-0009 客户类型](../dimensions/DIM-0009-customer-type.md)

## 数据源

- [SRC-0001](../sources/SRC-0001-channel-traffic-funnel.md)
- 取数规则: 由访问用户与商品详情用户计算。

## 业务事实

- [FACT-0008 自营App低意向投放扩张](../facts/FACT-0008-app-low-intent-paid-traffic.md)

## 关系备注

- 汇总时先汇总分子分母再计算。
- 付费访问增长而本指标下降，只能说明流量匹配变弱，不能单独证明投放造成销售下滑。
