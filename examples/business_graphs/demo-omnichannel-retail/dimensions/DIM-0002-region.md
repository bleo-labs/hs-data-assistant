---
type: dimension
id: DIM-0002
name: 区域
status: demo
updated_at: 2026-07-18
---

# DIM-0002 区域

## 维度定义

企业用于经营管理的一级地理区域。

## 可取值或取值来源

- 北区
- 东区
- 南区

## 适用指标

适用于全部可按城市向上聚合的经营、流量、交易、库存、财务、营销与履约指标，完整清单见 [指标索引](../indexes/METRIC_INDEX.md)。

## 数据源字段

- [SRC-0008](../sources/SRC-0008-dimension-mappings.md)
- 取数规则: 区域由区域-城市时间有效映射取得，不在事实表重复生成。

## 相关 hierarchy

- [HIER-0001 区域-城市-仓库](../hierarchies/HIER-0001-region-city-warehouse.md)

## 注意事项

- 比率、客单价、利润率和获客成本在区域层必须从基础分子分母重算。
- 区域是管理和展示口径，不应被自动解释为因果变量。
