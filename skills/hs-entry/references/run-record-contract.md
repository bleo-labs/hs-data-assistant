# Run Record Contract

`run_record` 是一次 Hs 任务的最小运行证据。`project_graph` 记录“计划怎么做”，`run_record` 记录“实际做了什么、在哪里偏离、如何被纠正”。

它不是完整思维链、工具日志或项目管理状态机。只记录足以复盘、回写和回归验证的关键事件。

## 1. 适用范围

- 标准任务和重型任务：必须建立运行记录。
- 轻量任务：默认不建立；一旦出现用户纠正、漏读、漏算、范围跑偏或需要回写，立即补建。
- 如果当前 AI 环境可以写文件，运行记录必须和 `project_graph` 放在同一任务目录。
- 如果当前环境不能写文件，用相同字段在对话或交接信息中维护“运行记录增量”，并在可写环境中补存。

默认位置：

```text
outputs/hs_entry/{YYYYMMDD}_{task_name}/
  project_graph.md
  run_record.md
  artifacts/
  regression/
```

`regression/` 只在本任务产生回归样本时创建。

## 2. 最小结构

初始化时优先复制 `templates/run/run_record.md`，也可以按以下同等结构生成：

```markdown
# Hs Run Record

## Run
- run_id:
- task:
- project_graph:
- business_graph:
- started_at:
- current_status: running / blocked / completed

## Events

### EVT-0001
- event_type: run_started
- node_id: N01
- skill: hs-entry
- action: 用户确认施工图，开始执行
- inputs: `任务启动卡路径`；`project_graph 路径`
- sources_read: `业务树 manifest 路径`；`指标索引路径`
- output: 进入下一节点
- observation: 无
- anomaly: 无
- next: N02
```

事件编号在同一任务内递增，不覆盖旧事件。

## 3. 什么时候追加事件

只在以下节点追加，不记录每次文件读取或工具调用：

1. **任务启动**：用户确认施工图，运行正式开始。
2. **节点完成**：某个 Project Graph 节点形成了可交接产物。
3. **节点阻塞**：缺数据、缺口径、校验失败或范围未命中，无法放行。
4. **用户纠正**：用户指出结果错误、遗漏、跑偏或不可用。
5. **修改提案**：`hs-feedback` 已定位根因并提出回写方案。
6. **回归验证**：修改后用原 Case 或最小 Case 重跑并得到验证结果。
7. **任务收口**：任务完成或明确停止。

推荐的 `event_type`：

- `run_started`
- `node_completed`
- `node_blocked`
- `user_correction`
- `change_proposed`
- `change_applied`
- `regression_verified`
- `run_closed`

## 4. 记录规则

- `node_id` 必须对应 `project_graph`；临时新增节点要先说明与原节点的关系。
- `inputs`、`sources_read` 和 `output` 优先写文件链接、Source 卡编号、表名或产物路径，不复制大段正文。
- `observation` 只写本节点实际观察到的事实。
- `anomaly` 只写偏离计划、校验异常或用户纠正；没有就写“无”。
- 结论强度变化、范围降级、数据替代和关键假设必须留痕。
- 不记录隐藏思维链，不记录与复盘无关的细碎操作，不复制原始敏感数据。
- 私有业务事实只留在私有任务目录；不得因记录运行事件而进入公开产品包。

## 5. 下游 Skill 的责任

标准或重型任务中，每个 Hs Skill 必须：

1. 开始前读取 `project_graph` 与当前 `run_record`。
2. 只执行分配给自己的节点。
3. 节点完成或阻塞时追加一条事件，并链接本节点产物。
4. 发现实际范围小于施工图范围时，记录异常并触发 Scope Gate 降级。
5. 收到用户纠正时，停止扩写原结论，追加 `user_correction`，转交 `hs-feedback`。

`run_record` 提供复盘证据，但不能替代数据契约、指标审计、业务图谱或最终报告。
