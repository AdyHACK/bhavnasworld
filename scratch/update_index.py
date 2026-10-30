import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update hero image tag
target1 = '<img id="hero-bg" src="" alt="" aria-hidden="true" loading="eager" />'
repl1 = '<img id="hero-bg" src="" alt="" aria-hidden="true" width="1157" height="1359" loading="eager" fetchpriority="high" decoding="sync" />'
assert target1 in content, "target1 not found"
content = content.replace(target1, repl1, 1)

# 2. Update final image tag
target2 = '<img id="final-photo" src="" alt="" class="img-cover"'
repl2 = '<img id="final-photo" src="" alt="" class="img-cover" width="1507" height="1044" loading="lazy" decoding="async"'
assert target2 in content, "target2 not found"
content = content.replace(target2, repl2, 1)

# 3. Update GSAP Hero reveal
target3 = """        /* ── 1. HERO — Blur-to-sharp + split editorial reveal ── */
        const heroBg = document.getElementById('hero-bg');
        if (heroBg && heroBg.classList.contains('loaded')) {
          gsap.fromTo(heroBg,
            { scale: 1.1, filter: 'blur(8px) saturate(0.75)' },
            { scale: 1,   filter: 'blur(0px) saturate(1.02)',
              duration: 2.2, ease: 'power4.out' });
        }"""
# Handle possible CRLF
target3_crlf = target3.replace('\n', '\r\n')
repl3 = """        /* ── 1. HERO — Editorial scale-down reveal ── */
        const heroBg = document.getElementById('hero-bg');
        if (heroBg) {
          gsap.fromTo(heroBg,
            { scale: 1.06, opacity: 0.7 },
            { scale: 1,   opacity: 1,
              duration: 1.6, ease: 'power3.out' });
        }"""

if target3_crlf in content:
    content = content.replace(target3_crlf, repl3.replace('\n', '\r\n'), 1)
    print("Replaced target3 (CRLF)")
elif target3 in content:
    content = content.replace(target3, repl3, 1)
    print("Replaced target3 (LF)")
else:
    raise AssertionError("target3 not found")

# 4. Update Universe mouse parallax
target4 = """        /* Universe mouse parallax */
        const universeSection = document.getElementById('universe');
        if (universeSection) {
          let ux = 0, uy = 0;
          universeSection.addEventListener('mousemove', e => {
            const rect = universeSection.getBoundingClientRect();
            ux = (e.clientX - rect.left) / rect.width - 0.5;
            uy = (e.clientY - rect.top)  / rect.height - 0.5;
            universeNodes.forEach((node, i) => {
              const depth = 0.8 + i * 0.3;
              gsap.to(node, {
                x: ux * 22 * depth, y: uy * 14 * depth,
                duration: 1.6, ease: 'power2.out', overwrite: 'auto',
              });
            });
          });
          universeSection.addEventListener('mouseleave', () => {
            universeNodes.forEach(node => {
              gsap.to(node, { x: 0, y: 0, duration: 1.8, ease: 'power2.out', overwrite: 'auto' });
            });
          });
        }"""
target4_crlf = target4.replace('\n', '\r\n')
repl4 = """        /* Universe mouse parallax */
        const universeSection = document.getElementById('universe');
        if (universeSection) {
          let ux = 0, uy = 0;
          let ticking = false;
          universeSection.addEventListener('mousemove', e => {
            const rect = universeSection.getBoundingClientRect();
            ux = (e.clientX - rect.left) / rect.width - 0.5;
            uy = (e.clientY - rect.top)  / rect.height - 0.5;
            if (!ticking) {
              ticking = true;
              requestAnimationFrame(() => {
                universeNodes.forEach((node, i) => {
                  const depth = 0.8 + i * 0.3;
                  gsap.to(node, {
                    x: ux * 22 * depth, y: uy * 14 * depth,
                    duration: 1.2, ease: 'power2.out', overwrite: 'auto',
                  });
                });
                ticking = false;
              });
            }
          }, { passive: true });
          universeSection.addEventListener('mouseleave', () => {
            universeNodes.forEach(node => {
              gsap.to(node, { x: 0, y: 0, duration: 1.2, ease: 'power2.out', overwrite: 'auto' });
            });
          });
        }"""

if target4_crlf in content:
    content = content.replace(target4_crlf, repl4.replace('\n', '\r\n'), 1)
    print("Replaced target4 (CRLF)")
elif target4 in content:
    content = content.replace(target4, repl4, 1)
    print("Replaced target4 (LF)")
else:
    raise AssertionError("target4 not found")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully updated index.html!")
