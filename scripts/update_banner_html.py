import sys
sys.stdout.reconfigure(encoding='utf-8')

# Update index.html
path_html = r'c:\Users\abduu\Desktop\Tawazon\frontend\index.html'
with open(path_html, 'r', encoding='utf-8') as f:
    html = f.read()

old_block = """  <!-- Executive Banner -->
  <div class="exec-header-banner">
    <div>
      <div style="display:inline-block; background:rgba(59,130,246,0.2); border:1px solid rgba(59,130,246,0.4); color:#60a5fa; font-size:.78rem; font-weight:800; padding:.2rem .75rem; border-radius:999px; margin-bottom:.5rem;">
        ⚡ Tawazon AI Intelligence Core
      </div>
      <h1 data-i18n="dash_title">Executive Analytics Dashboard</h1>
      <p data-i18n="dash_subtitle">Live enterprise workload intelligence & predictive burnout monitoring</p>
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

new_block = """  <!-- Executive Banner -->
  <div class="exec-header-banner">
    <div class="exec-banner-left">
      <div class="exec-ai-badge">⚡ Tawazon AI Intelligence Core</div>
      <h1 data-i18n="dash_title">Executive Analytics Dashboard</h1>
      <p data-i18n="dash_subtitle">Live enterprise workload intelligence & predictive burnout monitoring</p>
    </div>
    <div class="exec-banner-actions">
      <div class="exec-date-badge" id="liveDateBadge">📅 Live</div>
      <button class="exec-btn-pdf" onclick="window.print()">
        <span>📄</span> <span data-i18n="btn_export_pdf">Print PDF</span>
      </button>
      <a href="employees.html" class="exec-btn-emp">
        <span>👥</span> <span data-i18n="nav_employees">Employees</span>
      </a>
    </div>
  </div>"""

if old_block in html:
    html = html.replace(old_block, new_block)
    with open(path_html, 'w', encoding='utf-8') as f:
        f.write(html)
    print("index.html updated successfully!")
else:
    print("WARNING: old_block not found in index.html exactly, checking alternatives...")

