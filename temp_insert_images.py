from pathlib import Path
import re

root = Path(r'C:\Users\hp 830 g5\docs\docs')
expert_dir = root / 'STEMAIDE_CODER_PRO_Kit_Manual' / 'expert' / 'expert_II'
asset_root = root / 'assets' / 'project-files' / 'expert'

files = sorted(expert_dir.glob('4.2.*.md'))
updated = []
for md in files:
    text = md.read_text(encoding='utf-8')
    if 'assets/project-files/expert' in text:
        continue
    folder = md.stem
    sec_start = '## Mounting the component on the breadboard and wiring the circuit'
    sec_end = '## PROGRAMMING'
    start = text.find(sec_start)
    if start == -1:
        continue
    end = text.find(sec_end, start)
    if end == -1:
        end = len(text)
    section = text[start:end]

    def repl(match):
        step_no = int(match.group(2))
        return match.group(1) + f'\n\n![power connection](../../../assets/project-files/expert/{folder}/circuit_{step_no}.png)\n'

    new_section = re.sub(r'(\*\*Step (\d+):\*\*.*?)(?=\n\*\*Step \d+:\*\*|\n## PROGRAMMING|\Z)', repl, section, flags=re.S)
    if new_section != section:
        text = text[:start] + new_section + text[end:]
        md.write_text(text, encoding='utf-8')
        updated.append(md.name)

print('\n'.join(updated) if updated else 'No files updated.')
