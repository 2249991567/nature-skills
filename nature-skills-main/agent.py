"""
Nature Paper Writing Assistant - 对话 Agent
==========================================
专属 Nature 顶刊写作智能对话助手

完全依赖本地 Web 工具接口 (http://127.0.0.1:5000) 进行合规校验，
不自行实现任何规则判断，避免与 nature_checker 冲突。

核心能力：
1. 论文大纲生成（Nature 沙漏结构）
2. 自动调用本地接口检测论文
3. Yellow 高风险问题解析与改写方案
4. 分章节时态智能提醒
5. 审稿返修辅助

Usage:
    python agent.py
"""

import requests
import json
from pathlib import Path
from typing import Dict, List, Optional
import tempfile


class NaturePaperAgent:
    """Nature 论文写作对话 Agent"""
    
    def __init__(self, api_base_url: str = "http://127.0.0.1:5000"):
        self.api_base_url = api_base_url
        self.session_id = None
        self.last_report = None
        
    def check_api_health(self) -> bool:
        """检查本地 API 是否可用"""
        try:
            response = requests.get(f"{self.api_base_url}/api/health", timeout=2)
            return response.status_code == 200
        except Exception:
            return False
    
    def analyze_paper(self, text: str) -> Dict:
        """
        调用本地接口分析论文
        
        核心约束：Agent 自身不实现任何句长、拼写、时态、结构校验逻辑，
        所有合规检测请求全部转发本地接口。
        """
        if not self.check_api_health():
            raise RuntimeError("本地检测服务未启动，请先运行: python app.py")
        
        # 创建临时文件
        with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False, encoding='utf-8') as f:
            f.write(text)
            temp_path = f.name
        
        try:
            # 调用本地 /api/upload 接口
            with open(temp_path, 'rb') as f:
                files = {'file': ('paper.md', f, 'text/markdown')}
                response = requests.post(
                    f"{self.api_base_url}/api/upload",
                    files=files,
                    timeout=60
                )
            
            if response.status_code != 200:
                raise RuntimeError(f"接口调用失败: {response.text}")
            
            result = response.json()
            self.session_id = result['session_id']
            self.last_report = result
            return result
            
        finally:
            Path(temp_path).unlink(missing_ok=True)
    
    def parse_yellow_issues(self) -> List[Dict]:
        """解析 Yellow 级高风险问题"""
        if not self.last_report:
            return []
        
        yellow_issues = []
        stats = self.last_report['stats']
        
        if stats['sentences_over_30'] > 0:
            yellow_issues.append({
                'type': '句长超标',
                'severity': 'Yellow',
                'count': stats['sentences_over_30'],
                'description': f'发现 {stats["sentences_over_30"]} 个超过30词的句子',
                'suggestion': '建议拆分长句，每句控制在15-25词为佳',
                'rule_source': 'nature-polishing SKILL.md - 句长规范'
            })
        
        return yellow_issues


# 导入其他模块
from agent_outline import generate_outline
from agent_tense import generate_tense_reminders
from agent_revision import generate_revision_response


def main():
    """命令行交互界面"""
    agent = NaturePaperAgent()
    
    print("=" * 60)
    print("Nature Paper Writing Assistant - 对话 Agent")
    print("=" * 60)
    print("\n核心能力：")
    print("1. 生成 Nature 沙漏式论文大纲")
    print("2. 自动调用本地接口检测论文")
    print("3. Yellow 高风险问题解析")
    print("4. 分章节时态智能提醒")
    print("5. 审稿返修辅助")
    print("\n" + "=" * 60)
    
    if not agent.check_api_health():
        print("\n⚠️  本地检测服务未启动！")
        print("请先运行: python app.py")
        print("服务地址: http://127.0.0.1:5000")
        return
    
    print("\n✅ 本地检测服务已就绪")
    
    while True:
        print("\n\n请选择功能：")
        print("1. 生成论文大纲")
        print("2. 检测论文草稿")
        print("3. 查看时态规则")
        print("4. 生成返修回复")
        print("0. 退出")
        
        choice = input("\n请输入选项 (0-4): ").strip()
        
        if choice == '0':
            break
        elif choice == '1':
            topic = input("\n请输入研究课题: ").strip()
            innovation = input("请输入核心创新点: ").strip()
            outline = generate_outline(topic, innovation)
            print("\n" + outline)
            
            with open('nature_outline.md', 'w', encoding='utf-8') as f:
                f.write(outline)
            print("\n✅ 大纲已保存到 nature_outline.md")
            
        elif choice == '2':
            print("\n请粘贴论文草稿（输入 END 结束）：")
            lines = []
            while True:
                line = input()
                if line.strip() == 'END':
                    break
                lines.append(line)
            
            text = '\n'.join(lines)
            
            if text.strip():
                print("\n⏳ 正在调用本地接口检测...")
                try:
                    report = agent.analyze_paper(text)
                    print("\n✅ 检测完成！")
                    print(f"\n📊 统计概览：")
                    print(f"  - 总问题数: {report['stats']['total_issues']}")
                    print(f"  - 平均句长: {report['stats']['mean_words_per_sentence']} 词")
                    print(f"  - 超长句数: {report['stats']['sentences_over_30']}")
                    print(f"  - 最长句: {report['stats']['max_sentence_length']} 词")
                    
                    with open('agent_report.json', 'w', encoding='utf-8') as f:
                        json.dump(report, f, indent=2, ensure_ascii=False)
                    print("\n✅ 完整报告已保存到 agent_report.json")
                    
                    yellow_issues = agent.parse_yellow_issues()
                    if yellow_issues:
                        print("\n🟡 Yellow 级高风险问题：")
                        for issue in yellow_issues:
                            print(f"\n  类型: {issue['type']}")
                            print(f"  描述: {issue['description']}")
                            print(f"  建议: {issue['suggestion']}")
                            print(f"  规则: {issue['rule_source']}")
                    
                except Exception as e:
                    print(f"\n❌ 检测失败: {str(e)}")
            
        elif choice == '3':
            sections = {
                '1': 'Abstract', '2': 'Introduction', '3': 'Methods',
                '4': 'Results', '5': 'Discussion'
            }
            print("\n请选择章节：")
            for k, v in sections.items():
                print(f"{k}. {v}")
            
            section_choice = input("\n请输入选项 (1-5): ").strip()
            if section_choice in sections:
                reminders = generate_tense_reminders(sections[section_choice])
                print("\n" + reminders)
        
        elif choice == '4':
            print("\n请粘贴审稿人意见（输入 END 结束）：")
            lines = []
            while True:
                line = input()
                if line.strip() == 'END':
                    break
                lines.append(line)
            
            comments = '\n'.join(lines)
            if comments.strip():
                response = generate_revision_response(agent, comments)
                print("\n" + response)
                
                with open('revision_response.md', 'w', encoding='utf-8') as f:
                    f.write(response)
                print("\n✅ 回复已保存到 revision_response.md")


if __name__ == "__main__":
    main()
