# Nature Paper Checker - Web Interface

基于 Nature 期刊规范的学术论文检查与润色工具（Web 版）

完整复用 `nature_checker` 现有 CLI 逻辑，提供友好的 Web 界面。

---

## 快速启动

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 启动服务

```bash
python app.py
```

### 3. 访问界面

浏览器打开：**http://127.0.0.1:5000**

API 文档：**http://127.0.0.1:5000/docs**

---

## 功能特性

### ✅ 文件上传
- 支持 `.md` / `.docx` / `.txt` 格式
- 拖拽或点击上传，文件大小上限 10MB
- 自动格式与大小校验

### 📊 实时检查
- 句长统计（标注超过 30 词的句子）
- 时态校验（Results 过去时、Discussion hedging）
- 风格检查（口语、冗余、绝对化表述）
- 结构校验（沙漏结构与章节职责）

### ✨ 规范润色
- 按 Nature 标准优化全文
- 所有修改用下划线标注
- 红绿灯等级（Green/Yellow/Red）

### 📥 结果下载
- 润色后全文
- 修订说明（分章节 3-5 条）
- 合规性报告
- 一键下载 zip

---

## 技术架构

- **后端**：FastAPI + uvicorn（轻量级）
- **核心**：`nature_checker` 规则引擎（完全复用现有代码）
- **前端**：Vue 3 + Axios + Marked（无构建步骤）
- **隔离**：每个上传会话独立临时目录

---

## 目录结构

```
nature-skills-main/
├── app.py                         # FastAPI 后端入口
├── requirements.txt               # Python 依赖
├── README_WEB.md                  # 本文档
├── nature_checker/                # 核心检查引擎（原有CLI逻辑）
│   ├── __init__.py
│   ├── pipeline.py                # 端到端流水线
│   ├── checkers.py                # 四类规则检查
│   ├── polish.py                  # 规则润色 + 红绿灯
│   ├── report.py                  # Markdown 输出
│   └── ...
├── static/                        # 前端静态文件
│   ├── index.html                 # 主页面
│   ├── style.css                  # 样式
│   └── app.js                     # Vue 逻辑
└── temp/                          # 临时文件（自动创建）
    └── {session_id}/              # 每个上传会话独立目录
        ├── uploaded_file.*
        ├── result.md
        ├── result_revision_notes.md
        └── result_compliance_report.md
```

---

## API 端点

### `POST /api/upload`
上传并处理论文文件

**参数**：
- `file`：论文文件（.md / .docx / .txt）

**返回**：
```json
{
  "success": true,
  "session_id": "20260805_123456_789012",
  "filename": "my_paper.md",
  "stats": {
    "total_issues": 12,
    "mean_words_per_sentence": 18.5,
    "sentences_over_30": 3,
    "max_sentence_length": 42
  },
  "results": {
    "polished": "# Abstract\n\n...",
    "revision_notes": "## Revision Notes\n\n...",
    "compliance_report": "## Compliance Report\n\n..."
  }
}
```

### `GET /api/download/{session_id}`
下载结果文件 zip 包

**返回**：`results_{session_id}.zip`

### `DELETE /api/cleanup`
清理超过 24 小时的临时文件

**参数**：
- `max_age_hours`（可选，默认 24）

### `GET /api/health`
健康检查

---

## 强制规则（100% 溯源自 nature-polishing）

### 1. 句长规范
- 单句 ≤ 30 词
- 平均词长 15-25 词
- 超过 30 词的句子会被标注并建议拆分

### 2. 时态规范
- **Results**：统一使用过去时报告实验结果
- **Discussion**：使用谨慎的 hedging 语气（may, suggest, likely）

### 3. 风格约束
- 禁止口语化（a lot of → substantial）
- 禁止缩写（can't → cannot）
- 英式拼写统一为美式（behaviour → behavior）
- 避免过度宣称（clearly, obviously, undoubtedly）

