import re

with open(r'c:\Users\abduu\Desktop\Tawazon\scripts\build_ml_deck.py', encoding='utf-8') as f:
    code = f.read()

print('Length:', len(code))
fonts = set(re.findall(r'font\.name\s*=\s*[\'"]([^\'"]+)[\'"]', code))
print('Fonts used:', fonts)

# Look at slide generation functions
slides = re.findall(r'def\s+(slide_\w+)', code)
print('Slides:', slides)
