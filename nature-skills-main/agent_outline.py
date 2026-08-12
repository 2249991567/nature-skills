"""
Agent 模块 - 论文大纲生成
生成 Nature 沙漏式论文大纲，严格匹配 section-moves.md 章节职责规则
"""


def generate_outline(topic: str, innovation: str) -> str:
    """生成 Nature 沙漏式论文大纲"""
    outline = f"""
# Nature 论文大纲 - {topic}

## 核心创新点
{innovation}

---

## Abstract（独立完整的论文缩影）
### 写作目标
- 1句话背景（广泛问题）
- 1句话知识gap（现有研究局限）
- 1句话本文方法（核心创新）
- 2-3句话主要发现（定量结果）
- 1句话影响（broader impact）

### 避坑要点
- 单句≤30词
- 禁止 prove / demonstrate conclusively
- 用过去时报告结果
- 无引用、无缩写

---

## Introduction（沙漏结构：宽→窄→宽）
### 段落架构
**Para 1-2: 背景铺垫（宽）**
- 领域重要性（为什么重要？）
- 现有研究综述（他人做了什么？）

**Para 3: 知识gap（窄）**
- 现有方法的不足
- 待解决的核心问题

**Para 4: 本文方法（窄）**
- 我们的创新策略
- 技术路线概述

**Para 5: 主要发现与贡献（宽）**
- 关键结果预告
- 潜在影响

### 避坑要点
- 避免 "The best" / "For the first time"
- 多用 hedging: may, could, suggest
- 时态：背景现在时，他人工作过去时，本文工作过去时

---

## Methods（可复现的实验细节）
### 必备内容
- 材料来源（供应商、批号）
- 实验步骤（时间、温度、浓度）
- 数据分析流程（统计方法、软件版本）
- 伦理批准声明

### 避坑要点
- 全文过去时
- 禁止解释why（留给Discussion）
- 子标题分类清晰
- 可让他人复现

---

## Results（过去时报告，无解释）
### 段落逻辑
- 按实验逻辑顺序组织（不按图序）
- 每段对应一个科学问题
- 先综述发现，再引用图表

### 避坑要点
- **强制过去时**：showed / revealed / indicated
- 禁止解释机制（留给Discussion）
- 禁止 clearly / obviously
- 数据准确，误差范围标注

---

## Discussion（解释 + 限制 + 影响）
### 段落架构
**Para 1: 主要发现回顾**
- 重述核心结果

**Para 2-3: 机制解释**
- 与现有理论对比
- 可能的生物学/物理学机制

**Para 4: 局限性**
- 方法限制（样本量、技术局限）
- 结果适用范围

**Para 5: 未来方向与影响**
- 后续研究建议
- 临床/工业应用前景

### 避坑要点
- **强制 hedging**：may reflect / could indicate / suggest
- 避免 prove / confirm
- 承认局限性（显示科学诚实）
- 时态：现在时讨论意义

---

## Conclusion（简短总结）
### 写作目标
- 1-2段，重述核心发现
- 强调broader impact
- 展望未来

### 避坑要点
- 禁止引入新信息
- 避免过度宣称
- 简洁有力

---

## 红绿灯写作提醒
### 🟢 Green（安全表达）
- report, show, observe, find（过去时）
- suggest, indicate, may, could（hedging）
- consistent with, in line with

### 🟡 Yellow（需谨慎）
- significant, important（需数据支撑）
- novel, first（需文献验证）
- strong, clear（需客观证据）

### 🔴 Red（禁用）
- prove, demonstrate conclusively
- the best, optimal, perfect
- obviously, clearly, undoubtedly
- always, never, must

---

**下一步**：按此大纲逐章节撰写初稿，完成后粘贴全文，我将调用本地接口检测并给出优化方案。
"""
    return outline
