---
title: Green Hills MULTI map 文件的 AI 辅助分析
status: draft
created: 2026-05-18
updated: 2026-05-18
tags: [toolchain, ghs-multi, map-file, memlay, sop]
sources:
  - "【原文】GHS MULTI Building Applications 手册（检索关键词：Green Hills .map linker map file format / -map）"
  - "【原文】Anthropic docs：long context / prompt engineering（检索关键词：Claude long context tips）"
confidence: medium
related:
  - "[[linker-script-ai-review]]"
next-action: "下周拿一份脱敏后的 release 构建 map，跑一次 §3 SOP，把节省时间记进 50-experiments"
---

# Green Hills MULTI map 文件的 AI 辅助分析

## 0. 一句话用途
把 GHS `.map`（section 分布、symbol 大小、Flash/RAM 占用）交给 AI 做**初筛与变化归因**，
人保留对**位精确结论**的最终裁决。

## 1. 适用 / 不适用
- 适用：版本间 size diff 归因、Top-N 占用 symbol 提取、未预期落段排查的"假设生成"。
- **不适用**：直接相信 AI 给出的精确字节数/地址；AI 对大文件易**截断与算术幻觉**【推断】。

## 2. IP 脱敏前置（强制，先做再喂）
1. 删除/改名公司专有 symbol 前缀与模块名（保留结构特征即可）。
2. 删除绝对地址中可识别布局的部分，或整体平移成相对值。
3. 大 map 先用脚本切到关注的 section/区间，**不整文件上传**。
4. 不附带对应 `.elf/.o`。

## 3. SOP（可直接照做）
1. 本地用脚本（grep/awk 或 pyelftools 旁路）抽出：section 表 + Top-N symbol。
2. 喂给 AI 的 prompt 框架：
   - 角色：嵌入式 toolchain 工程师，熟悉 GHS 链接器。
   - 任务：仅基于我给的文本，列出 ① 占用最大的 5 个 section ② 任何落在
     非预期 region 的 symbol（给出"为什么可疑"）③ 你**不确定**的地方单列。
   - 约束："不要计算我没给你的数字；不确定就说不确定；区分观察与推断。"
3. 对 AI 输出逐条人审（见 §4 失败清单）。
4. 关键结论手算/用 MULTI 自带工具复核后，才写进笔记并升 `verified`。

## 4. 嵌入式高频失败模式清单（人审必查）
- **算术幻觉**：sum/diff 字节数对不上 → 一律以工具为准【推断】。
- **section vs segment 混淆**：AI 常把 load/run address、VMA/LMA 说反。
- **对齐与填充**：忽略 `ALIGN`/padding，导致 size 归因错误。
- **截断**：长 map 中段被静默丢弃，结论以"看到的部分"为全集。
- **GHS 特有语法**：与 GNU LD 习惯混淆（GHS 的 memory/section 指令不同）。

## 5. 我下周可以拿它做什么
对最近一次 S32K 构建的 size 增长，用 §3 SOP 生成 3 条归因假设，
再用 MULTI 验证哪条成立——记录 AI 是否真的省了时间（→ `50-experiments/`）。

## 6. Open Questions
- GHS map 是否有稳定可解析格式，值得写个 pre-parser？（→ `00-meta/open-questions.md` OQ-001）
