---
title: SOP — 链接脚本变更评审
status: draft
created: 2026-05-18
updated: 2026-05-18
tags: [workflow, sop, linker, memlay, review]
sources: []
confidence: medium
related:
  - "[[linker-script-ai-review]]"
  - "[[ld-vs-lsl-vs-ghs-dialects]]"
  - "[[memlay-architecture-ai-assist]]"
next-action: "下次改 .ld/LSL 时照此跑，统计 §3 清单命中率，达标则把 prompt 固化进 40-prompts/（OQ-002）"
---

# SOP — 链接脚本变更评审

> 高风险变更（动 region/对齐/LMA-VMA/拷贝表）适用。**AI 是第一遍 reviewer，不是裁决者。**

## 开始条件
有一处链接脚本 diff（脱敏可复现的最小片段）+ 明确变更目标（如"把 .data 搬到 TCM"）。

## 步骤
1. **脱敏** ⛔：region/symbol 改名，地址相对化（[[memlay-architecture-ai-assist]] §4）。
2. **钉死方言 + 锚片段** ⛔：注明 GHS/LSL/LD 哪个 + 贴权威骨架
   （[[ld-vs-lsl-vs-ghs-dialects]] §2），否则必先验污染。
3. **AI 审查**：用 [[linker-script-ai-review]] §2 的 Self-Critique prompt
   （逐条复述语义 → 对照目标列偏差 → 末步自我反驳）。
4. **按清单人审** ⛔：LMA/VMA、对齐链、region 边界、通配匹配、初始化次序、ABI/ISA
   （[[linker-script-ai-review]] §3）。
5. **独立交叉验证** ⛔：手算关键地址 / 链接后 map 比对 / 异 prompt 复核
   —— 满足"双人确认思想"才升 `verified`（CLAUDE.md §7）。

## 完成判据
所有偏差有结论；关键地址经独立手段确认；变更经步骤 5 才标 `verified`。

## 不可全自动的点
1、2（输入受控）、4（位精确人审）、5（独立交叉验证）——全程无"AI 说没问题就放行"。
