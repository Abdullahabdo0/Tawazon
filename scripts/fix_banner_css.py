"""Add exec banner CSS classes after .exec-header-banner p block."""
import sys
sys.stdout.reconfigure(encoding='utf-8')

css_path = r'c:\Users\abduu\Desktop\Tawazon\frontend\css\style.css'
with open(css_path, encoding='utf-8') as f:
    content = f.read()

# Find insertion point - after .exec-header-banner p closing brace
# and before .kpi-row
marker = '.kpi-row {'

NEW_CSS = """.exec-header-banner h1 { font-size: 1.65rem; font-weight: 800; letter-spacing: -.02em; margin-top: .3rem; }
.exec-header-banner p { color: #94a3b8; font-size: .88rem; margin-top: .2rem; }

/* \u2500\u2500 Exec Banner Sub-components \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500 */
.exec-banner-left { display: flex; flex-direction: column; }
.exec-ai-badge {
  display: inline-block;
  background: rgba(59,130,246,0.18);
  border: 1px solid rgba(59,130,246,0.38);
  color: #60a5fa;
  font-size: .72rem;
  font-weight: 800;
  padding: .18rem .7rem;
  border-radius: 999px;
  letter-spacing: .03em;
  width: fit-content;
}
.exec-banner-actions { display: flex; align-items: center; gap: .6rem; flex-wrap: wrap; }
.exec-date-badge {
  font-size: .75rem; color: #94a3b8;
  background: rgba(255,255,255,0.07);
  padding: .3rem .8rem; border-radius: 7px;
  border: 1px solid rgba(255,255,255,0.10);
  white-space: nowrap; font-weight: 600;
}
.exec-btn-pdf {
  background: rgba(255,255,255,0.09);
  border: 1px solid rgba(255,255,255,0.18);
  color: #cbd5e1; padding: .3rem .8rem;
  border-radius: 7px; font-size: .75rem; font-weight: 700;
  cursor: pointer; display: inline-flex; align-items: center;
  gap: .32rem; transition: var(--btn-transition); white-space: nowrap;
  font-family: 'Cairo', sans-serif;
}
.exec-btn-pdf:hover { background: rgba(255,255,255,0.18); color: #fff; border-color: rgba(255,255,255,0.35); transform: translateY(-1px); }
.exec-btn-emp {
  background: linear-gradient(135deg, #2563eb 0%, #1d4ed8 100%);
  color: #fff; border: none; padding: .32rem .95rem;
  border-radius: 7px; font-size: .75rem; font-weight: 700;
  cursor: pointer; display: inline-flex; align-items: center;
  gap: .32rem; transition: var(--btn-transition); white-space: nowrap;
  text-decoration: none; font-family: 'Cairo', sans-serif;
}
.exec-btn-emp:hover {
  background: linear-gradient(135deg, #1d4ed8 0%, #1e40af 100%);
  transform: translateY(-1px);
  box-shadow: 0 4px 14px rgba(37,99,235,.35);
  color: #fff; text-decoration: none;
}

"""

# Remove old exec-header-banner h1 and p rules (they're being replaced inline above)
import re
# Remove the old separate rules for h1 and p
content = re.sub(
    r'\.exec-header-banner h1 \{[^}]+\}\s*\.exec-header-banner p \{[^}]+\}\s*',
    '',
    content
)

# Insert new CSS before .kpi-row
if marker in content:
    content = content.replace(marker, NEW_CSS + marker)
    print("CSS inserted successfully!")
else:
    print("ERROR: .kpi-row not found!")

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Done!")
