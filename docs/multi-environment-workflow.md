# 多环境协作

这个仓库应是 Hs 的唯一产品真源。无论你在哪台电脑、哪个 AI 工作环境工作，都先更新仓库；只有使用 Codex 时才需要同步本机 Skill。

## 第一次在新电脑或新环境使用

```bash
git clone https://github.com/<你的账号>/hs-data-assistant.git
cd hs-data-assistant
./scripts/validate-package.py
```

如果该环境是 Codex，再运行：

```bash
./scripts/sync-to-codex.sh
```

其他 AI 环境则按[平台适配说明](platform-adapters.md)把所需的 Skill 与私有业务图谱接入项目知识库或工作区。

如果要使用 Demo，再运行：

```bash
./scripts/bootstrap-demo.sh
```

## 每次开始工作前

```bash
git pull --ff-only
./scripts/validate-package.py
```

若使用 Codex，再补一步 `./scripts/sync-to-codex.sh`。上述动作分别确保：拿到另一台电脑的最新版本、产品包没有结构错误、当前运行环境使用的是最新方法文件。

## 修改 Hs 后

1. 只修改仓库里的 `skills/`、`docs/`、`templates/`、`examples/` 或 `scripts/`。
2. 不直接修改任何运行环境生成的副本；Codex 的副本位于 `~/.codex/skills/hs-*`。
3. 运行校验，查看变更范围，确认无误后再提交并推送。

```bash
./scripts/validate-package.py
git status
git add <确认过的文件>
git commit -m "说明这次改了什么"
git push
```

## 发生冲突时

如果 `git pull --ff-only` 提示无法快进，不要强行覆盖或重置。先保留本地修改、查看两端分别改了什么，再决定合并方式。业务图谱和用户私有数据不应进入这个产品仓库，因此通常不会和通用 Skill 的修改混在一起。

## 发布版本时

只有在 Demo、安装、校验和关键真实 Case 都跑通后，才创建版本 tag，例如 `v0.1.0`。日常小修改先正常提交；不要每次改一个措辞就发布新版本。
