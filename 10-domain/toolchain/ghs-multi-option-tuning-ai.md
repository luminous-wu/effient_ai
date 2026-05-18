---
title: Green Hills MULTI 编译选项调优的 AI 辅助
status: draft
created: 2026-05-18
updated: 2026-05-18
tags: [toolchain, ghs-multi, optimization, #cross-psy]
sources:
  - "【原文】GHS MULTI Building Applications / Optimization（检索关键词：Green Hills -O optimization options inlining）"
  - "【推断】基于 LLM 语料 GCC/Clang ≫ GHS"
confidence: low
related:
  - "[[ghs-multi-map-ai-analysis]]"
  - "[[compiler-warning-triage-ai]]"
next-action: "把本地 GHS 优化指南(Word)的要点抽象成'选项→效果→风险'表，不入原文件"
---

# Green Hills MULTI 编译选项调优的 AI 辅助

## 0. 一句话
AI 给的是 **GCC/Clang 直觉**，不是 GHS 事实。用它生成**待验证的调优假设**，
效果一律以**实测 size/perf 对比**为准。

## 1. 核心失败模式
- **选项串味**：把 `-O`/`-flto`/`-ffunction-sections` 等 GCC 习惯当 GHS 等价物，
  GHS 选项名/语义不同【推断】，且 AI 语气自信。
- **未实测的性能断言**：AI 会说"开 X 提速 Y%"——典型厂商传声筒式废话，
  违反 CLAUDE.md §9，直接拒收。
- **位精确副作用忽略**：优化对 volatile/内存序/对齐/段归属的影响被一笔带过。
- **安全关键交互**：优化 × MISRA/可追溯性 × 调试信息裁剪，AI 不会主动提醒权衡。

## 2. SOP
1. AI 任务：基于目标（size or speed or 可调试性）列**候选选项 + 各自风险/副作用**，
   每条标"GHS 中是否存在需我核实"。**不要它给数字。**
2. 你用 GHS 文档核对选项真实存在与语义。
3. 受控实验：单变量改选项 → 用 [[ghs-multi-map-ai-analysis]] / 实测对比 → 记 `50-experiments/`。
4. 站得住的结论才升 `verified`，并写回访日期（编译器升级会使其过期）。

## 3. 现有资产
本地《GHS MULTI 优化指南》(中文 Word) **不入库**（`.gitignore` 已挡）。
入库的是抽象化"选项→效果→风险→是否实测"表（next-action 产出）。

## 4. 我下周可以拿它做什么
抽 3 个最常用优化选项，按 §2 跑单变量实验，建立首条**实测**记录，
对抗"听说开这个更快"的口口相传。

## 5. #cross-psy 反哺
自动化自满在调优场景表现为"采信好听的百分比"。规则化"AI 不给数字、
数字只来自实测"，把诱惑从源头掐断。
