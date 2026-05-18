---
title: Agentic 编码工具选型判据（非盘点）
status: draft
created: 2026-05-18
updated: 2026-05-18
tags: [agentic-coding, tooling, selection, #cross-phil]
sources:
  - "【原文】各工具官方文档（检索关键词：Claude Code, Cursor, Aider, Cline, Continue docs）"
  - "【推断】基于公开资料与通用 agentic 编码经验，未逐一长期实测"
confidence: low
related:
  - "[[mcp-skills-subagents-hooks]]"
next-action: "下周只在一个真实小任务上对比 Claude Code vs 现有流程，记净提效（含返工）"
---

# Agentic 编码工具选型判据（非盘点）

> 不做"X 大工具盘点"。给**判据**和**对我语境的取舍**，工具只是判据的取值。

## 1. 我的语境约束（决定权重）
- **IP 边界**：公司代码/二进制不出内网 → 能否本地/隔离、是否默认外传是一票否决项。
- **安全关键评审文化**：要可追溯 diff、可人审、可解释，不要"魔法大改"。
- **中英双语**：中文意图 → 英文代码/产物，工具对混排的稳健性。
- 主语言是工具链/分析脚本（Python/构建/链接脚本），非大型 Web 工程。

## 2. 判据 > 工具
| 判据 | 为何对我重要 |
|---|---|
| 数据流向（本地/云）与可隔离性 | IP 一票否决 |
| 变更可审性（diff 粒度、是否解释意图） | 安全关键评审 |
| 可扩展性（MCP/脚本/hook 接入确定性工具） | 我要把 AI 限制在叙事层（见域笔记主线） |
| 失败时的可控性（能否单步/回滚/限制范围） | 对抗 vibe-coding |
| 学习/维护成本 vs 我真实任务频率 | 避免为低频任务养重工具 |

## 3. 取值（对我语境，批判性，未长期实测→conf low）
- **Claude Code（CLI/SDK）**：可编排确定性工具（脚本/MCP）、diff 可审、可 hook
  约束——与本仓库主线契合度最高【推断】。重点验证：隔离环境下的可用性。
- **Cursor/Cline/Continue（编辑器内）**：补全/局部重构顺手；对"确定性工具编排+
  可追溯评审"支持取决于配置；编辑器深绑是迁移成本。
- **Aider**：git 原生、diff 透明、轻量，适合脚本/小改；大型 agentic 编排弱。
- **"流行但对我可能无用"**：面向大型前端/全栈的 agent 演示，与我任务结构错配——
  不被 demo 说服（CLAUDE.md §9）。

## 4. 选型不是一次性
工具/模型迭代快，本笔记 `confidence: low`，**只有 §6 实测能升 verified**；
设回访日期，过期即重评（对抗知识熵）。

## 5. 我下周可以拿它做什么
选一个真实小任务（如写 §map 预处理脚本），用 Claude Code 跑一遍 vs 手写，
记**净提效=省时−返工−脱敏开销**，进 `50-experiments/`。

## 6. #cross-phil 反哺
第二序思考：问的不是"哪个工具强"，而是"选它会如何改变我的工作方式与能力结构"
（见 [[skill-atrophy-and-antipatterns]] 待 PR5）。工具理性需要边界。
