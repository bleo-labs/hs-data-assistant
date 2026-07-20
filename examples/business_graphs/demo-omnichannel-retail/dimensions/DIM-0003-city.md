---
type: dimension
id: DIM-0003
name: 城市
status: demo
updated_at: 2026-07-18
---

# DIM-0003 城市

## 维度定义

区域下的最低稳定经营地理单元。

## 可取值或取值来源

- 北区: 北辰市、云岭市
- 东区: 东澜市、海岳市
- 南区: 南浦市、榕川市

以上均为虚构标签。

## 适用指标

适用于流量、交易、库存、财务、营销和履约的城市明细，完整清单见 [指标索引](../indexes/METRIC_INDEX.md)。

## 数据源字段

- [SRC-0001](../sources/SRC-0001-channel-traffic-funnel.md)
- [SRC-0002](../sources/SRC-0002-product-behavior-funnel.md)
- [SRC-0003](../sources/SRC-0003-order-transactions.md)
- [SRC-0004](../sources/SRC-0004-product-inventory.md)
- [SRC-0005](../sources/SRC-0005-financial-results.md)
- [SRC-0006](../sources/SRC-0006-marketing-campaigns.md)
- [SRC-0007](../sources/SRC-0007-fulfillment.md)
- [SRC-0008](../sources/SRC-0008-dimension-mappings.md)
- 取数规则: 事实表使用 `city`，区域和仓库关系由映射表校验。

## 相关 hierarchy

- [HIER-0001 区域-城市-仓库](../hierarchies/HIER-0001-region-city-warehouse.md)

## 注意事项

- 城市结果应先由城市基础量计算，再向区域汇总可加量。
- 不可加指标必须在目标层级重算，不能平均城市结果。
