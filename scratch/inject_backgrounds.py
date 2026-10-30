import sys
sys.stdout.reconfigure(encoding='utf-8')

# Read current index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Load generated snippets from scratch/generate_background_html.py
from generate_background_html import hero_bg, universe_bg, gallery_bg, scrapbook_bg, mosaic_bg, secret_bg, letter_bg, final_bg

divider = '''
      <!-- Section Transition Divider -->
      <div class="section-transition-divider" aria-hidden="true">
        <div class="transition-rule-line"></div>
        <span class="transition-glyph">✦</span>
        <div class="transition-rule-line"></div>
      </div>
'''

# 1. Insert hero_bg right after `<section id="hero" ...>`
target_hero = '<div class="hero-layout">'
if target_hero in html:
    html = html.replace(target_hero, f"{hero_bg}\n\n      {target_hero}", 1)
    print("Injected hero background")
else:
    print("ERROR: target_hero not found")

# 2. Insert universe_bg right after `<canvas id="universe-canvas" aria-hidden="true"></canvas>`
target_univ = '<canvas id="universe-canvas" aria-hidden="true"></canvas>'
if target_univ in html:
    html = html.replace(target_univ, f"{target_univ}\n\n{universe_bg}", 1)
    print("Injected universe background")
else:
    print("ERROR: target_univ not found")

# 3. Insert gallery_bg right after `<section id="gallery" class="section" aria-label="Gallery — A collection of little moments">`
target_gallery = '<section id="gallery" class="section" aria-label="Gallery — A collection of little moments">'
if target_gallery in html:
    html = html.replace(target_gallery, f"{target_gallery}\n\n{gallery_bg}", 1)
    print("Injected gallery background")
else:
    print("ERROR: target_gallery not found")

# 4. Insert scrapbook_bg right after `<section id="scrapbook" class="section" aria-label="Scrapbook — Little things, beautifully kept">`
target_scrap = '<section id="scrapbook" class="section" aria-label="Scrapbook — Little things, beautifully kept">'
if target_scrap in html:
    html = html.replace(target_scrap, f"{target_scrap}\n\n{scrapbook_bg}", 1)
    print("Injected scrapbook background")
else:
    print("ERROR: target_scrap not found")

# 5. Insert mosaic_bg right after `<section id="mosaic" class="section" aria-label="Mosaic — Every frame has its place">`
target_mosaic = '<section id="mosaic" class="section" aria-label="Mosaic — Every frame has its place">'
if target_mosaic in html:
    html = html.replace(target_mosaic, f"{target_mosaic}\n\n{mosaic_bg}", 1)
    print("Injected mosaic background")
else:
    print("ERROR: target_mosaic not found")

# 6. Insert secret_bg right after `<canvas id="secret-canvas" aria-hidden="true"></canvas>`
target_secret = '<canvas id="secret-canvas" aria-hidden="true"></canvas>'
if target_secret in html:
    html = html.replace(target_secret, f"{target_secret}\n\n{secret_bg}", 1)
    print("Injected secret background")
else:
    print("ERROR: target_secret not found")

# 7. Insert letter_bg right after `<section id="letter-section" class="section" style="padding:0;" aria-label="A letter for you">`
target_letter = '<section id="letter-section" class="section" style="padding:0;" aria-label="A letter for you">'
if target_letter in html:
    html = html.replace(target_letter, f"{target_letter}\n\n{letter_bg}", 1)
    print("Injected letter background")
else:
    print("ERROR: target_letter not found")

# 8. Insert final_bg right after `<canvas id="final-canvas" aria-hidden="true"></canvas>`
target_final = '<canvas id="final-canvas" aria-hidden="true"></canvas>'
if target_final in html:
    html = html.replace(target_final, f"{target_final}\n\n{final_bg}", 1)
    print("Injected final background")
else:
    print("ERROR: target_final not found")

# Write out the updated index.html
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("index.html successfully updated with all luxury background components!")
