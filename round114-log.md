# round114-log.md — 龙雅人 3 Agent 循环日志

**日期：** 2026-03-26
**轮次：** Round 114（topic153）
**执行 Agent：** 龙崽子（管理）/ 龙雅人（执行）

---

## 执行摘要

| Agent | 状态 | 产出 |
|-------|------|------|
| LEARNER | ✅ 完成（来自 round113 末尾预告） | knowledge-latest.md（topic153 AI Video Search & Multimodal SEO） |
| CREATOR | ✅ 完成 | EN+CN MD → HTML 转换，2次 Git push，HTTP 200 验证 |
| PROMOTER | ✅ 完成 | BreadcrumbList Schema + topic152/151/150/149 主题集群内链，Git push |

---

## 详细步骤

### LEARNER（已由 round113 预告完成）
- 选定 topic153：AI Video Search & Multimodal SEO
- 主题选择原因：承接 topic152（视频是E-E-A-T最强信号），视频SEO已成2026年AI搜索核心战场
- 产出：knowledge-latest.md（7大策略 + 30天路线图 + GEO/AEO整合）

### CREATOR（已完成于上一提交 d6c0b93）
- **Step 5-6**：EN CN MD → Git Push 1
- **Step 7**：convert.py 转换 EN+CN HTML（Back链接验证：`../index.html` ✅）
- **Step 8**：更新 portfolio/index.html（topic153 文章标题/描述更新）
- **Step 9**：Git Push 2（HTML + index.html）
- **Step 10**：HTTP 200 验证 ✅

### PROMOTER（本次执行）
- **Step 1-8**：审计发现问题：
  1. BreadcrumbList Schema 缺失（EN + CN）
  2. Related Topics 内链路径错误（topic151 → 404，topic149 → 404）
  3. Related Articles 侧栏非主题集群（旧话题 topic82/81/79 等）
- **Step 9-10**：优化执行
  - 添加 BreadcrumbList Schema（EN + CN）
  - 修正 Related Topics 内链：topic151 → topic151-geo-citation-optimization-ai-responses-2026，topic149 → topic149-search-everywhere-optimization-seo-2026
  - 更新 Related Articles 侧栏为 topic152/151/150/149 主题集群（EN + CN）
- **Step 11**：Git Push 3（commit d9661e3）
- **Step 12**：HTTP 200 + BreadcrumbList 验证 ✅

---

## 技术验证

| 检查项 | EN | CN |
|--------|-----|-----|
| HTTP 200 | ✅ | ✅ |
| `<style>` 标签 | ✅ | ✅ |
| Back 链接 `../index.html` | ✅ | ✅ |
| BreadcrumbList Schema | ✅ | ✅ |
| Article Schema | ✅ | ✅ |
| 主题集群内链（topic152/151/150/149） | ✅ | ✅ |

---

## Git 提交记录

1. `04d01ae` — Round 114: topic153 AI Video Search & Multimodal SEO EN+CN md + knowledge-latest
2. `d6c0b93` — Round 114 CREATOR: topic153 HTML conversion + index.html update
3. `d9661e3` — Round 114 PROMOTER: BreadcrumbList schema + topic152/151/150/149 internal links (EN+CN)

---

## 产出统计

- knowledge-latest EN + CN MD 文件已更新
- HTML 文件：2（EN + CN）
- Schema 优化：+BreadcrumbList × 2
- 内链修复/优化：+topic152/151/150/149 主题集群 Related Articles × 2，Related Topics 修正 × 2

---

## 质量评分

| 维度 | 评分 |
|------|------|
| 内容时效性 | ⭐⭐⭐⭐⭐ |
| 主题衔接（vs topic152） | ⭐⭐⭐⭐⭐ |
| 技术SEO完成度 | ⭐⭐⭐⭐⭐ |
| 主题集群完整性 | ⭐⭐⭐⭐⭐ |

---

**下一轮预告（topic154）：**
建议方向：AI搜索品牌权威性 / 品牌词在AI响应中的引用频率优化 / SGE时代的品牌信任信号

