---
type: metric
id: IND-0003
name: 净销售额
status: demo
updated_at: 2026-07-18
---

# IND-0003 净销售额

## 节点定位

- 用途: 核心销售结果，用于观察扣除退款后的真实销售贡献。
- 计算属性: 金额派生结果；由可加基础量计算后可按同口径汇总。

## 定义或计算公式

[GMV](IND-0001-gmv.md) - [退款金额](IND-0002-refund-amount.md)。

## 可拆解为

### 结构拆解

- 可按区域、渠道、一级品类和客户类型拆分；每条拆解需在同一口径重算。

### 公式拆解

- [GMV](IND-0001-gmv.md) - [退款金额](IND-0002-refund-amount.md)

### 条件性拆解

- 只有 GMV 与退款金额时间口径一致时公式才成立。

## 适用范围

适用于已支付交易的经营结果；不扣除商品成本和经营费用。

## 拆分维度

- [DIM-0001 月份](../dimensions/DIM-0001-month.md)
- [DIM-0002 区域](../dimensions/DIM-0002-region.md)
- [DIM-0003 城市](../dimensions/DIM-0003-city.md)
- [DIM-0004 销售渠道](../dimensions/DIM-0004-sales-channel.md)
- [DIM-0006 一级品类](../dimensions/DIM-0006-category-l1.md)
- [DIM-0009 客户类型](../dimensions/DIM-0009-customer-type.md)

## 数据源

- [SRC-0005](../sources/SRC-0005-financial-results.md)
- [SRC-0003](../sources/SRC-0003-order-transactions.md)
- 取数规则: 财务表为结果权威；必须由交易表的 GMV 与退款金额回算。

## 业务事实

- [FACT-0001 南区老客分层触达](../facts/FACT-0001-south-repeat-operation.md)
- [FACT-0003 小家电提价](../facts/FACT-0003-small-appliance-price-rise.md)
- [FACT-0004 全渠道大促](../facts/FACT-0004-omnichannel-sale.md)
- [FACT-0007 小家电补货暂停](../facts/FACT-0007-small-appliance-supply-pause.md)
- [FACT-0008 自营App低意向投放扩张](../facts/FACT-0008-app-low-intent-paid-traffic.md)
- [FACT-0009 小家电恢复补货](../facts/FACT-0009-small-appliance-restock.md)

## 关系备注

- 不得单独随机生成净销售额。
- 缺少 GMV 或退款金额任一基础量时停止计算。
