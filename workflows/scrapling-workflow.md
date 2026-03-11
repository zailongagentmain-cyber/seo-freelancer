# Scrapling + 反爬虫工作流

## 概述

这是一个整合了 Scrapling 和各种反爬虫解决方案的自动化工作流，用于处理 freelancer 网站注册、监控等工作。

---

## 工作流架构

```
┌─────────────────────────────────────────────────────────────┐
│                    自动化工作流                              │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐  │
│  │   第一层      │ -> │   第二层      │ -> │   第三层      │  │
│  │  Scrapling  │    │  浏览器自动化  │    │  外部服务    │  │
│  │  (基础爬取)  │    │  (Stealthy)  │    │  (CAPTCHA)  │  │
│  └──────────────┘    └──────────────┘    └──────────────┘  │
│        │                  │                  │              │
│        v                  v                  v              │
│  - 普通网站           - 高防护网站         - 验证码        │
│  - 数据采集          - 登录/注册          - 复杂验证      │
│  - SEO 研究          - 动态内容           - 代理IP       │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 使用方法

### 快速开始

```python
from workflow import FreelancerWorkflow

# 初始化工作流
wf = FreelancerWorkflow()

# 尝试访问网站
result = wf.access_site('fiverr')

if result.success:
    print("访问成功!")
else:
    print(f"需要进一步处理: {result.reason}")
```

### 完整示例

```python
from workflow import FreelancerWorkflow

wf = FreelancerWorkflow()

sites = ['fiverr', 'upwork', 'peopleperhour', 'guru', 'contra']

for site in sites:
    result = wf.access_site(site)
    
    if result.success:
        # 执行需要的操作
        wf.fill_registration(site, user_data)
    elif result.need_captcha:
        # 使用 CAPTCHA 服务
        wf.solve_captcha(result.page)
    elif result.need_proxy:
        # 更换代理
        wf.rotate_proxy()
    else:
        print(f"无法处理: {result.reason}")
```

---

## 层级详情

### 第一层: Scrapling 基础爬取

**适用场景**：
- 普通网站
- 数据采集
- SEO 研究

**代码**:
```python
from scrapling.fetchers import Fetcher

f = Fetcher()
p = f.get('https://example.com')
```

### 第二层: StealthyFetcher 浏览器自动化

**适用场景**：
- 高防护网站
- 登录/注册
- 动态内容

**代码**:
```python
from scrapling.fetchers import StealthyFetcher
import asyncio

async def fetch():
    f = StealthyFetcher()
    page = await f.async_fetch(url, headless=True)
    return page
```

### 第三层: 外部服务

**适用场景**：
- 复杂验证码
- IP 被封
- 高级防护

**服务**:
| 服务 | 用途 | API |
|------|------|-----|
| Capsolver | CAPTCHA 解决 | capsolver.com |
| 2Captcha | 人工+AI | 2captcha.com |
| Bright Data | 代理IP | brightdata.com |
| Oxylabs | 企业代理 | oxylabs.io |

---

## 网站适配表

| 网站 | 层级 | 成功率 | 备注 |
|------|------|--------|------|
| Fiverr | 2-3层 | 60-80% | 间歇性验证 |
| Upwork | 2层 | 90% | 需要正确URL |
| PeoplePerHour | 1层 | 95% | 直接访问 |
| Guru | 1层 | 95% | 直接访问 |
| Contra | 1层 | 95% | 直接访问 |
| Toptal | 2层 | 90% | 需要申请 |
| Freelancer | 2层 | 85% | 有简单验证 |

---

## 扩展指南

### 添加新网站

```python
# 在 sites.yaml 中添加
sites:
  new_site:
    url: "https://www.newsite.com/register"
    layer: 2  # 需要第几层
    wait_time: 5  # 等待时间
    form_fields:  # 表单字段
      - name
      - email
```

### 添加新 CAPTCHA 服务

```python
class CaptchaSolver:
    def __init__(self, provider='capsolver'):
        self.providers = {
            'capsolver': CapsolverAPI(),
            '2captcha': TwoCaptchaAPI(),
        }
        self.current = self.providers[provider]
    
    def solve(self, site_key, url):
        return self.current.solve(site_key, url)
```

---

## 维护记录

### 2026-03-12
- 初始版本
- 支持 6 个 freelancer 网站
- 整合 Scrapling + 外部服务

---

*持续更新...*
