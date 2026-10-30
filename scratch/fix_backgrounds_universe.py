with open('src/styles/backgrounds.css', 'r', encoding='utf-8') as f:
    css = f.read()

target = "#universe > *:not(.section-bg):not(canvas),\n"
if target not in css:
    target = "#universe > *:not(.section-bg):not(canvas),\r\n"

assert target in css, "target not found"
css = css.replace(target, "", 1)

with open('src/styles/backgrounds.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Successfully removed conflicting #universe rule from backgrounds.css!")
