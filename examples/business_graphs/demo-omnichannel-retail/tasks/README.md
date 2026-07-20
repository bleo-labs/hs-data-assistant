# 全渠道零售 Demo 任务集

> 全部任务、数据和答案均为虚构演示，不对应任何真实企业。

## 使用顺序

1. 从任务卡复制“用户命题”。
2. 通过 `hs-entry` 启动，确认它先扫描本业务图谱并展示施工图。
3. 用户确认施工图后，再进入任务卡规定的 Hs 路径。
4. 用标准答案检查证据路径、结论边界和错误阻断，不要求逐字一致。

## 任务清单

| id | 任务 | 强度 | 主要能力 | 标准答案 |
|---|---|---|---|---|
| `TASK-0001` | 2026 年 5 月净销售额为什么下降 | 标准 | 内部归因 | [ANSWER-0001](expected_answers/ANSWER-0001-may-decline.md) |
| `TASK-0002` | 哪个区域综合表现最好 | 标准 | 多指标评价 | [ANSWER-0002](expected_answers/ANSWER-0002-region-performance.md) |
| `TASK-0003` | 下一季度目标要承担什么压力 | 重型 | 关系型测算 | [ANSWER-0003](expected_answers/ANSWER-0003-target-pressure.md) |
| `TASK-0004` | 新增品类如何更新业务图谱 | 标准 | 图谱维护 | [ANSWER-0004](expected_answers/ANSWER-0004-new-category.md) |
| `TASK-0005` | 缺失退款字段时如何阻断并回写 | 轻量 | 数据契约与反馈 | [ANSWER-0005](expected_answers/ANSWER-0005-source-error.md) |

## 自动证据

- [证据快照](evidence/task_evidence.md)
- [机器可读证据](evidence/task_evidence.json)
- 生成脚本：[build_demo_task_evidence.py](../generator/build_demo_task_evidence.py)

前三个任务的数字必须来自自动证据。后两个任务验证工作流行为，不把缺失数据补成虚构结论。
