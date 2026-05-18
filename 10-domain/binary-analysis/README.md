# binary-analysis — 二进制与静态分析

pyelftools/Capstone 工作流、反汇编理解与调用图、栈/Flash/RAM 优化、与
Ghidra/Binary Ninja/IDA 的集成可能。

## 笔记
- [[pyelftools-capstone-workflow]] — 分析工具抽象化设计：确定性核心 + IR 契约 + AI 边界（draft, conf medium）
- [[call-graph-wcsd-ai-assist]] — 调用图/WCSD：soundness 是数学问题不是 AI 问题（draft, conf low）
- [[disasm-comprehension-ai]] — AI 读反汇编：ISA/ABI 先验污染（TriCore CSA/context）（draft, conf low）

## 本域贯穿主线
确定性工具产出**机读 IR（真值）**，AI 只消费 IR 做叙事/假设/报告，
**不参与解析、不给数字、不裁决 soundness**。

## 待补
预处理脚本/IR schema 实现（仅抽象化，不含公司代码）；与 `os-autosar/` 的栈模型衔接（PR6）。
