import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

divider = '''    <!-- Section Transition Divider -->
    <div class="section-transition-divider" aria-hidden="true">
      <div class="transition-rule-line"></div>
      <span class="transition-glyph">✦</span>
      <div class="transition-rule-line"></div>
    </div>\n\n'''

scenes = [
    '<!-- ══════════════════════════════════════════════════════════\n         SCENE 3 — INTERACTIVE UNIVERSE',
    '<!-- ══════════════════════════════════════════════════════════\n         SCENE 4 — GALLERY (Photography Exhibition)',
    '<!-- ══════════════════════════════════════════════════════════\n         SCENE 5 — DIGITAL SCRAPBOOK',
    '<!-- ══════════════════════════════════════════════════════════\n         SCENE 6 — PHOTO MOSAIC (Exhibition Wall)',
    '<!-- ══════════════════════════════════════════════════════════\n         SCENE 7 — THE HIDDEN SURPRISE',
    '<!-- ══════════════════════════════════════════════════════════\n         SCENE 8 — THE ENVELOPE & LETTER',
    '<!-- ══════════════════════════════════════════════════════════\n         SCENE 9 — FINAL CINEMATIC CLOSING'
]

for s in scenes:
    if s in html:
        html = html.replace(s, divider + '    ' + s)
        print(f"Inserted divider before: {s.splitlines()[1].strip()}")
    else:
        print(f"Warning: not found: {s[:50]}")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("All transition dividers successfully inserted!")
