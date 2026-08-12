"""
Rule-based Nature-style polishing.

Principles (SKILL.md):
1. Prefer structural/logic awareness first; then wording.
2. Never invent data, references, mechanisms, or core arguments.
3. Annotate edits with AI traffic lights (green / yellow / red).
"""

from __future__ import annotations

import re
from collections import OrderedDict
from dataclasses import dataclass, field

from .rules import (
    BRITISH_SPELLING,
    CANONICAL_SECTIONS,
    CONTRACTIONS,
    HEDGING_MARKERS,
    INFORMAL_PATTERNS,
    MAX_SENTENCE_WORDS,
    OVERCLAIM_REPLACEMENTS,
    RULE_SOURCES,
)
from .sections import PaperDocument
from .sentences import split_sentences, word_count


@dataclass
class Edit:
    section: str
    original: str
    polished: str
    reason: str
    rule_source: str
    traffic_light: str  # green | yellow | red


@dataclass
class PolishResult:
    bodies: dict[str, str] = field(default_factory=dict)
    bodies_marked: dict[str, str] = field(default_factory=dict)
    edits: list[Edit] = field(default_factory=list)
    revision_notes: dict[str, list[str]] = field(default_factory=dict)
    refused_red: list[str] = field(default_factory=list)


def _underline(text: str) -> str:
    return f"<u>{text}</u>"


def _strip_marks(text: str) -> str:
    return text.replace("<u>", "").replace("</u>", "")


def _case_match(raw: str, replacement: str) -> str:
    if not raw or not replacement:
        return replacement
    if raw.isupper():
        return replacement.upper()
    if raw[0].isupper():
        return replacement[0].upper() + replacement[1:]
    return replacement


def _expand_contractions(text: str) -> tuple[str, list[tuple[str, str]]]:
    changes: list[tuple[str, str]] = []

    def repl(m: re.Match[str]) -> str:
        raw = m.group(0)
        key = raw.lower()
        if key not in CONTRACTIONS:
            return raw
        rep = _case_match(raw, CONTRACTIONS[key])
        changes.append((raw, rep))
        return _underline(rep)

    pattern = re.compile(
        r"\b("
        + "|".join(re.escape(k) for k in sorted(CONTRACTIONS, key=len, reverse=True))
        + r")\b",
        re.I,
    )
    return pattern.sub(repl, text), changes


def _british_spelling(text: str) -> tuple[str, list[tuple[str, str]]]:
    changes: list[tuple[str, str]] = []
    out = text
    for am, br in BRITISH_SPELLING.items():
        if am == "program":
            continue

        def make_repl(b: str):
            def repl(m: re.Match[str]) -> str:
                raw = m.group(0)
                rep = _case_match(raw, b)
                changes.append((raw, rep))
                return _underline(rep)

            return repl

        out = re.sub(rf"\b{re.escape(am)}\b", make_repl(br), out, flags=re.I)
    return out, changes


def _soften_informal(text: str) -> tuple[str, list[tuple[str, str]]]:
    changes: list[tuple[str, str]] = []
    out = text
    for pat, repl in INFORMAL_PATTERNS:

        def make(r: str):
            def sub(m: re.Match[str]) -> str:
                raw = m.group(0)
                if not r:
                    changes.append((raw, ""))
                    return ""
                rep = _case_match(raw, r)
                changes.append((raw, rep))
                return _underline(rep)

            return sub

        out = re.sub(pat, make(repl), out, flags=re.I)
    out = re.sub(r"[ \t]{2,}", " ", out)
    out = re.sub(r"\s+([,.;:])", r"\1", out)
    return out.strip(), changes


def _soften_overclaims(text: str) -> tuple[str, list[tuple[str, str, str]]]:
    changes: list[tuple[str, str, str]] = []
    out = text
    for pat, repl, light in OVERCLAIM_REPLACEMENTS:

        def make(r: str, light_: str):
            def sub(m: re.Match[str]) -> str:
                raw = m.group(0)
                rep = _case_match(raw, r)
                changes.append((raw, rep, light_))
                return _underline(rep)

            return sub

        out = re.sub(pat, make(repl, light), out, flags=re.I)
    return out, changes


