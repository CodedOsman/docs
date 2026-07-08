from pathlib import Path
import re

root = Path(r'c:\Users\Bruker\docs\docs\STEMAIDE_AIDER_Kit_Manual\beginner\1.2 Basic Projects')
count = 0
for path in root.glob('*.md'):
    text = path.read_text(encoding='utf-8')
    if text.lstrip().startswith('# Project '):
        continue

    m = re.match(r'^(\d+(?:\.\d+)*)', path.stem)
    if not m:
        continue

    prefix = m.group(1)
    lines = text.splitlines()
    if not lines or not lines[0].startswith('# '):
        continue

    title = lines[0][2:].strip()
    new_lines = [f'# Project {prefix}', f'## {title}']

    if len(lines) > 1 and lines[1].strip() == '':
        rest = lines[2:]
    else:
        rest = lines[1:]

    new_text = '\n'.join(new_lines + rest)
    if text.endswith('\n'):
        new_text += '\n'

    if new_text != text:
        path.write_text(new_text, encoding='utf-8', newline='\n')
        count += 1

print(f'Updated files: {count}')
