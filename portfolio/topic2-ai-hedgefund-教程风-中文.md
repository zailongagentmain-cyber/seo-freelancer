# 从零搭建 AI 交易系统：开源方案实测

## 为什么研究 AI 交易？

- 📊 数据驱动决策
- 🤖 消除情绪干扰
- ⚡ 24/7 市场监控

## 项目对比

| 项目 | Stars | 特点 |
|------|-------|------|
| ai-hedge-fund | 48K | 多 Agent 模拟投资团队 |
| FinGPT | 12K | 开源金融大模型 |
| MarketGPT | 5K | 市场预测 |

## 快速部署教程

### 环境准备

```bash
# 克隆项目
git clone https://github.com/virattt/ai-hedge-fund.git

# 安装依赖
cd ai-hedge-fund
poetry install

# 配置 API
cp .env.example .env
# 添加你的 OpenAI API Key
```

### 运行演示

```bash
poetry run python -m app
```

## 核心模块解析

1. **Valuation Agent** — 计算股票内在价值
2. **Sentiment Agent** — 分析市场情绪
3. **Fundamentals Agent** — 基本面分析
4. **Technicals Agent** — 技术指标分析
5. **Risk Manager** — 风险管理

## 注意事项

⚠️ **不要用于真实交易！**
- 回测 ≠ 实盘
- 历史数据有幸存者偏差
- 市场环境会变化

---

*动手试试？在评论区分享你的结果*
