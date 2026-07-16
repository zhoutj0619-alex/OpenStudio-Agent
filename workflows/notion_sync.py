"""
Notion Sync — 将 Agent 输出自动同步至 Notion 内容日历

用法:
    python notion_sync.py --agent researcher  # 同步选题日报到 Notion
    python notion_sync.py --agent writer      # 同步脚本卡片到 Notion
    python notion_sync.py --agent distributor # 同步分发方案到 Notion

前置条件:
    1. 复制 .env.example 为 .env 并填入 NOTION_TOKEN 和 NOTION_CONTENT_DB_ID
    2. 在 Notion 中创建集成: https://www.notion.so/my-integrations
    3. 将集成添加到你的内容日历数据库
"""

import os
import json
import argparse
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

# ============================================================
# 配置
# ============================================================

# 尝试加载 .env 文件
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    print("⚠️  未安装 python-dotenv，将直接读取系统环境变量")
    print("   安装: pip install python-dotenv")

NOTION_TOKEN = os.getenv("NOTION_TOKEN")
NOTION_CONTENT_DB_ID = os.getenv("NOTION_CONTENT_DB_ID")

# ============================================================
# Notion API 客户端 (最小化实现，无需外部依赖)
# ============================================================

import urllib.request
import urllib.error

NOTION_API_BASE = "https://api.notion.com/v1"
NOTION_VERSION = "2022-06-28"


def notion_request(
    method: str,
    endpoint: str,
    body: dict | None = None,
) -> dict:
    """发送 Notion API 请求"""
    url = f"{NOTION_API_BASE}{endpoint}"
    headers = {
        "Authorization": f"Bearer {NOTION_TOKEN}",
        "Notion-Version": NOTION_VERSION,
        "Content-Type": "application/json",
    }

    data = json.dumps(body).encode("utf-8") if body else None
    req = urllib.request.Request(url, data=data, headers=headers, method=method)

    try:
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        error_body = e.read().decode("utf-8")
        print(f"❌ Notion API 错误 [{e.code}]: {error_body}")
        sys.exit(1)


def append_to_database(properties: dict) -> dict:
    """向 Notion 数据库添加一行"""
    return notion_request("POST", "/pages", body={
        "parent": {"database_id": NOTION_CONTENT_DB_ID},
        "properties": properties,
    })


# ============================================================
# 数据适配器 — 将 Agent 输出转换为 Notion 数据库属性
# ============================================================

def sync_research_report(report_data: dict) -> dict:
    """同步选题日报到 Notion"""
    properties = {
        "标题": {
            "title": [{"text": {"content": report_data.get("title", "无标题选题")}}],
        },
        "类型": {
            "select": {"name": "选题"},
        },
        "阶段": {
            "select": {"name": report_data.get("stage", "待评估")},
        },
        "热度": {
            "number": report_data.get("heat_score", 0),
        },
        "来源": {
            "rich_text": [{"text": {"content": report_data.get("source", "AI 生成")}}],
        },
        "核心角度": {
            "rich_text": [{"text": {"content": report_data.get("core_angle", "")}}],
        },
        "创建日期": {
            "date": {"start": datetime.now(timezone.utc).isoformat()},
        },
    }

    if report_data.get("priority") == "high":
        properties["优先级"] = {"select": {"name": "🔴 高"}}

    return append_to_database(properties)


def sync_script_card(script_data: dict) -> dict:
    """同步脚本卡片到 Notion"""
    properties = {
        "标题": {
            "title": [{"text": {"content": script_data.get("title", "无标题脚本")}}],
        },
        "类型": {
            "select": {"name": "脚本"},
        },
        "阶段": {
            "select": {"name": script_data.get("status", "待拍摄")},
        },
        "平台": {
            "multi_select": [
                {"name": p} for p in script_data.get("platforms", ["未指定"])
            ],
        },
        "脚本公式": {
            "select": {"name": script_data.get("formula_type", "未分类")},
        },
        "预估时长(秒)": {
            "number": script_data.get("duration_seconds", 60),
        },
    }

    # 如果有完整脚本文本，放入页面内容区域
    if script_data.get("full_script"):
        properties["脚本内容"] = {
            "rich_text": [{"text": {"content": script_data["full_script"][:2000]}}],
        }

    return append_to_database(properties)


def sync_distribution_plan(plan_data: dict) -> dict:
    """同步分发方案到 Notion"""
    publish_date = plan_data.get("publish_date", datetime.now(timezone.utc).isoformat())

    properties = {
        "标题": {
            "title": [{"text": {"content": plan_data.get("title", "无标题内容")}}],
        },
        "类型": {
            "select": {"name": "分发"},
        },
        "阶段": {
            "select": {"name": plan_data.get("status", "待发布")},
        },
        "发布日期": {
            "date": {"start": publish_date},
        },
        "目标平台": {
            "multi_select": [
                {"name": p} for p in plan_data.get("platforms", [])
            ],
        },
    }

    return append_to_database(properties)


# ============================================================
# CLI
# ============================================================

def main():
    parser = argparse.ArgumentParser(
        description="OpenStudio-Agent: Notion 同步工具"
    )
    parser.add_argument(
        "--agent",
        choices=["researcher", "writer", "distributor"],
        required=True,
        help="要同步的 Agent 类型",
    )
    parser.add_argument(
        "--input",
        type=str,
        required=True,
        help="Agent 输出的 JSON 文件路径",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="仅打印将要写入的数据，不实际调用 API",
    )
    args = parser.parse_args()

    # 前置检查
    if not NOTION_TOKEN or not NOTION_CONTENT_DB_ID:
        print("❌ 请在 .env 文件中设置 NOTION_TOKEN 和 NOTION_CONTENT_DB_ID")
        print("   参考 .env.example 文件")
        sys.exit(1)

    # 读取输入数据
    input_path = Path(args.input)
    if not input_path.exists():
        print(f"❌ 文件不存在: {input_path}")
        sys.exit(1)

    with open(input_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    # 选择适配器
    adapters = {
        "researcher": sync_research_report,
        "writer": sync_script_card,
        "distributor": sync_distribution_plan,
    }
    sync_fn = adapters[args.agent]

    if args.dry_run:
        print("🔍 [DRY RUN] 将写入以下数据:")
        print(json.dumps(data, ensure_ascii=False, indent=2))
        return

    # 执行同步
    print(f"📤 正在同步 {args.agent} 的输出到 Notion...")
    result = sync_fn(data)
    page_id = result.get("id", "unknown")
    print(f"✅ 同步成功！Notion 页面 ID: {page_id}")
    print(f"   链接: https://notion.so/{page_id.replace('-', '')}")


if __name__ == "__main__":
    main()
