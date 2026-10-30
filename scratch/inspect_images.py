import os
from PIL import Image

img_dir = os.path.join('public', 'images')
for f in os.listdir(img_dir):
    if f.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')):
        p = os.path.join(img_dir, f)
        with Image.open(p) as img:
            print(f"{f}: {img.size} ({img.format}) - {os.path.getsize(p)/1024:.1f} KB")
