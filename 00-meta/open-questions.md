# 活跃问题（Open Questions）

未决问题登记处。关闭时**不删除**，改 `状态` 为 `closed` 并补"结论"。

| ID | 状态 | 问题 | 来源笔记 | 结论（关闭时填） |
|---|---|---|---|---|
| OQ-001 | open | GHS MULTI map 是否有稳定可解析格式，值得写个 pre-parser？ | [[ghs-multi-map-ai-analysis]] | |
| OQ-002 | open | 链接脚本审查 prompt（Self-Critique 变体）命中率/误报率如何，是否值得固化进 `40-prompts/`？ | [[linker-script-ai-review]] | |
| OQ-003 | open | 能否用机读的硬件约束 schema（YAML）喂 AI，降低 memlay "自造约束"误报率？ | [[memlay-architecture-ai-assist]] | |
| OQ-004 | open | 是否值得维护"方言锚片段库"（每方言一段权威骨架）作为 prompt 前缀复用？ | [[ld-vs-lsl-vs-ghs-dialects]] | |
| OQ-005 | open | Capstone 对 TriCore (TC3xx) ISA 的覆盖度与正确性是否够用？需小样本实测 | [[pyelftools-capstone-workflow]] | |
| OQ-006 | open | 是否维护"ISA 锚小抄"（TriCore/ARM 各一页）作反汇编提问前缀？与 OQ-004 合并管理？ | [[disasm-comprehension-ai]] | |
| OQ-007 | open | 只读 IR MCP 能否实测降低算术幻觉？相对"贴 JSON 进 prompt"增益是否值这套基建？ | [[mcp-skills-subagents-hooks]] | |
| OQ-008 | open | subagent 交叉验证如何保证"独立性"（异 prompt/异模型/异方法）才算真双人确认？ | [[mcp-skills-subagents-hooks]] | |
