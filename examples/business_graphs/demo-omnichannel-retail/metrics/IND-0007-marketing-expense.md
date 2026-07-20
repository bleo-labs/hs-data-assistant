---
type: metric
id: IND-0007
name: 营销费用
status: demo
updated_at: 2026-07-18
---

# IND-0007 营销费用

## 节点定位

- 用途: 获客与利润计算基础，用于观察付费投放和营销活动支出。
- 计算属性: 金额基础量；相同费用范围内可加。

## 定义或计算公式

统计期内确认的付费获客与营销活动支出，单位为元。

## 可拆解为

### 结构拆解

- 可按区域、城市、渠道和可识别流量来源拆分。

### 公式拆解

- 总营销费用作为基础量。
- 可归因营销费用是其中满足归因契约的子集。

### 条件性拆解

- 只有可归因营销费用可以进入 [新客获客成本](IND-0033-new-customer-acquisition-cost.md) 和 [付费投放产出比](IND-0034-paid-media-output-ratio.md)。

## 适用范围

总费用用于贡献利润；归因子集用于投放效率。

## 拆分维度

- [DIM-0001 月份](../dimensions/DIM-0001-month.md)
- [DIM-0002 区域](../dimensions/DIM-0002-region.md)
- [DIM-0003 城市](../dimensions/DIM-0003-city.md)
- [DIM-0004 销售渠道](../dimensions/DIM-0004-sales-channel.md)
- [DIM-0005 流量来源](../dimensions/DIM-0005-traffic-source.md)

## 数据源

- [SRC-0005](../sources/SRC-0005-financial-results.md)
- [SRC-0006](../sources/SRC-0006-marketing-campaigns.md)
- 取数规则: 财务表记录总营销费用；投放表只记录可归因子集。

## 业务事实

- [FACT-0004 全渠道大促](../facts/FACT-0004-omnichannel-sale.md)
- [FACT-0008 自营App低意向投放扩张](../facts/FACT-0008-app-low-intent-paid-traffic.md)

## 关系备注

- 不得把总营销费用与可归因营销费用重复相加。
- 来源不可识别的支出只能进入总费用，不能硬分摊到获客效率。
