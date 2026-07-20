---
type: metric
id: IND-0032
name: 准时履约率
status: demo
updated_at: 2026-07-18
---

# IND-0032 准时履约率

## 节点定位

- 用途: 履约质量校准指标，用于识别仓库和配送是否稳定交付。
- 计算属性: 比率派生指标；不可加、不可直接平均。

## 定义或计算公式

准时完成订单数 / 已完成订单数。

## 可拆解为

### 结构拆解

- 可按区域、城市、仓库和一级品类观察。

### 公式拆解

- 准时完成订单数 / 已完成订单数

### 条件性拆解

- 取消订单不进入分母。
- 分母为 0 时不可计算。

## 适用范围

只适用于已进入履约且完成的订单。

## 拆分维度

- [DIM-0001 月份](../dimensions/DIM-0001-month.md)
- [DIM-0002 区域](../dimensions/DIM-0002-region.md)
- [DIM-0003 城市](../dimensions/DIM-0003-city.md)
- [DIM-0011 仓库](../dimensions/DIM-0011-warehouse.md)
- [DIM-0006 一级品类](../dimensions/DIM-0006-category-l1.md)

## 数据源

- [SRC-0007](../sources/SRC-0007-fulfillment.md)
- 取数规则: 由准时完成订单与已完成订单计算，取消订单不进入分母。

## 业务事实

- [FACT-0002 东区仓扩容](../facts/FACT-0002-east-warehouse-expansion.md)
- [FACT-0004 全渠道大促](../facts/FACT-0004-omnichannel-sale.md)
- [FACT-0006 东区仓系统切换](../facts/FACT-0006-east-warehouse-system-switch.md)

## 关系备注

- 汇总时必须汇总基础订单数再重算。
- 仓库系统事件应与长期履约能力变化区分。
