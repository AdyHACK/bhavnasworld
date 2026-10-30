with open('src/styles/responsive.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Update .universe-heading-area
target1 = """.universe-heading-area {
  position: absolute;
  top: var(--s-16);
  left: 50%;
  transform: translateX(-50%);
  z-index: 5;"""

rep1 = """.universe-heading-area {
  position: absolute;
  top: var(--s-16);
  left: 50%;
  transform: translateX(-50%);
  z-index: 6;"""

# 2. Update #universe-nodes
target2 = """/* Universe nodes overlay */
#universe-nodes {
  position: absolute;
  inset: 0;
  z-index: 6;
  pointer-events: none;
}"""

rep2 = """/* Universe nodes overlay */
#universe-nodes {
  position: absolute;
  inset: 0;
  z-index: 7;
  pointer-events: none;
}"""

# 3. Update .universe-scroll-hint
target3 = """.universe-scroll-hint {
  position: absolute;
  bottom: var(--s-6);
  left: 50%;
  transform: translateX(-50%);
  z-index: 5;"""

rep3 = """.universe-scroll-hint {
  position: absolute;
  bottom: var(--s-6);
  left: 50%;
  transform: translateX(-50%);
  z-index: 6;"""

for t, r in [(target1, rep1), (target2, rep2), (target3, rep3)]:
    t_norm = t.replace('\r\n', '\n')
    r_norm = r.replace('\r\n', '\n')
    css_norm = css.replace('\r\n', '\n')
    assert t_norm in css_norm, f"Failed to find {t[:30]}"
    css = css_norm.replace(t_norm, r_norm, 1)

with open('src/styles/responsive.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Successfully updated z-indices in responsive.css!")
