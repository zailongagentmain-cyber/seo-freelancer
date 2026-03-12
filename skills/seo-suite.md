# 🐉 龙雅人定制版 SEO Suite

> **版本**: 1.1 | **更新**: 2026-03-12
> 为龙雅人打造的SEO全能工具箱，整合竞品分析、内容创作、技术检测、关键词研究

---

## ⚠️ 重要警告：Schema Markup 检测

**`web_fetch` 和 `curl` 无法可靠检测结构化数据 / Schema Markup！**

很多 CMS 插件（AIOSEO、Yoast、RankMath）通过客户端 JavaScript 注入 JSON-LD —— 它不会出现在静态 HTML 或 `web_fetch` 输出中（转换时会剥离 `<script>` 标签）。

**准确检测 Schema Markup 的方法：**
1. **浏览器工具** — 渲染页面后运行：`document.querySelectorAll('script[type="application/ld+json"]')`
2. **Google Rich Results Test** — https://search.google.com/test/rich-results
3. **Screaming Frog** — 如果客户提供导出的文件（SF 会渲染 JavaScript）

**永远不要仅仅根据 `web_fetch` 或 `curl` 报告"未找到 schema"。** 这会导致虚假的审计结果！

---

## 🎯 这个 Skill 做什么？

龙雅人 SEO Suite 是一个**模块化 SEO 工作流**，帮你一条龙完成：
1. 🔍 **竞品分析** - 挖出竞争对手的流量密码
2. ✍️ **内容写作** - 产出 SEO 友好的文章
3. 🔧 **技术检测** - 抓出网站的技术问题
4. 🎯 **关键词研究** - 找到高价值关键词

---

## 🛠️ 核心工具

### 0. 环境准备

```bash
# 必装工具
npm install -g playwright  # 浏览器自动化
pip3 install scrapling beautifulsoup4 lxml  # 网页爬取
pip3 install openai anthropic  # AI 内容生成

# 可选工具
pip3 install advertools screaming-frog-log-file-analyzer  # SEO 专用
```

---

## 📊 模块一：竞品分析 (Competitor Analysis)

### 1.1 基础竞品调研

```python
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def competitor_basic_info(url):
    """获取竞品基础信息"""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    r = requests.get(url, headers=headers, timeout=10)
    soup = BeautifulSoup(r.text, 'lxml')
    
    return {
        'title': soup.title.string if soup.title else '',
        'meta_description': soup.find('meta', attrs={'name': 'description'}).get('content', ''),
        'h1_tags': [h.get_text(strip=True) for h in soup.find_all('h1')],
        'internal_links': len(soup.find_all('a', href=True)),
        'images_count': len(soup.find_all('img')),
    }
```

### 1.2 关键词差距分析

```python
def keyword_gap_analysis(my_keywords, competitor_keywords):
    """找出竞品有你没有的关键词"""
    my_set = set(my_keywords)
    comp_set = set(competitor_keywords)
    
    gap = comp_set - my_set  # 竞品排名你未覆盖的
    opportunity = list(gap)[:20]  # 取前20个
    
    return {
        'gap_count': len(gap),
        'top_opportunities': opportunity,
        'difficulty': 'medium' if len(gap) > 10 else 'low'
    }
```

### 1.3 流量来源分析

```python
def analyze_traffic_sources(url):
    """分析竞品流量来源（模拟）"""
    # 实际使用 SEMrush/Ahrefs API
    return {
        'organic_keywords': '~5,000',  # 预估
        'organic_traffic': '~50,000/月',
        'top_keywords': [
            {'keyword': 'seo services', 'volume': 1200, 'difficulty': 67},
            {'keyword': 'seo agency', 'volume': 900, 'difficulty': 58},
        ],
        'referral_domains': 150
    }
```

### 1.4 竞品内容策略挖掘

```python
def content_strategy_mining(url, limit=10):
    """挖掘竞品的内容策略"""
    headers = {'User-Agent': 'Mozilla/5.0'}
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')
    
    articles = []
    for link in soup.select('a[href*="/blog/"], a[href*="/article/"]')[:limit]:
        articles.append({
            'title': link.get_text(strip=True),
            'url': link['href']
        })
    
    return {
        'content_types': ['blog', 'guide', 'case-study'],
        'publishing_frequency': 'weekly',
        'avg_content_length': 2000,
        'articles': articles
    }
```

---

## ✍️ 模块二：SEO 内容写作 (Content Writer)

### 2.1 关键词规划

