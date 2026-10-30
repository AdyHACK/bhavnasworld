import sys

with open('src/components/app.js', 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Update Jupiter in planetConfigs
target1 = """    {
      id: 'jupiter',
      name: 'THE SCRAPBOOK',
      href: '#scrapbook',"""

replacement1 = """    {
      id: 'jupiter',
      name: 'PHOTO MOSAIC',
      href: '#mosaic',"""

# Normalize line endings for replacement
code_normalized = code.replace('\r\n', '\n')
target1_norm = target1.replace('\r\n', '\n')
replacement1_norm = replacement1.replace('\r\n', '\n')

assert target1_norm in code_normalized, "Target 1 not found"
code_normalized = code_normalized.replace(target1_norm, replacement1_norm, 1)

# 2. Update handlePlanetClick to add arrival highlight pulse
target2 = """    // Smooth scroll to target destination
    setTimeout(() => {
      const tgt = document.querySelector(cfg.href);
      if (tgt) tgt.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }, 280);"""

replacement2 = """    // Smooth scroll to target destination & highlight arrival badge
    setTimeout(() => {
      const tgt = document.querySelector(cfg.href);
      if (tgt) {
        tgt.scrollIntoView({ behavior: 'smooth', block: 'start' });
        const originBadge = tgt.querySelector('.section-planet-origin');
        if (originBadge) {
          originBadge.classList.remove('arrival-highlight');
          void originBadge.offsetWidth; // trigger reflow for clean re-animation
          originBadge.classList.add('arrival-highlight');
        }
      }
    }, 280);"""

target2_norm = target2.replace('\r\n', '\n')
replacement2_norm = replacement2.replace('\r\n', '\n')

assert target2_norm in code_normalized, "Target 2 not found"
code_normalized = code_normalized.replace(target2_norm, replacement2_norm, 1)

# Write back preserving CRLF if original had CRLF
if '\r\n' in code:
    final_code = code_normalized.replace('\n', '\r\n')
else:
    final_code = code_normalized

with open('src/components/app.js', 'w', encoding='utf-8') as f:
    f.write(final_code)

print("Successfully updated app.js with Jupiter mapping and arrival highlight!")
