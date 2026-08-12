"""
Rule constants derived ONLY from nature-polishing skill documents.

Sources:
- SKILL.md — sentence <=30 words; Results past tense; Discussion hedging;
  hourglass; section responsibilities; AI traffic-light; no invention
- references/writing-strategy.md — claim/evidence/boundary; hourglass; overclaim
- references/section-moves.md — section move orders and required questions
- references/phrasebank-playbook.md — evidence strength / hedging families
- references/style-guardrails.md — contractions, British spelling, overclaim list
"""

from __future__ import annotations

# SKILL.md § Sentence rules
MAX_SENTENCE_WORDS = 30
TARGET_AVG_WORDS_MIN = 15
TARGET_AVG_WORDS_MAX = 25
MULTI_PROPOSITION_WARN_WORDS = 20  # SKILL: if >20 words, check multi-proposition

# Canonical section ids (SKILL.md / section-moves.md)
CANONICAL_SECTIONS = (
    "Abstract",
    "Introduction",
    "Methods",
    "Results",
    "Discussion",
    "Conclusion",
)

# Heading aliases for section detection
SECTION_ALIASES: dict[str, tuple[str, ...]] = {
    "Abstract": ("abstract", "summary"),
    "Introduction": ("introduction", "background"),
    "Methods": (
        "methods",
        "materials and methods",
        "materials & methods",
        "methodology",
        "experimental procedures",
        "experimental methods",
    ),
    "Results": ("results", "results and findings"),
    "Discussion": ("discussion",),
    "Conclusion": (
        "conclusion",
        "conclusions",
        "concluding remarks",
        "summary and conclusions",
    ),
}

# Results reporting verbs — past tense preferred (SKILL.md Results)
RESULTS_PAST_MARKERS = (
    "was",
    "were",
    "had",
    "showed",
    "showed that",
    "detected",
    "increased",
    "decreased",
    "reduced",
    "elevated",
    "observed",
    "found",
    "achieved",
    "enabled",
    "revealed",
    "identified",
    "measured",
    "calculated",
    "performed",
    "analysed",
    "analyzed",
    "compared",
    "demonstrated",
    "indicated",
    "remained",
    "occurred",
    "yielded",
    "produced",
    "exhibited",
    "presented",
    "reported",
)

# Present-tense reporting that often violates Results past-tense rule
RESULTS_PRESENT_MARKERS = (
    r"\bshows?\b",
    r"\bincreases?\b",
    r"\bdecreases?\b",
    r"\breveals?\b",
    r"\bindicates?\b",
    r"\bdemonstrates?\b",
    r"\bsuggests?\b",
    r"\bachieves?\b",
    r"\benables?\b",
    r"\bfinds?\b",
    r"\bobserves?\b",
    r"\bwe show\b",
    r"\bwe find\b",
    r"\bwe demonstrate\b",
    r"\bis significantly\b",
    r"\bare significantly\b",
)

# Discussion hedging (phrasebank-playbook.md Speculative / Moderate)
HEDGING_MARKERS = (
    "may",
    "might",
    "could",
    "suggest",
    "suggests",
    "suggested",
    "indicate",
    "indicates",
    "indicated",
    "appear",
    "appears",
    "seem",
    "seems",
    "likely",
    "possibly",
    "perhaps",
    "plausible",
    "consistent with",
    "support the view",
    "point to",
    "may reflect",
    "could arise",
    "might be explained",
    "should be interpreted with caution",
    "a possible explanation",
    "these findings suggest",
)

# Absolute / overclaim language (style-guardrails + SKILL overclaim)
ABSOLUTE_PATTERNS = (
    r"\bprove[sd]?\b",
    r"\bproves\b",
    r"\bconclusively\b",
    r"\bunprecedented\b",
    r"\bclearly (shows|demonstrates|proves)\b",
    r"\balways\b",
    r"\bnever\b",
    r"\bwithout (any )?doubt\b",
    r"\bit is certain\b",
    r"\bmust be\b",
    r"\bthe best\b",
    r"\bsuperior to\b",
    r"\bfirst (ever |to |study |report )\b",
)

# Overclaim soft replacements (style-guardrails.md) — Green/Yellow polish map
OVERCLAIM_REPLACEMENTS: list[tuple[str, str, str]] = [
    # (pattern, replacement, light)  light: green|yellow
    (r"\bprove[sd]?\b", "suggest", "yellow"),
    (r"\bproves\b", "suggests", "yellow"),
    (r"\bconclusively\b", "strongly", "yellow"),
    (r"\bunprecedented\b", "unusual", "yellow"),
    (r"\bclearly shows\b", "suggests", "yellow"),
    (r"\bclearly demonstrates\b", "indicates", "yellow"),
    (r"\bclearly proves\b", "suggests", "yellow"),
    (r"\bthe best\b", "among the strongest", "yellow"),
    (r"\bsuperior to\b", "favourable relative to", "yellow"),
]

# Informal / spoken register (style-guardrails.md Academic style & register)
INFORMAL_PATTERNS: list[tuple[str, str]] = [
    (r"\ba lot of\b", "substantial"),
    (r"\blots of\b", "many"),
    (r"\breally\b", ""),
    (r"\bbasically\b", ""),
    (r"\bactually\b", ""),
    (r"\bpretty\b", "relatively"),
    (r"\bkind of\b", "somewhat"),
    (r"\bsort of\b", "somewhat"),
    (r"\bhuge\b", "substantial"),
    (r"\btiny\b", "small"),
    (r"\bnice\b", "useful"),
    (r"\bstuff\b", "material"),
    (r"\bin order to\b", "to"),
    (r"\bdue to the fact that\b", "because"),
    (r"\bit is important to note that\b", ""),
    (r"\bit should be noted that\b", ""),
    (r"\bas a matter of fact\b", ""),
]

