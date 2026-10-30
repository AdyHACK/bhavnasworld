with open('src/styles/responsive.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Update padding of #scrapbook
target1 = "  padding: var(--s-12) 0 calc(var(--s-16) + 56px);"
rep1 = "  padding: var(--s-12) 0 var(--s-16);"

css_norm = css.replace('\r\n', '\n')
target1_norm = target1.replace('\r\n', '\n')
rep1_norm = rep1.replace('\r\n', '\n')

assert target1_norm in css_norm, "target1 not found"
css_norm = css_norm.replace(target1_norm, rep1_norm, 1)

# 2. Update .scrapbook-grid
target2 = """.scrapbook-grid {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  grid-auto-rows: 200px;
  gap: 16px;
  align-items: start;
  padding-top: var(--s-4);
}"""

rep2 = """.scrapbook-grid {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  grid-auto-rows: minmax(210px, auto);
  gap: 20px;
  align-items: start;
  padding-top: var(--s-4);
  padding-bottom: var(--s-8);
}"""

target2_norm = target2.replace('\r\n', '\n')
rep2_norm = rep2.replace('\r\n', '\n')

assert target2_norm in css_norm, "target2 not found"
css_norm = css_norm.replace(target2_norm, rep2_norm, 1)

# 3. Update .scrap-card--wide to span 2 rows cleanly
target3 = """.scrap-card--wide {
  grid-column: span 7;
}"""

rep3 = """.scrap-card--wide {
  grid-column: span 7;
  grid-row: span 2;
}"""

target3_norm = target3.replace('\r\n', '\n')
rep3_norm = rep3.replace('\r\n', '\n')

assert target3_norm in css_norm, "target3 not found"
css_norm = css_norm.replace(target3_norm, rep3_norm, 1)

with open('src/styles/responsive.css', 'w', encoding='utf-8') as f:
    f.write(css_norm)

print("Successfully updated responsive.css!")
