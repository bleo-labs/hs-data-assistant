# Hs Data Assistant 仓库说明

这个仓库是 Hs Data Assistant 技能组的产品真源。

## 产品范围

Hs Data Assistant 帮用户把业务问题转成：

- 业务认知地图
- 指标树资产
- 内部经营分析
- 外部研究和对标结论
- 可读、可交付的报告和输出物

## 真源规则

技能文件优先在这里修改：

```text
skills/
```

如果当前运行环境是 Codex，再同步到本机：

```bash
./scripts/sync-to-codex.sh
```

不要把 `~/.codex/skills/hs-*` 当作产品真源直接维护；它只是 Codex 适配器的同步副本。

## 隐私规则

可复用的技能、模板、文档和示例，不能依赖某一个具体的私有业务、公司、项目或历史案例。

允许：

- 通用经营分析规则
- 虚构或公开安全的演示案例
- 空模板
- 可复用的文件契约

不允许：

- 私有公司数据
- 真实私有业务图谱
- 用户本地专属路径
- 只对某一个历史案例成立的规则

真实用户图谱应放在这个包之外，通常放在工作环境的 `business_graphs/` 目录下。

## Skill 设计规则

遵守 Skill Creator 的通用原则：

- `SKILL.md` 保持简洁
- 通过 `references/` 做渐进披露
- 确定性校验放进 `scripts/`
- 资产、模板和指令分开
- 避免同一规则在多个文件里重复维护

## 校验

每次认为工作完成前，运行：

```bash
./scripts/validate-package.py
```

如果修改了技能，并且需要更新本机 Codex 安装版，运行：

```bash
./scripts/sync-to-codex.sh
```

## 当前 Skill 组合

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
