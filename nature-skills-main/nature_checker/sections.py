"""Detect and split standard paper sections."""

from __future__ import annotations

import re
from dataclasses import dataclass, field

from .rules import CANONICAL_SECTIONS, SECTION_ALIASES


@dataclass
class Section:
    name: str
    body: str
    heading_raw: str = ""


@dataclass
class PaperDocument:
    raw_text: str
    preamble: str = ""
    sections: dict[str, Section] = field(default_factory=dict)
    detected_order: list[str] = field(default_factory=list)

    def get(self, name: str) -> str:
        sec = self.sections.get(name)
        return sec.body if sec else ""

    def has(self, name: str) -> bool:
        return name in self.sections and bool(self.sections[name].body.strip())


def _normalize_heading(line: str) -> str | None:
    """Map a heading line to a canonical section name, or None."""
    s = line.strip()
    # Markdown heading
    s = re.sub(r"^#{1,6}\s*", "", s)
    # Numbered: "1. Introduction" / "I. INTRODUCTION"
    s = re.sub(r"^[\divxIVXLC]+\.?\s+", "", s, flags=re.IGNORECASE)
    s = re.sub(r"^\d+(\.\d+)*\.?\s+", "", s)
    # Trailing punctuation
    s = s.strip(" .:;-—")
    low = s.lower()

    # Exact / alias match for short headings only
    if len(low) > 80:
        return None
    for canonical, aliases in SECTION_ALIASES.items():
        for alias in aliases:
            if low == alias or low.startswith(alias + " ") or low.startswith(alias + ":"):
                return canonical
            # ALL CAPS headings
            if low == alias:
                return canonical
    return None


def parse_sections(text: str) -> PaperDocument:
    """Split full text into Abstract/Introduction/Methods/Results/Discussion/Conclusion."""
    lines = text.replace("\r\n", "\n").replace("\r", "\n").split("\n")
    paper = PaperDocument(raw_text=text)

    current_name: str | None = None
    current_heading = ""
    buffer: list[str] = []
    preamble_buf: list[str] = []

    def flush() -> None:
        nonlocal buffer, current_name, current_heading
        body = "\n".join(buffer).strip()
        if current_name is None:
            if body:
                preamble_buf.append(body)
        else:
            # Append if section appears twice
            if current_name in paper.sections:
                prev = paper.sections[current_name].body
                body = (prev + "\n\n" + body).strip()
            else:
                paper.detected_order.append(current_name)
            paper.sections[current_name] = Section(
                name=current_name, body=body, heading_raw=current_heading
            )
        buffer = []

    for line in lines:
        mapped = _normalize_heading(line)
        # Only treat as heading if line is short / title-like
        is_heading = mapped is not None and (
            len(line.strip()) < 80
            and not line.strip().endswith(",")
            and (
                line.strip().startswith("#")
                or line.isupper()
                or re.match(r"^#{0,6}\s*\d", line.strip())
                or mapped.lower() == line.strip().lower().strip("# ").rstrip(".:")
                or any(
                    line.strip().lower().rstrip(".:") == a
                    for a in SECTION_ALIASES.get(mapped, ())
                )
                or re.match(
                    r"^(#{1,6}\s*)?(\d+(\.\d+)*\.?\s*)?(Abstract|Introduction|Methods|"
                    r"Materials and Methods|Results|Discussion|Conclusions?)\s*$",
                    line.strip(),
                    flags=re.IGNORECASE,
                )
            )
        )
        if is_heading and mapped:
            flush()
            current_name = mapped
            current_heading = line.strip()
            continue
        buffer.append(line)

    flush()
    paper.preamble = "\n\n".join(preamble_buf).strip()

    # Ensure all canonical keys exist (empty if missing)
    for name in CANONICAL_SECTIONS:
        if name not in paper.sections:
            paper.sections[name] = Section(name=name, body="")

    return paper


def sections_as_markdown(paper: PaperDocument, bodies: dict[str, str] | None = None) -> str:
    """Reassemble paper as Markdown with canonical headings."""
    parts: list[str] = []
    if paper.preamble.strip():
        parts.append(paper.preamble.strip())
        parts.append("")
    source = bodies if bodies is not None else {n: paper.get(n) for n in CANONICAL_SECTIONS}
    for name in CANONICAL_SECTIONS:
        body = (source.get(name) or "").strip()
        if not body and name not in paper.detected_order:
            continue
        parts.append(f"## {name}")
        parts.append("")
        parts.append(body if body else "*(section empty)*")
        parts.append("")
    return "\n".join(parts).strip() + "\n"
