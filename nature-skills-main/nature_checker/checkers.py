"""Compliance checkers: length, tense, style, structure."""

from __future__ import annotations

import re
from collections import Counter

from .models import CheckReport, Issue
from .rules import (
    ABSOLUTE_PATTERNS,
    CANONICAL_SECTIONS,
    CONCLUSION_MARKERS,
    DISCUSSION_WIDEN_MARKERS,
    HEDGING_MARKERS,
    INFORMAL_PATTERNS,
    INTRO_GAP_MARKERS,
    MAX_SENTENCE_WORDS,
    MULTI_PROPOSITION_WARN_WORDS,
    RESULTS_PAST_MARKERS,
    RESULTS_PRESENT_MARKERS,
    RULE_SOURCES,
    TARGET_AVG_WORDS_MAX,
    TARGET_AVG_WORDS_MIN,
    VAGUE_METHODS_PHRASES,
)
from .sections import PaperDocument
from .sentences import annotate_sentences, mean_word_count


def _suggest_split(sentence: str) -> str:
    """Heuristic split suggestion at coordinating conjunctions / relative clauses."""
    connectors = [
        ", and ",
        "; and ",
        ", but ",
        ", which ",
        ", while ",
        ", whereas ",
        ", although ",
        "; ",
        ", that ",
    ]
    lower = sentence
    best = None
    mid = len(sentence) // 2
    for conn in connectors:
        idx = lower.find(conn)
        while idx != -1:
            # Prefer split near middle
            if best is None or abs(idx - mid) < abs(best[0] - mid):
                best = (idx, conn)
            idx = lower.find(conn, idx + len(conn))
    if best:
        i, conn = best
        left = sentence[:i].rstrip(" ,;") + "."
        right = sentence[i + len(conn) :].lstrip()
        if right:
            right = right[0].upper() + right[1:]
        return f"{left} {right}"
    return (
        "Split into two sentences at the main clause boundary "
        "(one subject–verb proposition each; SKILL.md)."
    )


def check_sentence_length(paper: PaperDocument) -> CheckReport:
    report = CheckReport()
    all_counts: list[int] = []
    over_total = 0

    for name in CANONICAL_SECTIONS:
        body = paper.get(name)
        if not body.strip():
            continue
        sents = annotate_sentences(body)
        counts = [s.word_count for s in sents]
        all_counts.extend(counts)
        avg = mean_word_count(sents)
        report.stats[f"{name}_sentence_count"] = len(sents)
        report.stats[f"{name}_avg_words"] = round(avg, 2)

        for s in sents:
            if s.word_count > MAX_SENTENCE_WORDS:
                over_total += 1
                report.add(
                    Issue(
                        category="length",
                        severity="error",
                        section=name,
                        message=(
                            f"Sentence {s.index} has {s.word_count} words "
                            f"(limit {MAX_SENTENCE_WORDS})."
                        ),
                        rule_source=RULE_SOURCES["sentence_length"],
                        sentence=s.text,
                        suggestion=_suggest_split(s.text),
                        traffic_light="green",
                        meta={"word_count": s.word_count},
                    )
                )
            elif s.word_count > MULTI_PROPOSITION_WARN_WORDS:
                # SKILL: if >20 words, check multi-proposition
                if re.search(r"\b(and|but|which|while|whereas|although)\b", s.text, re.I):
                    report.add(
                        Issue(
                            category="length",
                            severity="warning",
                            section=name,
                            message=(
                                f"Sentence {s.index} has {s.word_count} words and may "
                                "contain more than one main proposition."
                            ),
                            rule_source=RULE_SOURCES["sentence_length"],
                            sentence=s.text,
                            suggestion="Prefer one core subject–verb proposition per sentence.",
                            traffic_light="green",
                        )
                    )

    if all_counts:
        overall_avg = sum(all_counts) / len(all_counts)
        report.stats["overall_sentence_count"] = len(all_counts)
        report.stats["overall_avg_words"] = round(overall_avg, 2)
        report.stats["over_30_count"] = over_total
        if not (TARGET_AVG_WORDS_MIN <= overall_avg <= TARGET_AVG_WORDS_MAX):
            report.add(
                Issue(
                    category="length",
                    severity="warning",
                    section="ALL",
                    message=(
                        f"Overall mean sentence length is {overall_avg:.1f} words "
                        f"(target {TARGET_AVG_WORDS_MIN}–{TARGET_AVG_WORDS_MAX})."
                    ),
                    rule_source=RULE_SOURCES["sentence_length"],
                    suggestion="Shorten dense sentences; split overloaded clauses.",
                    traffic_light="green",
                )
            )
    return report


