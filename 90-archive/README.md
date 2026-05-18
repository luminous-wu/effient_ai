# 90-archive — 归档

知识熵管理的出口。过时/被推翻/长期沉睡的内容移到这里，**不删除**——保留
"我曾经怎么想、为什么放弃"的轨迹。

## 约定
- 路径：`90-archive/YYYYMM/<原文件名>`，**不改原文件名**。
- frontmatter：`status: archived`，并在正文顶部加一行"归档原因 + 取代者链接（如有）"。
- 触发：月度回顾（`00-meta/templates/retrospective.md`）中识别的 `outdated` /
  长期 `draft` 沉睡笔记。
- ADR 不进归档：ADR 是不可变历史，被取代时用 `superseded-by` 字段标注，留在原处。
