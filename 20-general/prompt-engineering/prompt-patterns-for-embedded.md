---
title: 对嵌入式/安全关键真正有用的提示词模式
status: draft
created: 2026-05-18
updated: 2026-05-18
tags: [prompt-engineering, embedded, self-critique, #cross-psy]
sources:
  - "【原文】Anthropic prompt engineering docs（检索关键词：Claude system prompt, XML tags, chain of thought, prefill）"
confidence: medium
related:
  - "[[linker-script-ai-review]]"
  - "[[ld-vs-lsl-vs-ghs-dialects]]"
  - "[[disasm-comprehension-ai]]"
next-action: "下周把已散落在各域笔记里的 prompt 片段，抽成 40-prompts/ 可复用骨架（先 2 个）"
---

# 对嵌入式/安全关键真正有用的提示词模式

> 不科普 CoT/Few-shot 是什么。只记**在本仓库领域里被反复用到、且有抗错价值**的模式。

## 1. 已在用、真有价值的（来自域笔记，归纳）
| 模式 | 作用 | 出处 |
|---|---|---|
| **来源标注约束**：要求输出区分"可见/推断" | 把 CLAUDE.md §4 变成 prompt 内硬约束，逼出不确定性 | [[linker-script-ai-review]] §2 |
| **方言/ISA 钉死 + 锚片段** | 压制 dialect/ISA 先验污染 | [[ld-vs-lsl-vs-ghs-dialects]] §2, [[disasm-comprehension-ai]] §2 |
| **Self-Critique 末步自我反驳** | 逼模型暴露最可能错的结论 | [[linker-script-ai-review]] §2 |
| **"不要计算我没给的数字"负向约束** | 切断算术幻觉发生条件 | [[ghs-multi-map-ai-analysis]] §3 |
| **结构化输出（分列：观察/推断/待核）** | 让人审可逐条勾，对抗自动化自满 | 多处 |

→ 共性：**不是让 AI 更聪明，而是让它的不确定性可见、可审、可拒**。

## 2. 流行但对我低优先（批判）
- 复杂角色扮演/人格设定：对位精确任务收益低，徒增 token。
- 长 few-shot 堆例：嵌入式语料稀，示例反而引入"看起来对"的错误范式【推断】。
- "宪法式"对个人单任务多为过度工程；其内核（显式约束）已被 §1 吸收。

## 3. 反模式：提示词膨胀
症状：prompt 越加越长、互相矛盾、没人记得哪条在起作用。
对策：
- 每条约束写明**它防的是哪个失败模式**（无法对应的删）。
- prompt 进 `40-prompts/` 必须带迭代历史与"有效版本"判据（模板已就位）。
- 定期回顾删除"安抚性"约束（让输出好看但不抗错的）。

## 4. 我下周可以拿它做什么
把 §1 的"来源标注约束 + Self-Critique"固化成 `40-prompts/` 两个骨架，
各跑一次真实任务，记命中率（衔接 OQ-002）。

## 5. #cross-psy 反哺
好 prompt 的价值常不在"提取更多"，而在"让我不被流畅的错误说服"——
提示工程在此是认知偏差的工程对策，不是产能工具。
