---
title: 链接脚本片段的 AI 审查
status: draft
created: 2026-05-18
updated: 2026-05-18
tags: [linker, memlay, review, s32k, #cross-psy]
sources:
  - "【原文】NXP S32K5xx Reference Manual（检索关键词：S32K5xx memory map）— 本地，不入库"
  - "【原文】GNU LD / GHS linker 手册（检索关键词：LD SECTIONS ALIGN AT VMA LMA）"
confidence: low
related:
  - "[[ghs-multi-map-ai-analysis]]"
next-action: "下周拿一段脱敏 LD 片段（含 AT> 与 ALIGN）实跑审查 prompt，验证清单命中率"
---

# 链接脚本片段的 AI 审查

## 0. 一句话用途
用 AI 做链接脚本的**第一遍 reviewer**，专盯位精确/对齐/落段类错误，
人做最终裁决——**AI 在此处错误代价高，定位为辅助不为权威**。

## 1. 脱敏前置
改名专有 region/symbol，地址相对化，只留最小可复现片段；不附芯片 datasheet。

## 2. 审查 prompt 框架（Self-Critique 变体）
- 角色：资深 linker 工程师，谨慎、宁可标"不确定"也不猜。
- 输入：脱敏 LD 片段 + 目标（如"`.data` 的 LMA 应在 Flash、VMA 在 RAM"）。
- 要求：
  1. 先**逐条复述**该片段实际语义（VMA/LMA、对齐、填充）。
  2. 对照我的目标，列出**偏差**与**风险**，每条标 `【原文规则】/【推断】`。
  3. 最后做一次自我反驳："以上哪条我可能错？"
- 约束：不臆造未给出的 region/符号；不确定显式说明。

## 3. 嵌入式高频失败模式清单（AI 在链接脚本上易错点）
- **VMA/LMA 与 `AT>`**：把运行地址当加载地址，或忽略 `.data` 的 ROM→RAM 拷贝语义。
- **对齐**：`ALIGN`/`. = ALIGN()` 对后续 symbol 地址的连锁影响算错。
- **位精确/边界**：region `LENGTH` 边界、溢出、`>region AT>region2` 组合。
- **section 通配匹配**：`*(.text*)` 的贪婪匹配与顺序，KEEP/丢弃语义。
- **方言差异**：GHS vs GNU LD vs TriCore LSL 语法/语义不可互推【推断】。
- **原子性/初始化次序**：`.init_array`、C runtime 启动假设被忽略。
- **ABI/ISA**：TriCore vs ARM (S32K) 的对齐/段约定不同，AI 易跨架构串味。

## 4. 升 verified 的门槛
AI 结论必须经"另一独立手段"复核（手算地址 / 链接后 map 比对 /
另一模型交叉）方可从 `draft` → `verified`（见 CLAUDE.md §7 双人确认思想）。

## 5. 我下周可以拿它做什么
对 memlay 架构里一段 `.data`/`.bss` 放置规则，跑一次 §2 prompt，
统计清单(§3)命中率与误报率，决定这套 prompt 是否值得固化进 `40-prompts/`。

## 6. #cross-psy 反哺
自动化自满 (automation complacency)：AI 给出结构化、自信的审查结论时，
人最容易跳过验证。本笔记的"升级门槛(§4)"就是对抗该偏差的制度化手刹。
