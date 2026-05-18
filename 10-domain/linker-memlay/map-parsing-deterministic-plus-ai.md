---
title: map/ELF 解析的"确定性预处理 + AI 叙事"模式
status: draft
created: 2026-05-18
updated: 2026-05-18
tags: [linker, memlay, map-file, pyelftools, sop, #cross-psy]
sources:
  - "【原文】pyelftools（检索关键词：pyelftools ELFFile sections symbols）"
  - "【原文】GHS MULTI map 文件格式（检索关键词：Green Hills .map module summary）"
confidence: medium
related:
  - "[[ghs-multi-map-ai-analysis]]"
  - "[[ld-vs-lsl-vs-ghs-dialects]]"
next-action: "下周写最小预处理脚本：ELF→规范化 JSON（section/symbol/size），喂 AI 只做归因叙事"
---

# map/ELF 解析的"确定性预处理 + AI 叙事"模式

## 0. 一句话
**算术和提取交给脚本，叙事和假设交给 AI**。不让 LLM 数字节、不让脚本猜原因。

## 1. 为什么不直接喂 .map 文本
- 文本 map 格式随 toolchain/版本漂移，AI 解析脆弱、易**截断**与**算术幻觉**
  （见 [[ghs-multi-map-ai-analysis]] §4）。
- **优先解析 ELF 而非 .map**：ELF 有稳定结构，`pyelftools` 可确定性抽取
  section/symbol/size/地址【原文】。.map 仅作人读补充。
- 但 ELF 是公司产物：**留本地，不入库**；入库的是脚本与方法（CLAUDE.md §8）。

## 2. 模式（pipeline）
```
ELF(本地)  ──pyelftools脚本──▶  规范化JSON(脱敏)  ──▶  AI: 仅做归因/异常假设
   │                                                      │
   └── 数字真值来源（diff/sum 由脚本算）          人审 ◀──┘ 不接受AI给的新数字
```
1. 脚本输出：`{section, addr(相对化), size, top_symbols[]}` + 版本间 `size_delta`（脚本算）。
2. 脱敏：symbol/模块改名，地址平移为相对值。
3. 喂 AI 的**只有 JSON + 你的问题**："基于这些数字，给 size 增长的 3 条**可检验**假设，
   每条标如何验证；不要给我新的数字。"
4. 人按假设用脚本/链接器复核 → 成立的才升 `verified`。

## 3. 失败模式（本模式专属）
- **脱敏不彻底**：JSON 仍含专有命名 → 上传前过一遍改名表。
- **脚本与 AI 职责越界**：发现 AI 在回答里"重算"了数字 → 立即作废该结论。
- **ELF≠最终镜像**：post-build（locator/加密/压缩）后布局可能变，注明分析的是哪一阶段产物。

## 4. 我下周可以拿它做什么
写**最小**预处理脚本（pyelftools，~50 行）：ELF → 规范化 JSON；
拿一份脱敏样本跑通 §2 pipeline，记录 AI 是否还在偷偷算数（→ `50-experiments/`，关 OQ-001）。

## 5. #cross-psy 反哺
职责分离即偏差防御：把"数字真值"权限从 AI 收回给脚本，
是用架构手段消除"自动化自满"的发生条件，而非靠人每次自律。

## 6. 衔接
预处理脚本的设计细节归 `10-domain/binary-analysis/`（待 PR3，抽象化、不含公司代码）。
