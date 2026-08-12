"""Issue data structures for compliance checks."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class Issue:
    category: str  # length | tense | style | structure | integrity
    severity: str  # info | warning | error
    section: str
    message: str
    rule_source: str
    sentence: str = ""
    suggestion: str = ""
    traffic_light: str = "green"  # green | yellow | red
    meta: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return {
            "category": self.category,
            "severity": self.severity,
            "section": self.section,
            "message": self.message,
            "rule_source": self.rule_source,
            "sentence": self.sentence,
            "suggestion": self.suggestion,
            "traffic_light": self.traffic_light,
            "meta": self.meta,
        }


@dataclass
class CheckReport:
    issues: list[Issue] = field(default_factory=list)
    stats: dict[str, Any] = field(default_factory=dict)

    def add(self, issue: Issue) -> None:
        self.issues.append(issue)

    def by_category(self, category: str) -> list[Issue]:
        return [i for i in self.issues if i.category == category]

    def extend(self, other: "CheckReport") -> None:
        self.issues.extend(other.issues)
        self.stats.update(other.stats)
