#!/bin/bash
set -e
cd /Users/clawbot/projects/ai-money-projects/seo-freelancer

echo "=== Step 6: Git push MD files ==="
git add portfolio/en/topic254-GEO-engine-2026.md portfolio/cn/topic254-GEO-engine-2026-cn.md
git commit -m "Round 213 prep: Topic 254 GEO Engine md files (en + cn)"
git push
echo "MD files pushed"

echo "=== Step 7: Run convert.py ==="
cd portfolio
python3 convert.py
echo "convert.py done"

echo "=== Verify HTML files created ==="
ls -la en/topic254-GEO-engine-2026.html cn/topic254-GEO-engine-2026-cn.html 2>/dev/null || echo "HTML files check"

echo "=== Check back link in HTML ==="
grep -o 'href="[^"]*index\.html"' en/topic254-GEO-engine-2026.html | head -3
grep -o 'href="[^"]*index\.html"' cn/topic254-GEO-engine-2026-cn.html | head -3

echo "=== Step 8: Update index.html ==="
# Add topic254 to top of article list in index.html
# First backup
cp index.html index.html.bak

# Create temp script for sed
cat > /tmp/update_index.sed << 'SEDEOF'
/<li class="article-item">/{ h; n; /topic253/{ p; x; }
}
SEDEOF

# Use awk to insert topic254 entry before topic253
awk '
/topic253-ai-search-ui-wars-2026.html/ && !added {
  print "            <li class=\"article-item\">"
  print "                <div class=\"article-title\">"
  print "                    <a href=\"en/topic254-GEO-engine-2026.html\">🎯 The GEO Engine: How Generative AI Selects, Weights, and Rewards Content (EN)</a>"
  print "                    <a href=\"cn/topic254-GEO-engine-2026-cn.html\">🎯 GEO引擎：生成式AI如何选择、权重和奖励内容 (CN)</a>"
  print "                </div>"
  print "                <div class=\"article-meta\">"
  print "                    <span class=\"lang-badge lang-en\">English</span> <span class=\"lang-badge lang-cn\">中文</span> New: 2026-04-01</div>"
  print "            </li>"
  added=1
}
{ print }
' index.html > index.html.new && mv index.html.new index.html
echo "index.html updated"

echo "=== Update article count in meta description ==="
# Update 247 to 249 (adding 2 articles)
sed -i '' 's/247篇/249篇/g' index.html
sed -i '' 's/245篇/247篇/g' index.html
echo "Article counts updated"

echo "=== Step 9: Second Git push ==="
cd /Users/clawbot/projects/ai-money-projects/seo-freelancer
git add -A
git commit -m "Round 213: Publish Topic 254 GEO Engine articles (en + cn) + index.html update"
git push
echo "Second push done"

echo "=== Step 10: Verify HTTP 200 ==="
sleep 5
curl -s -o /dev/null -w "EN: %{http_code}\n" "https://zailongagentmain-cyber.github.io/seo-freelancer/portfolio/en/topic254-GEO-engine-2026.html"
curl -s -o /dev/null -w "CN: %{http_code}\n" "https://zailongagentmain-cyber.github.io/seo-freelancer/portfolio/cn/topic254-GEO-engine-2026-cn.html"

echo "=== ALL DONE ==="
