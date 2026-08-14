from pathlib import Path
import re

root = Path(r'c:\Users\Stemaide\docs\docs\STEMAIDE_AIDER_Kit_Manual\advance')

for path in root.rglob('*.md'):
    text = path.read_text(encoding='utf-8')
    original = text

    text = re.sub(r'(?:\.\./)+docs/ASSETS/COMPONENTS/', '../../../assets/aider/components/', text)
    text = re.sub(r'(?:\.\./)+ASSETS/COMPONENTS/', '../../../assets/aider/components/', text)
    text = text.replace('docs/ASSETS/COMPONENTS/', '../../../assets/aider/components/')

    if '## Circuit Connections' in text:
        m = re.search(r'(## Circuit Connections\s*\n\n)(.*?)(\n---\n\n## )', text, flags=re.S)
        if m:
            block = m.group(2)
            block = re.sub(r'^\|[-\s|:]+\|$', '| --- | --- | --- | --- |', block, flags=re.M)
            text = text[:m.start(2)] + block + text[m.end(2):]

    if text != original:
        path.write_text(text, encoding='utf-8')
