"""
每日选题自动化脚本 — 驱动 Researcher Agent 生成《选题日报》

用法:
    # 基础用法：用关键词生成选题日报
    python run_daily_digest.py \
        --keywords "AI工作流,自媒体自动化,一人公司" \
        --platforms douyin,bilibili,xiaohongshu

    # 完整用法：连接 Claude API 自动执行
    python run_daily_digest.py \
        --keywords "AI工作流,自媒体自动化,一人公司" \
        --platforms douyin,bilibili,xiaohongshu \
        --model claude-sonnet-5 \
        --output ./data/daily_digest_$(date +%Y%m%d).md \
        --sync-to-notion

前置条件:
    pip install anthropic python-dotenv
"""

import os
import sys
import json
import argparse
import subprocess
from datetime import datetime
from pathlib import Path

# ============================================================
# 配置加载
# ============================================================

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

PROJECT_ROOT = Path(__file__).resolve().parent.parent
AGENTS_DIR = PROJECT_ROOT / "agents"
DATA_DIR = PROJECT_ROOT / "data"

# ============================================================
# 核心逻辑
# ============================================================

def load_agent_prompt(agent_name: str) -> str:
    """加载 Agent 的 System Prompt"""
    import yaml  # 需要 pip install pyyaml

    yaml_path = AGENTS_DIR / f"{agent_name}.yaml"
    if not yaml_path.exists():
        raise FileNotFoundError(f"Agent 配置文件不存在: {yaml_path}")

    with open(yaml_path, "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)

    return config["system_prompt"]


def build_user_prompt(
    keywords: list[str],
    platforms: list[str],
    competitors: list[str] | None = None,
    date_range: str = "last_24h",
) -> str:
    """构建发送给 AI 的用户消息"""
    prompt_parts = [
        "请根据以下参数生成今日的《选题日报》：",
        "",
        f"## 账号定位关键词",
        ", ".join(keywords),
        "",
        f"## 监控平台",
        ", ".join(platforms),
        "",
        f"## 时间范围",
        date_range,
    ]

    if competitors:
        prompt_parts.extend([
            "",
            "## 竞品账号",
            "\n".join(f"- {c}" for c in competitors),
        ])

    prompt_parts.extend([
        "",
        "## 输出要求",
        "请严格按照 agents/researcher.yaml 中定义的输出格式，",
        "生成包含「热点速览表格」和「深度分析」的完整选题日报。",
    ])

    return "\n".join(prompt_parts)


def run_with_claude_api(system_prompt: str, user_prompt: str, model: str) -> str:
    """使用 Anthropic Claude API 执行"""
    try:
        import anthropic
    except ImportError:
        print("❌ 请安装 anthropic SDK: pip install anthropic")
        sys.exit(1)

    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        print("❌ 请在 .env 中设置 ANTHROPIC_API_KEY")
        sys.exit(1)

    client = anthropic.Anthropic(api_key=api_key)

    print(f"🤖 正在调用 {model}...")
    message = client.messages.create(
        model=model,
        max_tokens=4096,
        system=system_prompt,
        messages=[{"role": "user", "content": user_prompt}],
    )

    return message.content[0].text


def run_locally(system_prompt: str, user_prompt: str) -> str:
    """
    在本地运行（打印 System Prompt 和 User Prompt），
    供用户手动复制到 Claude Desktop / ChatGPT 使用
    """
    separator = "=" * 60
    output = f"""
{separator}
🤖 OpenStudio-Agent 每日选题生成器
{separator}

📋 **System Prompt (已内置，无需手动输入):**
{separator}
{system_prompt[:500]}...
(完整 System Prompt 见 agents/researcher.yaml)

{separator}
📝 **请将以下内容发送给 Claude / ChatGPT:**
{separator}
{user_prompt}

{separator}
💡 提示：
  - 设置 ANTHROPIC_API_KEY 环境变量可自动调用 Claude API
  - 或在 .env 文件中配置 OPENAI_API_KEY 使用 GPT-4o
  - 运行: python run_daily_digest.py --help 查看完整用法
{separator}
"""
    return output


def save_output(output: str, output_path: str | None = None) -> Path:
    """保存输出到文件"""
    DATA_DIR.mkdir(exist_ok=True)

    if output_path:
        save_path = Path(output_path)
    else:
        date_str = datetime.now().strftime("%Y%m%d_%H%M%S")
        save_path = DATA_DIR / f"daily_digest_{date_str}.md"

    save_path.parent.mkdir(parents=True, exist_ok=True)
    with open(save_path, "w", encoding="utf-8") as f:
        f.write(output)

    return save_path


def sync_to_notion(json_data_path: str) -> None:
    """调用 notion_sync.py 同步到 Notion"""
    script = PROJECT_ROOT / "workflows" / "notion_sync.py"
    if not script.exists():
        print("⚠️  notion_sync.py 不存在，跳过 Notion 同步")
        return

    subprocess.run([
        sys.executable, str(script),
        "--agent", "researcher",
        "--input", json_data_path,
    ])


# ============================================================
# CLI
# ============================================================

def main():
    parser = argparse.ArgumentParser(
        description="OpenStudio-Agent: 每日选题自动生成",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  # 使用 Claude API 自动生成
  python run_daily_digest.py -k "AI,自媒体" --model claude-sonnet-5

  # 生成 Prompt 模板（手动复制到 ChatGPT）
  python run_daily_digest.py -k "AI,自媒体" --local

  # 生成并同步到 Notion
  python run_daily_digest.py -k "AI,自媒体" --model claude-sonnet-5 --sync-to-notion
        """,
    )
    parser.add_argument(
        "-k", "--keywords",
        type=str,
        required=True,
        help="账号定位关键词，逗号分隔",
    )
    parser.add_argument(
        "-p", "--platforms",
        type=str,
        default="douyin,bilibili,xiaohongshu",
        help="监控平台，逗号分隔 (默认: douyin,bilibili,xiaohongshu)",
    )
    parser.add_argument(
        "-c", "--competitors",
        type=str,
        help="竞品账号名称，逗号分隔",
    )
    parser.add_argument(
        "--model",
        type=str,
        default=None,
        help="AI 模型名称 (如 claude-sonnet-5, gpt-4o)。不指定则使用本地模式",
    )
    parser.add_argument(
        "--local",
        action="store_true",
        help="本地模式：仅生成 Prompt，不调用 API",
    )
    parser.add_argument(
        "-o", "--output",
        type=str,
        help="输出文件路径",
    )
    parser.add_argument(
        "--sync-to-notion",
        action="store_true",
        help="生成后同步到 Notion",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="仅打印，不执行",
    )
    args = parser.parse_args()

    # 解析参数
    keywords = [k.strip() for k in args.keywords.split(",")]
    platforms = [p.strip() for p in args.platforms.split(",")]
    competitors = (
        [c.strip() for c in args.competitors.split(",")]
        if args.competitors
        else None
    )

    # 构建 Prompt
    system_prompt = load_agent_prompt("researcher")
    user_prompt = build_user_prompt(keywords, platforms, competitors)

    if args.dry_run:
        print("=" * 60)
        print("🔍 DRY RUN — 以下是构建好的 Prompt")
        print("=" * 60)
        print("\n【System Prompt (前 500 字符)】")
        print(system_prompt[:500] + "...")
        print("\n【User Prompt】")
        print(user_prompt)
        return

    # 执行
    if args.model and not args.local:
        output = run_with_claude_api(system_prompt, user_prompt, args.model)
    else:
        output = run_locally(system_prompt, user_prompt)

    # 保存
    save_path = save_output(output, args.output)
    print(f"\n📁 输出已保存: {save_path}")

    # Notion 同步
    if args.sync_to_notion and args.model:
        print("🔄 正在同步到 Notion...")
        sync_to_notion(str(save_path))


if __name__ == "__main__":
    main()
