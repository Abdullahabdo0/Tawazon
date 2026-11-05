"""Fix nav buttons - remove duplicate data-i18n from logout span
so applyLanguage() in i18n.js is the sole controller of nav button text."""
import os

files = [
    r'c:\Users\abduu\Desktop\Tawazon\frontend\employees.html',
    r'c:\Users\abduu\Desktop\Tawazon\frontend\index.html',
    r'c:\Users\abduu\Desktop\Tawazon\frontend\assess.html',
    r'c:\Users\abduu\Desktop\Tawazon\frontend\employee-portal.html',
]

for f in files:
    with open(f, 'r', encoding='utf-8') as fh:
        content = fh.read()

    # Remove data-i18n="nav_logout" attribute from the span inside btn-nav-logout
    # so applyLanguage() doesn't get overridden by the generic [data-i18n] loop
    content = content.replace(' data-i18n="nav_logout"', '')

    with open(f, 'w', encoding='utf-8') as fh:
        fh.write(content)
    print(f'Fixed: {os.path.basename(f)}')

print('Done!')