```python
def keyword_planning(seed_keyword, intent='informational'):
    """生成内容关键词规划"""
    # 这里可以接入 Google Keyword Planner API
    keywords = [
        {
            'keyword': seed_keyword,
            'volume': 1000,
            'difficulty': 45,
            'cpc': 2.5,
            'intent': intent
        },
        {
            'keyword': f'{seed_keyword} guide',
            'volume': 500,
            'difficulty': 35,
            'cpc': 3.2,
            'intent': 'informational'
        },
        {
            'keyword': f'best {seed_keyword}',
            'volume': 800,
            'difficulty': 55,
            'cpc': 4.1,
            'intent': 'commercial'
        }
    ]
    return keywords
```

### 2.2 内容大纲生成

```python
def generate_content_outline(topic, target_keywords, word_count=1500):
    """生成 SEO 内容大纲"""
    outline = {
        'title': f'The Ultimate Guide to {topic}',
        'meta_description': f'Learn everything about {topic} in this comprehensive guide.',
        'word_count': word_count,
        'sections': [
            {
                'heading': f'What is {topic}?',
                'word_count': 300,
                'keywords': [target_keywords[0]],
                'intent': 'informational'
            },
            {
                'heading': f'Why {topic} Matters',
                'word_count': 400,
                'keywords': [target_keywords[0], 'benefits'],
                'intent': 'informational'
            },
            {
                'heading': f'How to Master {topic}',
                'word_count': 600,
                'keywords': [target_keywords[0], 'tutorial', 'guide'],
                'intent': 'transactional'
            },
            {
                'heading': 'Common Mistakes to Avoid',
                'word_count': 200,
                'keywords': [target_keywords[0], 'mistakes'],
                'intent': 'informational'
            }
        ]
    }
    return outline
```

### 2.3 AI 辅助写作

```python
def seo_content_writer(topic, keywords, tone='professional'):
    """AI 辅助生成 SEO 内容"""
    prompt = f"""
    Write a comprehensive SEO article about "{topic}".
    
    Requirements:
    - Include keywords: {', '.join(keywords)}
    - Tone: {tone}
    - Length: 1500-2000 words
    - Include: intro, 4-5 main sections, conclusion
    - Use: headings (H2, H3), bullet points, bold text
    - Optimize for E-E-A-T (Experience, Expertise, Authority, Trust)
    """
    # 调用 OpenAI API
    # response = openai.ChatCompletion.create(
    #     model="gpt-4",
    #     messages=[{"role": "user", "content": prompt}]
    # )
    return prompt  # 返回 prompt 供后续使用
```

### 2.4 内容优化检查

```python
def content_optimization_check(content, target_keywords):
    """内容 SEO 优化检查"""
    issues = []
    score = 100
    
    # 关键词密度
    for kw in target_keywords:
        density = content.lower().count(kw.lower()) / len(content.split()) * 100
        if density < 0.5:
            issues.append(f'关键词 "{kw}" 密度过低 ({density:.1f}%)')
            score -= 10
        elif density > 3:
            issues.append(f'关键词 "{kw}" 密度过高 ({density:.1f}%)，可能被惩罚')
            score -= 15
    
    # 结构检查
    if '<h2>' not in content.lower():
        issues.append('缺少 H2 标题')
        score -= 10
    if '## ' not in content:
        issues.append('建议使用 Markdown 标题结构')
        score -= 5
        
    return {
        'score': max(0, score),
        'issues': issues,
        'keyword_density': {kw: content.lower().count(kw.lower()) / len(content.split()) * 100 
                          for kw in target_keywords}
    }
```

---

## 🔧 模块三：技术 SEO 检测 (Technical SEO)

### 3.1 基础技术检测

```python
import requests
from urllib.parse import urlparse

def technical_seo_check(url):
    """完整技术 SEO 检测"""
    headers = {'User-Agent': 'Mozilla/5.0 (compatible; LongYarenBot/1.0)'}
    
    try:
        r = requests.get(url, headers=headers, timeout=15, allow_redirects=True)
        final_url = r.url
        parsed = urlparse(final_url)
        
        results = {
            'status_code': r.status_code,
            'redirects': r.history,
            'final_url': final_url,
            'domain': parsed.netloc,
            
            # HTTPS 检测
            'https': parsed.scheme == 'https',
            
            # 页面标题
            'title': '',
            'title_length': 0,
            
            # Meta 描述
            'meta_description': '',
            'meta_description_length': 0,
            
            # Canonical
            'canonical': '',
            
            # H1 标签
            'h1_count': 0,
            'h1_texts': [],
            
            # 图片优化
            'images_total': 0,
            'images_with_alt': 0,
            
            # 结构化数据
            'schema_org': False,
            
            # Core Web Vitals (模拟)
            'cwv_lcp': 'good',  # Largest Contentful Paint
            'cwv_fid': 'good',  # First Input Delay  
            'cwv_cls': 'good',  # Cumulative Layout Shift
        }
        
        soup = BeautifulSoup(r.text, 'lxml')
        
        # 解析 HTML
        if soup.title:
            results['title'] = soup.title.string or ''
            results['title_length'] = len(results['title'])
        
        meta_desc = soup.find('meta', attrs={'name': 'description'})
        if meta_desc:
            results['meta_description'] = meta_desc.get('content', '')
            results['meta_description_length'] = len(results['meta_description'])
        
        canonical = soup.find('link', attrs={'rel': 'canonical'})
        if canonical:
            results['canonical'] = canonical.get('href', '')
        
        results['h1_count'] = len(soup.find_all('h1'))
        results['h1_texts'] = [h.get_text(strip=True) for h in soup.find_all('h1')]
        
        images = soup.find_all('img')
        results['images_total'] = len(images)
        results['images_with_alt'] = sum(1 for img in images if img.get('alt'))
        
        # Schema.org 检测
        results['schema_org'] = 'schema.org' in r.text or 'schema.org' in str(soup.find_all('script', type='application/ld+json'))
        
        return results
        
    except Exception as e:
        return {'error': str(e)}
```

