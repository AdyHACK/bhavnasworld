import sys

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

target = """        const universeNodes = document.querySelectorAll('.universe-node');
        if (universeNodes.length) {
          gsap.set(universeNodes, { opacity: 0, scale: 0.4, y: 20 });
          ScrollTrigger.create({
            trigger: '#universe', start: 'top 75%', once: true,
            onEnter: () => {
              gsap.to(universeNodes, {
                opacity: 1, scale: 1, y: 0,
                duration: 1.0, ease: 'back.out(1.6)',
                stagger: { each: 0.18, from: 'random' },
              });
            },
          });
        }"""

replacement = """        const canvas3D = document.getElementById('universe-3d-canvas');
        if (canvas3D) {
          gsap.fromTo(canvas3D,
            { opacity: 0, scale: 0.94 },
            { opacity: 1, scale: 1, duration: 1.5, ease: 'power3.out',
              scrollTrigger: { trigger: '#universe', start: 'top 80%', once: true }
            }
          );
        }

        const planetCards = document.querySelectorAll('.universe-planet-card');
        if (planetCards.length) {
          gsap.set(planetCards, { opacity: 0, y: 25, scale: 0.95 });
          ScrollTrigger.create({
            trigger: '#universe', start: 'top 75%', once: true,
            onEnter: () => {
              gsap.to(planetCards, {
                opacity: 1, y: 0, scale: 1,
                duration: 1.0, ease: 'power3.out',
                stagger: { each: 0.12 },
              });
            },
          });
        }"""

if target in content:
    content = content.replace(target, replacement, 1)
    print("Replaced target (LF).")
elif target.replace('\n', '\r\n') in content:
    content = content.replace(target.replace('\n', '\r\n'), replacement.replace('\n', '\r\n'), 1)
    print("Replaced target (CRLF).")
else:
    print("Target not found directly, inspecting...")
    idx = content.find('universeNodes')
    print(repr(content[idx-50:idx+200]))
    raise AssertionError("GSAP target not found")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully updated GSAP universe triggers!")
