---
type: metric
id: IND-0010
name: 贡献利润
status: demo
updated_at: 2026-07-18
---

# IND-0010 贡献利润

## 节点定位

- 用途: 第一版最终经营目标，用于判断规模增长扣除直接经营成本后是否创造价值。
- 计算属性: 金额派生结果；由销售、成本和费用基础量闭合计算。

## 定义或计算公式

[毛利润](IND-0005-gross-profit.md) - [营销费用](IND-0007-marketing-expense.md) - [履约费用](IND-0008-fulfillment-expense.md) - [渠道费用](IND-0009-channel-fee.md)。

## 可拆解为

### 结构拆解

- 可按区域、渠道和一级品类拆分。
- 只有费用已按同口径合理归属时，明细贡献利润才能汇总。

### 公式拆解

- [毛利润](IND-0005-gross-profit.md) - [营销费用](IND-0007-marketing-expense.md) - [履约费用](IND-0008-fulfillment-expense.md) - [渠道费用](IND-0009-channel-fee.md)

### 条件性拆解

- 共同费用未分配时，明细贡献利润应披露未分配项，不得强行摊平。

## 适用范围

用于第一版经营质量判断，不等于会计净利润。

## 拆分维度

- [DIM-0001 月份](../dimensions/DIM-0001-month.md)
- [DIM-0002 区域](../dimensions/DIM-0002-region.md)
- [DIM-0003 城市](../dimensions/DIM-0003-city.md)
- [DIM-0004 销售渠道](../dimensions/DIM-0004-sales-channel.md)
- [DIM-0006 一级品类](../dimensions/DIM-0006-category-l1.md)

## 数据源

- [SRC-0005](../sources/SRC-0005-financial-results.md)
- 取数规则: 由毛利润减营销、履约和渠道费用逐分回算。

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

- 不得独立随机生成贡献利润。
- 分析规模增长时必须同步检查本指标与 [贡献利润率](IND-0011-contribution-margin.md)。