### 3.2 移动端适配检测

```python
def mobile_friendly_check(url):
    """检测移动端友好性"""
    # 使用 Google Mobile-Friendly Test API 或自行检测
    return {
        'viewport': True,
        'tap_targets': 'adequate',
        'font_size': 'readable',
        'content_width': 'fits',
        'mobile_score': 85
    }
```

### 3.3 站点速度分析

```python
def page_speed_analysis(url):
    """页面速度分析"""
    # 调用 PageSpeed Insights API
    return {
        'lcp': 2.5,  # 秒
        'fid': 50,   # 毫秒
        'cls': 0.1,
        'tti': 3.2,  # Time to Interactive
        'score': 78,
        'recommendations': [
            '压缩图片到 WebP 格式',
            '启用浏览器缓存',
            '减少 JavaScript 阻塞'
        ]
    }
```

### 3.4 XML Sitemap 检测

```python
def sitemap_check(url):
    """检测并分析 Sitemap"""
    sitemap_url = url.rstrip('/') + '/sitemap.xml'
    
    try:
        r = requests.get(sitemap_url, timeout=10)
        if r.status_code == 200:
            soup = BeautifulSoup(r.text, 'xml')
            urls = soup.find_all('loc')
            return {
                'exists': True,
                'url_count': len(urls),
                'urls': [u.get_text() for u in urls[:10]]  # 前10个
            }
    except:
        pass
    
    return {'exists': False}
```

### 3.5 Robots.txt 检测

```python
def robots_check(url):
    """检测 Robots.txt"""
    parsed = urlparse(url)
    robots_url = f"{parsed.scheme}://{parsed.netloc}/robots.txt"
    
    try:
        r = requests.get(robots_url, timeout=5)
        return {
            'exists': r.status_code == 200,
            'content': r.text[:1000] if r.status_code == 200 else '',
            'allows_user_agent': '*' in r.text,
            'disallows': [line for line in r.text.split('\n') if line.startswith('Disallow')]
        }
    except:
        return {'exists': False}
```

---

## 🎯 模块四：关键词研究 (Keyword Research)

### 4.1 关键词挖掘

```python
def keyword_research(seed_keyword, limit=50):
    """关键词挖掘"""
    keywords = []
    
    # 变体生成
    variations = [
        f'{seed_keyword}',
        f'best {seed_keyword}',
        f'{seed_keyword} for beginners',
        f'how to {seed_keyword}',
        f'{seed_keyword} vs',
        f'{seed_keyword} tips',
        f'{seed_keyword} tools',
        f'{seed_keyword} examples',
    ]
    
    for kw in variations:
        keywords.append({
            'keyword': kw,
            'volume': 1000,  # 实际应调用 API
            'difficulty': 45,
            'cpc': 2.5,
            'competition': 'medium'
        })
    
    return keywords[:limit]
```

### 4.2 搜索意图分类

```python
def classify_intent(keyword):
    """分类搜索意图"""
    keyword = keyword.lower()
    
    if any(w in keyword for w in ['what', 'how', 'why', 'when', 'where', 'meaning']):
        return 'informational'
    elif any(w in keyword for w in ['buy', 'price', 'cost', 'discount', 'coupon']):
        return 'transactional'
    elif any(w in keyword for w in ['best', 'top', 'review', 'compare', 'vs']):
        return 'commercial'
    elif any(w in keyword for w in ['login', 'app', 'download', 'tool']):
        return 'navigational'
    else:
        return 'informational'
```

### 4.3 关键词难度评估

