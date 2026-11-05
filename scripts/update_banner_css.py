import sys
sys.stdout.reconfigure(encoding='utf-8')

path_css = r'c:\Users\abduu\Desktop\Tawazon\frontend\css\style.css'
with open(path_css, 'r', encoding='utf-8') as f:
    css = f.read()

import re

# Find the block from .exec-header-banner to .kpi-row
old_pattern = r'\.exec-header-banner\s*\{[\s\S]*?\.kpi-row\s*\{'

new_banner_css = """.exec-header-banner {
  background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
  border-radius: var(--radius);
  padding: 1.2rem 1.6rem;
  color: #fff;
  margin-bottom: 1.75rem;
  box-shadow: 0 8px 24px rgba(15,23,42,.15);
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 1rem;
  border: 1px solid rgba(255,255,255,.08);
}
.exec-banner-left {
  display: flex;
  flex-direction: column;
}
.exec-header-banner h1 {
  font-size: 1.45rem;
  font-weight: 800;
  letter-spacing: -.02em;
  margin-top: .3rem;
  line-height: 1.25;
}
.exec-header-banner p {
  color: #94a3b8;
  font-size: .84rem;
  margin-top: .15rem;
}

/* ── Exec Banner Actions & Badges ── */
.exec-ai-badge {
  display: inline-flex;
  align-items: center;
  gap: .3rem;
  background: rgba(59,130,246,0.18);
  border: 1px solid rgba(59,130,246,0.38);
  color: #60a5fa;
  font-size: .72rem;
  font-weight: 800;
  padding: .18rem .7rem;
  border-radius: 999px;
  letter-spacing: .02em;
  width: fit-content;
}
.exec-banner-actions {
  display: inline-flex;
  align-items: center;
  gap: .55rem;
  flex-wrap: wrap;
}
.exec-date-badge {
  font-size: .75rem;
  color: #94a3b8;
  background: rgba(255,255,255,0.06);
  padding: .35rem .75rem;
  border-radius: 8px;
  border: 1px solid rgba(255,255,255,0.10);
  white-space: nowrap;
  font-weight: 600;
  display: inline-flex;
  align-items: center;
}
.exec-btn-pdf {
  background: rgba(255,255,255,0.08);
  border: 1px solid rgba(255,255,255,0.18);
  color: #e2e8f0;
  padding: .35rem .85rem;
  border-radius: 8px;
  font-size: .78rem;
  font-weight: 700;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  gap: .35rem;
  transition: var(--btn-transition);
  white-space: nowrap;
  font-family: inherit;
}
.exec-btn-pdf:hover {
  background: rgba(255,255,255,0.18);
  color: #fff;
  border-color: rgba(255,255,255,0.35);
  transform: translateY(-1px);
}
.exec-btn-emp {
  background: linear-gradient(135deg, #2563eb 0%, #1d4ed8 100%);
  color: #fff;
  border: 1px solid transparent;
  padding: .35rem .95rem;
  border-radius: 8px;
  font-size: .78rem;
  font-weight: 700;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  gap: .35rem;
  transition: var(--btn-transition);
  white-space: nowrap;
  text-decoration: none;
  font-family: inherit;
  box-shadow: 0 2px 8px rgba(37,99,235,0.22);
}
.exec-btn-emp:hover {
  background: linear-gradient(135deg, #1d4ed8 0%, #1e40af 100%);
  transform: translateY(-1px);
  box-shadow: 0 4px 14px rgba(37,99,235,.35);
  color: #fff;
  text-decoration: none;
}

.kpi-row {"""

match = re.search(old_pattern, css)
if match:
    css = css[:match.start()] + new_banner_css + css[match.end():]
    with open(path_css, 'w', encoding='utf-8') as f:
        f.write(css)
    print("style.css updated successfully!")
else:
    print("Pattern not matched!")
