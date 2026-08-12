# Compliance Check Report

Rules sourced exclusively from `nature-polishing/` (SKILL.md, writing-strategy.md, section-moves.md, phrasebank-playbook.md, style-guardrails.md).

## Summary statistics

- Total issues flagged: **17**
- Sentences overall: 30
- Mean words / sentence: 9.43 (target 15–25; hard max 30)
- Sentences > 30 words: 0
- Sections present: Abstract, Introduction, Methods, Results, Discussion, Conclusion
- Sections missing: none

### Issues by category

- `integrity`: 1
- `length`: 1
- `style`: 9
- `tense`: 6

## Sentence-length checks

- **[WARNING][GREEN]** ALL: Overall mean sentence length is 9.4 words (target 15–25).
  - Rule: SKILL.md § Sentence rules — every sentence <= 30 words
  - Suggestion: Shorten dense sentences; split overloaded clauses.

## Tense & hedging checks

- **[ERROR][YELLOW]** Results: Sentence 1 appears non-past for Results reporting.
  - Rule: SKILL.md § Results — stay mainly in past tense
  - Sentence: Figure 1 shows the main comparison across cohorts.
  - Suggestion: Rewrite in past tense (e.g. showed / increased / was detected).
- **[ERROR][YELLOW]** Results: Sentence 2 appears non-past for Results reporting.
  - Rule: SKILL.md § Results — stay mainly in past tense
  - Sentence: The proposed model achieves higher AUROC than baselines.
  - Suggestion: Rewrite in past tense (e.g. showed / increased / was detected).
- **[ERROR][YELLOW]** Results: Sentence 3 appears non-past for Results reporting.
  - Rule: SKILL.md § Results — stay mainly in past tense
  - Sentence: Accuracy increases from 0.71 to 0.84 on the held-out set.
  - Suggestion: Rewrite in past tense (e.g. showed / increased / was detected).
- **[ERROR][YELLOW]** Results: Sentence 4 appears non-past for Results reporting.
  - Rule: SKILL.md § Results — stay mainly in past tense
  - Sentence: We find that latency is significantly lower for the compact variant.
  - Suggestion: Rewrite in past tense (e.g. showed / increased / was detected).
- **[ERROR][YELLOW]** Discussion: Sentence 1 uses absolute / unhedged interpretive language.
  - Rule: SKILL.md § Discussion + phrasebank-playbook.md hedging families
  - Sentence: These results prove that multimodal fusion is necessary in all settings.
  - Suggestion: Use moderate/speculative phrasing: suggest / may reflect / could indicate (phrasebank-playbook.md).
- **[ERROR][YELLOW]** Discussion: Sentence 2 uses absolute / unhedged interpretive language.
  - Rule: SKILL.md § Discussion + phrasebank-playbook.md hedging families
  - Sentence: The method clearly demonstrates superiority and is unprecedented in this domain.
  - Suggestion: Use moderate/speculative phrasing: suggest / may reflect / could indicate (phrasebank-playbook.md).

## Style & register checks

- **[WARNING][GREEN]** Abstract: Contraction 'can't' found.
  - Rule: style-guardrails.md § Academic style — avoid contractions
  - Sentence: X remains challenging because a lot of prior work can't capture dynamic behaviour.
  - Suggestion: Expand contractions (style-guardrails.md).
- **[WARNING][GREEN]** Abstract: Informal / redundant phrasing matched /\ba lot of\b/.
  - Rule: style-guardrails.md § Academic register
  - Sentence: X remains challenging because a lot of prior work can't capture dynamic behaviour.
  - Suggestion: Prefer more precise academic wording (e.g. 'substantial').
- **[ERROR][YELLOW]** Abstract: Overclaim language matched /\bprove[sd]?\b/.
  - Rule: style-guardrails.md § Overclaim checklist
  - Sentence: We show that performance increases by 18% and proves the method is the best.
  - Suggestion: Soften: show / suggest / to our knowledge / among the strongest / in this cohort.
- **[ERROR][YELLOW]** Abstract: Overclaim language matched /\bproves\b/.
  - Rule: style-guardrails.md § Overclaim checklist
  - Sentence: We show that performance increases by 18% and proves the method is the best.
  - Suggestion: Soften: show / suggest / to our knowledge / among the strongest / in this cohort.
- **[ERROR][YELLOW]** Abstract: Overclaim language matched /\bthe best\b/.
  - Rule: style-guardrails.md § Overclaim checklist
  - Sentence: We show that performance increases by 18% and proves the method is the best.
  - Suggestion: Soften: show / suggest / to our knowledge / among the strongest / in this cohort.
- **[ERROR][YELLOW]** Methods: Vague Methods phrase: 'under standard conditions'.
  - Rule: SKILL.md § Materials and Methods — reject vague phrases
  - Suggestion: Replace with reproducible detail (parameters, controls, software versions).
- **[ERROR][YELLOW]** Discussion: Overclaim language matched /\bprove[sd]?\b/.
  - Rule: style-guardrails.md § Overclaim checklist
  - Sentence: These results prove that multimodal fusion is necessary in all settings.
  - Suggestion: Soften: show / suggest / to our knowledge / among the strongest / in this cohort.
- **[ERROR][YELLOW]** Discussion: Overclaim language matched /\bunprecedented\b/.
  - Rule: style-guardrails.md § Overclaim checklist
  - Sentence: The method clearly demonstrates superiority and is unprecedented in this domain.
  - Suggestion: Soften: show / suggest / to our knowledge / among the strongest / in this cohort.
- **[ERROR][YELLOW]** Discussion: Overclaim language matched /\bclearly (shows|demonstrates|proves)\b/.
  - Rule: style-guardrails.md § Overclaim checklist
  - Sentence: The method clearly demonstrates superiority and is unprecedented in this domain.
  - Suggestion: Soften: show / suggest / to our knowledge / among the strongest / in this cohort.

## Hourglass & section-structure checks

- No issues in this category.

## Integrity / risk reminders

- **[INFO][RED]** ALL: Red-line reminder: do not invent references, data, mechanisms, or rewrite the paper's core scientific argument.
  - Rule: SKILL.md § AI traffic-light + style-guardrails.md Integrity rules
  - Suggestion: AI may polish wording only; authors own the core argument.

## Risk summary

- **Green** items are mechanical language fixes; still verify terminology.
- **Yellow** items change claim strength or section logic; require author review.
- **Red** items mark forbidden AI actions (fabrication / core-argument authorship).
