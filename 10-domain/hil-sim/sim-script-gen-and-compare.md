---
title: 仿真脚本生成与仿真-实测对比的 AI 辅助
status: draft
created: 2026-05-18
updated: 2026-05-18
tags: [hil-sim, qemu, lauterbach, t32, scripting]
sources:
  - "【原文】T32/QEMU 脚本通识（检索关键词：Lauterbach PRACTICE cmm script, QEMU machine, gdb monitor）"
  - "【推断】基于脚本生成与模型保真度通用经验"
confidence: low
related:
  - "[[disasm-comprehension-ai]]"
  - "[[log-trace-ai-analysis]]"
next-action: "下周让 AI 生成一段 T32 cmm 小脚本，记需人改的次数与最常见 API 幻觉"
---

# 仿真脚本生成与仿真-实测对比

## 0. 一句话
AI 写**脚本骨架**省样板时间；**API 真实性、模型保真度、差异归因**靠
文档/实测裁决，不靠 AI。

## 1. 失败模式
- **PRACTICE/脚本 API 幻觉**：T32 cmm、QEMU 选项 AI 易编命令/参数（语料稀，串味
  通用 shell/gdb 习惯）【推断】。
- **模型保真度盲区**：QEMU 不精确建模外设/时序/cache，AI 把"仿真过了"当"芯片上对"。
- **差异归因草率**：仿真≠实测差异，AI 倾向给单一顺因，忽略建模误差这一项。
- **平台串味**：把 ARM/QEMU 习惯套 TriCore 目标（同 ISA 串味，见 [[disasm-comprehension-ai]]）。

## 2. SOP
1. AI 生成脚本**骨架** + 标"我不确定该 API 是否存在/参数对"。
2. 对照官方文档核 API ⛔（不信 AI 记忆）。
3. 干运行/小范围跑通，再扩。
4. 仿真 vs 实测差异：先把**建模误差**列为候选因之一，再让 AI 辅助叙事其余假设。
5. 关键差异经实测确认才升 `verified`。

## 3. 我下周可以拿它做什么
让 AI 生成一段最小 T32 cmm（如设断点+读内存），记**API 幻觉次数**与
人改成本，评估它在脚本骨架上的真实净提效（→ `50-experiments/`）。

## 4. 衔接
仿真产生的 trace/log 分析走 [[log-trace-ai-analysis]]；
反汇编理解走 [[disasm-comprehension-ai]]。