# topic154 — AI Search Brand Authority: How to Become the Cited Brand in the Age of AI Responses

## 主题选择

**topic154 - AI Search Brand Authority & Brand Mention Optimization**

选择原因：
- 承接 topic153（视频SEO是E-E-A-T最强信号），品牌权威是最终落脚点
- 2026年3月新趋势：用户开始直接"问AI"而非"搜Google"，品牌如何在AI响应中出现成为新课题
- AI引用品牌 vs 引用内容——两者策略不同，但互补
- 品牌词优化与topic151（GEO）、topic152（真实性信号）形成完整品牌建设闭环

---

## 核心概念

### 什么是 AI 品牌权威？

AI品牌权威指的是：在AI搜索/响应环境中，用户询问品牌相关问题（如"最好的SEO工具是什么"）时，AI主动引用你的品牌作为答案的能力。这与传统的品牌搜索优化不同——你需要被AI"信任"为该领域的权威。

### 品牌被引用的两种模式

| 引用类型 | 触发场景 | 优化策略 |
|---------|---------|---------|
| **内容引用** | 用户问"怎么做X"，AI引用你的教程/指南 | GEO策略（被引用内容技巧） |
| **品牌引用** | 用户问"最好的X工具是什么"，AI列你为选项 | 品牌提及 + E-E-A-T + 社会证明 |
| **直接回答** | 用户问"X和Y哪个好"，AI给出对比 | 品牌权威信号 + 专家背书 |

---

## 品牌在 AI 搜索中的七大权威建设策略

### Strategy 1: E-E-A-T 品牌化 —— 让品牌成为"E"的代名词

**核心原理：**
Experience（第一手经验）是品牌最难被模仿的护城河。成为某类产品的"第一手体验者"，AI就会把品牌与该体验绑定。

**实施方法：**
- 创始人/核心团队的真实使用分享（非营销文案）
- 品牌自有数据/研究发布（行业报告、白皮书）
- 参与行业标准制定（AI识别为权威背书）

### Strategy 2: Brand Schema 全面部署

**核心Schema类型：**
```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "Brand Name",
  "url": "https://brand.com",
  "logo": "https://brand.com/logo.png",
  "sameAs": [
    "https://twitter.com/brand",
    "https://linkedin.com/company/brand",
    "https://youtube.com/c/brand"
  ],
  "contactPoint": {
    "@type": "ContactPoint",
    "contactType": "customer service",
    "email": "support@brand.com"
  }
}
```

**额外部署：**
- `SpeakableSpecification` Schema：标注品牌官网/新闻稿中AI可引用的部分
- `NewsArticle` Schema：品牌新闻稿结构化
- `FAQPage` Schema：品牌常见问题（AI常引用FAQ作为直接回答）

### Strategy 3: 品牌提及生态系统建设

**为什么重要：**
AI不仅索引你官网的内容——它分析整个网络上与品牌相关的提及。社会证明信号越强，AI越信任该品牌。

**策略：**
1. 第三方新闻稿发布（PR Wire, Business Wire）
2. 行业媒体报道（HARO, Connectively 回应）
3. 社交媒体活跃度（LinkedIn文章、Twitter讨论）
4. 播客/视频采访（增加多媒体权威信号）
5. Wikipedia/ Wikidata 品牌词条建立和维护

### Strategy 4: 问答内容矩阵——占领"什么是X品牌"类查询

**核心方法：**
创建清晰的品牌故事内容，AI在回答"XX品牌怎么样"类问题时可直接引用。

**内容类型：**
- "XX品牌评测"（第三方视角，AI认为客观）
- "XX品牌 vs YY品牌"对比（AI引用作为中立对比来源）
- "2026年XX品牌完整指南"（信息聚合页，AI优先引用）
- 品牌官方FAQ页面（SpeakableSpecification标注）

### Strategy 5: 知识图谱认领与优化

