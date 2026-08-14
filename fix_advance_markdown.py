from pathlib import Path
import re

root = Path('docs/STEMAIDE_AIDER_Kit_Manual/advance')
files = list(root.rglob('*.md'))

header = '| Component | Connection | Pin / reference | Notes |\n| --- | --- | --- | --- |'

for path in files:
    text = path.read_text(encoding='utf-8')
    original = text

    # Normalize circuit connection tables
    text = text.replace('|---------------|-------------|---------------------------------|-------|', header)

    # Replace outdated component asset paths with the live docs asset path
    text = text.replace('../../docs/ASSETS/COMPONENTS/', '../../../assets/aider/components/')
    text = text.replace('../../../docs/ASSETS/COMPONENTS/', '../../../assets/aider/components/')
    text = text.replace('../../../../docs/ASSETS/COMPONENTS/', '../../../assets/aider/components/')
    text = text.replace('../../../../assets/aider/components/', '../../../assets/aider/components/')
    text = text.replace('../../../../docs/assets/aider/components/', '../../../assets/aider/components/')
    text = text.replace('../../docs/assets/aider/components/', '../../../assets/aider/components/')
    text = text.replace('../../../docs/assets/aider/components/', '../../../assets/aider/components/')

    # Fix any remaining broken relative links that still point to the old docs layout
    text = re.sub(r'\]\((?:\.\./)+docs/ASSETS/COMPONENTS/([^\)]+)\)', r'](../../../assets/aider/components/\1)', text)
    text = re.sub(r'\]\((?:\.\./)+docs/assets/aider/components/([^\)]+)\)', r'](../../../assets/aider/components/\1)', text)

    if text != original:
        path.write_text(text, encoding='utf-8')

print(f'Updated {len(files)} markdown files')
