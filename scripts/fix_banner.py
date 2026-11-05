"""
Fix exec-header-banner in index.html:
- Make buttons smaller and more compact
- Better organized layout
- Remove inline styles and use cleaner markup
"""
import sys
sys.stdout.reconfigure(encoding='utf-8')

path = r'c:\Users\abduu\Desktop\Tawazon\frontend\index.html'
with open(path, encoding='utf-8') as f:
    content = f.read()

OLD_BANNER = """  <!-- Executive Banner -->
  <div class="exec-header-banner">
    <div>
      <div style="display:inline-block; background:rgba(59,130,246,0.2); border:1px solid rgba(59,130,246,0.4); color:#60a5fa; font-size:.78rem; font-weight:800; padding:.2rem .75rem; border-radius:999px; margin-bottom:.5rem;">
        ⚡ Tawazon AI Intelligence Core
      </div>
      <h1 data-i18n="dash_title">Executive Analytics Dashboard</h1>
      <p data-i18n="dash_subtitle">Live enterprise workload intelligence & predictive burnout monitoring</p>
    </div>
    <div style="display:flex; align-items:center; gap:.75rem; flex-wrap:wrap;">
      <div style="font-size:.85rem; color:#94a3b8; background:rgba(255,255,255,0.06); padding:.5rem 1rem; border-radius:8px; border:1px solid rgba(255,255,255,0.1);" id="liveDateBadge">
        📅 Live
      </div>
      <button class="btn-export-pdf" style="margin-top:0; background:rgba(255,255,255,0.1); border-color:rgba(255,255,255,0.2); color:#fff;" onclick="window.print()">
        📄 <span data-i18n="btn_export_pdf">Export / Print PDF</span>
      </button>
      <a href="employees.html" class="btn-primary" style="box-shadow:none;">
        <span>👥</span>
        <span data-i18n="nav_employees">Manage Workforce</span>
      </a>
    </div>
  </div>"""

NEW_BANNER = """  <!-- Executive Banner -->
  <div class="exec-header-banner">
    <div class="exec-banner-left">
      <div class="exec-ai-badge">⚡ Tawazon AI Intelligence Core</div>
      <h1 data-i18n="dash_title">Executive Analytics Dashboard</h1>
      <p data-i18n="dash_subtitle">Live enterprise workload intelligence &amp; predictive burnout monitoring</p>
    </div>
    <div class="exec-banner-actions">
      <div class="exec-date-badge" id="liveDateBadge">📅 Live</div>
      <button class="exec-btn-pdf" onclick="window.print()">
        📄 <span data-i18n="btn_export_pdf">Print PDF</span>
      </button>
      <a href="employees.html" class="exec-btn-emp">
        👥 <span data-i18n="nav_employees">Employees</span>
      </a>
    </div>
  </div>"""

if OLD_BANNER in content:
    content = content.replace(OLD_BANNER, NEW_BANNER)
    print("Banner replaced successfully!")
else:
    print("ERROR: Banner not found - checking partial match...")
    if 'exec-header-banner' in content:
        print("exec-header-banner class exists in file")
    # Try a more targeted approach - just fix the action buttons div
    

with open(path, encoding='utf-8') as f:
    check = f.read()
    
if OLD_BANNER not in check and NEW_BANNER in content:
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("File written!")
elif OLD_BANNER not in content:
    print("SKIPPED - old content not found, need manual check")
