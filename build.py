#!/usr/bin/env python3
"""Build a portable static dictionary with all data embedded locally."""
from pathlib import Path
import json

root = Path(__file__).resolve().parent
data = json.loads((root / 'data.json').read_text())
assert len(data['families']) == 103
assert len(data['terms']) == 509
payload = json.dumps(data, ensure_ascii=False, separators=(',', ':')).replace('<', '\\u003c')
html = (root / 'template.html').read_text().replace('__DICTIONARY_DATA__', payload).replace('__STYLES__', (root / 'styles.css').read_text())
assert '__DICTIONARY_DATA__' not in html
(root / 'dist').mkdir(exist_ok=True)
(root / 'dist' / 'index.html').write_text(html)
(root / 'dist' / '.nojekyll').write_text('')
print(f"Built {len(data['families'])+len(data['terms'])} cards into dist/index.html ({len(html.encode())} bytes)")