def check_tense(paper: PaperDocument) -> CheckReport:
    report = CheckReport()

    # Results: flag non-past reporting
    results = paper.get("Results")
    if results.strip():
        for s in annotate_sentences(results):
            text = s.text
            has_past = any(re.search(rf"\b{re.escape(m)}\b", text, re.I) for m in RESULTS_PAST_MARKERS)
            present_hits = [
                p for p in RESULTS_PRESENT_MARKERS if re.search(p, text, re.I)
            ]
            # Discussion syntax leaking into Results
            discussion_leak = bool(
                re.search(
                    r"\b(may reflect|could indicate|is likely due to|may facilitate)\b",
                    text,
                    re.I,
                )
            )
            if present_hits and not has_past:
                report.add(
                    Issue(
                        category="tense",
                        severity="error",
                        section="Results",
                        message=(
                            f"Sentence {s.index} appears non-past for Results reporting."
                        ),
                        rule_source=RULE_SOURCES["results_tense"],
                        sentence=text,
                        suggestion=(
                            "Rewrite in past tense (e.g. showed / increased / was detected)."
                        ),
                        traffic_light="yellow",
                        meta={"present_patterns": present_hits},
                    )
                )
            elif discussion_leak:
                report.add(
                    Issue(
                        category="tense",
                        severity="warning",
                        section="Results",
                        message=(
                            f"Sentence {s.index} uses Discussion-style interpretation syntax."
                        ),
                        rule_source=RULE_SOURCES["results_tense"],
                        sentence=text,
                        suggestion=(
                            "Results = what happened; move interpretation to Discussion."
                        ),
                        traffic_light="yellow",
                    )
                )

    # Discussion: absolute claims without hedging
    discussion = paper.get("Discussion")
    if discussion.strip():
        for s in annotate_sentences(discussion):
            text = s.text
            abs_hits = [p for p in ABSOLUTE_PATTERNS if re.search(p, text, re.I)]
            has_hedge = any(h in text.lower() for h in HEDGING_MARKERS)
            # Strong claim verbs without hedge
            strong_no_hedge = bool(
                re.search(
                    r"\b(demonstrates?|proves?|establishes?|confirms?)\b",
                    text,
                    re.I,
                )
            ) and not has_hedge
            if abs_hits or strong_no_hedge:
                report.add(
                    Issue(
                        category="tense",
                        severity="error",
                        section="Discussion",
                        message=(
                            f"Sentence {s.index} uses absolute / unhedged interpretive language."
                        ),
                        rule_source=RULE_SOURCES["discussion_hedging"],
                        sentence=text,
                        suggestion=(
                            "Use moderate/speculative phrasing: suggest / may reflect / "
                            "could indicate (phrasebank-playbook.md)."
                        ),
                        traffic_light="yellow",
                        meta={"absolute_patterns": abs_hits},
                    )
                )
    return report


