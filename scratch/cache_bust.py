with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace('src="src/components/app.js"', 'src="src/components/app.js?v=realistic-3d"')
c = c.replace('href="src/styles/responsive.css"', 'href="src/styles/responsive.css?v=realistic-3d"')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(c)

print("Added cache-busting version params in index.html")
