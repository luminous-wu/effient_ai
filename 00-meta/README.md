# 00-meta — 元信息入口

知识库的"管理后台"：决策、模板、迭代记录、未决问题。

## 索引

| 项 | 路径 | 用途 |
|---|---|---|
| ADR 模板 | `decisions/0000-adr-template.md` | 复制它写新决策 |
| 结构决策 | `decisions/0001-kb-structure-and-conventions.md` | 根目录布局 / 数字前缀 / 模板位置 |
| 笔记模板 | `templates/` | 工具调研 / 提示词记录 / 实验 / 回顾 |
| 迭代日志 | `iteration-log.md` | 每个 PR 一行 |
| 活跃问题 | `open-questions.md` | 未决问题，关闭附结论 |

## ADR 规则

- ADR 是**不可变历史**：只追加、不重写；被推翻时新开一条并在旧条目注明"被 NNNN 取代"。
- 编号四位递增（`0001`、`0002`…）。
- 任何影响结构/约定/工具选型的关键取舍都应留 ADR。

## 模板规则

新笔记从 `templates/` 复制，不直接在模板上写作。模板本身演化时记入 `iteration-log.md`。
