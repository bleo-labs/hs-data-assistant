---
type: metric
id: IND-0011
name: 贡献利润率
status: demo
updated_at: 2026-07-18
---

# IND-0011 贡献利润率

## 节点定位

- 用途: 跨区域、渠道和品类比较经营质量。
- 计算属性: 比率派生指标；不可加、不可直接平均。

## 定义或计算公式

[贡献利润](IND-0010-contribution-profit.md) / [净销售额](IND-0003-net-sales.md)。

## 可拆解为

### 结构拆解

- 可按区域、渠道和一级品类比较，不存在可直接相加的结构项。

### 公式拆解

- [贡献利润](IND-0010-contribution-profit.md) / [净销售额](IND-0003-net-sales.md)

### 条件性拆解

- 分母为 0 时不可计算。

## 适用范围

适用于净销售额大于 0 且费用口径完整的经营单元。

## 拆分维度

- [DIM-0001 月份](../dimensions/DIM-0001-month.md)
- [DIM-0002 区域](../dimensions/DIM-0002-region.md)
- [DIM-0003 城市](../dimensions/DIM-0003-city.md)
- [DIM-0004 销售渠道](../dimensions/DIM-0004-sales-channel.md)
- [DIM-0006 一级品类](../dimensions/DIM-0006-category-l1.md)

## 数据源

- [SRC-0005](../sources/SRC-0005-financial-results.md)
- 取数规则: 聚合贡献利润与净销售额后重算。

## 业务事实

- [FACT-0001 南区老客分层触达](../facts/FACT-0001-south-repeat-operation.md)
- [FACT-0002 东区仓扩容](../facts/FACT-0002-east-warehouse-expansion.md)
- [FACT-0003 小家电提价](../facts/FACT-0003-small-appliance-price-rise.md)
- [FACT-0004 全渠道大促](../facts/FACT-0004-omnichannel-sale.md)
- [FACT-0006 东区仓系统切换](../facts/FACT-0006-east-warehouse-system-switch.md)
- [FACT-0007 小家电补货暂停](../facts/FACT-0007-small-appliance-supply-pause.md)
- [FACT-0008 自营App低意向投放扩张](../facts/FACT-0008-app-low-intent-paid-traffic.md)
- [FACT-0009 小家电恢复补货](../facts/FACT-0009-small-appliance-restock.md)

## 关系备注

- 汇总时先汇总分子分母再相除。
- 不得用平均明细利润率代表整体。
