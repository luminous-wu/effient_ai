---
title: Obsidian/Logseq + AI：把本仓库当 PKM 用
status: draft
created: 2026-05-18
updated: 2026-05-18
tags: [pkm-rag, obsidian, knowledge-management, #cross-phil]
sources:
  - "【原文】Obsidian 双链/属性通识（检索关键词：Obsidian backlinks, properties/frontmatter, dataview）"
  - "【推断】基于本仓库约定设计，未长期实测"
confidence: medium
related:
  - "[[personal-rag]]"
  - "[[cross-discipline-reading-assistant-v4]]"
next-action: "下周用 Obsidian 打开本仓库，验证双链/frontmatter 可用，跑一次孤儿笔记盘点"
---

# Obsidian/Logseq + AI：把本仓库当 PKM 用

## 0. 一句话
**这个 git 仓库本身就是 PKM**——Markdown + frontmatter + `[[双链]]` 已是可迁移底座；
AI 是其上的检索/综合层，不是存储层。

## 1. 已就位的底座（CLAUDE.md §3 落实）
- `[[file-slug]]` 双链不带路径 → Obsidian/Logseq 直接可用、可迁移。
- frontmatter（status/tags/confidence/related）= 机读元数据，供 Dataview/脚本/AI 过滤。
- 数字前缀目录 + 各域 README 索引 = 人工导航骨架。

## 2. AI 在 PKM 里做什么 / 不做什么
| 做 | 不做 |
|---|---|
| 跨笔记综合、找矛盾、提"你漏了"问题 | 当真值源（结论仍要回链原始来源 §4） |
| 按 frontmatter 批量体检（孤儿/过期/缺回访） | 自动改 status（状态机由人推进，CLAUDE.md §5） |
| 起草索引/回顾草稿 | 替代月度回顾的判断 |

## 3. 知识熵的工程化（对抗"信息墓地"）
用 frontmatter 做可查询体检（Dataview 或小脚本，AI 起草查询）：
- 孤儿笔记（无 `related`、无被链）。
- 久未 `updated` 的 `draft`（沉睡）。
- `verified` 但过 `next-action`/回访日期未复查。
→ 月度回顾（`00-meta/templates/retrospective.md`）消费这些清单。

## 4. 与阅读助手 v4 的接口
[[cross-discipline-reading-assistant-v4]] 是 PKM 的**上游输入器**：
跨学科阅读产出 → 若反哺工程/AI 使用 → 落对应笔记并打 `#cross-*`。
正文待你提供后补全（不臆造，CLAUDE.md §4）。

## 5. 我下周可以拿它做什么
Obsidian 打开仓库，写 1 条 Dataview 查询列出所有孤儿/沉睡 draft，
作为首次知识熵体检基线（→ 喂月度回顾）。

## 6. #cross-phil 反哺
工具可迁移性即第二序思考：底座是纯文本不是某 App，
AI/Obsidian 都是可替换的上层——不把判断力押在某个工具上。
