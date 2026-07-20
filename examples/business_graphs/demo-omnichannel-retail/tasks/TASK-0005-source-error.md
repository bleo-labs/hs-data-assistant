# TASK-0005：缺失退款字段时如何阻断并回写

## 用户命题

把订单 Source 临时切换到 `datasets/bad_samples/order_transactions_missing_refund_amount.csv`，再尝试分析 2026 年 5 月净销售额下降原因，验证 Hs 是否会停止并正确路由修复。

## 任务启动标准

- 强度：轻量。本任务只验证契约识别、阻断和路由，不进入数据计算。
- 故障：`refund_amount` 字段缺失。
- 受影响指标：退款金额、净销售额、退款率、毛利润、贡献利润和对应归因。
- 路径：`hs-entry -> hs-data-contract -> hs-feedback -> hs-graph`。

## 预期施工图

```mermaid
flowchart LR
  A["Graph Scan 发现 Source 契约不一致"] --> B["数据契约标记 blocked"]
  B --> C["列出受影响指标与不可交付项"]
  C --> D["生成 Feedback 卡"]
  D --> E["修复 Source 路径或字段契约"]
  E --> F["重新审计后再启动原任务"]
```

## Scope Gate

- 不得把缺失退款金额当作 0。
- 不得使用其他月份比例代填后继续给确定性结论。
- 不得只写“数据可能不准”却照常输出完整归因。

## 交付要求

- 状态明确为 `blocked`。
- 缺失字段、受影响指标、影响范围和修复责任清楚。
- 生成反馈卡并指向 `hs-graph` 或 Source 维护动作。
- 修复前不产出完整业务结论。
