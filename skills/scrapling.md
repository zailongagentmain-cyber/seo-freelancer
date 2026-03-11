# Scrapling 技能库

## 简介

**Scrapling** - 自适应网页爬虫框架
- GitHub: https://github.com/D4Vinci/Scrapling
- 文档: https://scrapling.readthedocs.io
- 版本: 0.2.99

## 安装

```bash
pip3 install scrapling
```

## 核心功能

### 1. 基础爬取
```python
from scrapling.fetchers import Fetcher

f = Fetcher()
p = f.get('https://example.com')
title = p.css('title::text').get()
```

### 2. 智能元素追踪
```python
# 即使网站结构变化，也能找到元素
products = p.css('.product', adaptive=True)
```

### 3. 异步爬取
```python
import asyncio
from scrapling.fetchers import AsyncFetcher

async def crawl():
    f = AsyncFetcher()
    p = await f.async_fetch('https://example.com')
```

### 4. Spider 框架
```python
from scrapling.spiders import Spider

class MySpider(Spider):
    name = "demo"
    start_urls = ["https://example.com/"]
    
    async def parse(self, response):
        for item in response.css('.product'):
            yield {"title": item.css('h2::text').get()}

MySpider().start()
```

### 5. 代理轮换
```python
from scrapling.spiders import Spider, ProxyRotator

rotator = ProxyRotator(['proxy1', 'proxy2'])
```

### 6. MCP Server (AI 辅助)
```bash
scrapling-mcp-server
```

## 适用场景

1. **数据采集** - 产品信息、新闻文章
2. **竞品分析** - 价格监控、评论抓取
3. **SEO 研究** - 关键词分析、排名监控
4. **内容聚合** - 多源内容整合

## 注意事项

- 需要 Python 3.9+
- StealthyFetcher 需要 camoufox 浏览器
- 遵守网站的 robots.txt 和服务条款

## 测试状态

✅ 基本爬取：正常工作  
⚠️ StealthyFetcher：需要额外安装 camoufox  
✅ 文档：完整

---

*更新时间：2026-03-12*