def _split_long_sentence(sentence: str) -> list[str]:
    if word_count(sentence) <= MAX_SENTENCE_WORDS:
        return [sentence]

    connectors = [
        (", and ", ". "),
        ("; and ", ". "),
        (" and ", ". "),
        (", but ", ". However, "),
        (" but ", ". However, "),
        (", which ", ". This "),
        (" which ", ". This "),
        (", while ", ". Meanwhile, "),
        (", whereas ", ". By contrast, "),
        (" when ", ". This occurred when "),
        ("; ", ". "),
    ]
    mid = len(sentence) // 2
    candidates: list[tuple[int, str, str]] = []
    for conn, joiner in connectors:
        start = 0
        while True:
            idx = sentence.find(conn, start)
            if idx == -1:
                break
            # Prefer splits near the middle; avoid tiny fragments
            left = sentence[:idx].rstrip(" ,;")
            right = sentence[idx + len(conn) :].lstrip()
            if word_count(left) >= 6 and word_count(right) >= 6:
                candidates.append((abs(idx - mid), conn, joiner))
            start = idx + len(conn)
    candidates.sort(key=lambda x: x[0])
    for _, conn, joiner in candidates:
        idx = sentence.find(conn)
        left = sentence[:idx].rstrip(" ,;")
        right = sentence[idx + len(conn) :].lstrip()
        if joiner.startswith(". "):
            lead = joiner[2:]
            if lead:
                right = lead + (right[0].lower() + right[1:] if right else "")
            elif right:
                right = right[0].upper() + right[1:]
        s1 = left if left.endswith((".", "?", "!")) else left + "."
        s2 = right if right.endswith((".", "?", "!")) else right.rstrip(".") + "."
        parts: list[str] = []
        for piece in (s1, s2):
            if word_count(piece) > MAX_SENTENCE_WORDS and piece != sentence:
                parts.extend(_split_long_sentence(piece))
            else:
                parts.append(piece)
        if len(parts) > 1:
            return parts
    return [sentence]