# Contractions (style-guardrails.md: avoid contractions)
CONTRACTIONS: dict[str, str] = {
    "don't": "do not",
    "doesn't": "does not",
    "didn't": "did not",
    "can't": "cannot",
    "couldn't": "could not",
    "won't": "will not",
    "wouldn't": "would not",
    "shouldn't": "should not",
    "isn't": "is not",
    "aren't": "are not",
    "wasn't": "was not",
    "weren't": "were not",
    "hasn't": "has not",
    "haven't": "have not",
    "hadn't": "had not",
    "it's": "it is",
    "that's": "that is",
    "there's": "there is",
    "we're": "we are",
    "they're": "they are",
    "we're": "we are",
    "we've": "we have",
    "they've": "they have",
    "i'm": "I am",
    "let's": "let us",
    "what's": "what is",
    "who's": "who is",
}

# British spelling (style-guardrails.md Nature-style default)
BRITISH_SPELLING: dict[str, str] = {
    "analyze": "analyse",
    "analyzes": "analyses",
    "analyzed": "analysed",
    "analyzing": "analysing",
    "behavior": "behaviour",
    "behaviors": "behaviours",
    "color": "colour",
    "colors": "colours",
    "colored": "coloured",
    "favor": "favour",
    "favors": "favours",
    "favored": "favoured",
    "favorable": "favourable",
    "fiber": "fibre",
    "fibers": "fibres",
    "harbor": "harbour",
    "labeled": "labelled",
    "labeling": "labelling",
    "modeling": "modelling",
    "modeled": "modelled",
    "neighbor": "neighbour",
    "neighbors": "neighbours",
    "optimize": "optimise",
    "optimized": "optimised",
    "optimizing": "optimising",
    "organization": "organisation",
    "organizations": "organisations",
    "recognize": "recognise",
    "recognized": "recognised",
    "recognizing": "recognising",
    "signalize": "signalise",
    "signaling": "signalling",
    "summarize": "summarise",
    "summarized": "summarised",
    "utilization": "utilisation",
    "utilize": "utilise",
    "utilized": "utilised",
    "generalizable": "generalisable",
    "generalizability": "generalisability",
    "program": "programme",  # academic sense; careful with computer "program"
}

# Vague Methods phrases to flag (SKILL.md Materials and Methods)
VAGUE_METHODS_PHRASES = (
    "under standard conditions",
    "using routine methods",
    "data were analyzed statistically",
    "data were analysed statistically",
    "differences were significant",
    "samples were randomly assigned",
    "the method was validated",
)

# Introduction gap / narrowing markers (hourglass + section-moves)
INTRO_GAP_MARKERS = (
    "however",
    "remains",
    "poorly understood",
    "little is known",
    "few studies",
    "gap",
    "unresolved",
    "unclear",
    "limited attention",
    "has not been",
    "have not been",
    "unknown",
    "controversy",
    "here, we",
    "in this study",
    "the present study",
    "we investigate",
    "we examine",
    "we aim",
)

# Discussion widen markers (hourglass)
DISCUSSION_WIDEN_MARKERS = (
    "implication",
    "implications",
    "limitation",
    "limitations",
    "caution",
    "broader",
    "field",
    "previous",
    "earlier",
    "consistent with",
    "in contrast",
    "further work",
    "future",
    "may reflect",
    "suggest",
)

# Conclusion three-part close markers (SKILL.md Conclusion)
CONCLUSION_MARKERS = (
    "contribute",
    "contribution",
    "indicate",
    "suggest",
    "implication",
    "limit",
    "further",
    "overall",
    "in summary",
    "taken together",
)

# AI traffic-light descriptions (SKILL.md)
TRAFFIC_LIGHT = {
    "green": "Green: grammar, clarity, concision, or tone only (author verification still advised).",
    "yellow": "Yellow: logic restructuring or claim-strength change; requires strong human control.",
    "red": "Red: inventing data, references, mechanisms, or core argument — forbidden.",
}

RULE_SOURCES = {
    "sentence_length": "SKILL.md § Sentence rules — every sentence <= 30 words",
    "results_tense": "SKILL.md § Results — stay mainly in past tense",
    "discussion_hedging": "SKILL.md § Discussion + phrasebank-playbook.md hedging families",
    "style_contractions": "style-guardrails.md § Academic style — avoid contractions",
    "style_overclaim": "style-guardrails.md § Overclaim checklist",
    "style_register": "style-guardrails.md § Academic register",
    "hourglass": "SKILL.md § Use the hourglass structure; writing-strategy.md",
    "section_moves": "section-moves.md — section questions and move order",
    "methods_vague": "SKILL.md § Materials and Methods — reject vague phrases",
    "integrity": "SKILL.md § AI traffic-light + style-guardrails.md Integrity rules",
    "british": "style-guardrails.md — British spelling for Nature-style prose",
    "core_argument": "SKILL.md § Protect the core argument — do not invent or rewrite core claims",
}
