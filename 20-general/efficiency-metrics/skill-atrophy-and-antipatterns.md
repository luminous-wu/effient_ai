---
title: 能力退化与反模式：vibe-coding / 过度自动化
status: draft
created: 2026-05-18
updated: 2026-05-18
tags: [efficiency-metrics, antipattern, skill-atrophy, #cross-buddhism, #cross-phil]
sources:
  - "【原文】自动化自满/技能退化通识（检索关键词：automation complacency, deskilling, automation bias）"
confidence: medium
related:
  - "[[measuring-net-productivity]]"
  - "[[agentic-tool-selection]]"
next-action: "下周选 1 项核心技能（如手读 map/反汇编）设'不借 AI'定期保养，记可观察退化指标"
---

# 能力退化与反模式

> 短期净提效为正，长期仍可能亏——亏在**判断力**。本笔记是反向 KPI。

## 1. 三个反模式（对我语境的具体危害）
- **vibe-coding**：靠"看起来对"推进链接脚本/启动代码——位精确领域里
  "能跑"≠"正确"，错误延迟到集成/路测才爆，代价不对称。
- **能力退化 (deskilling)**：长期不手读 map/反汇编 → 失去**校验 AI 的能力**，
  最终连"AI 错没错"都判不了 → 双人确认思想空心化（CLAUDE.md §7）。
- **过度自动化盲区**：MCP/hook/skill 链路一长，错误在中间被"自信地传递"，
  人只看末端绿灯（呼应 [[mcp-skills-subagents-hooks]] §3 假绿）。

## 2. 早期信号（自查）
- 不再能不借 AI 解释自己刚"完成"的链接脚本/反汇编。
- 跳过域笔记里的人审闸，因为"一直没出事"。
- prompt 越写越长，但说不清哪条在起作用（提示词膨胀）。
- 只记 AI 成功的案例。

## 3. 对策（制度化，不靠自律）
- **核心技能保养**：定期"不借 AI"做一次手读 map/反汇编基准，记是否变慢/出错。
- **人审闸不可裁撤**：SOP 里 ⛔ 步骤是结构性的，不因"长期没事"放松
  （安全关键遗产：偏差需理由+记录）。
- **基建有淘汰机制**：MCP/skill/hook 纳入月度回顾，摊不回成本就删。
- **失败入库**：`50-experiments/` 收集拖慢/翻车，对抗幸存者偏差。

## 4. 我下周可以拿它做什么
挑 1 项核心技能设"AI-free 保养"基准（手读一段 map，计时+查错），
作为长期退化探针的第 0 条记录。

## 5. #cross-buddhism / #cross-phil 反哺
不执着于工具（无常）：工具会变，可迁移的是判断力。
第二序思考：问的不是"这次快了多少"，而是"长期我变得更强还是更依赖"。
工具理性的边界——效率不应以判断力为代价支付。
