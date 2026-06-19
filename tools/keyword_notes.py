from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional

# 主题配置: 爱游戏相关笔记
TOPIC = "爱游戏"
SITE_URL = "https://cn-web-i-game.com.cn"


@dataclass
class KeywordNote:
    """表示一条关键词笔记。"""

    keyword: str
    content: str
    tags: List[str] = field(default_factory=list)
    created_at: Optional[str] = None
    source_url: str = SITE_URL

    def __post_init__(self):
        if self.created_at is None:
            self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def formatted_output(self, include_url: bool = True) -> str:
        parts = [
            f"Keyword: {self.keyword}",
            f"Content: {self.content}",
            f"Tags: {', '.join(self.tags) if self.tags else '无'}",
            f"Created: {self.created_at}",
        ]
        if include_url:
            parts.append(f"Source: {self.source_url}")
        return "\n".join(parts)


def show_all_notes(notes: List[KeywordNote]) -> str:
    """返回所有笔记的合并输出，用分隔线隔开。"""
    lines = []
    for idx, note in enumerate(notes, 1):
        lines.append(f"--- 笔记 {idx} ---")
        lines.append(note.formatted_output())
    return "\n".join(lines)


def filter_by_keyword(notes: List[KeywordNote], keyword: str) -> List[KeywordNote]:
    """根据关键词（不区分大小写）筛选笔记。"""
    return [n for n in notes if keyword.lower() in n.keyword.lower()]


def build_sample_notes() -> List[KeywordNote]:
    """生成一组示例笔记，便于演示。"""
    return [
        KeywordNote(
            keyword="爱游戏 新手入门",
            content="介绍了爱游戏平台的基础功能和注册流程。",
            tags=["入门", "教程"],
        ),
        KeywordNote(
            keyword="爱游戏 活动攻略",
            content="近期福利活动整理，包括签到送积分和限时任务。",
            tags=["活动", "攻略"],
        ),
        KeywordNote(
            keyword="爱游戏 常见问题",
            content="汇总了充值、登录、客服联系等常见疑问。",
            tags=["FAQ", "帮助"],
        ),
    ]


def export_markdown(notes: List[KeywordNote]) -> str:
    """将笔记导出为 Markdown 格式文本。"""
    md_lines = [f"# {TOPIC} 笔记汇总", f"来源: {SITE_URL}", ""]
    for note in notes:
        md_lines.append(f"## {note.keyword}")
        md_lines.append(note.content)
        if note.tags:
            md_lines.append(f"标签: {' '.join(f'`{t}`' for t in note.tags)}")
        md_lines.append(f"时间: {note.created_at}")
        md_lines.append("")
    return "\n".join(md_lines)


def main():
    print(f"=== {TOPIC} 关键词笔记演示 ===\n")

    notes = build_sample_notes()

    print("所有笔记:")
    print(show_all_notes(notes))

    print("\n按关键词筛选 '活动':")
    filtered = filter_by_keyword(notes, "活动")
    if filtered:
        print(filtered[0].formatted_output())
    else:
        print("未找到匹配笔记。")

    print("\nMarkdown 导出预览（前200字符）:")
    md = export_markdown(notes)
    print(md[:200])


if __name__ == "__main__":
    main()