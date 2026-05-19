---
title: AUTOSAR OS 配置与 WCET/WCSD 的 AI 辅助
status: draft
created: 2026-05-18
updated: 2026-05-18
tags: [os-autosar, wcet, wcsd, scheduling, #cross-psy]
sources:
  - "【原文】AUTOSAR OS / OSEK 通识（检索关键词：AUTOSAR OS Task ISR Resource priority ceiling, OsStackMonitoring）"
  - "【推断】基于实时调度与静态分析局限"
confidence: low
related:
  - "[[call-graph-wcsd-ai-assist]]"
  - "[[arxml-ai-assist]]"
next-action: "下周列一份'OS 配置 × 栈/时序'交互清单，作为 WCSD 叠加 ISR 抢占的人审锚"
---

# AUTOSAR OS 配置与 WCET/WCSD 的 AI 辅助

## 0. 一句话
OS 配置决定**抢占与栈叠加模型**，二进制调用图不含这层。AI 解释配置可以，
**WCET/WCSD 数值与调度可行性裁决不行**（延续 [[call-graph-wcsd-ai-assist]] 主线）。

## 1. 易错点（AUTOSAR OS 规范细节，人审必查）
- **priority ceiling / Resource**：AI 易忽略 GetResource 抬升优先级对抢占链的改变。
- **ISR category 1 vs 2**：栈与可调度性语义不同，混淆即栈模型错。
- **抢占叠加 ≠ 最深调用链**：把单任务最深链当 WCSD，漏 ISR 嵌套叠加。
- **conformance class (BCC/ECC)**：多激活/事件语义差异被忽略。
- **stack monitoring 的局限**：OsStackMonitoring 是检测非证明，AI 易当"安全保证"。

## 2. SOP
1. OS 配置（脱敏 ARXML，见 [[arxml-ai-assist]]）作为**外部输入**并入栈/时序模型。
2. 确定性：每任务/ISR 局部栈 + 可解调用图由脚本算（[[call-graph-wcsd-ai-assist]] §4）。
3. **人按优先级/抢占模型叠加 ISR** ⛔ —— AI 仅生成"你是否漏了这些抢占边"的反问。
4. WCSD/WCET 数由脚本+人算或工具实测；AI 不给数。
5. 栈染色/实测复核才升 `verified`（CLAUDE.md §7）。

## 3. 我下周可以拿它做什么
做"OS 配置 × 栈/时序交互"可勾选清单（priority ceiling / ISR cat / 抢占叠加），
对一个脱敏小配置走一遍，记 AI 漏报的抢占边数（→ `50-experiments/`）。

## 4. #cross-psy 反哺
最危险是 AI 对"它本质无法保证的可调度性/WCSD"给自信结论。
把"给数字/给保证"的权限物理收回，是结构性防御而非每次靠自律。
