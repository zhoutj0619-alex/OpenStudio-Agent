<p align="center">
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT">
  <img src="https://img.shields.io/badge/Status-Active-brightgreen.svg" alt="Status: Active">
  <img src="https://img.shields.io/badge/AI_Engine-Claude%20%7C%20GPT--4o%20%7C%20DeepSeek-blue.svg" alt="AI Engine">
  <img src="https://img.shields.io/badge/Build_in_Public-🔥-orange.svg" alt="Build in Public">
</p>

<h1 align="center">🏠 OpenStudio-Agent</h1>
<p align="center"><strong>一人公司的 AI 操作系统 · The Open-Source Operating System for One-Person Media Companies</strong></p>
<p align="center">
  <a href="#-项目简介">中文</a> •
  <a href="#-overview">English</a> •
  <a href="#-快速开始">快速开始</a> •
  <a href="#-架构设计">架构</a> •
  <a href="#-agent-团队">Agent 团队</a>
</p>

---

> **"我不是在卖工具。我把自己整个公司的 AI 系统开源给你。"**
>
> 这个仓库不是教程，不是 Demo，不是「教你用 ChatGPT 写文案」的泛泛之谈。
> 它是一个**可以运行的一人自媒体公司 AI 系统**。
>
> 4 个 AI Agent · 每人一个岗位 · 在 GitHub 上公开构建。
>
> Clone → 配置 → 运行。你的 AI 团队今天上线。

---

## 📖 项目简介

**OpenStudio-Agent** 是一个开源的 AI 工作流系统，专为 **一人自媒体公司** 设计。

我把自媒体公司拆解成 **4 个标准岗位**，每个岗位由一个 AI Agent 负责：

| Agent | 岗位 | 对标人类角色 | 你得到什么 |
|-------|------|------------|-----------|
| 🕵️ **Researcher** | 选题与情报官 | 内容总监 / 编辑 | 每日选题日报，含热度评分 + 切入角度 + 竞品分析 |
| ✍️ **Writer** | 爆款脚本策划师 | 首席编剧 / 文案 | 三种黄金框架的完整脚本（痛点前置/反常识/故事驱动） |
| 🎨 **Visual Designer** | 视觉与素材包装师 | 美术指导 | 封面方案 + Midjourney Prompt + 分镜建议 |
| 📡 **Distributor** | 全渠道运营分发员 | 运营总监 | 6 平台适配文案 + 发布排期 + SEO 优化 + 数据模板 |

**把这些 Agent 串起来，你就有了一个 24/7 运转的 AI 内容工厂。**

---

## 🎯 核心理念：Build in Public

> **开源不是慈善，是最高级的营销。**

在 AI 时代，「公开构建」比你藏着掖着的 ROI 高 10 倍：

- 📹 **天然内容源**：「如何用 AI 运营自媒体」本身就是爆款选题，你的仓库就是你的视频素材库
- 🤝 **信任即货币**：观众可以看到你的真实系统而不是只看到你出镜，信任感指数级上升
- 🧠 **免费的外脑**：开源社区的开发者会帮你 PR、修 Bug、接入新模型——你的公司凭空多了一个工程团队
- 🔄 **飞轮效应**：越多人 Star → 越多人看到你的内容 → 越多人关注你 → 越多人用你的开源项目

**你的壁垒不是代码，是你本人。** 你的经历、你的观点、你的表达方式——这三样东西永远抄不走。

---

## 🏗 架构设计

```
                         ┌──────────────────────┐
                         │    📅 Notion 内容日历   │
                         │   (你的指挥中心)        │
                         └──────────┬───────────┘
                                    │
         ┌──────────────────────────┼──────────────────────────┐
         │                          │                          │
         ▼                          ▼                          ▼
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│  🕵️ Researcher  │    │  ✍️ Writer      │    │  🎨 Visual       │
│  选题与情报官     │    │  爆款脚本策划师   │    │  Designer       │
│                 │    │                 │    │  视觉与素材包装师  │
│  输入:          │    │  输入:          │    │                 │
│  · 关键词       │    │  · 选题日报      │    │  输入:          │
│  · 平台热搜     │    │  · 内容风格      │    │  · 完整脚本     │
│  · 竞品动态     │    │                 │    │  · 品牌色板     │
│                 │    │                 │    │                 │
│  输出:          │    │  输出:          │    │  输出:          │
│  · 选题日报      │───▶│  · 完整脚本      │───▶│  · 封面方案     │
│  · 角度建议     │    │  · 拍摄建议      │    │  · MJ Prompt   │
│  · 竞品分析     │    │                 │    │  · 分镜建议     │
└─────────────────┘    └─────────────────┘    └────────┬────────┘
                                                       │
                                                       ▼
                                              ┌─────────────────┐
                                              │  📡 Distributor │
                                              │  全渠道运营分发员  │
                                              │                 │
                                              │  输入:          │
                                              │  · 内容成品     │
                                              │                 │
                                              │  输出:          │
                                              │  · 6平台文案    │
                                              │  · SEO优化      │
                                              │  · 发布排期     │
                                              └────────┬────────┘
                                                       │
                                                       ▼
                                              ┌─────────────────┐
                                              │  📊 数据回收     │
                                              │  复盘 → 迭代     │
                                              └─────────────────┘
```

