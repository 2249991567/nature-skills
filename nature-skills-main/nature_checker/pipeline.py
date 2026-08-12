"""End-to-end pipeline: load → parse → check → polish → write reports."""

from __future__ import annotations

from pathlib import Path
from typing import Optional

from .checkers import run_all_checks
from .io_loader import load_document, load_text
from .models import CheckReport
from .polish import PolishResult, polish_paper
from .report import (
    resolve_output_paths,
    write_compliance_report,
    write_polished_full,
    write_revision_notes,
)
from .sections import PaperDocument, parse_sections


def polish_text(text: str) -> tuple[PaperDocument, CheckReport, PolishResult]:
    """Public API: polish a raw text string (no file I/O)."""
    paper = parse_sections(load_text(text))
    report = run_all_checks(paper)
    polished = polish_paper(paper)
    return paper, report, polished


def run_pipeline(
    input_path: Optional[str | Path] = None,
    output_path: Optional[str | Path] = None,
    text: Optional[str] = None,
) -> dict:
    """
    Run the full checker/polisher.

    Provide either ``input_path`` (.docx / .md / .txt) or ``text``.
    If ``output_path`` is set, write the three Markdown artefacts.
    """
    if text is not None:
        raw = load_text(text)
    elif input_path is not None:
        raw = load_document(input_path)
    else:
        raise ValueError("Provide input_path or text")

    paper, report, polished = polish_text(raw)

    written: dict[str, str] = {}
    if output_path is not None:
        paths = resolve_output_paths(output_path)
        write_polished_full(paths["polished"], paper, polished)
        write_revision_notes(paths["revision"], polished)
        write_compliance_report(paths["compliance"], report)
        written = {k: str(v) for k, v in paths.items()}

    return {
        "paper": paper,
        "report": report,
        "polished": polished,
        "written": written,
    }
