# CLAUDE.md — AI 高效工作知识库主记忆

> 本文件是 Claude Code 在本仓库的长期记忆。每次会话默认遵守以下约定。
> 这是**个人学习用私有仓库**，无外部合规约束，但坚持 IP 最小安全实践。

## 1. 我是谁（不要重复向我科普基础）

- 汽车电子区域控制器**嵌入式软件工程师**（中德合资）。
- 技术域：MCU 链接脚本、OS、工具链开发、二进制静态分析。
- 芯片：Infineon AURIX TriCore (TC2xx/TC3xx)、NXP S32K5xx。
- 工具链：Green Hills MULTI (GHS)。
- 在研：S32K5xx 内存布局（memlay）架构；ELF 分析工具（pyelftools + Capstone，
  目标含调用图 / WCSD / AUTOSAR OS 集成）。
- AI 使用：Anthropic 重度用户。**默认我懂 LLM 基础**，无需"什么是 prompt"式解释。

## 2. 中英文混排规则

- 正文中文为主，**技术术语保留英文**（便于直接复用到内部沟通）。
- 首次出现的概念给一次中英对照，后续只用英文术语。
- 术语对照表（节选，新增请追加并保持英文为准）：

| 中文 | 英文（仓库统一用法） |
|---|---|
| 链接脚本 | linker script（GHS: `.ld`；TriCore: LSL；GNU: GLD/LD） |
| 内存布局 | memory layout / memlay |
| 重定位 | relocation |
| 段 / 节 | section（`.text/.data/.bss/.rodata`） |
| 程序段 | segment（program header） |
| 对齐 | alignment |
| 调用图 | call graph |
| 最坏栈深度 | WCSD (worst-case stack depth) |
| 最坏执行时间 | WCET |
| 反汇编 | disassembly |
| 工具链 | toolchain |

## 3. 文件命名与 frontmatter

- 命名：`topic-slug.md`（全小写、连字符）。需区分版本/日期时加 `-vN` 或 `-YYYYMM`。
- 归档：移动到 `90-archive/YYYYMM/`，**不改原文件名**，frontmatter 置 `status: archived`。
- 每篇笔记必须含 YAML frontmatter：

```yaml
---
title: 链接脚本片段的 AI 审查
status: draft            # draft | verified | outdated | archived
created: 2026-05-18
updated: 2026-05-18
tags: [linker, memlay, review, #cross-psy]
sources:                 # 链接或检索关键词；区分原文/推断见 §4
  - "Anthropic prompt engineering docs（检索关键词）"
confidence: medium       # low | medium | high（对结论的把握，非情绪）
related:
  - "[[ghs-multi-map-ai-analysis]]"
next-action: "下周拿一段脱敏后的 S32K LD 片段实跑一次审查 prompt"
---
```

- **双向链接**用 Obsidian 风格 `[[file-slug]]`（不带路径、不带 `.md`），保持可迁移。

## 4. 引用与来源标注规范（强制）

每条事实性结论必须可追溯，并显式区分三类来源：

- `【原文】` — 出自外部文档/论文/官方文档的原话或忠实转述（附链接或检索关键词）。
- `【推断】` — 我或 Claude 基于原文的推理，**未经实测**。
- `【实测】` — 在本仓库 `50-experiments/` 有对应实验记录支撑。

未标注的句子默认视为 `【推断】`，不得用肯定语气描述工具效果。
禁止编造 URL；无确切链接时写"检索关键词：…"。

## 5. 状态机

`draft → verified`（经 `【实测】`或可信交叉验证）→ `outdated`（被推翻/过时）→ `archived`。
每篇 `verified` 笔记应在 `next-action` 或回顾中写明**回访日期**，对抗知识熵。

## 6. 跨学科标签（反哺工程与 AI 使用）

- `#cross-buddhism` 正念 / 无常 / 不执着于工具
- `#cross-psy` 认知偏差 / 自动化自满 (automation complacency)
- `#cross-phil` 第二序思考 / 工具理性的边界

仅在确有反哺洞见时打标，**禁止为打标而打标**。

## 7. 安全关键工程文化遗产（即使无合规也借鉴）

ISO 26262 / MISRA 思维迁移到 AI 输出治理：
- **评审**：AI 生成的链接脚本/配置，按"人审清单"过一遍位精确语义。
- **可追溯**：结论 ↔ 来源 ↔ 实验，三者可链。
- **双人确认思想**：高风险输出至少经一次独立交叉验证（另一模型/手算/工具）才升 `verified`。

## 8. IP 边界（最小安全实践）

- **不入库**：公司源码、真实 `.map/.elf/.o`、内部 ARXML、datasheet PDF、`.docx` 规格。
  （见 `.gitignore`）
- **抽象化复述**：描述问题用通用化、改名、删除专有常量后的最小复现片段。
- **不上传二进制**；分析方法/心得入库，原始产物留本地。

## 9. 我厌恶的输出风格（主动规避）

- "X 大工具盘点"式无个人验证清单。
- 冗长礼貌性前言/总结；正确的废话。
- 把仓库做成收藏夹；堆砌名词。
- 当工具厂商传声筒；用肯定语气描述未实测效果。
- 假定我是 AI 新手。
- 重复造轮子（已有优质 awesome/综述时直接引用 `60-references/`）。

## 10. 工作节奏

- **先规划再填充**；每次专注一个子目录/主题，类似一个 PR。
- 关键设计写 `00-meta/decisions/` ADR；每次 PR 在 `00-meta/iteration-log.md` 追加一行。
- 每个工具/方法附一句"**我下周可以拿它做什么**"。
