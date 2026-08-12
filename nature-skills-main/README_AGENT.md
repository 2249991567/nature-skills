# Nature Paper Writing Assistant - 对话 Agent

**专属 Nature 顶刊写作智能对话助手**

完全依赖本地 Web 工具接口 (http://127.0.0.1:5000) 进行合规校验，不自行实现任何规则判断。

---

## 核心能力

### 1. 📝 论文大纲生成
输入课题/研究方向，自动生成 Nature 沙漏式完整论文大纲
- Abstract / Introduction / Methods / Results / Discussion / Conclusion 分章节细分写作要点
- 严格匹配 section-moves.md 章节职责规则
- 红绿灯写作提醒

### 2. 🔍 自动调用本地接口检测
用户粘贴中英文论文草稿，自动发起本地接口调用
- 获取三份标准报告：润色全文、修订说明、合规报告
- 提取统计数据：总问题数、平均句长、超长句数、最长句

### 3. 🟡 Yellow 高风险问题解析
解析报告中 Yellow 级高风险问题
- 章节缺失、过度宣称、时态错误、逻辑断层
- 分章节给出可直接复用的重写优化方案

### 4. ⏰ 分章节时态智能提醒
强制区分时态规则
- Results：过去式（showed, revealed, indicated）
- Discussion：缓和对冲 hedging 表述（may, could, suggest）
- 批量修正绝对化词汇清单

### 5. 📨 审稿返修辅助
提取合规报告内全部缺陷
- 生成符合 Nature 审稿回复规范的逐条回应段落
- 区分 Minor/Major Revision
- 附带规则溯源

---

## 快速启动

### 前置条件
确保本地检测服务已启动：

```bash
# 终端1：启动 Web 服务
cd c:\Users\Administrator\Desktop\nature-skills-main
python app.py
# 访问 http://127.0.0.1:5000 确认服务正常
```

### 启动 Agent

```bash
# 终端2：启动 Agent
python agent.py
```

---

## 使用示例

### 场景 1：生成论文大纲

```
请选择功能：1

请输入研究课题: Deep Learning for Cancer Diagnosis
请输入核心创新点: Multi-modal fusion of CT and MRI images using attention mechanism

[Agent 自动生成完整大纲]
✅ 大纲已保存到 nature_outline.md
```

### 场景 2：检测论文草稿

```
请选择功能：2

请粘贴论文草稿（输入 END 结束）：

# Abstract

Cancer diagnosis remains a challenging task in clinical practice...
[粘贴完整论文]
END

⏳ 正在调用本地接口检测...
✅ 检测完成！

📊 统计概览：
  - 总问题数: 15
  - 平均句长: 22.3 词
  - 超长句数: 3
  - 最长句: 42 词

🟡 Yellow 级高风险问题：
  类型: 句长超标
  描述: 发现 3 个超过30词的句子
  建议: 建议拆分长句，每句控制在15-25词为佳
  规则: nature-polishing SKILL.md - 句长规范

✅ 完整报告已保存到 agent_report.json
```

### 场景 3：查看时态规则

```
请选择功能：3

请选择章节：
1. Abstract
2. Introduction
3. Methods
4. Results
5. Discussion

请输入选项 (1-5): 4

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
...
```

### 场景 4：生成返修回复

```
请选择功能：4

请粘贴审稿人意见（输入 END 结束）：

Reviewer 1:
The manuscript is well-written but needs revision...
1. Some sentences are too long and difficult to follow.
2. The Results section uses inconsistent tenses.
...
END

[Agent 自动生成 Nature 风格回复]
✅ 回复已保存到 revision_response.md
```

---

## 硬性约束（Agent 设计原则）

### 1. ✅ 完全依赖本地接口
- Agent 自身**不实现**任何句长、拼写、时态、结构校验逻辑
- 所有合规检测请求全部转发 `http://127.0.0.1:5000/api/upload`
- 避免与 `nature_checker` 规则冲突

### 2. 📚 规则溯源标注
输出所有优化建议时，必须标注对应规则来源：
- `nature-polishing SKILL.md`
- `section-moves.md`
- `style-guardrails.md`
- `phrasebank-playbook.md`

### 3. 🚦 红绿灯等级输出
- **Green**：仅格式/拼写短句优化，直接给出修改句
- **Yellow**：逻辑、论断强度调整，提供2版改写方案并标注风险
- **Red**：核心论点、数据、引用禁止改动，仅提示人工完善

### 4. 📏 严格遵循 Nature 写作约束
- 单句≤30词
- 英式拼写 → 美式拼写
- 沙漏结构（宽 → 窄 → 宽）
- 禁止 prove / the best / must 等夸大表述

### 5. 🚫 伦理红线
- 不编造实验数据、参考文献、机制解释
- 所有修改仅基于用户原文 + 本地工具检测结果

---

## 文件说明

```
nature-skills-main/
├── agent.py                    # 主程序入口
├── agent_outline.py            # 大纲生成模块
├── agent_tense.py              # 时态提醒模块
├── agent_revision.py           # 返修辅助模块
├── agent_report.json           # 最近一次检测报告（自动生成）
├── nature_outline.md           # 生成的大纲（自动生成）
└── revision_response.md        # 生成的返修回复（自动生成）
```

---

## API 依赖

Agent 依赖以下本地 Web 接口：

| 端点 | 用途 |
|------|------|
| `GET /api/health` | 检查服务状态 |
| `POST /api/upload` | 上传论文进行检测 |

**重要**：Agent 不会修改 `app.py`、`nature_checker` 或前端代码，完全复用现有校验引擎。

---

## 常见问题

### Q: Agent 会自己判断语法错误吗？
A: **不会**。Agent 自身不实现任何规则，所有检测都调用本地 `http://127.0.0.1:5000/api/upload` 接口。

### Q: 如果本地服务未启动会怎样？
A: Agent 启动时会检查服务状态，如果未启动会提示：
```
⚠️  本地检测服务未启动！
请先运行: python app.py
服务地址: http://127.0.0.1:5000
```

### Q: Agent 生成的大纲是固定的吗？
A: 大纲框架固定（遵循 Nature 沙漏结构），但会根据用户输入的课题和创新点自动填充。

### Q: Yellow 级问题如何处理？
A: Agent 会提供2个改写方案（保守版 vs 积极版），并标注风险，由用户最终决定。

### Q: 可以离线使用吗？
A: 可以。Agent 仅调用本地接口 `127.0.0.1:5000`，不访问任何外网。

---

## 工作流程图

```
用户输入课题
    ↓
Agent 生成 Nature 大纲
    ↓
用户撰写初稿
    ↓
粘贴到 Agent
    ↓
Agent 调用本地接口 /api/upload
    ↓
获取三份报告（润色/修订/合规）
    ↓
Agent 解析 Yellow 问题
    ↓
生成优化方案（Green/Yellow/Red）
    ↓
用户修改论文
    ↓
审稿人返修意见
    ↓
Agent 生成 Nature 风格回复
    ↓
提交修改稿
```

---

## 技术栈

- **Python 3.8+**
- **requests** - HTTP 客户端（调用本地接口）
- **json** - 解析检测报告
- **tempfile** - 临时文件处理

---

## 致谢

本 Agent 完整依赖 **nature-polishing** 技能集（Yuan Yizhe, MIT License）的规则体系，通过本地 Web 接口复用 `nature_checker` 核心引擎。

规则来源：
- Nature 期刊作者指南
- 已发表 Nature 论文
- 学术写作课程（MIT OpenCourseWare）
- Academic Phrasebank（University of Manchester）

---

**当前版本**：v1.0.0

**启动命令**：`python agent.py`（确保 `python app.py` 已运行）

**本地服务**：http://127.0.0.1:5000