**工作流全景**: `关键词 + 热点` → `选题日报` → `完整脚本` → `封面方案` → `多平台分发` → `数据回收`

---

## 🚀 快速开始

### 前提条件

- Python 3.10+
- 一个 AI API Key（Claude / OpenAI / DeepSeek 任选其一）
- （可选）Notion 账号 + Integration Token

### 1. Clone 仓库

```bash
git clone https://github.com/YOUR_USERNAME/OpenStudio-Agent.git
cd OpenStudio-Agent
```

### 2. 安装依赖

```bash
pip install -r requirements.txt
```

### 3. 配置环境变量

```bash
cp .env.example .env
# 编辑 .env，填入你的 API Keys
```

### 4. 运行第一个 Agent

```bash
# 生成今日选题日报
python workflows/run_daily_digest.py \
  --keywords "AI工作流,自媒体自动化,一人公司" \
  --model claude-sonnet-5

# 也可以用 GPT-4o
python workflows/run_daily_digest.py \
  --keywords "AI工作流,自媒体自动化,一人公司" \
  --model gpt-4o
```

### 5. （可选）同步到 Notion

```bash
python workflows/notion_sync.py \
  --agent researcher \
  --input data/daily_digest_20250716.md
```

### 最快上手方式

**如果你不想跑代码**，直接打开 `agents/` 文件夹：

1. 复制 `researcher.yaml` 中的 System Prompt
2. 粘贴到 Claude / ChatGPT 的自定义指令中
3. 开始对话：「请根据 agents/researcher.yaml 的规则，为我生成今天的选题日报」

**零代码，零配置，三分钟上线。**

---

## 👥 Agent 团队

每个 Agent 都是一个完整的岗位定义，包含：
- 📋 **System Prompt** — 经过实战打磨的角色设定
- 🔧 **工具配置** — 这个岗位需要什么工具
- 📥 **输入 Schema** — 它接受什么输入
- 📤 **输出格式** — 它产出什么，以什么格式

详见 `agents/` 目录下的每个 `.yaml` 文件。

| Agent | 配置文件 | 推荐模型 | 用法场景 |
|-------|---------|---------|---------|
| 🕵️ 选题情报官 | [researcher.yaml](agents/researcher.yaml) | Claude Sonnet / GPT-4o | 每天早上跑一次，生成选题日报 |
| ✍️ 脚本策划师 | [writer.yaml](agents/writer.yaml) | Claude Opus（推荐）/ GPT-4o | 选题确定后，生成完整脚本 |
| 🎨 视觉包装师 | [visual_designer.yaml](agents/visual_designer.yaml) | Claude Sonnet / GPT-4o | 脚本完成后，生成封面和分镜方案 |
| 📡 分发运营员 | [distributor.yaml](agents/distributor.yaml) | Claude Sonnet / GPT-4o | 内容制作完成后，生成多平台分发方案 |

---

## 📂 目录结构

```
OpenStudio-Agent/
├── .github/workflows/       # CI/CD 自动化（如定时触发选题抓取）
├── agents/                  # 🤖 各岗位 Agent 的 System Prompt 和配置
│   ├── researcher.yaml      #   选题与情报官
│   ├── writer.yaml          #   爆款脚本策划师
│   ├── visual_designer.yaml #   视觉与素材包装师
│   └── distributor.yaml     #   全渠道运营分发员
├── workflows/               # 🔧 自动化连接脚本
│   ├── notion_sync.py       #   Agent 输出 → Notion 自动同步
│   └── run_daily_digest.py  #   每日选题自动生成器
├── templates/               # 📋 用户模板
│   ├── Notion_Database_Template.md  # Notion 内容日历模板（一键复制）
│   └── Video_Script_Template.md     # 三种爆款脚本框架模板
├── docs/                    # 📚 详细文档（待补充）
├── examples/                # 💡 真实案例（脱敏后）
├── .env.example             # 环境变量模板
├── .gitignore
├── LICENSE                  # MIT
└── README.md                # 你正在看的这个文件
```

