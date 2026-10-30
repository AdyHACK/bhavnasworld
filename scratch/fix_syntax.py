with open('src/components/app.js', 'r', encoding='utf-8') as f:
    code = f.read()

target = "set(shayari-line-, line);"
replacement = "set('shayari-line-' + (i + 1), line);"

if target in code:
    code = code.replace(target, replacement, 1)
    with open('src/components/app.js', 'w', encoding='utf-8') as f:
        f.write(code)
    print("SUCCESS: syntax error fixed")
else:
    print("ERROR: target not found")
