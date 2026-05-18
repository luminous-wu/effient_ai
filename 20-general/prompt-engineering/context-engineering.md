---
title: 上下文工程：放什么、不放什么、用什么锚
status: draft
created: 2026-05-18
updated: 2026-05-18
tags: [prompt-engineering, context, rag, ip-boundary]
sources:
  - "【原文】Anthropic docs：long context tips / retrieval（检索关键词：Claude long context, place instructions, grounding）"
confidence: medium
related:
  - "[[map-parsing-deterministic-plus-ai]]"
  - "[[pyelftools-capstone-workflow]]"
next-action: "下周给一类高频任务（map 归因）写一份'上下文清单'：必放/禁放/锚片段，模板化"
---

# 上下文工程：放什么、不放什么、用什么锚

> 上下文工程 = 决定**喂什么、不喂什么、以什么作锚** —— 在本仓库它同时是
> 抗错手段和 **IP 边界执行点**。

## 1. 三条硬规则
1. **机读 IR 优先于原始产物**：喂规范化 JSON，不喂整份 .map/.elf 文本
   （见 [[map-parsing-deterministic-plus-ai]]）。原始产物=脆弱解析+截断+IP 风险。
2. **锚片段制度化**：方言/ISA/约定类问题，前缀一段你写的权威小抄
   （呼应 OQ-004/006 锚库）。锚 > 解释。
3. **上下文即 IP 闸门**：放进 context 的每段都过一遍脱敏（改名/相对化/删专有常量）。
   "能不能放进 prompt" 与 "能不能入库" 同一把尺（CLAUDE.md §8）。

## 2. 必放 / 禁放（按任务建清单）
| 必放 | 禁放 |
|---|---|
| 任务目标 + 成功判据 | 整份未脱敏 map/elf |
| 脱敏后的最小相关片段 | 与任务无关的"以防万一"上下文（噪声=幻觉燃料【推断】） |
| 方言/ISA 锚小抄 | 公司命名/地址/datasheet 原文 |
| 输出格式与来源标注约束 | 互相矛盾的历史 prompt 残留 |

## 3. 失败模式
- **"塞越多越好"**：无关上下文稀释注意力、诱发自信编造【推断】。
- **锚缺失**：不给权威片段就问方言细节 → 必然先验污染。
- **脱敏与上下文构造脱节**：临时往 prompt 里贴了未脱敏片段（最危险，无 git 拦截兜底）。

## 4. 我下周可以拿它做什么
为"map size 归因"任务写第一份**上下文清单模板**（必放/禁放/锚），
放 `30-workflows/`，下次真用时照单执行并记是否减少返工。

## 5. 安全关键遗产
"输入受控才有可追溯输出"：上下文清单 ≈ 评审用的"输入基线"，
让结论可回链到确切喂了什么（CLAUDE.md §7）。
