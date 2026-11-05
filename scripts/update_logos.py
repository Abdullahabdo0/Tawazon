# -*- coding: utf-8 -*-
"""
update_logos.py
===============
Updates all HTML files to replace generic emoji/icons with the new official Tawazon logo
and adds the favicon link.
"""

import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FRONTEND_DIR = os.path.join(ROOT, "frontend")

HTML_FILES = [
    "index.html",
    "login.html",
    "assess.html",
    "employees.html",
    "employee-portal.html",
]

for filename in HTML_FILES:
    filepath = os.path.join(FRONTEND_DIR, filename)
    if not os.path.exists(filepath):
        continue

    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Add favicon if not present
    if "assets/favicon.png" not in content and '<link rel="stylesheet"' in content:
        content = content.replace(
            '<link rel="stylesheet"',
            '<link rel="icon" type="image/png" href="assets/favicon.png" />\n  <link rel="stylesheet"',
            1
        )

    # 2. Update navbar brand
    # Match patterns like:
    # <a href="..." class="nav-brand">⚡ Tawa<span>zon</span> (Admin)</a>
    # <a href="..." class="nav-brand">⚡ Tawa<span>zon</span></a>
    content = re.sub(
        r'<a\s+href="([^"]+)"\s+class="nav-brand">\s*(?:⚡|\?|&#9889;)?\s*Tawa<span>zon</span>(\s*\([^)]+\))?\s*</a>',
        r'<a href="\1" class="nav-brand"><img src="assets/logo.png" alt="Tawazon Logo" class="brand-logo-img" /> Tawa<span>zon</span>\2</a>',
        content
    )

    # 3. Special handling for login.html
    if filename == "login.html":
        # Replace auth-brand-badge SVG icon with the new logo
        svg_badge_pattern = re.compile(
            r'<div class="auth-brand-badge">\s*<div class="auth-brand-icon">.*?</div>\s*</div>',
            re.DOTALL
        )
        new_logo_badge = (
            '<div class="auth-brand-badge">\n'
            '        <img src="assets/logo.png" alt="Tawazon Logo" '
            'style="width:100%; height:100%; object-fit:cover; border-radius:50%;" />\n'
            '      </div>'
        )
        content = svg_badge_pattern.sub(new_logo_badge, content)

        # Update CSS for .auth-brand-badge
        old_badge_css = """.auth-brand-badge {
      width: 62px;
      height: 62px;
      margin: 0 auto 1.25rem;
      border-radius: 18px;
      background: linear-gradient(145deg, #0ea5e9 0%, #2563eb 50%, #7c3aed 100%);
      color: #ffffff;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 30px;
      box-shadow: 0 10px 25px -5px rgba(37, 99, 235, 0.35), 0 4px 10px -3px rgba(124, 58, 237, 0.2);
      position: relative;
      overflow: hidden;
    }"""
        new_badge_css = """.auth-brand-badge {
      width: 78px;
      height: 78px;
      margin: 0 auto 1.25rem;
      border-radius: 50%;
      background: #ffffff;
      display: flex;
      align-items: center;
      justify-content: center;
      box-shadow: 0 10px 25px -5px rgba(16, 185, 129, 0.25), 0 4px 12px -2px rgba(15, 23, 42, 0.12);
      border: 2px solid #e2e8f0;
      padding: 3px;
      position: relative;
      overflow: hidden;
    }"""
        if old_badge_css in content:
            content = content.replace(old_badge_css, new_badge_css)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"[OK] Processed {filename}")

print("Logo update completed.")
