# 贡献指南

> 🏠 OpenStudio-Agent 因 **Build in Public** 而生。欢迎一切形式的贡献。

## 核心原则

### 🔴 绝对不要做的事

- **不要提交 API Key**：任何情况下都不要在代码中 hardcode API Key、Token、密码
- **不要提交私人数据**：包括你的真实选题库、脚本内容、Notion 数据库链接
- **不要提交 .env 文件**：`.env` 已在 `.gitignore` 中，永远不要 force-add

### 🟢 推荐做的事

- **改进 System Prompt**：如果你的 Prompt 变体产出了更好的内容，欢迎 PR
- **接入新平台**：B站/抖音/小红书/YouTube/公众号等平台的适配规则更新
- **新增 Agent**：如果你设计了一个新的 Agent 岗位（比如「数据分析师」「评论区运营」），欢迎贡献
- **修复 Bug**：工作流脚本的错误修复
- **完善文档**：错别字、更清晰的说明、更多案例

## 贡献流程

### 1. 提交 Issue

- 🐛 Bug 报告：描述复现步骤、期望行为、实际行为
- 💡 功能建议：描述你的使用场景和期望的解决方案
- 📖 案例分享：分享你用 OpenStudio-Agent 做出的真实内容

### 2. 提交 Pull Request

```bash
# 1. Fork 本仓库
# 2. Clone 你的 Fork
git clone https://github.com/YOUR_USERNAME/OpenStudio-Agent.git
cd OpenStudio-Agent

# 3. 创建功能分支
git checkout -b feat/your-feature-name

# 4. 修改代码...

# 5. 提交前检查
git diff  # 再次确认没有敏感数据
git add .
git commit -m "feat: description of your changes"

# 6. Push 并创建 PR
git push origin feat/your-feature-name
```

### 3. PR 审核标准

- [ ] 是否引入了新的依赖？如果有，是否必要？
- [ ] 是否包含硬编码的私密信息？
- [ ] 是否对用户有明确的文档说明？
- [ ] Agent Prompt 是否有实际的改进效果说明？

## Agent Prompt 贡献指南

贡献新的或改进的 Agent Prompt 时，请在 PR 描述中说明：

1. **改进了什么**：增加了什么能力？修复了什么缺陷？
2. **测试结果**：用同样的输入，新旧 Prompt 的输出有什么差异？
3. **适用场景**：这个改进对什么类型的内容/账号最有效？

## 代码风格

- Python 脚本：遵循 PEP 8
- YAML 配置：2 空格缩进
- Markdown 文档：中文使用全角标点，英文使用半角

## 行为准则

- 保持友善和专业
- 建设性批评，不人身攻击
- 尊重不同的内容风格和创作理念

## 许可证

贡献的代码默认使用 MIT License（与本项目一致）。
