---
title: 日志 / CAN / UART trace 的 AI 辅助分析
status: draft
created: 2026-05-18
updated: 2026-05-18
tags: [debug-diagnostics, trace, can, uart, #cross-psy]
sources:
  - "【原文】CAN/诊断通识（检索关键词：CAN frame DBC decoding, UDS ISO 14229, timestamp clock domain）"
  - "【推断】基于通用日志分析经验"
confidence: medium
related:
  - "[[map-parsing-deterministic-plus-ai]]"
  - "[[datasheet-rag]]"
next-action: "下周用确定性解码器（DBC/协议）先解一段脱敏 trace，再让 AI 仅做时序叙事/异常假设"
---

# 日志 / CAN / UART trace 的 AI 辅助分析

## 0. 一句话
**解码确定（用 DBC/协议规范），叙事交 AI**。不让 LLM 猜帧语义、不让它定因果。

## 1. 模式
```
原始 trace(本地) ─确定性解码(DBC/UDS/协议)→ 结构化事件(脱敏) → AI: 时序叙事/异常假设
```
帧/信号语义来自规范与 DBC，**不问 AI**（同 [[map-parsing-deterministic-plus-ai]] 思路）。

## 2. 失败模式
- **相关≠因果**：AI 把时间相邻当因果，给似是而非根因。
- **时钟域/时间戳**：多源 trace 时基不同/漂移，AI 默认同一时间轴 → 误排序。
- **帧语义幻觉**：未给 DBC/规范时编造信号含义、字节序、缩放。
- **采样盲区**：丢帧/触发前数据缺失，AI 用"看到的"当全集（截断同源）。
- **协议版本/厂商扩展**：UDS/诊断私有子服务被通用化误读。

## 3. SOP
1. 脱敏 ⛔：删车型/项目标识、私有 DID/地址。
2. 确定性解码：DBC/协议解码器产结构化事件 + 显式标时钟域。
3. AI 仅：重建时序叙事 + 列**可检验**异常假设（每条写如何用 trace 验证）。
4. 人按假设回到原始 trace 验证 ⛔ —— 因果由证据定，不由 AI 定。
5. 复现/实测确认才升 `verified`。

## 4. 我下周可以拿它做什么
取一段脱敏 CAN trace，DBC 解码后跑 §3，统计 AI 因果误判与时钟域误排序次数
（→ `50-experiments/`）。

## 5. #cross-psy 反哺
叙事流畅性 = 可信度错觉。trace 分析里 AI 最强也最危险的就是"讲一个顺的故事"，
人审闸专门拦这种顺。
