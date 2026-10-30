import os
from PIL import Image

for name in ['photo-04.webp', 'photo-05.webp', 'photo-06.webp']:
    path = os.path.join('public/images', name)
    if os.path.exists(path):
        im = Image.open(path)
        print(f"{name}: size={im.size}, mode={im.mode}")
