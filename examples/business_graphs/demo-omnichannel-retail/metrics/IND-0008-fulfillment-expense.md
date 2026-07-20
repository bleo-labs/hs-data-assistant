---
type: metric
id: IND-0008
name: 履约费用
status: demo
updated_at: 2026-07-18
---

# IND-0008 履约费用

## 节点定位

- 用途: 利润计算与履约效率观察的成本基础。
- 计算属性: 金额基础量；相同口径下可加。

## 定义或计算公式

统计期内确认的仓储、打包和配送费用，单位为元。

## 可拆解为

### 结构拆解

- 可按区域、城市、仓库、渠道和一级品类拆分。

### 公式拆解

- 第一版作为财务基础量，不使用单均成本反推。

### 条件性拆解

- 费用归属需与实际服务仓的当期映射一致。

## 适用范围

适用于进入履约环节的订单相关费用。

## 拆分维度

- [DIM-0001 月份](../dimensions/DIM-0001-month.md)
- [DIM-0002 区域](../dimensions/DIM-0002-region.md)
- [DIM-0003 城市](../dimensions/DIM-0003-city.md)
- [DIM-0011 仓库](../dimensions/DIM-0011-warehouse.md)
- [DIM-0004 销售渠道](../dimensions/DIM-0004-sales-channel.md)
- [DIM-0006 一级品类](../dimensions/DIM-0006-category-l1.md)

## 数据源

- [SRC-0005](../sources/SRC-0005-financial-results.md)
- 取数规则: 履约费用以财务结果月表为权威；履约表不记录费用。

## 业务事实

- [FACT-0002 东区仓扩容](../facts/FACT-0002-east-warehouse-expansion.md)
- [FACT-0004 全渠道大促](../facts/FACT-0004-omnichannel-sale.md)
- [FACT-0006 东区仓系统切换](../facts/FACT-0006-east-warehouse-system-switch.md)

## 关系备注

- 城市与仓库必须通过 [HIER-0001](../hierarchies/HIER-0001-region-city-warehouse.md) 对齐。
- 不得把履约费用变化直接等同于履约质量变化。
