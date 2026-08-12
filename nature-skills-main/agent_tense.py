"""
Agent 模块 - 分章节时态智能提醒
规则来源：nature-polishing section-moves.md
"""


def generate_tense_reminders(section: str) -> str:
    """分章节时态智能提醒"""
    tense_guide = {
        'Abstract': """
**Abstract 时态规则**
- 背景/重要性：现在时（is, are, remains）
- 本文工作：过去时（showed, revealed, demonstrated）
- 主要发现：过去时（indicated, suggested）
- 影响展望：现在时/情态动词（may, could）

**示例：**
✅ Correct: "Cancer therapy **remains** challenging. We **developed** a novel approach that **showed** efficacy."
❌ Wrong: "Cancer therapy **remained** challenging. We **develop** a novel approach that **shows** efficacy."

**规则来源：** nature-polishing section-moves.md
""",
        'Introduction': """
**Introduction 时态规则**
- Para 1-2（背景）：现在时（is, are, plays）
- Para 3（他人工作）：现在完成时/过去时（have shown, reported）
- Para 4（本文工作）：过去时（developed, investigated）
- Para 5（结果预告）：过去时（revealed, found）

**示例：**
✅ "Previous studies **have shown**... However, we **developed** a method that **revealed**..."
❌ "Previous studies **show**... However, we **develop** a method that **reveals**..."

**规则来源：** nature-polishing section-moves.md
""",
        'Methods': """
**Methods 时态规则**
- **全文强制过去时**（collected, performed, analyzed）
- 材料来源：过去时（were obtained from...）
- 实验步骤：过去时（were incubated, was measured）
- 统计分析：过去时（was performed using...）

**示例：**
✅ "Samples **were collected** and **were analyzed** using..."
❌ "Samples **are collected** and **are analyzed** using..."

**批量修正清单：**
- collect → collected
- perform → performed
- analyze → analyzed
- measure → measured
- incubate → incubated

**规则来源：** nature-polishing section-moves.md
""",
        'Results': """
**Results 时态规则**
- **全文强制过去时**（showed, revealed, indicated, demonstrated）
- 禁止解释（不用 because, suggesting）
- 仅报告观察结果

**示例：**
✅ "Treatment **increased** survival rate by 40% (Fig. 1a)."
❌ "Treatment **increases** survival rate, **suggesting** efficacy."

**批量修正清单：**
- show → showed
- reveal → revealed
- indicate → indicated
- demonstrate → demonstrated
- increase → increased
- decrease → decreased

**规则来源：** nature-polishing section-moves.md
""",
        'Discussion': """
**Discussion 时态规则**
- 结果回顾：过去时（showed, revealed）
- 机制解释：现在时 + hedging（may reflect, could indicate）
- 文献对比：现在完成时（have reported, has been shown）
- 影响展望：情态动词（may, could, might）

**强制 hedging 词汇：**
✅ suggest, indicate, may, could, might, likely, possibly
❌ prove, confirm, demonstrate, clearly, obviously

**示例：**
✅ "Our results **suggest** that the mechanism **may involve**..."
❌ "Our results **prove** that the mechanism **involves**..."

**规则来源：** nature-polishing section-moves.md, phrasebank-playbook.md
"""
    }
    
    return tense_guide.get(section, "请指定章节：Abstract / Introduction / Methods / Results / Discussion")
