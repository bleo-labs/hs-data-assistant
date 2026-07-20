---
type: metric
id: IND-0009
name: 渠道费用
status: demo
updated_at: 2026-07-18
---

# IND-0009 渠道费用

## 节点定位

- 用途: 利润计算基础，用于识别不同销售渠道产生的佣金和技术服务成本。
- 计算属性: 金额基础量；相同渠道费用口径下可加。

## 定义或计算公式

统计期内确认的第三方渠道佣金及相关技术服务费，单位为元。

## 可拆解为

### 结构拆解

- 按销售渠道拆分；第三方平台为主要组成。

### 公式拆解

- 第一版作为财务基础量。

### 条件性拆解

- 自营渠道如产生支付技术费，只能使用明确单列的费用口径。
- 不得按统一费率给所有渠道机械估算。

## 适用范围

适用于已确认渠道服务成本的交易。

## 拆分维度

- [DIM-0001 月份](../dimensions/DIM-0001-month.md)
- [DIM-0002 区域](../dimensions/DIM-0002-region.md)
- [DIM-0003 城市](../dimensions/DIM-0003-city.md)
- [DIM-0004 销售渠道](../dimensions/DIM-0004-sales-channel.md)
- [DIM-0006 一级品类](../dimensions/DIM-0006-category-l1.md)

## 数据源

- [SRC-0005](../sources/SRC-0005-financial-results.md)
- 取数规则: 渠道费用以财务结果月表为权威。

## 业务事实

- [FACT-0004 全渠道大促](../facts/FACT-0004-omnichannel-sale.md)

## 关系备注

- 渠道费用不是商品成本。
- 第三方平台是销售渠道，不代表平台入驻商家业务。
