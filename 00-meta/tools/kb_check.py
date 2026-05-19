#!/usr/bin/env python3
"""KB 约定校验器（零依赖）。

强制执行 CLAUDE.md 的三类约定：
  §3  笔记 frontmatter 必填字段 + status/confidence 枚举
  §3  Obsidian 双链 [[slug]] 不得死链
  §8  脱敏关键词黑名单（IP 边界）—— 黑名单由你维护，默认空

用法：
  python3 00-meta/tools/kb_check.py            # 全仓库
  python3 00-meta/tools/kb_check.py --staged   # 仅 git 暂存的 .md（pre-commit 用）

退出码：0 干净 / 1 有违规。
"""
import os
import re
import subprocess
import sys

REPO = subprocess.run(
    ["git", "rev-parse", "--show-toplevel"],
    capture_output=True, text=True, check=True,
).stdout.strip()

# 需要 frontmatter 的目录前缀（README.md 与模板除外）
NOTE_PREFIXES = ("10-domain/", "20-general/", "30-workflows/", "40-prompts/")
REQUIRED_KEYS = ("title", "status", "created", "updated", "tags", "confidence")
STATUS_ENUM = {"draft", "verified", "outdated", "archived"}
CONFIDENCE_ENUM = {"low", "medium", "high"}

# 概念占位，不视为真实双链（见 00-meta/tools/README.md）
LINK_ALLOWLIST = {"file-slug", "slug", "双链", "slick", "YYYYMM"}

BLACKLIST_FILE = os.path.join(REPO, "00-meta/tools/sanitize-blacklist.txt")


def all_md():
    out = subprocess.run(
        ["git", "ls-files", "*.md"], cwd=REPO,
        capture_output=True, text=True, check=True,
    ).stdout.split()
    return out


def staged_md():
    out = subprocess.run(
        ["git", "diff", "--cached", "--name-only", "--diff-filter=ACM"],
        cwd=REPO, capture_output=True, text=True, check=True,
    ).stdout.split()
    return [p for p in out if p.endswith(".md")]


def strip_code(text):
    text = re.sub(r"```.*?```", "", text, flags=re.S)
    text = re.sub(r"`[^`\n]*`", "", text)
    return text


def known_slugs():
    return {os.path.splitext(os.path.basename(p))[0] for p in all_md()}


def is_note(path):
    base = os.path.basename(path)
    if base == "README.md" or base.endswith("-template.md"):
        return False
    if "/templates/" in path:
        return False
    return path.startswith(NOTE_PREFIXES)


def check_frontmatter(path, text, errs):
    if not is_note(path):
        return
    if not text.startswith("---"):
        errs.append(f"{path}: 缺 YAML frontmatter（CLAUDE.md §3）")
        return
    fm = text.split("---", 2)
    if len(fm) < 3:
        errs.append(f"{path}: frontmatter 未正确闭合")
        return
    block = fm[1]
    keys = set(re.findall(r"(?m)^([A-Za-z][\w-]*):", block))
    for k in REQUIRED_KEYS:
        if k not in keys:
            errs.append(f"{path}: frontmatter 缺字段 '{k}'")
    m = re.search(r"(?m)^status:\s*(\S+)", block)
    if m and m.group(1) not in STATUS_ENUM:
        errs.append(f"{path}: status='{m.group(1)}' 不在 {sorted(STATUS_ENUM)}")
    m = re.search(r"(?m)^confidence:\s*(\S+)", block)
    if m and m.group(1) not in CONFIDENCE_ENUM:
        errs.append(f"{path}: confidence='{m.group(1)}' 不在 {sorted(CONFIDENCE_ENUM)}")


def check_links(path, text, slugs, errs):
    body = strip_code(text)
    for raw in re.findall(r"\[\[([^\]]+)\]\]", body):
        slug = re.split(r"[|#]", raw)[0].strip()
        if slug in LINK_ALLOWLIST or slug in slugs:
            continue
        errs.append(f"{path}: 死链 [[{slug}]]（无对应 .md）")


def load_blacklist():
    pats = []
    if os.path.exists(BLACKLIST_FILE):
        for ln in open(BLACKLIST_FILE, encoding="utf-8"):
            ln = ln.strip()
            if ln and not ln.startswith("#"):
                pats.append(re.compile(ln, re.I))
    return pats


def check_sanitize(path, text, pats, errs):
    for p in pats:
        if p.search(text):
            errs.append(f"{path}: 命中脱敏黑名单 /{p.pattern}/（CLAUDE.md §8，提交前脱敏）")


def main():
    staged = "--staged" in sys.argv
    targets = staged_md() if staged else all_md()
    slugs = known_slugs()
    pats = load_blacklist()
    errs = []
    for rel in targets:
        ap = os.path.join(REPO, rel)
        if not os.path.exists(ap):
            continue
        text = open(ap, encoding="utf-8").read()
        check_frontmatter(rel, text, errs)
        check_links(rel, text, slugs, errs)
        check_sanitize(rel, text, pats, errs)
    if errs:
        print("KB 校验失败：", file=sys.stderr)
        for e in errs:
            print("  - " + e, file=sys.stderr)
        print(f"\n共 {len(errs)} 处。修正后再提交。", file=sys.stderr)
        return 1
    print(f"KB 校验通过（{len(targets)} 个 .md）。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
