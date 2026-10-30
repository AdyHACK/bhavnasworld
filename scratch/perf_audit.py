import sys, os, re
sys.stdout.reconfigure(encoding='utf-8')

print("=== AUDIT 1: CSS Blurs and Backdrop-Filters ===")
css_files = ['globals.css', 'animations.css', 'responsive.css', 'backgrounds.css']
for f in css_files:
    path = os.path.join('src', 'styles', f)
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as fp:
            content = fp.read()
        blurs = re.findall(r'([^{}]+)\{[^{}]*(?:backdrop-filter|filter:\s*blur)[^{}]*\}', content)
        print(f"{f}: found {len(blurs)} blur/backdrop-filter rules")
        for b in blurs[:10]:
            sel = b.strip().split('\n')[-1].strip()
            print(f"   -> {sel}")

print("\n=== AUDIT 2: Continuous Infinite CSS Animations ===")
for f in css_files:
    path = os.path.join('src', 'styles', f)
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as fp:
            content = fp.read()
        anims = re.findall(r'([^{}]+)\{[^{}]*animation:[^;}]*infinite[^{}]*\}', content)
        print(f"{f}: found {len(anims)} infinite animations")
        for a in anims:
            sel = a.strip().split('\n')[-1].strip()
            print(f"   -> {sel}")

print("\n=== AUDIT 3: JavaScript RAF, Event Listeners, and Intervals in app.js ===")
with open(os.path.join('src', 'components', 'app.js'), 'r', encoding='utf-8') as fp:
    app_js = fp.read()

listeners = re.findall(r'addEventListener\([\'"]([^\'"]+)[\'"]', app_js)
print("Event listeners in app.js:", set(listeners))
for l in ['scroll', 'mousemove', 'resize']:
    count = len(re.findall(rf'addEventListener\([\'"]{l}[\'"]', app_js))
    print(f"   '{l}' listeners: {count}")

rafs = re.findall(r'requestAnimationFrame', app_js)
print(f"requestAnimationFrame occurrences: {len(rafs)}")

intervals = re.findall(r'setInterval', app_js)
print(f"setInterval occurrences: {len(intervals)}")

print("\n=== AUDIT 4: GSAP & ScrollTrigger in index.html ===")
with open('index.html', 'r', encoding='utf-8') as fp:
    html = fp.read()

st_matches = re.findall(r'ScrollTrigger\.create|\.to\([^)]*scrollTrigger', html)
print(f"ScrollTrigger references in index.html: {len(st_matches)}")

print("\n=== AUDIT 5: Public Images Size & Formats ===")
img_dir = os.path.join('public', 'images')
if os.path.exists(img_dir):
    for img in os.listdir(img_dir):
        fpath = os.path.join(img_dir, img)
        size_kb = os.path.getsize(fpath) / 1024
        print(f"   {img}: {size_kb:.1f} KB")