def check_style(paper: PaperDocument) -> CheckReport:
    report = CheckReport()
    contraction_re = re.compile(
        r"\b(don't|doesn't|didn't|can't|couldn't|won't|wouldn't|shouldn't|"
        r"isn't|aren't|wasn't|weren't|hasn't|haven't|hadn't|it's|that's|"
        r"there's|we're|they're|we've|they've|i'm|let's|what's|who's)\b",
        re.I,
    )
    we_re = re.compile(r"\bwe\b", re.I)
    rhetorical_re = re.compile(r"\?\s*$")

    for name in CANONICAL_SECTIONS:
        body = paper.get(name)
        if not body.strip():
            continue
        sents = annotate_sentences(body)
        we_count = 0
        for s in sents:
            text = s.text
            # Contractions
            for m in contraction_re.finditer(text):
                report.add(
                    Issue(
                        category="style",
                        severity="warning",
                        section=name,
                        message=f"Contraction '{m.group(0)}' found.",
                        rule_source=RULE_SOURCES["style_contractions"],
                        sentence=text,
                        suggestion="Expand contractions (style-guardrails.md).",
                        traffic_light="green",
                    )
                )
            # Informal
            for pat, repl in INFORMAL_PATTERNS:
                if re.search(pat, text, re.I):
                    suggestion = (
                        f"Prefer more precise academic wording"
                        + (f" (e.g. '{repl}')" if repl else "")
                        + "."
                    )
                    report.add(
                        Issue(
                            category="style",
                            severity="warning",
                            section=name,
                            message=f"Informal / redundant phrasing matched /{pat}/.",
                            rule_source=RULE_SOURCES["style_register"],
                            sentence=text,
                            suggestion=suggestion,
                            traffic_light="green",
                        )
                    )
            # Overclaim lexicon
            for pat in ABSOLUTE_PATTERNS:
                if re.search(pat, text, re.I):
                    report.add(
                        Issue(
                            category="style",
                            severity="error",
                            section=name,
                            message=f"Overclaim language matched /{pat}/.",
                            rule_source=RULE_SOURCES["style_overclaim"],
                            sentence=text,
                            suggestion=(
                                "Soften: show / suggest / to our knowledge / "
                                "among the strongest / in this cohort."
                            ),
                            traffic_light="yellow",
                        )
                    )
            # Rhetorical questions
            if rhetorical_re.search(text) and name != "Introduction":
                report.add(
                    Issue(
                        category="style",
                        severity="warning",
                        section=name,
                        message="Rhetorical question in polished manuscript prose.",
                        rule_source=RULE_SOURCES["style_register"],
                        sentence=text,
                        suggestion="Avoid rhetorical questions (style-guardrails.md).",
                        traffic_light="green",
                    )
                )
            we_count += len(we_re.findall(text))

        # Excessive first person
        if sents and we_count / max(len(sents), 1) > 0.45 and we_count >= 4:
            report.add(
                Issue(
                    category="style",
                    severity="warning",
                    section=name,
                    message=(
                        f"First-person 'we' appears {we_count} times across "
                        f"{len(sents)} sentences (possible overuse)."
                    ),
                    rule_source=RULE_SOURCES["style_register"],
                    suggestion=(
                        "Use 'we' only when it suits the discipline; keep prose impersonal where appropriate."
                    ),
                    traffic_light="green",
                )
            )

        # Vague Methods
        if name == "Methods":
            low = body.lower()
            for phrase in VAGUE_METHODS_PHRASES:
                if phrase in low:
                    report.add(
                        Issue(
                            category="style",
                            severity="error",
                            section="Methods",
                            message=f"Vague Methods phrase: '{phrase}'.",
                            rule_source=RULE_SOURCES["methods_vague"],
                            suggestion=(
                                "Replace with reproducible detail (parameters, controls, software versions)."
                            ),
                            traffic_light="yellow",
                        )
                    )
    return report


