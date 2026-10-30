import os
from PIL import Image

img_dir = os.path.join('public', 'images')
images = [
    'photo-hero.png', 'photo-01.png', 'photo-02.png', 'photo-03.png',
    'photo-04.png', 'photo-05.png', 'photo-06.png', 'photo-07.png', 'photo-final.png'
]

total_orig = 0
total_new = 0

for fname in images:
    src_path = os.path.join(img_dir, fname)
    if not os.path.exists(src_path):
        print(f"Skipping {fname}: file not found")
        continue

    orig_sz = os.path.getsize(src_path)
    total_orig += orig_sz

    base_name = os.path.splitext(fname)[0]
    webp_name = f"{base_name}.webp"
    webp_path = os.path.join(img_dir, webp_name)

    with Image.open(src_path) as img:
        # Save as high-fidelity WebP
        img.save(webp_path, 'WEBP', quality=88, method=6)

    webp_sz = os.path.getsize(webp_path)
    total_new += webp_sz
    print(f"Converted {fname} -> {webp_name}: {orig_sz/1024:.1f} KB -> {webp_sz/1024:.1f} KB (saved {(1 - webp_sz/orig_sz)*100:.1f}%)")

print(f"\nTOTAL: {total_orig/(1024*1024):.2f} MB -> {total_new/(1024*1024):.2f} MB")
print(f"OVERALL SAVINGS: {(1 - total_new/total_orig)*100:.1f}%")