def _mark_diffs(original: str, polished: str) -> str:
    """Underline tokens that differ from the original sentence."""
    if original == polished:
        return polished
    o_tokens = re.findall(r"\S+|\s+", original)
    p_tokens = re.findall(r"\S+|\s+", polished)
    # Fallback: underline whole polished sentence when token streams diverge heavily
    if abs(len(o_tokens) - len(p_tokens)) > max(4, len(o_tokens) // 2):
        # Mark contiguous changed spans via simple LCS-unaware pairwise
        return " ".join(
            _underline(t) if t.strip() and t not in original else t
            for t in polished.split(" ")
        )

    from difflib import SequenceMatcher

    sm = SequenceMatcher(a=o_tokens, b=p_tokens)
    out: list[str] = []
    for tag, _i1, _i2, j1, j2 in sm.get_opcodes():
        chunk = "".join(p_tokens[j1:j2])
        if tag == "equal":
            out.append(chunk)
        elif tag in {"replace", "insert"}:
            # underline non-whitespace pieces
            parts = re.findall(r"\S+|\s+", chunk)
            for p in parts:
                if p.strip():
                    out.append(_underline(p))
                else:
                    out.append(p)
        # delete: nothing to emit from polished
    return "".join(out)


def _results_to_past(sentence: str) -> tuple[str, bool]:
    pairs = [
        (r"\bshows that\b", "showed that"),
        (r"\bshow that\b", "showed that"),
        (r"\bshows\b", "showed"),
        (r"\bincreases\b", "increased"),
        (r"\bdecreases\b", "decreased"),
        (r"\breveals\b", "revealed"),
        (r"\bindicates\b", "indicated"),
        (r"\bdemonstrates\b", "demonstrated"),
        (r"\bwe show\b", "we showed"),
        (r"\bwe find\b", "we found"),
        (r"\bwe demonstrate\b", "we demonstrated"),
        (r"\bachieves\b", "achieved"),
        (r"\benables\b", "enabled"),
        (r"\bis significantly\b", "was significantly"),
        (r"\bare significantly\b", "were significantly"),
    ]
    out = sentence
    changed = False
    for pat, repl in pairs:

        def sub(m: re.Match[str], r: str = repl) -> str:
            return _underline(_case_match(m.group(0), r))

        new_out, n = re.subn(pat, sub, out, flags=re.I)
        if n:
            out = new_out
            changed = True
    return out, changed


def _add_discussion_hedging(sentence: str) -> tuple[str, bool]:
    low = sentence.lower()
    if any(h in low for h in HEDGING_MARKERS):
        return sentence, False
    patterns = [
        (
            r"^These results (prove|demonstrate|establish|confirm) that\b",
            "These results suggest that",
        ),
        (r"^This (proves|demonstrates|establishes|confirms) that\b", "This suggests that"),
        (r"^We (prove|demonstrate|establish|confirm) that\b", "We suggest that"),
        (r"\bdemonstrates that\b", "suggests that"),
        (r"\bproves that\b", "suggests that"),
        (r"\bconfirms that\b", "is consistent with the view that"),
        (r"\bclearly shows\b", "suggests"),
    ]
    out = sentence
    changed = False
    for pat, repl in patterns:
        new_out, n = re.subn(pat, lambda m, r=repl: _underline(r), out, flags=re.I)
        if n:
            out = new_out
            changed = True
    return out, changed


def _polish_sentence(sentence: str, section: str) -> tuple[str, list[Edit]]:
    edits: list[Edit] = []
    original = sentence
    working = sentence

    # 1) contractions — green
    marked, ch = _expand_contractions(working)
    for a, b in ch:
        edits.append(
            Edit(
                section,
                a,
                b,
                "Expanded contraction",
                RULE_SOURCES["style_contractions"],
                "green",
            )
        )
    working = _strip_marks(marked)

    # 2) informal — green
    marked, ch = _soften_informal(working)
    for a, b in ch:
        edits.append(
            Edit(
                section,
                a,
                b or "[removed]",
                "Reduced informal/redundant phrasing",
                RULE_SOURCES["style_register"],
                "green",
            )
        )
    working = _strip_marks(marked)

    # 3) British — green
    marked, ch = _british_spelling(working)
    for a, b in ch:
        edits.append(
            Edit(
                section,
                a,
                b,
                "British spelling (Nature-style)",
                RULE_SOURCES["british"],
                "green",
            )
        )
    working = _strip_marks(marked)

    # 4) overclaim — yellow
    marked, ch4 = _soften_overclaims(working)
    for a, b, light in ch4:
        edits.append(
            Edit(
                section,
                a,
                b,
                "Softened overclaim to match evidence strength",
                RULE_SOURCES["style_overclaim"],
                light,
            )
        )
    working = _strip_marks(marked)

    # 5) Results past tense — yellow
    if section == "Results":
        marked, changed = _results_to_past(working)
        if changed:
            edits.append(
                Edit(
                    section,
                    working,
                    _strip_marks(marked),
                    "Results reporting converted toward past tense",
                    RULE_SOURCES["results_tense"],
                    "yellow",
                )
            )
            working = _strip_marks(marked)

    # 6) Discussion hedging — yellow
    if section == "Discussion":
        marked, changed = _add_discussion_hedging(working)
        if changed:
            edits.append(
                Edit(
                    section,
                    working,
                    _strip_marks(marked),
                    "Added Discussion hedging (moderate evidence language)",
                    RULE_SOURCES["discussion_hedging"],
                    "yellow",
                )
            )
            working = _strip_marks(marked)

    # 7) sentence length split — green
    if word_count(working) > MAX_SENTENCE_WORDS:
        parts = _split_long_sentence(working)
        if len(parts) > 1:
            joined = " ".join(parts)
            edits.append(
                Edit(
                    section,
                    original,
                    joined,
                    f"Split sentence exceeding {MAX_SENTENCE_WORDS} words",
                    RULE_SOURCES["sentence_length"],
                    "green",
                )
            )
            working = joined

    marked_final = _mark_diffs(original, working) if working != original else working
    return marked_final, edits


def polish_section(name: str, body: str) -> tuple[str, str, list[Edit]]:
    """Return (plain_polished, marked_polished, edits)."""
    if not body.strip():
        return body, body, []

    paragraphs = re.split(r"\n\s*\n", body.strip())
    plain_paras: list[str] = []
    marked_paras: list[str] = []
    all_edits: list[Edit] = []

    for para in paragraphs:
        stripped = para.strip()
        if stripped.startswith(("#", "|")):
            plain_paras.append(stripped)
            marked_paras.append(stripped)
            continue
        sents = split_sentences(para)
        if not sents:
            plain_paras.append(stripped)
            marked_paras.append(stripped)
            continue
        plain_out: list[str] = []
        marked_out: list[str] = []
        for sent in sents:
            marked, edits = _polish_sentence(sent, name)
            all_edits.extend(edits)
            plain_out.append(_strip_marks(marked))
            marked_out.append(marked)
        plain_paras.append(" ".join(plain_out))
        marked_paras.append(" ".join(marked_out))

    return "\n\n".join(plain_paras), "\n\n".join(marked_paras), all_edits


def _build_revision_notes(edits: list[Edit], paper: PaperDocument) -> dict[str, list[str]]:
    notes: dict[str, list[str]] = {n: [] for n in CANONICAL_SECTIONS}

    for name in CANONICAL_SECTIONS:
        sec_edits = [e for e in edits if e.section == name]
        if not sec_edits:
            if not paper.has(name):
                notes[name].append(
                    "[Yellow] Section missing — ensure rhetorical duties in "
                    f"section-moves.md ({RULE_SOURCES['section_moves']})."
                )
            else:
                notes[name].append(
                    "[Green] No automated wording edits in this section; "
                    "manual review of claim–evidence–boundary still advised "
                    f"({RULE_SOURCES['core_argument']})."
                )
                notes[name].append(
                    "[Yellow] Verify section move order against section-moves.md."
                )
                notes[name].append(
                    "[Red] Do not invent data, references, or mechanisms here."
                )
            # ensure 3–5
            while len(notes[name]) < 3:
                notes[name].append(
                    "[Yellow] Re-check hourglass / section responsibility after human edit."
                )
            notes[name] = notes[name][:5]
            continue

        seen: OrderedDict[tuple[str, str], int] = OrderedDict()
        for e in sec_edits:
            key = (e.reason, e.traffic_light)
            seen[key] = seen.get(key, 0) + 1

        for (reason, light), count in list(seen.items())[:5]:
            sample = next(e for e in sec_edits if e.reason == reason)
            notes[name].append(
                f"[{light.capitalize()}] {reason} (×{count}). Rule: {sample.rule_source}"
            )

        # Pad to at least 3 with concrete examples
        idx = 0
        while len(notes[name]) < 3 and idx < len(sec_edits):
            e = sec_edits[idx]
            idx += 1
            bullet = (
                f"[{e.traffic_light.capitalize()}] Example: "
                f"'{e.original[:70]}' → '{e.polished[:70]}'. Rule: {e.rule_source}"
            )
            if bullet not in notes[name]:
                notes[name].append(bullet)
        notes[name] = notes[name][:5]

    notes["Integrity"] = [
        "[Red] Refused: inventing citations, data, experimental conclusions, or mechanisms "
        f"({RULE_SOURCES['integrity']}).",
        "[Red] Refused: drafting or replacing the paper's core scientific argument "
        f"({RULE_SOURCES['core_argument']}).",
        "[Green/Yellow] Allowed: grammar, clarity, hedging calibration, and limited "
        "wording restructuring only (SKILL.md AI traffic-light).",
    ]
    return notes


def polish_paper(paper: PaperDocument) -> PolishResult:
    result = PolishResult()
    result.refused_red = [
        "Did not generate fictional references or DOIs.",
        "Did not invent quantitative results, p-values, or sample sizes.",
        "Did not invent mechanistic explanations not present in the source.",
        "Did not rewrite the core scientific question or novelty claim from scratch.",
    ]

    all_edits: list[Edit] = []
    for name in CANONICAL_SECTIONS:
        body = paper.get(name)
        plain, marked, edits = polish_section(name, body)
        result.bodies[name] = plain
        result.bodies_marked[name] = marked
        all_edits.extend(edits)

    result.edits = all_edits
    result.revision_notes = _build_revision_notes(all_edits, paper)
    return result
