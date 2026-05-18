---
title: SOP — 版本 size 回归排查（map/ELF）
status: draft
created: 2026-05-18
updated: 2026-05-18
tags: [workflow, sop, map-file, toolchain]
sources: []
confidence: medium
related:
  - "[[ghs-multi-map-ai-analysis]]"
  - "[[map-parsing-deterministic-plus-ai]]"
  - "[[context-engineering]]"
next-action: "下次真出现 size 回归时照此跑一遍，记净提效进 50-experiments，再决定升 verified"
---

# SOP — 版本 size 回归排查

> 把三篇域笔记收敛成一条可照做流程。**人审闸标 ⛔，不可跳过。**

## 开始条件
某次构建 Flash/RAM 占用异常增长，有"前/后"两个本地构建产物（ELF 优先于 .map）。

## 步骤
1. **脚本提取（真值层）**：pyelftools 旁路抽 前/后 的 section/symbol/size，
   `size_delta` 由脚本算。→ 产出规范化 JSON。
2. **脱敏** ⛔：symbol/模块名过改名表，地址相对化（[[context-engineering]] §1）。
3. **AI 仅做归因假设**：喂 JSON + "给 3 条可检验的增长假设，每条写如何验证，
   不要给我新数字"（[[map-parsing-deterministic-plus-ai]] §2）。
4. **人审每条假设** ⛔：对照 [[ghs-multi-map-ai-analysis]] §4 失败清单
   （算术幻觉/对齐填充/截断/方言）。
5. **确定性验证**：用脚本/链接器逐条证伪或证实，定位真实根因。
6. **记录**：根因 + AI 假设命中情况 → `50-experiments/`。

## 完成判据
根因经确定性手段确认；AI 命中率与净提效已记录；结论标 `verified` 仅当步骤 5 通过。

## 不可全自动的点
2（脱敏，无 git 兜底时风险最高）、4（假设人审）、5（真值裁决）。
