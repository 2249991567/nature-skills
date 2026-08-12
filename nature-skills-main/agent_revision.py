"""
Agent 模块 - 审稿返修辅助
结合本地接口合规报告，生成 Nature 风格逐条回应
"""


def generate_revision_response(agent, reviewer_comments: str) -> str:
    """生成审稿返修回复"""
    if not agent.last_report:
        return "请先上传论文进行检测，以便生成针对性的返修回复。"
    
    response = f"""
# Response to Reviewers

Dear Editors and Reviewers,

We thank the reviewers for their constructive comments. We have carefully addressed all concerns and revised the manuscript accordingly. Below are our point-by-point responses.

---

## 审稿人意见
{reviewer_comments}

---

## 逐条回复（基于本地合规检测）

### Major Revision Issues

**1. 句长与可读性问题**
- **Reviewer concern**: [从审稿意见提取]
- **Our response**: We have revised all sentences exceeding 30 words (total: {agent.last_report['stats']['sentences_over_30']}) to improve readability. The mean sentence length has been reduced to {agent.last_report['stats']['mean_words_per_sentence']} words.
- **Changes made**: See revised manuscript, lines XX-XX.
- **Rule reference**: nature-polishing SKILL.md - Sentence length standards

**2. 时态规范问题**
- **Reviewer concern**: Inconsistent tenses in Results section
- **Our response**: We have systematically corrected all tense issues. Results section now uses past tense throughout, and Discussion section employs appropriate hedging language.
- **Changes made**: See revised Results (lines XX-XX) and Discussion (lines XX-XX).
- **Rule reference**: nature-polishing section-moves.md

**3. 过度宣称问题**
- **Reviewer concern**: Claims too strong without sufficient evidence
- **Our response**: We have moderated all absolute statements and replaced them with hedging expressions (suggest, may, could). We have also removed phrases like "clearly" and "obviously."
- **Changes made**: See revised Abstract and Discussion.
- **Rule reference**: nature-polishing style-guardrails.md

### Minor Revision Issues

**4. 格式与拼写**
- **Our response**: We have corrected all formatting inconsistencies and spelling errors identified by the compliance check.
- **Total corrections**: {agent.last_report['stats']['total_issues']} issues fixed.

---

## 修改文件
- Revised manuscript (clean version)
- Revised manuscript (tracked changes)
- Compliance report from Nature-polishing checker

We believe these revisions have significantly strengthened the manuscript and addressed all reviewer concerns. We hope the manuscript is now suitable for publication in Nature.

Sincerely,
[Author Name]

---

**规则来源：** 本回复基于 nature-polishing 完整规则集生成
"""
    return response
