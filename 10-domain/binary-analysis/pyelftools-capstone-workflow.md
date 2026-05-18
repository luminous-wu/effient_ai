---
title: pyelftools + Capstone 分析工具的抽象化设计
status: draft
created: 2026-05-18
updated: 2026-05-18
tags: [binary-analysis, pyelftools, capstone, elf, architecture]
sources:
  - "【原文】pyelftools（检索关键词：pyelftools ELFFile iter_sections symbol_tables DWARF）"
  - "【原文】Capstone（检索关键词：Capstone disassembler CS_ARCH CS_MODE details groups）"
confidence: medium
related:
  - "[[map-parsing-deterministic-plus-ai]]"
  - "[[call-graph-wcsd-ai-assist]]"
next-action: "下周把 ELF→规范化 IR(JSON) 的 schema 草拟出来（section/symbol/reloc/insn），作为脚本与 AI 的契约"
---

# pyelftools + Capstone 分析工具的抽象化设计

> **抽象化设计笔记，不含公司代码**（CLAUDE.md §8）。只记架构与 AI 边界。

## 0. 一句话
确定性核心（pyelftools 取结构 + Capstone 反汇编）产出**机读 IR**；
AI 只消费 IR 做叙事/假设，**不参与解析与算术**。

## 1. 分层（职责即偏差防线）
| 层 | 工具 | 产出 | 谁可信 |
|---|---|---|---|
| L0 解析 | pyelftools | sections / symbols / relocs / DWARF | 确定性，真值 |
| L1 反汇编 | Capstone | 指令流 + 操作数 + 分组(call/jump) | 确定性，真值 |
| L2 规范化 | 自研脚本 | 统一 JSON IR（脱敏） | 确定性 |
| L3 叙事 | LLM | 异常假设、可读解释、审查清单 | **不可信，需复核** |

切口在 **L2/L3 之间**：IR 是脚本与 AI 的契约，AI 拿不到原始 ELF。

## 2. IR 契约要点（下周要落的 schema）
- 稳定字段：`sections[]`(name,addr相对,size,flags)、`symbols[]`(name脱敏,bind,size)、
  `relocs[]`(type,sym)、`insns[]`(addr相对,mnemonic,op_str,groups)。
- 地址一律相对化；symbol/段名过改名表。
- 版本/构建阶段标注（pre/post-locator），避免"分析错对象"。

## 3. 失败模式（设计时就要防）
- **DWARF 缺失/裁剪**：release 无调试信息时 symbol/类型信息退化，AI 易据残缺信息编造。
- **Capstone 架构/模式选错**：TriCore vs ARM thumb/arm 模式错 → 指令流全错；
  TriCore 支持需确认（Capstone 多架构但覆盖度不均，**待核**）【推断】。
- **数据被当指令**：常量池/跳转表反汇编成"指令"，AI 不会自己识别 → IR 层需标 data/code。
- **重定位未解析**：静态文件里地址是占位，AI 把占位地址当真。

## 4. 我下周可以拿它做什么
草拟 IR JSON schema（仅 schema，不含真实数据），定下 L2/L3 契约 →
为 [[call-graph-wcsd-ai-assist]] 与 [[map-parsing-deterministic-plus-ai]] 提供共用输入。

## 5. Open Questions → `00-meta/open-questions.md`
- OQ-005：Capstone 对 TriCore (TC3xx) ISA 的覆盖度与正确性是否够用？需小样本实测。