### 4. 结构校验
- **沙漏结构**：宽（背景）→ 窄（核心问题）→ 宽（影响）
- 各章节职责：
  - Abstract：独立完整的论文缩影
  - Introduction：背景 → 问题 → 方法概述
  - Methods：可复现的实验细节
  - Results：过去时报告，无解释
  - Discussion：解释 + 限制 + 影响

### 5. 伦理红线
- ❌ 绝不编造引用、数据、实验结论
- ❌ 绝不改写核心论点（仅优化表述）
- ✅ 所有修改标注 AI 红绿灯等级

---

## 使用示例

### 场景 1：上传 Markdown 文件

1. 访问 http://127.0.0.1:5000
2. 点击上传区域，选择 `my_paper.md`
3. 点击「Check Paper」按钮
4. 查看 3 个标签页：
   - ✨ 润色后全文（修改处有下划线）
   - 📝 修订说明（分章节列出核心修改）
   - 📊 合规报告（句长/时态/风格问题清单）
5. 点击「Download All Results」下载 zip

### 场景 2：命令行 API 调用

```bash
# 上传文件
curl -X POST "http://127.0.0.1:5000/api/upload" \
  -F "file=@my_paper.docx"

# 下载结果（替换 session_id）
curl -X GET "http://127.0.0.1:5000/api/download/20260805_123456" \
  -o results.zip
```

### 场景 3：Python 脚本调用

```python
import requests

# 上传文件
with open("my_paper.md", "rb") as f:
    response = requests.post(
        "http://127.0.0.1:5000/api/upload",
        files={"file": f}
    )
    result = response.json()
    print(f"Issues: {result['stats']['total_issues']}")
    print(f"Session ID: {result['session_id']}")

# 下载结果
session_id = result['session_id']
response = requests.get(f"http://127.0.0.1:5000/api/download/{session_id}")
with open("results.zip", "wb") as f:
    f.write(response.content)
```

---

## 常见问题

### Q: 支持哪些文件格式？
A: `.md`（Markdown）、`.docx`（Word）、`.txt`（纯文本）

### Q: 文件大小限制？
A: 单个文件最大 10MB

### Q: 临时文件会自动清理吗？
A: 是的，调用 `/api/cleanup` 端点可清理超过 24 小时的文件

### Q: 可以在服务器上部署吗？
A: 可以，修改 `app.py` 最后一行：
```python
uvicorn.run(app, host="0.0.0.0", port=5000)
```

### Q: 如何关闭服务？
A: 在终端按 `Ctrl+C`

### Q: 润色结果准确吗？
A: 工具基于规则引擎（非 LLM），适合合规检查与确定性改写。复杂逻辑重组会标为 **Yellow** 供人工把关。

---

## 开发与扩展

### 添加新的检查规则
编辑 `nature_checker/checkers.py`，在 `run_all_checks()` 中添加新检查函数。

### 自定义润色规则
编辑 `nature_checker/polish.py`，在 `REPLACEMENTS` 字典中添加新的替换规则。

### 修改前端样式
编辑 `static/style.css`，所有颜色、字体、布局可自定义。

### 集成到现有项目
```python
from nature_checker.pipeline import polish_text

text = "Your paper content..."
paper, report, polished = polish_text(text)

print(f"Issues: {len(report.issues)}")
print(f"Polished: {polished.polished_sections['Abstract']}")
```

---

## 致谢

本工具完整实现了 **nature-polishing** 技能集（Yuan Yizhe, MIT License）。

规则来源：
- Nature 期刊作者指南
- 已发表 Nature 论文
- 学术写作课程（MIT OpenCourseWare）
- Academic Phrasebank（University of Manchester）

---

## 许可证

本项目继承原技能集的 MIT License。

---

**当前版本**：v1.0.0（Web 界面）

**启动命令**：`python app.py`

**访问地址**：http://127.0.0.1:5000
