---
title: 用 AI 理解反汇编：ISA/ABI 失败模式
status: draft
created: 2026-05-18
updated: 2026-05-18
tags: [binary-analysis, disassembly, isa, abi, tricore]
sources:
  - "【原文】TriCore Architecture Manual（检索关键词：TriCore context CSA upper/lower context call/ret）— 本地，不入库"
  - "【推断】基于 LLM 语料分布，x86/ARM 远多于 TriCore"
confidence: low
related:
  - "[[pyelftools-capstone-workflow]]"
  - "[[ld-vs-lsl-vs-ghs-dialects]]"
next-action: "下周拿一段脱敏 TriCore 反汇编，测 AI 对 CSA/context 切换的解释正确率"
---

# 用 AI 理解反汇编：ISA/ABI 失败模式

## 0. 一句话
AI 读反汇编=**带强先验的猜**。先验来自 x86/ARM 语料；TriCore/嵌入式 ABI
是它的薄弱区——**当解释器用，不当真值源**。

## 1. 核心失败模式：ISA/ABI 先验污染
与方言串味同源（见 [[ld-vs-lsl-vs-ghs-dialects]] §0）：
- 语料里 **x86/ARM ≫ TriCore**【推断】→ 把 ARM 调用约定/寄存器语义套到 TriCore。
- **TriCore 特有机制**最易错：
  - **CSA / context save area**：`call/ret` 通过 upper/lower context 链，
    AI 常按"压栈"叙事错解【推断】。
  - **A 寄存器 vs D 寄存器**、地址/数据分离。
  - **circular/bit-reverse 寻址**、特殊 DSP 指令。
- **调用约定/参数传递**：寄存器分配 AI 易按通用 EABI 猜。

## 2. 提问硬规则
1. 钉死架构与手册版本："这是 **TriCore TC3xx**，按其 Architecture Manual 解释，
   **不要类比 ARM/x86**。"
2. 附寄存器/上下文模型小抄（你写的几行权威约定）作锚。
3. 要求区分 `【指令字面可见】` vs `【我按 ISA 推断，需手册核】`。
4. 涉及 context/中断/异常返回的解释默认 `confidence: low`，手册复核才采纳。

## 3. 适用 / 不适用
- 适用：把一段反汇编翻成可读控制流叙事、生成"这里为何这样"的待查问题。
- 不适用：相信 AI 对 TriCore 特殊机制的语义裁决；据其结论改 startup/异常代码。

## 4. 我下周可以拿它做什么
脱敏一小段含 `call`/context 切换的 TriCore 反汇编，
对照手册评 AI 解释正确率与"自信错误"占比 → 决定是否值得维护 ISA 锚小抄
（呼应 OQ-004 锚片段库思路）。

## 5. Open Questions → `00-meta/open-questions.md`
- OQ-006：是否维护"ISA 锚小抄"（TriCore/ARM 各一页）作为反汇编提问前缀？与 OQ-004 合并管理？
