#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Nature Paper Checker & Polisher
================================
Implements the mandatory rules from nature-polishing/
(SKILL.md + references/writing-strategy.md, section-moves.md,
phrasebank-playbook.md, style-guardrails.md).

Features
--------
- Input: .docx / .md / .txt, or --text for direct strings
- Auto-split: Abstract / Introduction / Methods / Results / Discussion / Conclusion
- Hard checks: sentence length (<=30 words), Results past tense,
  Discussion hedging, style/register, hourglass structure
- Rule-based polishing with Green/Yellow/Red AI traffic lights
- Never invents data, citations, mechanisms, or core arguments

Install
-------
    pip install -r requirements.txt
    # only external dependency: python-docx (for .docx)

Usage
-----
    python nature_paper_checker.py --input ./my_paper.md --output ./polished_result.md

    python nature_paper_checker.py --input ./my_paper.docx --output ./out/polished_result.md

    python nature_paper_checker.py --text "Abstract\\n\\n..." --output ./polished_result.md

Outputs (three Markdown files)
------------------------------
    polished_result.md
    polished_result_revision_notes.md
    polished_result_compliance_report.md
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Nature-journal academic paper checker and polisher "
            "(rules from nature-polishing skill set)."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument(
        "--input",
        "-i",
        type=str,
        default=None,
        help="Path to paper (.docx, .md, or .txt)",
    )
    parser.add_argument(
        "--output",
        "-o",
        type=str,
        required=True,
        help="Output path prefix, e.g. ./polished_result.md",
    )
    parser.add_argument(
        "--text",
        "-t",
        type=str,
        default=None,
        help="Direct text string input (alternative to --input)",
    )
    args = parser.parse_args(argv)

    if not args.input and not args.text:
        parser.error("Provide --input or --text")

    # Ensure package import works when run as a script from repo root
    root = Path(__file__).resolve().parent
    if str(root) not in sys.path:
        sys.path.insert(0, str(root))

    from nature_checker.pipeline import run_pipeline

    try:
        result = run_pipeline(
            input_path=args.input,
            output_path=args.output,
            text=args.text,
        )
    except Exception as exc:  # noqa: BLE001 — CLI boundary
        print(f"[ERROR] {exc}", file=sys.stderr)
        return 1

    written = result["written"]
    report = result["report"]
    print("Nature paper checker finished.")
    print(f"  Issues flagged : {report.stats.get('total_issues', len(report.issues))}")
    print(f"  Mean words/sent: {report.stats.get('overall_avg_words', 'n/a')}")
    print(f"  Sentences >30  : {report.stats.get('over_30_count', 'n/a')}")
    if written:
        print("  Outputs:")
        for key, path in written.items():
            print(f"    - {key}: {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
