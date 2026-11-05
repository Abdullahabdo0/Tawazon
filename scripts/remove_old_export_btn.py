def run():
    p = 'frontend/css/style.css'
    with open(p, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Normalize to LF
    lines = [l.replace('\r\n', '\n') for l in lines]
    c = ''.join(lines)

    # Remove old btn-export-pdf block (lines 876-895 roughly)
    old_block = (
        '/* \u2500\u2500 Export / Print PDF Button \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500 */\n'
        '.btn-export-pdf {\n'
        '  display: inline-flex;\n'
        '  align-items: center;\n'
        '  gap: 0.5rem;\n'
        '  background: #f8fafc;\n'
        '  border: 1px solid #cbd5e1;\n'
        '  color: #334155;\n'
        '  padding: 0.55rem 1.1rem;\n'
        '  border-radius: 8px;\n'
        '  font-weight: 700;\n'
        '  font-size: 0.88rem;\n'
        '  cursor: pointer;\n'
        '  transition: all 0.2s ease;\n'
        '  margin-top: 1rem;\n'
        '}\n'
        '.btn-export-pdf:hover {\n'
        '  background: #e2e8f0;\n'
        '  color: #0f172a;\n'
        '}\n'
    )
    if old_block in c:
        c = c.replace(old_block, '/* btn-export-pdf \u2192 see TAWAZON DESIGN SYSTEM below */\n')
        print('Removed duplicate btn-export-pdf block')
    else:
        print('old btn-export-pdf block not found, skipping')

    with open(p, 'w', encoding='utf-8', newline='\r\n') as f:
        f.write(c)
    print('Done!')

if __name__ == '__main__':
    run()
