import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

with open('src/styles/backgrounds.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Check for unclosed tags or syntax issues
import re
print("Checking section-bg elements in index.html:")
bg_elements = re.findall(r'class=["\']([^"\']*section-bg[^"\']*)["\']', html)
for b in bg_elements:
    print(f"  [FOUND] {b}")

print(f"\nTotal section-bg elements found: {len(bg_elements)}")

print("\nChecking transition dividers:")
dividers = re.findall(r'section-transition-divider', html)
print(f"Total dividers found: {len(dividers)}")

# Check CSS classes
classes_to_check = [
    'section-bg', 'section-bg--hero', 'section-bg--universe', 'section-bg--gallery',
    'section-bg--scrapbook', 'section-bg--mosaic', 'section-bg--secret', 'section-bg--letter',
    'section-bg--final', 'hero-sunbeam', 'hero-botanical-tl', 'hero-botanical-br',
    'hero-editorial-watermark', 'universe-armillary-svg', 'universe-chart-overlay',
    'gallery-arch-svg', 'gallery-french-rule-grid', 'scrapbook-herbarium-left',
    'scrapbook-herbarium-right', 'scrapbook-postal-mark', 'mosaic-architectural-svg',
    'secret-ambient-aura', 'secret-postal-chevrons', 'secret-seal-watermark-svg',
    'letter-stationery-crest-svg', 'letter-corner-flourish', 'letter-desk-light',
    'final-cinematic-halo', 'final-starlight-ring-svg', 'section-transition-divider',
    'transition-rule-line', 'transition-glyph'
]

print("\nChecking CSS classes presence in backgrounds.css:")
missing = []
for c in classes_to_check:
    if f".{c}" in css:
        print(f"  [OK] .{c}")
    else:
        print(f"  [MISSING] .{c}")
        missing.append(c)

if missing:
    print(f"\nWARNING: Missing classes: {missing}")
else:
    print("\nALL BACKGROUND CLASSES VERIFIED IN backgrounds.css!")