---

## 🛣 路线图

### ✅ 第一阶段：核心 Agent 开源（已完成）
- [x] 4 个 Agent System Prompt 开源
- [x] 三种脚本黄金框架模板
- [x] Notion 内容日历模板
- [x] 每日选题自动化脚本
- [x] Notion 同步脚本
- [x] 中英双语 README

### 🚧 第二阶段：自动化工作流（进行中）
- [ ] Make.com / n8n 蓝图（零代码方案）
- [ ] RSS + 热搜自动聚合器
- [ ] 脚本 → 提词器 自动格式化
- [ ] 多平台发布 API 集成（B站/抖音/小红书）

### 🔮 第三阶段：全自动 Agent 管道
- [ ] Dify DSL 导出（一键导入 Dify 平台）
- [ ] Agent 间自动串联（选题 → 脚本 → 封面 → 分发 全自动）
- [ ] 数据回收 Agent（自动收集各平台数据，生成复盘报告）
- [ ] 本地优先方案（Ollama + 本地大模型，完全离线运行）

---

## 🤝 贡献指南

这个项目因 **Build in Public** 而生。欢迎一切形式的贡献：

- 🐛 **发现 Bug？** 提 Issue
- 💡 **有更好的 Prompt？** 提 PR 到 `agents/`
- 🔧 **接入新平台？** 贡献 workflow 脚本
- 📖 **用了这个系统？** 在 Discussion 里分享你的案例

**请在 PR 前阅读 [CONTRIBUTING.md](CONTRIBUTING.md)**（核心原则：不要提交包含你个人 API Key 和私密数据的代码）。

---

## ⚠️ 安全提示

> 🔴 **绝对不要** 在代码中 hardcode 你的 API Key、密码或私密 Notion 链接。
>
> 🟢 **始终** 使用 `.env` 文件存储敏感信息。
>
> 🟢 **始终** 检查 `git diff` 确认没有敏感数据后再 `git push`。
>
> 如果不小心提交了敏感信息，立即在 API 提供商后台 **撤销该 Key** 并重新生成。

---

## 📄 许可证

MIT License — 详见 [LICENSE](LICENSE)

**你可以**：商用、修改、分发、私用
**你需要**：保留版权声明、不追究作者责任

---

## ⭐ Star 历史

如果这个项目对你有用，点个 Star ⭐ 让我知道。每一个 Star 都是下一期视频的素材。

---

<p align="center">
  <strong>🏠 OpenStudio-Agent</strong><br>
  一人公司的 AI 操作系统<br>
  <sub>Built in Public · Powered by Claude & GPT · MIT Licensed</sub>
</p>

---

## 📖 English Overview

**OpenStudio-Agent** is an open-source AI workflow system for **one-person media companies**.

It breaks down a media company into 4 AI-powered roles:

| Agent | Role | What It Does |
|-------|------|-------------|
| 🕵️ **Researcher** | Trend Scout & Topic Curator | Generates daily topic reports with heat scores, angles, and competitor analysis |
| ✍️ **Writer** | Viral Script Architect | Produces complete video scripts using 3 proven frameworks with hook design |
| 🎨 **Visual Designer** | Art Director | Creates thumbnail concepts, Midjourney prompts, and shot-by-shot visual plans |
| 📡 **Distributor** | Omni-Channel Publisher | Adapts content for 6+ platforms with SEO optimization and publishing schedules |

### Why Open Source?

In the AI era, **Build in Public is the ultimate marketing strategy**:

- Every feature becomes video content
- Transparency builds unbeatable trust
- The open-source community becomes your free engineering team
- Your code is copyable; your story, perspective, and voice are not

### Quick Start (English)

```bash
git clone https://github.com/YOUR_USERNAME/OpenStudio-Agent.git
cd OpenStudio-Agent
pip install -r requirements.txt
cp .env.example .env  # fill in your API keys

# Generate today's topic report
python workflows/run_daily_digest.py \
  --keywords "AI workflow,content automation,solo entrepreneur" \
  --model claude-sonnet-5
```

**Zero-code approach**: Copy any System Prompt from `agents/*.yaml`, paste into Claude/ChatGPT, start creating.

### License

MIT — use it, modify it, build your business on it. Just keep the attribution.
