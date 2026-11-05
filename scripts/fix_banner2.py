"""
Fix exec-header-banner actions in index.html using line-by-line replacement.
Replace the 3 action elements (date badge, PDF btn, emp btn) with compact versions.
"""
import sys
sys.stdout.reconfigure(encoding='utf-8')

path = r'c:\Users\abduu\Desktop\Tawazon\frontend\index.html'
with open(path, encoding='utf-8') as f:
    lines = f.readlines()

# Find range: line with "display:flex; align-items:center; gap:.75rem" to "</div>" after employees link
start_line = None
end_line = None
for i, line in enumerate(lines):
    if 'display:flex; align-items:center; gap:.75rem; flex-wrap:wrap;' in line and start_line is None:
        start_line = i
    if start_line is not None and i > start_line and line.strip() == '</div>' and end_line is None:
        # Check if the closing div is at proper indent (4 spaces)
        if line.startswith('    </div>'):
            end_line = i
            break

print(f"start_line={start_line}, end_line={end_line}")
if start_line is None or end_line is None:
    print("ERROR: Could not find target range")
    exit(1)

print("Lines to replace:")
for i in range(start_line, end_line+1):
    print(f"  L{i+1}: {lines[i].rstrip()}")

NEW_SECTION = """    <div class="exec-banner-actions">
      <div class="exec-date-badge" id="liveDateBadge">\U0001f4c5 Live</div>
      <button class="exec-btn-pdf" onclick="window.print()">
        \U0001f4c4 <span data-i18n="btn_export_pdf">Print PDF</span>
      </button>
      <a href="employees.html" class="exec-btn-emp">
        \U0001f465 <span data-i18n="nav_employees">Employees</span>
      </a>
    </div>
"""

lines[start_line:end_line+1] = [NEW_SECTION]

with open(path, 'w', encoding='utf-8') as f:
    f.writelines(lines)

print(f"\nReplaced lines {start_line+1}-{end_line+1} with compact banner actions.")
print("Done!")
