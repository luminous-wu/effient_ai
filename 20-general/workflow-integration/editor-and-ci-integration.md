---
title: 编辑器与 CI 中的 AI：守约定，不做创作
status: draft
created: 2026-05-18
updated: 2026-05-18
tags: [workflow-integration, ci, hooks, automation]
sources:
  - "【原文】git hooks / CI 通识（检索关键词：pre-commit hook, CI lint markdown, link checker）"
  - "【推断】基于本仓库约定自动化需求"
confidence: medium
related:
  - "[[mcp-skills-subagents-hooks]]"
  - "[[obsidian-ai-pkm]]"
next-action: "下周写最小 pre-commit：frontmatter 必填字段 + 双链死链 + .gitignore 脱敏前置检查"
---

# 编辑器与 CI 中的 AI：守约定，不做创作

## 0. 一句话
集成层的正当职责是**强制执行已定约定**（确定性校验），不是让 AI 在
commit/CI 里自由生成——后者把幻觉送进不可逆环节。

## 1. 该自动化的（确定性，非 AI）
- frontmatter 必填字段/枚举值校验（status ∈ 状态机）。
- `[[slug]]` 死链检查（呼应 [[personal-rag]] §3 回链幻觉）。
- **脱敏前置闸**：提交含可疑专有命名/疑似未脱敏片段 → 阻断
  （CLAUDE.md §8 自动化，比 `.gitignore` 更进一步）。
- 孤儿/沉睡 draft 报表（喂月度回顾）。
→ 这些是脚本/linter，**不需要也不应该用 LLM 裁决**。

## 2. AI 在集成层的有限位置
- 起草上述校验脚本/规则（人审后入库）。
- PR/commit 摘要草稿（人改定）。
- **不做**：自动改代码/笔记内容、自动升 status、CI 里"AI 说没问题就过"。
  —— 同 [[mcp-skills-subagents-hooks]] §3 假绿风险。

## 3. 失败模式
- **hook 静默失败**：脱敏闸逻辑漏，给虚假安全（不对称风险，最危险）。
- **AI 进了不可逆环节**：commit/CI 里 AI 生成被自动接受，错误无人审。
- **配置熵**：hook/CI 规则堆积无人维护，成新信息墓地（纳入月度回顾淘汰）。

## 4. 我下周可以拿它做什么
写最小 pre-commit（纯脚本）：必填 frontmatter + 死链 + 脱敏关键词黑名单，
让 CLAUDE.md §4/§8 从"自觉"变"被执行"（呼应 OQ-007/009，回访机制 PR）。

## 5. 安全关键遗产
集成层 = 评审与可追溯的自动化下沉：闸是结构性的，
不因"长期没触发"裁撤（见 [[skill-atrophy-and-antipatterns]] §3）。
