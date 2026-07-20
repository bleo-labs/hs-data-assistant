# 平台适配说明

Hs 的核心资产是 Markdown：Skill 工作流、业务图谱、指标树、维度、Source 卡和回写记录。它们不绑定某一个 AI 产品；差异只发生在“AI 如何发现这些文件、能否读写工作区、能否自动调用工作流”。

## 三档接入能力

| 环境类型 | 适用方式 | 能力边界 |
|---|---|---|
| 有本地工作区和文件工具的 Agent 环境 | 克隆仓库，把 `skills/` 与私有 `business_graphs/` 放在同一工作区 | 可完整执行读取、建表、审计、回写与文件维护 |
| 支持项目知识库/长期指令的对话环境 | 上传需要的 Skill、references、业务图谱和数据源文件 | 可完成施工图、分析与报告；文件的增删改查需要用户确认或手工保存 |
| 只支持单次对话的 AI 环境 | 作为本次任务附件提供最小材料包 | 可完成局部分析，不适合承担长期资产维护 |

## 第一次接入的最小材料包

无论使用哪种平台，第一次请优先提供：

1. `skills/hs-entry/SKILL.md`
2. `skills/hs-entry/references/project-graph.md`
3. `skills/hs-entry/references/routing-rules.md`
4. 对应业务的 `business_graphs/<business_id>/manifest.md`、索引、相关指标/维度/Source 卡
5. 本次任务需要的原始数据、报告或公开研究材料

任务进入分析、外部研究、输出或回写时，再补入对应 Skill 及其 references。这样既保留 Hs 的完整约束，也避免把所有文档一次性塞进上下文。

## Codex 适配器

Codex 是当前唯一提供一键安装体验的适配器：

```bash
./scripts/sync-to-codex.sh
```

它会把 `skills/hs-*` 复制至 `~/.codex/skills/`；各 Skill 下的 `agents/openai.yaml` 负责界面展示与命名调用。它们是 Codex 的便利层，不改变 Hs 的业务分析逻辑。

## 非 Codex 环境的使用原则

- 不要求出现 `$hs-entry` 等命令名。直接说“按 hs-entry 工作流处理”即可。
- 不承诺平台能自动沿链接读取全部文档；需要让 AI 明确读取当前任务关联的文件。
- 不承诺平台能直接编辑本地 Excel、运行脚本或创建文件。遇到这些能力缺口，应输出可执行的表结构、计算公式或回写清单，而不是假装已经写入。
- 私有业务图谱和原始数据仍应保留在用户控制的工作区，不因换平台进入公开仓库。

## 维护原则

所有通用规则只改仓库中的 `skills/`、`templates/`、`docs/` 与 `examples/`。各平台中的副本、项目知识库附件或自定义指令都是派生物；更新后从仓库重新同步或重新上传。
