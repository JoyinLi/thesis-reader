#!/usr/bin/env python3
"""Validate the structure of Thesis Reader Markdown outputs."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


MODE_SECTIONS = {
    "triage-brief": [
        ("core introduction", ["核心介绍", "核心观点", "core idea", "core introduction"]),
        ("AI future significance", ["ai 未来", "未来发展", "why it matters", "significance"]),
        ("value rating", ["价值判断", "value rating", "high", "medium", "low"]),
        ("reading decision", ["是否值得精读", "值得精读", "deep-read decision", "yes", "maybe", "no"]),
        ("confidence and limits", ["可信度", "限制", "source confidence", "limitation"]),
    ],
    "deep-read": [
        ("basic information", ["论文基本信息", "basic information", "paper information"]),
        ("motivation", ["研究动机", "motivation"]),
        ("method", ["核心方法", "方法", "method", "framework", "模型"]),
        ("evidence", ["实验设计", "论证方法", "evidence", "experiment", "results"]),
        ("conclusion and limits", ["结论与局限", "局限", "limitations", "conclusion"]),
        ("plain-language understanding", ["个人理解", "通俗", "plain language"]),
        ("AI/UX/HCI implications", ["ux", "hci", "ai pm", "设计启发", "产品启发"]),
        ("actionable direction", ["可复现", "可改进", "作品集", "reproduction", "portfolio"]),
    ],
    "paper-knowledge-package": [
        ("source metadata", ["source metadata", "metadata", "source confidence", "源", "来源"]),
        ("verified core", ["verified core", "core thesis", "核心", "research problem"]),
        ("evidence strength", ["evidence strength", "证据强度", "key evidence"]),
        ("discussion synthesis", ["discussion synthesis", "讨论", "user conclusions", "concepts clarified"]),
        ("AI/UX/HCI translation", ["ai / ux / hci", "ux", "hci", "interface implication", "设计"]),
        ("knowledge base recommendation", ["knowledge base recommendation", "add to knowledge base", "belief update", "知识库"]),
        ("handoff gate", ["research knowledge base loop", "handoff gate", "是否将", "转入"]),
    ],
    "quick-brief": [
        ("one-line conclusion", ["一句话结论", "one-line", "one sentence"]),
        ("importance", ["为什么重要", "why it matters", "importance"]),
        ("method", ["核心方法", "method"]),
        ("evidence", ["关键证据", "evidence"]),
        ("limitation", ["最大局限", "limitation"]),
        ("reading decision", ["值得精读", "worth reading"]),
    ],
}


def normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text).lower()


def contains_any(text: str, aliases: list[str]) -> bool:
    return any(alias.lower() in text for alias in aliases)


def approximate_chinese_chars(text: str) -> int:
    """Count CJK characters plus alphanumeric words as a rough Chinese-length proxy."""
    cjk = re.findall(r"[\u4e00-\u9fff]", text)
    latin_words = re.findall(r"[A-Za-z0-9]+", text)
    return len(cjk) + len(latin_words)


def validate_sections(text: str, mode: str) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    normalized = normalize(text)

    for label, aliases in MODE_SECTIONS.get(mode, []):
        if not contains_any(normalized, aliases):
            errors.append(f"Missing required section: {label}")

    if mode == "triage-brief":
        length = approximate_chinese_chars(text)
        if length > 500:
            errors.append(f"Triage brief should be within 500 Chinese characters; estimated length is {length}.")
        if not contains_any(normalized, ["verified reading loop", "完整", "继续", "是否进入"]):
            warnings.append("No explicit prompt asking whether to continue into the full verified loop detected.")
        if contains_any(normalized, ["实验设计", "可复现", "作品集叙事"]):
            warnings.append("Triage brief may be drifting into full deep-read structure.")

    if mode == "deep-read":
        if not re.search(r"https?://|\[[^\]]+\]\([^\)]+\)", text):
            warnings.append("No URL or Markdown citation detected; confirm source grounding manually.")
        if len(text.split()) < 250 and len(text) < 1200:
            warnings.append("Deep-read output is unusually short; confirm evidence coverage.")

    if mode == "paper-knowledge-package":
        if contains_any(normalized, ["updated concept-index", "updated belief-map", "已写入知识库"]):
            warnings.append("Package may be claiming downstream knowledge-base writes; confirm user approval.")
        if not contains_any(normalized, ["add to knowledge base", "generate knowledge card", "skip", "跳过"]):
            warnings.append("No explicit handoff options detected.")

    return errors, warnings


def validate_visual_deck(text: str) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    pages = re.findall(r"(?im)^#{1,4}\s*page\s*(\d+)\b", text)
    page_count = len(set(pages))

    if not 4 <= page_count <= 6:
        errors.append(f"Visual deck must contain 4-6 Page headings; found {page_count}.")

    required_labels = {
        "title": ["标题", "title"],
        "one-sentence point": ["一句话观点", "one-sentence", "point"],
        "layout": ["画面布局", "视觉布局", "layout"],
        "copy": ["正文", "main copy", "copy"],
        "highlight": ["高亮", "highlight"],
    }
    normalized = normalize(text)
    for label, aliases in required_labels.items():
        if not contains_any(normalized, aliases):
            errors.append(f"Missing visual-deck field: {label}")

    if not contains_any(normalized, ["对话", "discussion", "conversation insight", "讨论"]):
        warnings.append("No explicit discussion-derived insight detected.")

    return errors, warnings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", type=Path, help="Markdown output to validate")
    parser.add_argument(
        "--mode",
        choices=["triage-brief", "deep-read", "paper-knowledge-package", "quick-brief", "visual-deck"],
        default="deep-read",
    )
    args = parser.parse_args()

    if not args.output.is_file():
        print(json.dumps({"valid": False, "errors": ["Output file not found."], "warnings": []}))
        return 2

    text = args.output.read_text(encoding="utf-8")
    if args.mode == "visual-deck":
        errors, warnings = validate_visual_deck(text)
    else:
        errors, warnings = validate_sections(text, args.mode)

    result = {
        "valid": not errors,
        "mode": args.mode,
        "errors": errors,
        "warnings": warnings,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
