with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re

for s in ['hero', 'universe', 'gallery', 'scrapbook', 'mosaic', 'secret', 'letter-section']:
    pattern = rf'(</section>\s*(?:<!--[^\n]*-->\s*)*<section[^>]*id=["\'](?:universe|gallery|scrapbook|mosaic|secret|letter-section|final-scene)["\'])'
    m = re.search(pattern, text)
    if m:
        print(f"Matched transition around {s}")
        print(m.group(1)[:120])
        print("...")