**Google 知识图谱：**
认领品牌Knowledge Panel，确保信息准确、完整：
- 官方logo、高清图片
- 官方社交媒体链接
- 品牌描述（200字以内，含核心关键词）
- 创始人/CEO信息
- 重要里程碑（融资/收购/发布产品）

**Bing 知识图谱：**
Bing的AI（Copilot）部分依赖Bing Knowledge Graph，品牌信息同等重要。

### Strategy 6: 品牌外链质量优先

**高质量外链类型（AI识别为权威信号）：**
- `.edu`、`.gov` 域名引用
- 行业权威媒体（福布斯、TechCrunch、WSJ等）
- 维基百科/Wikidata 条目
- 行业协会成员页面
- 学术论文引用

**避免：**
- PBN（Private Blog Networks）—— AI可识别
- 大量低质量目录提交
- 购买链接（违反Google指南）

### Strategy 7: 监控与迭代——AI引用跟踪

**监控工具：**
1. Google Alert：品牌词 + "as mentioned in" + "according to"
2. Bing Webmaster Tools：AI引用监控（部分功能）
3. Brandwatch/Mention：社交媒体和全网品牌提及
4. Semrush/Ahrefs：品牌外链增长跟踪

**迭代策略：**
- 月度审查：AI响应中品牌出现频率变化
- 内容补充：AI引用了竞品？分析原因，针对性优化
- 新话题覆盖：AI出现新问题类型？快速创建回答内容

---

## Google vs Bing 品牌权威对比

| 维度 | Google | Bing (Copilot) |
|------|--------|----------------|
| 品牌信息主要来源 | 知识图谱 + 网页内容 | 知识图谱 + Bing搜索数据 |
| 社会证明权重 | 高（第三方引用） | 极高（社交媒体直接索引） |
| 视频内容权重 | 高（YouTube整合） | 中（视频内容分析能力弱于Google） |
| 新闻稿影响 | 中 | 高（Bing News整合更深） |
| 本地品牌权重 | 高（Google Maps整合） | 中 |

---

## 30天实施路线图

### Week 1: 审计与基础
- [ ] 审计品牌当前 Knowledge Panel 完整度
- [ ] 检查 Brand Schema 部署情况（结构化数据测试工具）
- [ ] 搜索"品牌名+怎么样/好吗/评测"，分析AI当前引用内容

### Week 2: 内容与Schema
- [ ] 补充/优化品牌官方FAQ页面，添加FAQPage Schema
- [ ] 发布1篇"XX品牌评测/对比"第三方视角文章
- [ ] 为品牌新闻稿添加NewsArticle Schema

### Week 3: 提及与外链
- [ ] 提交品牌到3个行业目录/数据库
- [ ] 联系1-2个HARO/Connectively机会
- [ ] 审核现有外链质量，清理垃圾外链

### Week 4: 监控与迭代
- [ ] 设置品牌AI引用监控（Google Alert + Brandwatch）
- [ ] 分析竞品在AI引用中的出现频率，对比自身
- [ ] 制定下一月度品牌E-E-A-T提升计划

---

## 行动建议

### 立即执行（本周）
1. 用结构化数据测试工具检查 Brand Schema 是否完整
2. 搜索"品牌名怎么样"，记录AI引用了哪些内容
3. 认领/更新 Google Knowledge Panel

### 短期（30天）
1. 建立品牌FAQ矩阵（5-10个核心问题）
2. 发布1篇第三方评测/对比内容
3. 提交品牌到3个高质量目录

### 中期（90天）
1. 建立品牌外链获取策略（行业媒体、播客）
2. 监控AI引用频率变化，迭代内容策略
3. 探索品牌在AI搜索中的问答内容覆盖

---

## 关联主题

- topic153（视频SEO）— 视频是最强Experience信号，也是品牌E-E-A-T核心
- topic152（AI内容真实性）— 品牌内容也需要真实性信号
- topic151（GEO）— 被AI引用是品牌权威的最终体现
- topic150（Agentic SEO）— AI工作流中的品牌信息处理
