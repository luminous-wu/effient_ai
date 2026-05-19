# 10-domain — 领域专项 AI 应用

针对具体嵌入式工作的 AI 实用方法、工具、案例与陷阱。每个子域有自己的 `README.md` 索引。

| 子域 | 范围 | 当前状态 |
|---|---|---|
| `linker-memlay/` | 链接脚本（LSL/GLD/LD）、内存布局、map 分析、跨芯片对比 | PR1+2：4 篇 |
| `toolchain/` | GHS MULTI 选项调优、编译产物（list/map/asm）分析、告警分类 | PR1+3：3 篇 |
| `binary-analysis/` | pyelftools/Capstone 工作流、调用图、WCSD、与 Ghidra/IDA 集成 | PR3：3 篇 |
| `os-autosar/` | ARXML 解析/生成、OS Task/ISR/Resource 配置、WCET/WCSD 辅助 | PR6：2 篇 |
| `debug-diagnostics/` | 日志智能分析、CAN/UART trace、datasheet/UM 的 RAG 检索 | PR6：2 篇 |
| `hil-sim/` | QEMU / T32-Lauterbach 脚本生成、仿真结果对比 | PR6：1 篇 |

## 贯穿原则
- 所有喂给 AI 的产物**先脱敏**（CLAUDE.md §8）。
- 高风险输出（链接脚本、OS 配置）走"双人确认思想"才升 `verified`（CLAUDE.md §7）。
