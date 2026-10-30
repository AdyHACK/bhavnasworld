import urllib.request

urls = [
    'http://localhost:5173/public/vendor/three.min.js',
    'http://localhost:5173/public/textures/planets/earth.webp',
    'http://localhost:5173/public/textures/planets/saturn_ring_topdown.png',
    'http://localhost:5173/src/styles/responsive.css',
    'http://localhost:5173/src/components/app.js'
]

for url in urls:
    try:
        req = urllib.request.Request(url, method='HEAD')
        with urllib.request.urlopen(req) as response:
            print(f"{url} -> {response.status}")
    except Exception as e:
        print(f"{url} -> Error: {e}")
