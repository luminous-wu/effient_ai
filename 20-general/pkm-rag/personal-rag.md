---
title: 个人 RAG：检索自己的笔记与参考
status: draft
created: 2026-05-18
updated: 2026-05-18
tags: [pkm-rag, rag, retrieval, local-llm]
sources:
  - "【原文】RAG 通识（检索关键词：retrieval augmented generation, embedding chunking, citation grounding）"
confidence: low
related:
  - "[[datasheet-rag]]"
  - "[[obsidian-ai-pkm]]"
next-action: "下周搭最小本地 RAG（仅索引本仓库 .md），测'回答必带 [[slug]] 来源'的命中率"
---

# 个人 RAG：检索自己的笔记与参考

## 0. 一句话
对**本仓库自有内容**做 RAG（IP 安全），回答必须**回链 `[[slug]]` + 章节**；
无来源即视为未覆盖，不接受脑补。

## 1. 与 datasheet-rag 的关键区别
| | [[datasheet-rag]] | 本笔记 |
|---|---|---|
| 语料 | 受控手册 | 自有笔记/已脱敏摘录 |
| IP 风险 | 高，须本地/隔离 | 低（仓库已是脱敏产物） |
| 真值 | 回原文逐位核 | 回链笔记 + 笔记自身的来源标注 |
→ 自有 RAG 风险低，但**不能绕过 §4 来源标注**：检索到的是笔记，笔记结论本身
仍带 `【原文/推断/实测】`，RAG 不能把 `【推断】`答成事实。

## 2. 设计要点
- 索引单位：按 `##` 小节切，保 frontmatter 为元数据（status/confidence 可过滤）。
- 回答契约：`结论 + 来源：[[slug]] §N + 该结论原始标注等级`。
- 过滤：默认排除 `status: outdated/archived`；`confidence: low` 结论显式标注。
- 本地优先（Ollama/llama.cpp）——与 [[datasheet-rag]] 共用本地推理退路。

## 3. 失败模式
- **把低置信笔记当结论**：RAG 抹平 confidence → 必须透传标注等级。
- **过期命中**：检索到 `outdated` 笔记仍照答 → 索引层过滤 + 回答标日期。
- **回链幻觉**：编造不存在的 `[[slug]]` → 回答后用脚本校验链接存在性。

## 4. 我下周可以拿它做什么
最小本地 RAG 仅索引本仓库 `.md`，建 10 个跨笔记问题评测集，
测"回答带正确 `[[slug]]` 且透传 confidence"的比例（→ `50-experiments/`，关 OQ-011）。

## 5. Open Questions → `00-meta/open-questions.md`
- OQ-011：个人 RAG 是否值得？vs 直接 Obsidian 搜索+双链。增益须实测，别为建而建。