def check_structure(paper: PaperDocument) -> CheckReport:
    report = CheckReport()
    present = [n for n in CANONICAL_SECTIONS if paper.has(n)]
    missing = [n for n in CANONICAL_SECTIONS if not paper.has(n)]
    report.stats["sections_present"] = present
    report.stats["sections_missing"] = missing

    for name in missing:
        report.add(
            Issue(
                category="structure",
                severity="warning",
                section=name,
                message=f"Section '{name}' is missing or empty.",
                rule_source=RULE_SOURCES["section_moves"],
                suggestion=f"Ensure {name} fulfils its rhetorical questions (section-moves.md).",
                traffic_light="yellow",
            )
        )

    # Hourglass: Introduction should narrow (gap + study aim)
    intro = paper.get("Introduction")
    if intro.strip():
        low = intro.lower()
        gap_hits = [m for m in INTRO_GAP_MARKERS if m in low]
        if len(gap_hits) < 2:
            report.add(
                Issue(
                    category="structure",
                    severity="warning",
                    section="Introduction",
                    message=(
                        "Introduction may lack hourglass narrowing "
                        "(gap / unresolved question / study aim)."
                    ),
                    rule_source=RULE_SOURCES["hourglass"],
                    suggestion=(
                        "Move order: importance → known → gap → aim "
                        "(section-moves.md Introduction)."
                    ),
                    traffic_light="yellow",
                    meta={"markers_found": gap_hits},
                )
            )
        # Results leaking into Introduction
        if re.search(r"\b(p\s*[<＝=]\s*0\.\d+|we found that|significantly higher)\b", low):
            report.add(
                Issue(
                    category="structure",
                    severity="warning",
                    section="Introduction",
                    message="Introduction appears to summarise Results (SKILL.md forbids this).",
                    rule_source=RULE_SOURCES["hourglass"],
                    suggestion="Do not summarise Results or Conclusion in the Introduction.",
                    traffic_light="yellow",
                )
            )

    # Discussion should widen: implications / limitations / prior work
    disc = paper.get("Discussion")
    if disc.strip():
        low = disc.lower()
        widen = [m for m in DISCUSSION_WIDEN_MARKERS if m in low]
        if len(widen) < 2:
            report.add(
                Issue(
                    category="structure",
                    severity="warning",
                    section="Discussion",
                    message=(
                        "Discussion may not widen back to field, limits, or implications "
                        "(hourglass)."
                    ),
                    rule_source=RULE_SOURCES["hourglass"],
                    suggestion=(
                        "Include interpretation, comparison with earlier work, limitations, "
                        "and bounded implications."
                    ),
                    traffic_light="yellow",
                    meta={"markers_found": widen},
                )
            )
        # Results repetition heuristic: many pure reporting past sentences without hedge
        sents = annotate_sentences(disc)
        report_like = 0
        for s in sents:
            if re.search(r"\b(was|were|showed|increased|decreased)\b", s.text, re.I) and not any(
                h in s.text.lower() for h in HEDGING_MARKERS
            ):
                report_like += 1
        if sents and report_like / len(sents) > 0.5:
            report.add(
                Issue(
                    category="structure",
                    severity="warning",
                    section="Discussion",
                    message=(
                        "Discussion may be repeating Results without interpretation "
                        "(Results vs Discussion mix)."
                    ),
                    rule_source=RULE_SOURCES["hourglass"],
                    suggestion="Results = what we observed; Discussion = how we understand it.",
                    traffic_light="yellow",
                )
            )

    # Conclusion three-part close
    conclusion = paper.get("Conclusion")
    if conclusion.strip():
        low = conclusion.lower()
        hits = [m for m in CONCLUSION_MARKERS if m in low]
        if len(hits) < 2:
            report.add(
                Issue(
                    category="structure",
                    severity="warning",
                    section="Conclusion",
                    message="Conclusion may lack the three-part close (contribution / evidence / bounded implication).",
                    rule_source=RULE_SOURCES["section_moves"],
                    suggestion=(
                        "Restate central contribution, key evidence, then implication with a boundary."
                    ),
                    traffic_light="yellow",
                )
            )
        # New data in conclusion
        if re.search(r"\b(n\s*=\s*\d+|p\s*[<＝=]\s*0\.\d+)\b", low):
            report.add(
                Issue(
                    category="structure",
                    severity="error",
                    section="Conclusion",
                    message="Conclusion appears to introduce new quantitative data.",
                    rule_source=RULE_SOURCES["section_moves"],
                    suggestion="Do not introduce new data in the Conclusion (SKILL.md).",
                    traffic_light="red",
                )
            )

    # Abstract mini-paper pattern
    abstract = paper.get("Abstract")
    if abstract.strip():
        low = abstract.lower()
        has_gap = any(x in low for x in ("however", "remain", "poorly", "gap", "need", "challenge"))
        has_approach = any(x in low for x in ("here", "we ", "this study", "using"))
        has_result = any(x in low for x in ("found", "show", "result", "increased", "decreased", "%"))
        has_impl = any(x in low for x in ("suggest", "implicat", "may", "could", "these findings"))
        missing_bits = []
        if not has_gap:
            missing_bits.append("gap/objective")
        if not has_approach:
            missing_bits.append("approach")
        if not has_result:
            missing_bits.append("key results")
        if not has_impl:
            missing_bits.append("implication")
        if missing_bits:
            report.add(
                Issue(
                    category="structure",
                    severity="info",
                    section="Abstract",
                    message=(
                        "Abstract may be incomplete as a mini-paper "
                        f"(missing signals: {', '.join(missing_bits)})."
                    ),
                    rule_source=RULE_SOURCES["section_moves"],
                    suggestion="Pattern: context/problem → gap → approach → key results → implication.",
                    traffic_light="yellow",
                )
            )

    # Integrity reminder (always)
    report.add(
        Issue(
            category="integrity",
            severity="info",
            section="ALL",
            message=(
                "Red-line reminder: do not invent references, data, mechanisms, "
                "or rewrite the paper's core scientific argument."
            ),
            rule_source=RULE_SOURCES["integrity"],
            suggestion="AI may polish wording only; authors own the core argument.",
            traffic_light="red",
        )
    )
    return report


def run_all_checks(paper: PaperDocument) -> CheckReport:
    report = CheckReport()
    for fn in (check_sentence_length, check_tense, check_style, check_structure):
        report.extend(fn(paper))
    # Aggregate counts
    cats = Counter(i.category for i in report.issues)
    report.stats["issue_counts_by_category"] = dict(cats)
    report.stats["total_issues"] = len(report.issues)
    return report
