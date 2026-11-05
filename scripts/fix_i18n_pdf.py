import sys
sys.stdout.reconfigure(encoding='utf-8')

path = r'c:\Users\abduu\Desktop\Tawazon\frontend\js\i18n.js'
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

# Fix Arabic btn_export_pdf
text = text.replace('btn_export_pdf:       "📄 طباعة / حفظ كتقرير PDF",', 'btn_export_pdf:       "طباعة تقرير PDF",')
text = text.replace('btn_export_pdf:       "Export / Print PDF Report",', 'btn_export_pdf:       "Print PDF Report",')

with open(path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated i18n.js successfully!")
