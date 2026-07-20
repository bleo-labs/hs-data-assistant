# 数据源状态

> 全部数据均为固定种子生成的虚构数据，仅用于 Hs 演示。

## 已生成数据源

| id | 数据源 | 状态 | Source 卡 |
|---|---|---|---|
| `SRC-0001` | 渠道流量漏斗月表 | demo_ready | [打开](SRC-0001-channel-traffic-funnel.md) |
| `SRC-0002` | 商品行为漏斗月表 | demo_ready | [打开](SRC-0002-product-behavior-funnel.md) |
| `SRC-0003` | 订单交易月表 | demo_ready | [打开](SRC-0003-order-transactions.md) |
| `SRC-0004` | 商品库存月表 | demo_ready | [打开](SRC-0004-product-inventory.md) |
| `SRC-0005` | 财务结果月表 | demo_ready | [打开](SRC-0005-financial-results.md) |
| `SRC-0006` | 营销投放月表 | demo_ready | [打开](SRC-0006-marketing-campaigns.md) |
| `SRC-0007` | 履约月表 | demo_ready | [打开](SRC-0007-fulfillment.md) |
| `SRC-0008` | 维度映射表 | demo_ready | [打开](SRC-0008-dimension-mappings.md) |

## 生成与审计

- [数据生成契约](../design/data-contract.md)
- [数据生成器](../generator/generate_demo_data.py)
- [独立审计器](../generator/validate_demo_data.py)
- [最近一次审计报告](../datasets/audit/data_generation_audit.md)

## 硬约束

- Source 卡与对应 CSV 必须同时存在。
- 指标文件必须链接命中的 Source 卡，不能只写一个没有入口的编号。
- 数据生成必须先生成可加的基础量，再由公式计算派生指标。
- 跨 Source 的重复基础量必须通过一套权威值映射，不能分别随机生成。
- 隔离坏样本不属于任何正常 Source，不能进入分析范围。
