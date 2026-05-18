# linker-memlay — 链接脚本 / 内存布局

LSL（TriCore）/ GLD-LD（GNU/GHS）编写与审查、内存映射可视化、跨芯片
（TriCore vs S32K）布局对比、map 文件分析。直接服务于在研的 S32K5xx memlay 架构。

## 笔记
- [[linker-script-ai-review]] — 链接脚本片段的 AI 审查（draft）
- [[memlay-architecture-ai-assist]] — 内存布局架构设计的 AI 辅助：约束驱动，AI 只做方案枚举（draft, conf low）
- [[ld-vs-lsl-vs-ghs-dialects]] — 方言对比 + AI 跨方言串味失败模式（draft, **待你校正后升 verified**）
- [[map-parsing-deterministic-plus-ai]] — "确定性预处理 + AI 叙事"模式：脚本算数、AI 叙事（draft, conf medium）

## 本域贯穿主线
**AI 只做组合/叙事/枚举，硬件事实与数字真值由你/脚本提供**——三篇笔记都是这条线的展开。

## 待补（PR3 衔接）
预处理脚本设计细节 → `10-domain/binary-analysis/`（抽象化、不含公司代码）。
