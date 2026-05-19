---
title: 图表即代码：Mermaid/PlantUML + AI
status: draft
created: 2026-05-18
updated: 2026-05-18
tags: [workflow-integration, mermaid, plantuml, diagrams-as-code]
sources:
  - "【原文】Mermaid/PlantUML 通识（检索关键词：Mermaid syntax flowchart, PlantUML, diagrams as code）"
confidence: medium
related:
  - "[[memlay-architecture-ai-assist]]"
  - "[[call-graph-wcsd-ai-assist]]"
next-action: "下周让 AI 把一段脱敏 memlay 文字描述转 Mermaid，检查图是否与描述位级一致"
---

# 图表即代码：Mermaid/PlantUML + AI

## 0. 一句话
图用文本写、随仓库版本化、可 diff；AI 擅长**文字↔图骨架**互转，
**图与真相的一致性靠人核**（图会比文字更"看着对"地骗人）。

## 1. 为什么 diagrams-as-code 适合本仓库
- 与 Markdown-as-Code 同源：纯文本、git 可追溯、Obsidian 可渲染。
- 二进制图片不入库（CLAUDE.md §8 精神）；图源即文本。
- AI 转换成本低、收益稳：memlay 布局、调用图、状态机的草图化。

## 2. AI 的高价值用法
- 文字 SOP/架构描述 → Mermaid 流程/时序草图（[[memlay-architecture-ai-assist]] 方案可视化）。
- 调用图 IR（脚本产）→ Mermaid 渲染（数据来自脚本，AI 只排版，
  延续 [[call-graph-wcsd-ai-assist]]：AI 不算、只画）。

## 3. 失败模式
- **图比文字更骗人**：错误布局画成整齐框图，比错误文字更易被信（视觉权威错觉）。
- **图与源漂移**：手改文字没更新图（或反之）→ 图必须由唯一真相源生成或人核。
- **语法幻觉**：Mermaid/PlantUML 版本特性 AI 易编 → 渲染失败或静默错画。
- **位级失真**：地址/大小/对齐在图里被"取整美化"，丢精度。

## 4. 规则
- 图的**数据来源**与文字结论同一个（脚本 IR / 已审笔记），不让 AI 既造数又画图。
- 图旁注明来源与 confidence；位精确信息以文字/表为准，图仅辅助直觉。
- 图源进 git，渲染产物不进（同二进制策略）。

## 5. 我下周可以拿它做什么
取一段脱敏 memlay 文字描述 → AI 转 Mermaid → 逐项核"图 vs 文字"一致性，
记错画率，决定哪类图值得交给 AI（→ `50-experiments/`）。
