"""Check initial HTML of nav buttons in all 4 HTML files."""
import sys
import os
sys.stdout.reconfigure(encoding='utf-8')

files = [
    r'c:\Users\abduu\Desktop\Tawazon\frontend\employees.html',
    r'c:\Users\abduu\Desktop\Tawazon\frontend\index.html',
    r'c:\Users\abduu\Desktop\Tawazon\frontend\assess.html',
    r'c:\Users\abduu\Desktop\Tawazon\frontend\employee-portal.html',
]
for f in files:
    name = os.path.basename(f)
    with open(f, encoding='utf-8') as fh:
        for i, line in enumerate(fh, 1):
            if 'lang-btn' in line or 'btn-nav-logout' in line:
                print(f'{name} L{i}: {line.rstrip()}')
