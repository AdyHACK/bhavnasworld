with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re

sections = ['intro', 'hero', 'universe', 'gallery', 'scrapbook', 'mosaic', 'secret', 'letter-section', 'final-scene']

for s in sections:
    pattern = rf'(<section[^>]*id=["\']{s}["\'][^>]*>)(.*?)(</section>)'
    m = re.search(pattern, html, re.DOTALL)
    if m:
        first_part = m.group(2).strip()[:200].replace('\n', ' ')
        print(f"=== {s} ===")
        print(f"Opening: {m.group(1)}")
        print(f"Start content: {first_part}...")
        print()
