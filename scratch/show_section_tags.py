with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re

sections = ['hero', 'universe', 'gallery', 'scrapbook', 'mosaic', 'secret', 'letter-section', 'final-scene']

for s in sections:
    m = re.search(rf'(<section[^>]*id=["\']{s}["\'][^>]*>)', text)
    if m:
        start_idx = m.start()
        print(f"--- {s} ---")
        print(text[start_idx:start_idx+180])
        print()
