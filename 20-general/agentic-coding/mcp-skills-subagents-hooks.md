---
title: MCP / Skills / Subagent / Hooks：对嵌入式工程师何时值得
status: draft
created: 2026-05-18
updated: 2026-05-18
tags: [agentic-coding, mcp, hooks, subagent, claude-code]
sources:
  - "【原文】Claude Code / Agent SDK 文档（检索关键词：Claude Code MCP, hooks, subagents, skills, settings.json）"
confidence: low
related:
  - "[[agentic-tool-selection]]"
  - "[[pyelftools-capstone-workflow]]"
  - "[[context-engineering]]"
next-action: "下周做最小 PoC：一个只读 MCP 把 ELF→IR（见 pyelftools 笔记）暴露给 Claude，AI 只查不算"
---

# MCP / Skills / Subagent / Hooks：何时值得

> 高阶机制不是越多越好。对每个机制问同一句：**它是否把 AI 更牢地限制在
> "叙事层"、把确定性还给工具？** 是→值得；只是"更自动"→警惕。

## 1. 逐机制取舍（对我语境）
| 机制 | 对我的高价值用法 | 警惕 |
|---|---|---|
| **MCP** | 把 pyelftools/Capstone 的**确定性 IR** 做成只读 server，AI 只查询不解析不算（落实 [[pyelftools-capstone-workflow]] L2/L3 切口） | 写型 MCP 触碰真实产物=IP+破坏风险，默认只读 |
| **Hooks** | 强制执行约定：提交前跑脱敏/`.gitignore` 校验、阻止未脱敏片段、注入来源标注提醒（CLAUDE.md §4/§8 自动化） | hook 静默失败比没有更糟，需可见反馈 |
| **Subagent** | 并行**独立审查**：一个 agent 查对齐、一个查 LMA/VMA → 近似"双人确认"（CLAUDE.md §7） | 并行≠独立，若共享同偏差则是伪交叉验证 |
| **Skills** | 固化高频 SOP（如 map 归因清单）为可调用流程，减少 prompt 膨胀 | 沦为又一处"收藏夹"；需迭代历史与淘汰 |

## 2. 主线一致性检查
这四者唯一正当目的：**让 AI 不解析、不给数字、不裁决 soundness**
（贯穿 10-domain 主线）。任何让 AI 直接碰真值的高阶配置都是反向的。

## 3. 失败模式
- **MCP 越权**：给了写/执行权 → AI 改了不该改的产物。
- **Hook 假绿**：脱敏校验逻辑漏，给虚假安全感（不对称风险，类比告警误判）。
- **伪交叉验证**：多 subagent 同 prompt 同模型，错误一致 → 看似双确认实则单点。
- **配置熵**：MCP/hook/skill 堆积无人维护，成新"信息墓地"。

## 4. 我下周可以拿它做什么
最小 PoC：只读 MCP 暴露**脱敏 IR**（不接真实 ELF），让 Claude 仅查询；
验证"AI 是否还试图自己算"。结果进 `50-experiments/`，关联 OQ-007。

## 5. Open Questions → `00-meta/open-questions.md`
- OQ-007：只读 IR MCP 能否实测降低算术幻觉？相对"贴 JSON 进 prompt"增益是否值这套基建？
- OQ-008：subagent 交叉验证如何保证"独立性"（异 prompt/异模型/异方法）才算真双人确认？
