import os
from PIL import Image

p = os.path.join('public', 'images', 'photo-hero.png')
out = os.path.join('public', 'images', 'photo-hero.webp')

with Image.open(p) as img:
    img.save(out, 'WEBP', quality=88, method=6)

print(f"Original PNG: {os.path.getsize(p)/1024:.1f} KB")
print(f"Compressed WebP: {os.path.getsize(out)/1024:.1f} KB")
print(f"Savings: {(1 - os.path.getsize(out)/os.path.getsize(p))*100:.1f}%")
