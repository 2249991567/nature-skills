"""Markdown report writers for the three required outputs."""

from __future__ import annotations

from pathlib import Path

from .models import CheckReport, Issue
from .polish import PolishResult
from .rules import CANONICAL_SECTIONS, TRAFFIC_LIGHT
from .sections import PaperDocument, sections_as_markdown


def _issue_md(issue: Issue) -> str:
    lines = [
        f"- **[{issue.severity.upper()}][{issue.traffic_light.upper()}]** "
        f"{issue.section}: {issue.message}",
        f"  - Rule: {issue.rule_source}",
    ]
    if issue.sentence:
        snippet = issue.sentence if len(issue.sentence) <= 220 else issue.sentence[:217] + "..."
        lines.append(f"  - Sentence: {snippet}")
    if issue.suggestion:
        lines.append(f"  - Suggestion: {issue.suggestion}")
    return "\n".join(lines)


def write_polished_full(path: Path, paper: PaperDocument, polish: PolishResult) -> None:
    """Output 1: polished full text with <u> marks on key edits."""
    body = sections_as_markdown(paper, bodies=polish.bodies_marked)
    header = (
        "# Polished Manuscript (Nature-polishing rules)\n\n"
        "> Key automated edits are marked with HTML `<u>underline</u>`.\n"
        "> Logic-first principle: structural issues are flagged in Revision Notes "
        "and the Compliance Report; wording edits never invent data or citations.\n\n"
        "---\n\n"
    )
    path.write_text(header + body, encoding="utf-8")


def write_revision_notes(path: Path, polish: PolishResult) -> None:
    """Output 2: per-section 3–5 revision notes with traffic lights."""
    lines = [
        "# Revision Notes",
        "",
        "Notes follow SKILL.md output format: major structural and stylistic changes,",
        "with AI traffic-light labels (Green / Yellow / Red).",
        "",
        "## Traffic-light legend",
        "",
        f"- {TRAFFIC_LIGHT['green']}",
        f"- {TRAFFIC_LIGHT['yellow']}",
        f"- {TRAFFIC_LIGHT['red']}",
        "",
    ]
    for name in list(CANONICAL_SECTIONS) + ["Integrity"]:
        bullets = polish.revision_notes.get(name) or []
        if not bullets:
            continue
        lines.append(f"## {name}")
        lines.append("")
        for b in bullets[:5]:
            lines.append(f"- {b}")
        lines.append("")

    if polish.refused_red:
        lines.append("## Red-line refusals (this run)")
        lines.append("")
        for r in polish.refused_red:
            lines.append(f"- {r}")
        lines.append("")

    path.write_text("\n".join(lines), encoding="utf-8")


def write_compliance_report(path: Path, report: CheckReport) -> None:
    """Output 3: compliance report — length, tense, style, structure, risks."""
    stats = report.stats
    lines = [
        "# Compliance Check Report",
        "",
        "Rules sourced exclusively from `nature-polishing/` "
        "(SKILL.md, writing-strategy.md, section-moves.md, "
        "phrasebank-playbook.md, style-guardrails.md).",
        "",
        "## Summary statistics",
        "",
        f"- Total issues flagged: **{stats.get('total_issues', len(report.issues))}**",
        f"- Sentences overall: {stats.get('overall_sentence_count', 'n/a')}",
        f"- Mean words / sentence: {stats.get('overall_avg_words', 'n/a')} "
        "(target 15–25; hard max 30)",
        f"- Sentences > 30 words: {stats.get('over_30_count', 'n/a')}",
        f"- Sections present: {', '.join(stats.get('sections_present', [])) or 'none'}",
        f"- Sections missing: {', '.join(stats.get('sections_missing', [])) or 'none'}",
        "",
        "### Issues by category",
        "",
    ]
    counts = stats.get("issue_counts_by_category", {})
    if counts:
        for cat, n in sorted(counts.items()):
            lines.append(f"- `{cat}`: {n}")
    else:
        lines.append("- (none)")
    lines.append("")

    categories = [
        ("length", "Sentence-length checks"),
        ("tense", "Tense & hedging checks"),
        ("style", "Style & register checks"),
        ("structure", "Hourglass & section-structure checks"),
        ("integrity", "Integrity / risk reminders"),
    ]
    for cat, title in categories:
        issues = report.by_category(cat)
        lines.append(f"## {title}")
        lines.append("")
        if not issues:
            lines.append("- No issues in this category.")
            lines.append("")
            continue
        for issue in issues:
            lines.append(_issue_md(issue))
        lines.append("")

    lines.extend(
        [
            "## Risk summary",
            "",
            "- **Green** items are mechanical language fixes; still verify terminology.",
            "- **Yellow** items change claim strength or section logic; require author review.",
            "- **Red** items mark forbidden AI actions (fabrication / core-argument authorship).",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def resolve_output_paths(output: str | Path) -> dict[str, Path]:
    """
    Map --output path to three Markdown files.

    If output is `./polished_result.md`, produce:
      polished_result.md
      polished_result_revision_notes.md
      polished_result_compliance_report.md
    """
    out = Path(output)
    if out.suffix.lower() in {".md", ".markdown", ".txt"}:
        stem = out.with_suffix("")
        parent = out.parent
    else:
        # treat as directory or stem without suffix
        if out.exists() and out.is_dir():
            parent = out
            stem = parent / "polished_result"
        else:
            parent = out.parent if out.suffix else out.parent
            stem = out if out.suffix else out
            if not out.suffix:
                parent = out.parent
                stem = out

    parent.mkdir(parents=True, exist_ok=True)
    return {
        "polished": Path(str(stem) + ".md"),
        "revision": Path(str(stem) + "_revision_notes.md"),
        "compliance": Path(str(stem) + "_compliance_report.md"),
    }
