# 00-meta/tools — 约定执行基建

把 CLAUDE.md 的约定从"自觉"变成"被执行"。这是知识库从信息变系统的关键件
（见 [[editor-and-ci-integration]]、[[skill-atrophy-and-antipatterns]] §3）。

## kb_check.py

零依赖（仅标准库 + git）。校验三类约定：

| 检查 | 依据 | 范围 |
|---|---|---|
| frontmatter 必填字段 + status/confidence 枚举 | CLAUDE.md §3 / §5 | `10/20/30/40-` 下的笔记（README、模板除外） |
| 双链 `[[slug]]` 不死链 | CLAUDE.md §3 | 全 .md（跳过代码块/行内代码） |
| 脱敏关键词黑名单 | CLAUDE.md §8 | 全 .md |

```bash
python3 00-meta/tools/kb_check.py            # 全仓库（CI 用）
python3 00-meta/tools/kb_check.py --staged   # 仅暂存（pre-commit 用）
```

- **概念占位允许表**：`file-slug / slug / 双链 / slick / YYYYMM` 不算真实双链
  （文档里讲解双链语法时会写到，非死链）。新增占位在脚本 `LINK_ALLOWLIST` 维护。

## sanitize-blacklist.txt

§8 的可执行化。**默认空**：真实专有 token 只有你知道，且本库正文合法地讨论
`.map/.elf/ARXML` 等主题词——预填会误伤自身。你按内部改名表逐条加正则。

## 启用 pre-commit（你自己执行一次）

Claude 不替你改 git config。手动启用：

```bash
git config core.hooksPath 00-meta/hooks
```

之后每次 commit 自动跑 `kb_check.py --staged`。确认是误报时才
`git commit --no-verify`（并考虑把误报模式加进允许表/调脚本）。

## CI 接线（可选）

任何 CI 跑 `python3 00-meta/tools/kb_check.py`（全量）即可，退出码即门禁。
注意 [[editor-and-ci-integration]] §1：这是确定性校验，**不引入 LLM 裁决**。

## 维护

脚本/黑名单变更记 `00-meta/iteration-log.md`；规则纳入月度回顾淘汰评估，
防止成新"配置熵"（[[mcp-skills-subagents-hooks]] §3）。
