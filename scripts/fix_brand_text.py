# -*- coding: utf-8 -*-
"""
fix_brand_text.py
=================
Fixes the bug where 'Tawa' became transparent/invisible in Chromium.
Explicitly styles:
- 'Tawa' in crisp Logo Green (#22c55e)
- 'zon'  in crisp Logo Wave Blue (#0ea5e9)
Ensures 100% visibility and flawless display in both RTL and LTR across all browsers.
"""

import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FRONTEND_DIR = os.path.join(ROOT, "frontend")

# 1. Update style.css
css_path = os.path.join(FRONTEND_DIR, "css", "style.css")
with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

# Replace the entire nav-brand CSS block
nav_css_regex = re.compile(
    r'\.nav-brand\s*\{[^}]*\}.*?\.brand-logo-img:hover[^}]*\}',
    re.DOTALL
)

clean_nav_css = """.nav-brand {
  font-size: 1.35rem;
  font-weight: 800;
  text-decoration: none;
  display: inline-flex;
  align-items: center;
  gap: .55rem;
  white-space: nowrap;
  direction: ltr !important; /* Force brand to read Logo + Tawa + zon */
  line-height: 1;
  background: none !important;
  -webkit-text-fill-color: initial !important;
  color: #22c55e !important;
}

.brand-tawa {
  color: #22c55e !important; /* Vibrant Logo Green */
  -webkit-text-fill-color: #22c55e !important;
  font-weight: 800;
}

.brand-zon {
  color: #0ea5e9 !important; /* Logo Wave Blue */
  -webkit-text-fill-color: #0ea5e9 !important;
  font-weight: 800;
}

.nav-brand span.brand-role {
  font-size: 0.78rem;
  font-weight: 600;
  color: #94a3b8 !important;
  -webkit-text-fill-color: #94a3b8 !important;
  background: rgba(255, 255, 255, 0.08);
  border: 1px solid rgba(255, 255, 255, 0.15);
  padding: 0.15rem 0.5rem;
  border-radius: 6px;
  margin-left: 0.25rem;
}

.brand-logo-img {
  width: 44px;
  height: 44px;
  object-fit: contain;
  /* Completely frameless: no box, no border, no background */
  border: none !important;
  border-radius: 0 !important;
  background: transparent !important;
  box-shadow: none !important;
  filter: drop-shadow(0 2px 8px rgba(34, 197, 94, 0.5)) drop-shadow(0 2px 5px rgba(14, 165, 233, 0.4));
  transition: transform 0.25s ease, filter 0.25s ease;
  flex-shrink: 0;
}

.nav-brand:hover .brand-logo-img {
  transform: scale(1.12) rotate(4deg);
  filter: drop-shadow(0 4px 14px rgba(34, 197, 94, 0.75)) drop-shadow(0 3px 8px rgba(14, 165, 233, 0.65));
}"""

if nav_css_regex.search(css):
    css = nav_css_regex.sub(clean_nav_css, css)
else:
    # Alternative match
    css = re.sub(r'\.nav-brand\s*\{[^}]*\}.*?\.brand-logo-img\s*\{[^}]*\}', clean_nav_css, css, flags=re.DOTALL)

with open(css_path, "w", encoding="utf-8") as f:
    f.write(css)
print("[OK] style.css updated.")

# 2. Update all HTML files
html_files = [
    "index.html",
    "login.html",
    "assess.html",
    "employees.html",
    "employee-portal.html"
]

brand_pattern = re.compile(
    r'<a\s+href="([^"]+)"\s+class="nav-brand">\s*<img[^>]+>\s*Tawa<span>zon</span>(\s*\([^)]+\))?\s*</a>',
    re.DOTALL
)

for fname in html_files:
    fpath = os.path.join(FRONTEND_DIR, fname)
    if not os.path.exists(fpath):
        continue

    with open(fpath, "r", encoding="utf-8") as f:
        html = f.read()

    def repl(m):
        href = m.group(1)
        role = m.group(2)
        role_html = f' <span class="brand-role">{role.strip()}</span>' if role else ""
        return (
            f'<a href="{href}" class="nav-brand">'
            f'<img src="assets/logo.png" alt="Tawazon Logo" class="brand-logo-img" />'
            f'<span class="brand-tawa">Tawa</span><span class="brand-zon">zon</span>{role_html}</a>'
        )

    html = brand_pattern.sub(repl, html)

    # Special handling for login.html
    if fname == "login.html":
        # In the card header
        card_title_pattern = re.compile(r'<h1 class="auth-brand-title">.*?</h1>', re.DOTALL)
        new_card_title = '<h1 class="auth-brand-title"><span class="brand-tawa">Tawa</span><span class="brand-zon">zon</span></h1>'
        html = card_title_pattern.sub(new_card_title, html)

        # In login.html CSS
        login_css_title_pattern = re.compile(r'\.auth-brand-title\s*\{[^}]*\}(?:\s*\.auth-brand-title\s*span\s*\{[^}]*\})?', re.DOTALL)
        new_login_css_title = """.auth-brand-title {
      font-size: 2.5rem;
      font-weight: 800;
      letter-spacing: -0.03em;
      margin-bottom: 0.25rem;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      direction: ltr !important;
      line-height: 1.1;
    }
    .auth-brand-title .brand-tawa {
      color: #16a34a !important; /* Logo Green */
      font-weight: 800;
    }
    .auth-brand-title .brand-zon {
      color: #0284c7 !important; /* Logo Wave Blue */
      font-weight: 800;
    }"""
        html = login_css_title_pattern.sub(new_login_css_title, html)

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"[OK] {fname} updated.")

print("All brand text fixes completed.")
