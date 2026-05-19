---
title: 核心技能 AI-free 季度保养清单
status: verified
created: 2026-05-18
updated: 2026-05-18
tags: [meta, skill-atrophy, review, #cross-buddhism]
sources: []
confidence: medium
related:
  - "[[skill-atrophy-and-antipatterns]]"
next-action: "每季度执行一次；下次回访：2026-08-18"
---

# 核心技能 AI-free 季度保养清单

> [[skill-atrophy-and-antipatterns]] §3 的执行化。本清单本身设 `verified`：
> 它是被执行的制度，不是待验证的观点。月度回顾模板已加强制行引用本表。

## 为什么

短期净提效为正仍可能长期亏在判断力。失去"不借 AI 也能校验 AI"的能力，
等于 CLAUDE.md §7 的双人确认思想空心化。本清单是反向 KPI 的执行体。

## 季度动作（每季选 ≥1 项，AI-free 完成并计时/记错）

- [ ] **手读一段 map**：不借 AI，解释 section/symbol 占用与一处异常。记耗时与是否出错。
- [ ] **手读一段反汇编**：TriCore 或 ARM，解释一处 call/context 或 ABI 行为，对照手册。
- [ ] **手算一次对齐/LMA-VMA**：给定片段，纸面推 region 边界，再用工具验证。
- [ ] **手追一条调用链/栈估算**：不借工具走一遍，再与脚本结果对比。

记录去 `50-experiments/`（类型标 `skill-maintenance`），与上季对比：变慢？错更多？

## 退化预警（任一为真即升级关注，写进当期回顾）

- [ ] 已无法不借 AI 解释自己刚"完成"的链接脚本/反汇编。
- [ ] 因"一直没出事"而跳过 SOP 的 ⛔ 人审闸。
- [ ] 提示词膨胀且说不清哪条在起作用。
- [ ] 只记 AI 成功案例（幸存者偏差）。

## 回访

每季度执行；本表 `next-action` 写下次日期。连续两季退化预警命中 →
开 ADR 重评 AI 使用边界（对抗知识熵与能力熵）。

## #cross-buddhism 反哺

不执着于工具（无常）：工具会更替，可迁移的资产是判断力本身。
保养的不是怀旧手艺，是校验权——交出校验权，就交出了对正确性的最终责任。
