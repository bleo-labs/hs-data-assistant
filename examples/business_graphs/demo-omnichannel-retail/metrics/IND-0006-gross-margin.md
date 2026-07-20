---
type: metric
id: IND-0006
name: 毛利率
status: demo
updated_at: 2026-07-18
---

# IND-0006 毛利率

## 节点定位

- 用途: 跨规模比较商品盈利质量。
- 计算属性: 比率派生指标；不可加、不可直接平均。

## 定义或计算公式

[毛利润](IND-0005-gross-profit.md) / [净销售额](IND-0003-net-sales.md)。

## 可拆解为

### 结构拆解

- 可按区域、渠道和一级品类观察，不存在可直接相加的结构项。

### 公式拆解

- [毛利润](IND-0005-gross-profit.md) / [净销售额](IND-0003-net-sales.md)

### 条件性拆解

- 分母为 0 时返回不可计算，不返回 0。

## 适用范围

适用于净销售额大于 0 的经营单元。

## 拆分维度

- [DIM-0001 月份](../dimensions/DIM-0001-month.md)
- [DIM-0002 区域](../dimensions/DIM-0002-region.md)
- [DIM-0003 城市](../dimensions/DIM-0003-city.md)
- [DIM-0004 销售渠道](../dimensions/DIM-0004-sales-channel.md)
- [DIM-0006 一级品类](../dimensions/DIM-0006-category-l1.md)

## 数据源

- [SRC-0005](../sources/SRC-0005-financial-results.md)
- 取数规则: 聚合毛利润与净销售额后重算，不平均明细毛利率。

## 业务事实

- [FACT-0003 小家电提价](../facts/FACT-0003-small-appliance-price-rise.md)
- [FACT-0004 全渠道大促](../facts/FACT-0004-omnichannel-sale.md)

## 关系备注

- 汇总时必须先汇总毛利润与净销售额，再相除。
- 不得平均城市、渠道或品类毛利率。
