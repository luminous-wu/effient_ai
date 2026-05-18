---
title: 链接脚本方言对比（GNU LD / TASKING LSL / GHS）与 AI 串味
status: draft
created: 2026-05-18
updated: 2026-05-18
tags: [linker, memlay, dialects, ghs, lsl, ld]
sources:
  - "【原文】GNU LD manual（检索关键词：ld SECTIONS MEMORY AT VMA LMA ALIGN）"
  - "【原文】TASKING TriCore LSL（检索关键词：TASKING Linker Script Language memory section_layout）"
  - "【原文】GHS MULTI Building Applications（检索关键词：Green Hills linker directives MEMORY/SECTIONS .ld）"
confidence: low
related:
  - "[[linker-script-ai-review]]"
  - "[[memlay-architecture-ai-assist]]"
next-action: "请你校正下表（你是 GHS/TriCore 实务方），校正后升 confidence 并标 verified"
---

# 链接脚本方言对比与 AI 串味

> **本表 confidence: low，需你这个实务方校正后才升 `verified`**（CLAUDE.md §7）。
> 列出对比的主要目的不是教方言，而是**定位 AI 的跨方言串味失败模式**。

## 0. 核心失败模式：dialect contamination
AI 训练语料里 **GNU LD 远多于 LSL/GHS**【推断】。后果：
- 问 GHS/LSL 语法，常给 GNU LD 答案，且语气自信。
- 把 GNU LD 的 `AT>`、`. = ALIGN()`、`KEEP()` 习惯硬套到 LSL/GHS。
→ **对策**：prompt 中**显式钉死方言 + 粘贴一段权威片段做锚**，并要求"未在我给的片段中出现的语法一律标【推断】"。

## 1. 概念映射（待你校正）
| 概念 | GNU LD | TASKING LSL (TriCore) | GHS MULTI |
|---|---|---|---|
| 物理内存声明 | `MEMORY { }` | `memory { }`（in derivative/board） | `MEMORY { }`（GHS 语法，待核） |
| 段放置 | `SECTIONS { }` | `section_layout { }` | `SECTIONS { }`（指令集不同，待核） |
| 加载 vs 运行地址 | `AT>` / LMA-VMA | `copytable` / `run_addr`,`load_addr` | 待核（GHS 自有机制） |
| 对齐 | `. = ALIGN(n)` / `ALIGN()` | `align = n` 属性 | 待核 |
| 强制保留 | `KEEP()` | `keep` / 引用根 | 待核 |
| 启动拷贝表 | 手写 / 运行时拷贝 | LSL 自动生成 `copytable` | 待核 |

> 标"待核"的格子**不要相信 AI 填**——这正是它最容易编造的地方。请你逐格订正。

## 2. 对 AI 提问的硬规则
1. 第一句钉死："仅回答 **<GHS MULTI 5.x 的 .ld 语法>**，不要给 GNU LD 等价写法。"
2. 附 5–15 行**该方言的真实（脱敏）片段**作为锚。
3. 要求输出区分：`【你给的片段中可见】` vs `【我的推断，需你用手册核实】`。
4. 任何"拷贝表/启动序列"相关答案默认 `confidence: low`，必须手册或链接实测复核。

## 3. 我下周可以拿它做什么
用一段脱敏 GHS `.ld` 片段，做对照实验：
（a）不钉方言提问 vs（b）钉死方言+锚片段提问，统计串味次数 → 记 `50-experiments/`。

## 4. Open Questions → `00-meta/open-questions.md`
- OQ-004：是否值得维护一份"方言锚片段库"（每方言一段权威骨架），作为 prompt 前缀复用？
