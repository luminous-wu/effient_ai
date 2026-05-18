# 迭代日志

每个 PR 一行：日期 / 范围 / 关键决策 / 下一步。最新在上。

| 日期 | PR | 范围 | 关键决策 / ADR | 下一步 |
|---|---|---|---|---|
| 2026-05-18 | PR3 | `10-domain/binary-analysis/` 3 篇（工具抽象设计/调用图-WCSD/反汇编 ISA）+ `toolchain/` 2 篇（选项调优/告警分类） | 强化主线：AI 不解析、不给数字、不裁决 soundness；新增 OQ-005/006 | PR4：`20-general/prompt-engineering/` + `agentic-coding/`（含 MCP/Skills/Subagent 选型） |
| 2026-05-18 | PR2 | 充实 `10-domain/linker-memlay/`：memlay 架构辅助、方言对比+串味、map/ELF 确定性预处理+AI 叙事（3 篇） | 贯穿主线：AI 只做组合/叙事/枚举，硬件事实与数字真值由人/脚本提供；新增 OQ-003/004 | PR3：`10-domain/binary-analysis/`（pyelftools/Capstone 抽象化设计、调用图、预处理脚本细节）+ `toolchain/` 充实 |
| 2026-05-18 | PR1 | 骨架 + CLAUDE.md + README + .gitignore + 4 模板 + ADR-0000/0001 + 2 示例笔记 + 各域 README 占位 | ADR-0001：根目录布局 / 数字前缀 / 模板集中 `00-meta/templates/` | PR2：充实 `10-domain/linker-memlay/`（memlay 实战、LD/LSL 对比、map 解析） |
