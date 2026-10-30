import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

boundaries = ['hero', 'universe', 'gallery', 'scrapbook', 'mosaic', 'secret', 'letter-section', 'final-scene']

for i, line in enumerate(lines):
    for b in boundaries:
        if f'id="{b}"' in line or f"id='{b}'" in line:
            print(f"Line {i+1} starts #{b}")
            for k in range(max(0, i-3), i):
                print(f"  prev: {lines[k].strip()}")
