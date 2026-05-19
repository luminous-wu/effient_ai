---
title: ARXML 解析/生成的 AI 辅助
status: draft
created: 2026-05-18
updated: 2026-05-18
tags: [os-autosar, arxml, autosar, validation]
sources:
  - "【原文】AUTOSAR 模板与 schema 通识（检索关键词：AUTOSAR ARXML schema AUTOSAR XSD, ARXML reference DEST）"
  - "【推断】基于 XML/schema 通用经验，未对具体 ARXML 工具链实测"
confidence: low
related:
  - "[[os-config-wcet-wcsd-ai]]"
  - "[[map-parsing-deterministic-plus-ai]]"
next-action: "下周拿一段脱敏 ARXML 片段，测 AI 改写后是否仍过 schema/引用完整性校验"
---

# ARXML 解析/生成的 AI 辅助

## 0. 一句话
ARXML 是**强 schema + 引用密集**的机读格式。AI 用来导航/解释/起草，
**结构有效性与引用完整性由 schema 校验器裁决，不由 AI**。

## 1. AI 能帮 / 不能帮
| 任务 | 价值 | 风险 |
|---|---|---|
| 解释一段 ARXML 在配什么、定位某容器 | 高 | 低 |
| 起草小改片段（草稿） | 中 | 中：易破 schema/断引用 |
| 跨文件引用关系叙事 | 中 | 中 |
| **保证 schema 有效 / DEST 引用一致** | 极低 | **高：静默生成无效 XML** |
| **AUTOSAR 语义合规裁决** | 低 | **高：规范细节幻觉** |

## 2. 失败模式（ARXML 专属）
- **schema 违规但"看着对"**：元素顺序、必选子元素、多重性约束被破坏【推断】。
- **引用断裂**：`*-REF` 的 `DEST` 与目标路径不一致、改名未同步全引用。
- **UUID/SHORT-NAME 路径**：AI 易篡改或编造稳定标识。
- **规范版本串味**：不同 AUTOSAR 版本模板差异，AI 混用。
- **大文件截断**：与 map 同源失败模式（见 [[map-parsing-deterministic-plus-ai]]）。

## 3. SOP
1. 脱敏 ⛔：删/改专有 ECU 名、路径、私有参数。
2. AI 仅产**草稿** + 标"我不确定是否合 schema 的点"。
3. **确定性校验** ⛔：XSD/工具链校验器跑 schema + 引用完整性——这是真值闸，AI 不替代。
4. 失败回灌校验器报错让 AI 修，但每轮都必须重过 §3。
5. 配置器（Tresos/EB）二次确认后才落生产，结论才升 `verified`。

## 4. 我下周可以拿它做什么
取一段脱敏 ARXML，让 AI 做一处典型小改，统计**改后仍过校验的比例**与
最常见违规类型 → 决定 AI 在 ARXML 上的可信边界（→ `50-experiments/`）。

## 5. Open Questions → `00-meta/open-questions.md`
- OQ-009：能否把 XSD/引用校验做成 hook 或 MCP 工具，让 AI 改写后强制过闸（呼应 OQ-007）？
