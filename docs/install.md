# 接入 Hs

## 前置条件

- 能保存或上传 Markdown 文件的 AI 环境。若希望自动读取/更新图谱和数据，优先使用具备工作区文件访问能力的环境。
- Git 用于取得与更新产品包；Bash 仅在使用本地校验、Demo 初始化或 Codex 适配器时需要。当前脚本面向 macOS / Linux；Windows 尚未做正式支持。

## 1. 获取通用核心包

在你准备存放 Hs 的本地目录中运行：

```bash
git clone https://github.com/<你的账号>/hs-data-assistant.git
cd hs-data-assistant
./scripts/validate-package.py
```

如果你已经克隆过仓库，更新时运行：

```bash
git pull
./scripts/validate-package.py
```

`skills/`、`templates/` 和你的私有 `business_graphs/` 共同构成 Hs 的通用核心。接下来按你的 AI 环境选择接入方式。

## 2A. Codex 适配器

Codex 目前支持一键复制到本机 Skill 目录：

```bash
./scripts/sync-to-codex.sh
```

这会把所有 Hs 技能复制到：

```text
~/.codex/skills/
```

如果技能列表没有立刻刷新，重启或刷新 Codex。

如果技能列表没有立刻刷新，重启或刷新 Codex。`agents/openai.yaml` 只是 Codex 的界面元数据，其他环境可以忽略。

## 2B. 其他 AI 环境

不需要安装到 `~/.codex`。将 `skills/` 中所需的 Skill 文档和相关 `references/` 放进项目知识库、长期指令或本次对话附件；再把你的私有 `business_graphs/` 与数据源材料提供给 AI。

建议第一次先从 `hs-entry` 开始，让它读取业务图谱并给出施工图；需要时再加入后续的 `hs-analysis`、`hs-research`、`hs-output` 等文档。不同平台的最小接入包与能力边界见[平台适配说明](platform-adapters.md)。

## Codex 中应看到的技能

- `hs-entry`
- `hs-onboarding`
- `hs-graph`
- `hs-analysis`
- `hs-data-contract`
- `hs-metric-audit`
- `hs-table-builder`
- `hs-research`
- `hs-output`
- `hs-feedback`

## 修改规则

优先修改仓库根目录里的文件：

```text
skills/
```

需要时再同步到对应平台。把本机安装目录里的技能文件视为适配器生成的副本，不要把它当作长期维护位置。

## 安装后验证

首次使用建议运行：

```bash
./scripts/bootstrap-demo.sh
```

然后按 [Demo 演练](demo-walkthrough.md) 走完一次施工图、数据契约、分析、审计和输出闭环。
