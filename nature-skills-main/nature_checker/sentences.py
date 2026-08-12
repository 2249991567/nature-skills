"""Sentence utilities for length and tense checks."""

from __future__ import annotations

import re
from dataclasses import dataclass


# Protect common abbreviations / decimals during split
_ABBREV = (
    "e.g.",
    "i.e.",
    "et al.",
    "Fig.",
    "Figs.",
    "Eq.",
    "Dr.",
    "Prof.",
    "vs.",
    "cf.",
    "approx.",
    "No.",
    "Vol.",
    "pp.",
)


@dataclass
class Sentence:
    text: str
    index: int  # 1-based within section
    word_count: int


def word_count(text: str) -> int:
    tokens = re.findall(r"[A-Za-z0-9]+(?:['-][A-Za-z0-9]+)?", text)
    return len(tokens)


def split_sentences(text: str) -> list[str]:
    """Split prose into sentences with light abbreviation protection."""
    if not text or not text.strip():
        return []
    protected = text
    placeholders: dict[str, str] = {}
    for i, abbr in enumerate(_ABBREV):
        key = f"__ABBR{i}__"
        placeholders[key] = abbr
        protected = protected.replace(abbr, key)
        protected = protected.replace(abbr.upper(), key)
        protected = protected.replace(abbr.capitalize(), key)

    # Protect decimal numbers: 3.14
    def _dec(m: re.Match[str]) -> str:
        key = f"__DEC{len(placeholders)}__"
        placeholders[key] = m.group(0)
        return key

    protected = re.sub(r"\d+\.\d+", _dec, protected)

    parts = re.split(r"(?<=[.!?])\s+(?=[A-Z\"'(\[])", protected.strip())
    sentences: list[str] = []
    for part in parts:
        s = part.strip()
        if not s:
            continue
        for key, val in placeholders.items():
            s = s.replace(key, val)
        sentences.append(s)
    return sentences


def annotate_sentences(text: str) -> list[Sentence]:
    out: list[Sentence] = []
    for i, s in enumerate(split_sentences(text), start=1):
        out.append(Sentence(text=s, index=i, word_count=word_count(s)))
    return out


def mean_word_count(sentences: list[Sentence]) -> float:
    if not sentences:
        return 0.0
    return sum(s.word_count for s in sentences) / len(sentences)
