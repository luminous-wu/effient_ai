# AI 高效工作知识库

个人学习用、私有、可长期演化的 AI 提效知识库。服务于汽车电子嵌入式软件工程
（链接脚本 / OS-AUTOSAR / 工具链 / 二进制分析）。
设计原则与所有约定见 [`CLAUDE.md`](./CLAUDE.md)，**先读它再贡献**。

## 30 秒导航

| 目录 | 一句话 |
|---|---|
| `00-meta/` | 元信息：ADR 决策、笔记模板、迭代日志、活跃问题 |
| `10-domain/` | 领域专项：linker-memlay / os-autosar / toolchain / binary-analysis / debug-diagnostics / hil-sim |
| `20-general/` | 通用 AI 提效：提示工程 / agentic 编码 / PKM-RAG / 提效度量 / 工作流集成 |
| `30-workflows/` | 可执行 SOP（"周一早上做什么"级别） |
| `40-prompts/` | 提示词库（含跨学科阅读助手 v4） |
| `50-experiments/` | 对比实验 / A-B 提示词 / 失败案例 |
| `60-references/` | 外部资料摘录与链接（含已有 awesome 列表引用） |
| `90-archive/` | 归档（`90-archive/YYYYMM/`） |

## 如何使用本库

1. **状态机**：`draft → verified → outdated → archived`。仅经实测或可信交叉
   验证的内容可升 `verified`（见 CLAUDE.md §5/§7）。
2. **来源标注**：每条事实性结论标 `【原文】/【推断】/【实测】`（CLAUDE.md §4）。
3. **回访**：`verified` 笔记写明回访日期；月度回顾用 `00-meta/templates/retrospective.md`。
4. **新笔记**：从 `00-meta/templates/` 复制对应模板，按 frontmatter 规范填写。
5. **活跃问题**：未决问题登记到 `00-meta/open-questions.md`，关闭时附结论。

## 本库不做什么

- 不做收藏夹 / "X 大工具盘点" / 未验证的肯定式工具吹捧。
- 不入库公司源码、二进制、真实 `.map/.elf`、内部规格（见 `.gitignore` 与 CLAUDE.md §8）。
- 不重复造轮子：已有优质综述直接引用 `60-references/`。

## 入口锚点

- 首个示例笔记：[`10-domain/toolchain/ghs-multi-map-ai-analysis.md`](./10-domain/toolchain/ghs-multi-map-ai-analysis.md)
- 首个示例笔记：[`10-domain/linker-memlay/linker-script-ai-review.md`](./10-domain/linker-memlay/linker-script-ai-review.md)
- 结构决策：[`00-meta/decisions/0001-kb-structure-and-conventions.md`](./00-meta/decisions/0001-kb-structure-and-conventions.md)
