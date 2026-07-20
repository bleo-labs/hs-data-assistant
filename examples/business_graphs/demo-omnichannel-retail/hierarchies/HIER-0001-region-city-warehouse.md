---
type: hierarchy
id: HIER-0001
name: 区域-城市-仓库
status: demo
updated_at: 2026-07-18
---

# HIER-0001 区域-城市-仓库

## 层级目的

区域与城市是经营管理关系，城市与仓库是履约服务关系；两者不是同一种父子关系，因此用一个 hierarchy 中控时间有效映射。

## 参与维度

- [区域](../dimensions/DIM-0002-region.md)
- [城市](../dimensions/DIM-0003-city.md)
- [仓库](../dimensions/DIM-0011-warehouse.md)

## 映射关系

| 区域  | 城市  | 默认服务仓 |
| --- | --- | ----- |
| 北区  | 北辰市 | 北区仓   |
| 北区  | 云岭市 | 北区仓   |
| 东区  | 东澜市 | 东区仓   |
| 东区  | 海岳市 | 东区仓   |
| 南区  | 南浦市 | 南区仓   |
| 南区  | 榕川市 | 南区仓   |

## 适用范围

适用于城市向区域汇总，以及库存、履约、财务结果之间的城市仓库对齐。

## 例外规则

- 城市实际服务仓以当月有效映射为准。
- 映射缺失时，库存与履约分析应阻断，不得默认使用区域仓。
- 城市基础量先计算，再向区域汇总；比率在区域层重算。

## 支撑数据源

- [SRC-0008](../sources/SRC-0008-dimension-mappings.md)
- [SRC-0004](../sources/SRC-0004-product-inventory.md)
- [SRC-0007](../sources/SRC-0007-fulfillment.md)
- 取数规则: 映射表为关系权威；库存与履约表用于检验实际组合。

## 影响指标

- [有货率](../metrics/IND-0025-in-stock-rate.md)
- [履约费用](../metrics/IND-0008-fulfillment-expense.md)
- [准时履约率](../metrics/IND-0032-on-time-fulfillment-rate.md)
- [贡献利润](../metrics/IND-0010-contribution-profit.md)
