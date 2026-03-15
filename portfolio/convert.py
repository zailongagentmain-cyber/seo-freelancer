#!/usr/bin/env python3
"""Convert Markdown to HTML with template"""

import os
import re
import sys
from datetime import datetime

def md_to_html(md_content, title="Article"):
    """Convert basic Markdown to HTML"""
    
    # Simple markdown to html conversion
    html = md_content
    
    # Headers - Convert # to h2 instead of h1 to avoid duplicate H1
    html = re.sub(r'^#### (.+)$', r'<h4>\1</h4>', html, flags=re.MULTILINE)
    html = re.sub(r'^### (.+)$', r'<h3>\1</h3>', html, flags=re.MULTILINE)
    html = re.sub(r'^## (.+)$', r'<h2>\1</h2>', html, flags=re.MULTILINE)
    html = re.sub(r'^# (.+)$', r'<h2>\1</h2>', html, flags=re.MULTILINE)
    
    # Bold and Italic
    html = re.sub(r'\*\*\*(.+?)\*\*\*', r'<strong><em>\1</em></strong>', html)
    html = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', html)
    html = re.sub(r'\*(.+?)\*', r'<em>\1</em>', html)
    
    # Code blocks
    html = re.sub(r'```(\w+)?\n(.*?)```', r'<pre><code>\2</code></pre>', html, flags=re.DOTALL)
    html = re.sub(r'`(.+?)`', r'<code>\1</code>', html)
    
    # Links
    html = re.sub(r'\[(.+?)\]\((.+?)\)', r'<a href="\2">\1</a>', html)
    
    # Lists
    html = re.sub(r'^- (.+)$', r'<li>\1</li>', html, flags=re.MULTILINE)
    html = re.sub(r'(<li>.*</li>\n?)+', r'<ul>\g<0></ul>', html)
    
    # Paragraphs (lines that don't start with HTML tags)
    lines = html.split('\n')
    new_lines = []
    in_para = False
    for line in lines:
        stripped = line.strip()
        if stripped and not stripped.startswith(('<h', '<ul', '<ol', '<li', '<pre', '<block', '<p', '< ')):
            if not in_para:
                new_lines.append('<p>')
                in_para = True
            new_lines.append(stripped)
        else:
            if in_para:
                new_lines.append('</p>')
                in_para = False
            new_lines.append(line)
    if in_para:
        new_lines.append('</p>')
    html = '\n'.join(new_lines)
    
    # Blockquotes
    html = re.sub(r'^> (.+)$', r'<blockquote>\1</blockquote>', html, flags=re.MULTILINE)
    
    # Tables (| col | col | → <table><tr><td>)
    def convert_table(match):
        lines = match.group(0).strip().split('\n')
        if len(lines) < 2:
            return match.group(0)
        
        html_parts = ['<table>']
        for i, line in enumerate(lines):
            cells = [c.strip() for c in line.strip('|').split('|')]
            if i == 0:  # Header row
                html_parts.append('<thead><tr>')
                for cell in cells:
                    if cell:
                        html_parts.append(f'<th>{cell}</th>')
                html_parts.append('</tr></thead><tbody>')
            elif '---' in line:  # Skip separator
                continue
            else:  # Data row
                html_parts.append('<tr>')
                for cell in cells:
                    if cell:
                        html_parts.append(f'<td>{cell}</td>')
                html_parts.append('</tr>')
        html_parts.append('</tbody></table>')
        return '\n'.join(html_parts)
    
    html = re.sub(r'(\|.+\|\n)+', convert_table, html)
    
    # Horizontal rules
    html = re.sub(r'^---$', '<hr>', html, flags=re.MULTILINE)
    
    return html

def convert_file(md_path, template_path, output_path):
    """Convert a single markdown file to HTML"""
    
    # Read markdown
    with open(md_path, 'r', encoding='utf-8') as f:
        md_content = f.read()
    
    # Extract title from first heading
    title_match = re.search(r'^# (.+)$', md_content, re.MULTILINE)
    title = title_match.group(1) if title_match else os.path.basename(md_path)
    
    # Extract description from first paragraph (non-heading line, skip blockquote)
    lines = md_content.split('\n')
    description = ""
    for line in lines:
        line = line.strip()
        # Skip headings, blockquotes, code blocks, empty lines
        if line and not line.startswith('#') and not line.startswith('```') and not line.startswith('>') and not line.startswith('|') and not line.startswith('-') and len(line) > 20:
            # Clean markdown formatting and take first 160 chars
            desc = re.sub(r'[*_`\[\](){}]', '', line)
            description = desc[:160]
            break
    
    # Convert content
    content = md_to_html(md_content, title)
    
    # Read template
    with open(template_path, 'r', encoding='utf-8') as f:
        template = f.read()
    
    # Replace placeholders
    html = template.replace('{{title}}', title)
    html = html.replace('{{content}}', content)
    html = html.replace('{{date}}', datetime.now().strftime('%Y-%m-%d'))
    html = html.replace('{{description}}', description)
    
    # Write output
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"Converted: {md_path} -> {output_path}")

def main():
    portfolio_dir = os.path.dirname(os.path.abspath(__file__))
    template_path = os.path.join(portfolio_dir, 'template.html')
    
    # Convert files in en/ and cn/ directories
    for lang in ['en', 'cn']:
        lang_dir = os.path.join(portfolio_dir, lang)
        if not os.path.exists(lang_dir):
            continue
            
        for filename in os.listdir(lang_dir):
            if filename.endswith('.md'):
                md_path = os.path.join(lang_dir, filename)
                html_filename = filename.replace('.md', '.html')
                output_path = os.path.join(lang_dir, html_filename)
                
                try:
                    convert_file(md_path, template_path, output_path)
                except Exception as e:
                    print(f"Error converting {filename}: {e}")

if __name__ == '__main__':
    main()
