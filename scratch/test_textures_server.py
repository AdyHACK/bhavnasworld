import urllib.request

urls = [
    'http://localhost:5173/public/vendor/three.min.js',
    'http://localhost:5173/public/textures/planets/earth.webp',
    'http://localhost:5173/public/textures/planets/earth_clouds.webp',
    'http://localhost:5173/public/textures/planets/mars.webp',
    'http://localhost:5173/public/textures/planets/jupiter.webp',
    'http://localhost:5173/public/textures/planets/moon.webp',
    'http://localhost:5173/public/textures/planets/saturn.webp',
    'http://localhost:5173/public/textures/planets/saturn_ring_topdown.png',
]

for u in urls:
    try:
        req = urllib.request.Request(u, method='HEAD')
        with urllib.request.urlopen(req) as resp:
            name = u.split('/')[-1]
            print(f'{name}: {resp.status} {resp.reason}')
    except Exception as e:
        print(f'{u}: ERROR {e}')
