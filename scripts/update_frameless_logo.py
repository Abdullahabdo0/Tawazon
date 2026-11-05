# -*- coding: utf-8 -*-
"""
update_frameless_logo.py
========================
Takes the logo completely out of any frame/box/border and makes it prominent.
Colors the word 'Tawazon' to match the brand logo palette (Green, Gold, Blue).
"""

import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FRONTEND_DIR = os.path.join(ROOT, "frontend")

# 1. Update login.html
login_path = os.path.join(FRONTEND_DIR, "login.html")
if os.path.exists(login_path):
    with open(login_path, "r", encoding="utf-8") as f:
        html = f.read()

    # Replace auth-brand-badge CSS
    css_badge_pattern = re.compile(r'\.auth-brand-badge\s*\{[^}]*\}', re.DOTALL)
    new_badge_css = """.auth-brand-badge {
      width: 125px;
      height: 125px;
      margin: 0 auto 1.15rem;
      background: transparent !important;
      border: none !important;
      box-shadow: none !important;
      padding: 0 !important;
      display: flex;
      align-items: center;
      justify-content: center;
      position: relative;
    }
    .auth-brand-badge img {
      width: 100%;
      height: 100%;
      object-fit: contain;
      filter: drop-shadow(0 8px 24px rgba(34, 197, 94, 0.4)) drop-shadow(0 4px 12px rgba(14, 165, 233, 0.35));
      transition: transform 0.3s ease;
    }
    .auth-brand-badge:hover img {
      transform: scale(1.08) rotate(3deg);
    }"""
    html = css_badge_pattern.sub(new_badge_css, html, count=1)

    # Replace auth-brand-title CSS
    css_title_pattern = re.compile(r'\.auth-brand-title\s*\{[^}]*\}(?:\s*\.auth-brand-title\s*span\s*\{[^}]*\})?', re.DOTALL)
    new_title_css = """.auth-brand-title {
      font-size: 2.5rem;
      font-weight: 800;
      letter-spacing: -0.03em;
      margin-bottom: 0.25rem;
      display: inline-block;
      background: linear-gradient(135deg, #16a34a 0%, #ca8a04 45%, #0284c7 95%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      background-clip: text;
      color: #16a34a;
    }
    .auth-brand-title span {
      background: linear-gradient(135deg, #ca8a04 15%, #0284c7 85%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      background-clip: text;
      color: #0284c7;
    }"""
    html = css_title_pattern.sub(new_title_css, html, count=1)

    # Clean the img tag in auth-brand-badge HTML
    html = re.sub(
        r'<div class="auth-brand-badge">\s*<img[^>]+>\s*</div>',
        '<div class="auth-brand-badge">\n        <img src="assets/logo.png" alt="Tawazon Logo" />\n      </div>',
        html
    )

    with open(login_path, "w", encoding="utf-8") as f:
        f.write(html)
    print("[OK] login.html updated.")

# 2. Update style.css
css_path = os.path.join(FRONTEND_DIR, "css", "style.css")
if os.path.exists(css_path):
    with open(css_path, "r", encoding="utf-8") as f:
        css = f.read()

    # Update .nav-brand and .brand-logo-img
    nav_pattern = re.compile(
        r'\.nav-brand\s*\{[^}]*\}.*?\.nav-brand\s*span\s*\{[^}]*\}',
        re.DOTALL
    )
    new_nav_css = """.nav-brand {
  font-size: 1.38rem;
  font-weight: 800;
  text-decoration: none;
  display: inline-flex;
  align-items: center;
  gap: .65rem;
  white-space: nowrap;
  direction: ltr;
  letter-spacing: -0.01em;
  /* Brand color matching logo: vibrant green fallback */
  color: #22c55e;
  transition: all 0.2s ease;
}

/* Match the exact 3 brand colors of the logo: Green -> Gold -> Wave Blue */
.nav-brand-text, .nav-brand strong {
  background: linear-gradient(135deg, #22c55e 0%, #eab308 50%, #0ea5e9 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  font-weight: 800;
}

.nav-brand {
  background: linear-gradient(135deg, #22c55e 0%, #eab308 50%, #0ea5e9 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.nav-brand span {
  background: linear-gradient(135deg, #eab308 10%, #38bdf8 90%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  color: #38bdf8;
}

.brand-logo-img {
  width: 46px;
  height: 46px;
  object-fit: contain;
  /* Completely out of the frame: no circle frame, no border, no background box */
  border-radius: 0 !important;
  border: none !important;
  background: transparent !important;
  box-shadow: none !important;
  filter: drop-shadow(0 3px 10px rgba(34, 197, 94, 0.45)) drop-shadow(0 2px 6px rgba(14, 165, 233, 0.35));
  transition: transform 0.25s ease, filter 0.25s ease;
  flex-shrink: 0;
}

.nav-brand:hover .brand-logo-img {
  transform: scale(1.15) rotate(4deg);
  filter: drop-shadow(0 5px 16px rgba(34, 197, 94, 0.7)) drop-shadow(0 3px 10px rgba(14, 165, 233, 0.6));
}"""

    css = nav_pattern.sub(new_nav_css, css, count=1)
    with open(css_path, "w", encoding="utf-8") as f:
        f.write(css)
    print("[OK] style.css updated.")

print("All updates applied successfully.")