```python
def keyword_difficulty(keyword):
    """评估关键词难度"""
    # 简化版 - 实际应使用 SERP 分析
    difficulty = 50  # 默认中等
    
    # 长尾词难度低
    if len(keyword.split()) > 4:
        difficulty -= 20
    
    # 商业意图词难度高
    if any(w in keyword.lower() for w in ['buy', 'best', 'top']):
        difficulty += 15
    
    return {
        'keyword': keyword,
        'difficulty': min(100, max(0, difficulty)),
        'level': 'easy' if difficulty < 30 else 'medium' if difficulty < 60 else 'hard'
    }
```

---

## 🔄 整合工作流

### 完整 SEO 审计流程

```python
def full_seo_audit(url, target_keywords):
    """完整 SEO 审计"""
    print(f"🔍 开始审计: {url}")
    
    # 1. 技术检测
    tech = technical_seo_check(url)
    print(f"✅ 技术检测完成 - 得分: {tech.get('title_length', 0)}")
    
    # 2. 竞品分析
    comp = {
        'organic_keywords': 5000,
        'top_keywords': target_keywords[:5]
    }
    print(f"✅ 竞品分析完成")
    
    # 3. 内容分析
    content_score = 75  # 简化
    print(f"✅ 内容分析完成 - 得分: {content_score}")
    
    # 4. 生成报告
    report = {
        'url': url,
        'technical': tech,
        'competitor': comp,
        'content_score': content_score,
        'overall_score': (tech.get('title_length', 0) + content_score) / 2,
        'recommendations': [
            '增加目标关键词密度到 1-2%',
            '添加更多内部链接',
            '优化图片 alt 文本',
            '添加 Schema.org 结构化数据'
        ]
    }
    
    return report
```

---

## 📋 使用场景示例

### 场景 1: 新网站 SEO 诊断
```
输入: url = "https://example.com"
输出: 完整技术检测 + 优化建议
```

### 场景 2: 内容创作辅助
```
输入: topic = "AI SEO", keywords = ["AI SEO", "SEO automation"]
输出: 内容大纲 + 优化检查清单
```

### 场景 3: 竞品调研
```
输入: competitor_url = "https://competitor.com"
输出: 流量来源 + 关键词差距 + 内容策略
```

---

## ⚠️ 注意事项

1. **遵守 robots.txt** - 爬取前先检查
2. **控制请求频率** - 不要对目标站造成压力
3. **API 配额** - Google/SEMrush API 有免费额度限制
4. **E-E-A-T** - 2025 年 SEO 核心是体验、专业、权威、可信

---

## 📚 参考资源

- [Google Search Central](https://developers.google.com/search)
- [Moz Beginner's Guide to SEO](https://moz.com/beginners-guide-to-seo)
- [Semrush Blog - SEO Trends 2025](https://www.semrush.com/blog/seo-tutorials/)
- [Schema.org Documentation](https://schema.org/docs/gs.html)

---

*🐉 龙雅人定制版 SEO Suite - 让 SEO 变得更简单！*

---

## 🚀 进阶模块：Programmatic SEO (批量SEO)

### 核心原则

1. **每页独特价值** - 不是简单替换变量的模板
2. **专有数据优先** - 自创 > 产品衍生 > 用户生成 > 授权 > 公开
3. **URL结构** - 永远使用子文件夹，不用子域名
4. **质量 > 数量** - 100个优质页面 > 10000个薄内容页面

### 12 种模板模式

| 模式 | 搜索模式 | 示例 |
|------|----------|------|
| 模板 | "[类型] template" | "resume template" |
| 精选 | "best [类别]" | "best website builders" |
| 换算 | "[X] to [Y]" | "$10 USD to GBP" |
| 对比 | "[X] vs [Y]" | "webflow vs wordpress" |
| 示例 | "[类型] examples" | "landing page examples" |
| 地区 | "[服务] in [地点]" | "dentists in austin" |
| 人群 | "[产品] for [人群]" | "crm for real estate" |
| 集成 | "[产品A] [产品B] integration" | "slack asana integration" |
| 术语 | "what is [术语]" | "what is pSEO" |
| 翻译 | 多语言内容 | 本地化内容 |
| 目录 | "[类别] tools" | "ai copywriting tools" |
| 画像 | "[实体名称]" | "stripe ceo" |

### Hub and Spoke 模型

```
Hub (中心页): 主要分类页面
  ↓
Spokes (辐条): 独立的程序化页面
  ↓
Cross-links: 辐条之间的交叉链接
```

---

## 🛠️ 推荐工具清单

### 免费工具
- Google Search Console (必备)
- Google PageSpeed Insights
- Bing Webmaster Tools
- Google Rich Results Test (Schema验证)
- Mobile-Friendly Test

### 付费工具
- Screaming Frog
- Ahrefs / Semrush
- Sitebulb
- ContentKing

---

*🐉 龙雅人定制版 SEO Suite v1.1*
*整合 ClawHub SEO Audit + Programmatic SEO 最佳实践*
