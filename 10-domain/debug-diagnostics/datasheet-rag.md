---
title: datasheet / UM / RM 的 RAG 检索
status: draft
created: 2026-05-18
updated: 2026-05-18
tags: [debug-diagnostics, rag, datasheet, local-llm, ip-boundary]
sources:
  - "【原文】RAG 通识（检索关键词：retrieval augmented generation chunking, citation grounding, table extraction PDF）"
  - "【原文】本地 LLM（检索关键词：Ollama, llama.cpp, vLLM, LM Studio）"
confidence: low
related:
  - "[[context-engineering]]"
  - "[[log-trace-ai-analysis]]"
next-action: "下周用 1 份公开 datasheet（非公司）搭最小本地 RAG，测寄存器表检索的引用准确率"
---

# datasheet / UM / RM 的 RAG 检索

## 0. 一句话
让 AI **带页码/章节引用地回答**手册问题；**无引用的答案默认不可信**，
寄存器位级细节必须回原文核对。

## 1. IP 边界（本场景最敏感）
- datasheet/UM/RM 多为受控文档：**不入库、优先本地/隔离推理**
  （Ollama/llama.cpp/vLLM；CLAUDE.md §8）。
- 入库的只有方法、chunking 策略、评测脚本——不是手册内容。
- 公司内网禁云端时，本地 RAG 是退路方案，不是可选项。

## 2. 失败模式（手册 RAG 专属）
- **表格/寄存器位域被切碎**：PDF 表跨页/多列，naive chunking 破坏位定义 →
  AI 给错 bit 含义（位精确灾难）。
- **无引用幻觉**：检索没命中也照答，且自信。
- **跨芯片/派生型号串味**：同系列不同 derivative 寄存器差异被抹平。
- **版本错配**：手册 errata/revision 未对齐，引用了过期定义。

## 3. SOP
1. 索引阶段：对寄存器/位域表用**结构感知切分**（保表完整），标页码/章节元数据。
2. 回答必须附 `来源：<doc> p.X §Y`，无来源即视为未知，不接受推测。
3. 位级/时序结论 ⛔ 回原文逐位核对才采纳（CLAUDE.md §7）。
4. 注明芯片 derivative 与手册 revision，防串味。

## 4. 我下周可以拿它做什么
用一份**公开**(非公司) datasheet 搭最小本地 RAG，建评测集（10 个寄存器位问题），
测引用命中率与位域错误率 → 决定这套是否值得用于真实手册（→ `50-experiments/`）。

## 5. Open Questions → `00-meta/open-questions.md`
- OQ-010：本地小模型在寄存器表 RAG 上的位精确正确率是否够用？vs 仅做检索+人读原文。
