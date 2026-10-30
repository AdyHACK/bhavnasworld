import sys

with open('src/styles/responsive.css', 'r', encoding='utf-8') as f:
    css = f.read()

target = '/* Individual node wrapper */'

new_styles = """/* Planet Card Travel Action */
.planet-card-travel {
  display: inline-flex;
  align-items: center;
  font-family: var(--font-nav);
  font-size: 0.50rem;
  font-weight: 700;
  letter-spacing: 0.18em;
  color: var(--soft-caramel);
  text-transform: uppercase;
  margin-top: 0.35rem;
  border-top: 1px dashed rgba(189, 149, 107, 0.25);
  padding-top: 0.35rem;
  width: 100%;
  transition: color 0.3s;
}
.universe-planet-card:hover .planet-card-travel,
.universe-planet-card.is-hovered .planet-card-travel {
  color: var(--chestnut);
}

/* Nav Planet Indicator Tag */
.nav-planet-tag {
  font-size: 0.54rem;
  letter-spacing: 0.12em;
  font-weight: 600;
  text-transform: uppercase;
  color: var(--soft-caramel);
  opacity: 0.72;
  margin-left: 0.32rem;
  padding: 0.08rem 0.32rem;
  border-radius: 3px;
  background: rgba(189, 149, 107, 0.12);
  vertical-align: middle;
  transition: all 0.3s ease;
}
.nav-links a:hover .nav-planet-tag,
.nav-links a.active .nav-planet-tag {
  color: var(--chestnut);
  background: rgba(189, 149, 107, 0.26);
  opacity: 1;
}

/* ════════════════════════════════════════════════
   PLANETARY ORIGIN BADGES & SECTION TIE-IN
════════════════════════════════════════════════ */
.section-planet-origin {
  display: inline-flex;
  align-items: center;
  gap: 0.65rem;
  padding: 0.38rem 0.95rem;
  background: rgba(253, 249, 243, 0.94);
  border: 1px solid rgba(189, 149, 107, 0.42);
  border-radius: 20px;
  box-shadow: 0 4px 16px rgba(78, 46, 14, 0.08), inset 0 1px 0 rgba(255, 255, 255, 0.95);
  margin-bottom: 0.9rem;
  transition: all 0.3s cubic-bezier(0.22, 1, 0.36, 1);
  width: fit-content;
}
.section-planet-origin:hover {
  background: rgba(255, 253, 250, 0.98);
  border-color: rgba(189, 149, 107, 0.85);
  box-shadow: 0 8px 24px rgba(110, 72, 32, 0.14), 0 0 14px rgba(223, 194, 157, 0.35);
  transform: translateY(-2px);
}
.section-planet-origin.arrival-highlight {
  animation: origin-pulse 1.6s ease-out;
}
@keyframes origin-pulse {
  0%   { box-shadow: 0 0 0 0 rgba(189, 149, 107, 0.7); transform: scale(1); }
  50%  { box-shadow: 0 0 0 12px rgba(189, 149, 107, 0); transform: scale(1.05); }
  100% { box-shadow: 0 4px 16px rgba(78, 46, 14, 0.08); transform: scale(1); }
}

.origin-planet-icon {
  width: 18px;
  height: 18px;
  border-radius: 50%;
  position: relative;
  display: inline-block;
  flex-shrink: 0;
  box-shadow: 0 0 8px rgba(189, 149, 107, 0.45);
}
.origin-planet-icon--earth {
  background: radial-gradient(circle at 35% 35%, #8bc34a 0%, #1976d2 45%, #0d47a1 85%);
  box-shadow: 0 0 10px rgba(66, 165, 245, 0.55);
}
.origin-planet-icon--mars {
  background: radial-gradient(circle at 35% 35%, #ffab91 0%, #d84315 50%, #4e1a0b 90%);
  box-shadow: 0 0 10px rgba(226, 123, 88, 0.55);
}
.origin-planet-icon--jupiter {
  background: repeating-linear-gradient(180deg, #d7ccc8 0px, #bcaaa4 3px, #a1887f 6px, #d7ccc8 9px);
  box-shadow: 0 0 10px rgba(212, 170, 112, 0.55);
}
.origin-planet-icon--moon {
  background: radial-gradient(circle at 35% 35%, #eceff1 0%, #90a4ae 55%, #37474f 90%);
  box-shadow: 0 0 10px rgba(176, 190, 197, 0.55);
}
.origin-planet-icon--saturn {
  background: radial-gradient(circle at 35% 35%, #ffe082 0%, #d4aa70 50%, #6d4c41 90%);
  box-shadow: 0 0 10px rgba(238, 208, 152, 0.55);
}
.origin-planet-icon--saturn::after {
  content: '';
  position: absolute;
  top: 50%; left: 50%;
  width: 28px; height: 9px;
  border: 1.5px solid rgba(223, 194, 157, 0.9);
  border-radius: 50%;
  transform: translate(-50%, -50%) rotate(-25deg);
  pointer-events: none;
}

.origin-planet-tag {
  font-family: var(--font-nav);
  font-size: 0.58rem;
  font-weight: 700;
  letter-spacing: 0.20em;
  color: var(--chestnut);
  text-transform: uppercase;
}
.origin-sep {
  color: var(--soft-caramel);
  font-size: 0.55rem;
  opacity: 0.7;
}
.origin-orbit-link {
  font-family: var(--font-nav);
  font-size: 0.52rem;
  font-weight: 600;
  letter-spacing: 0.15em;
  color: var(--caramel);
  text-decoration: none;
  text-transform: uppercase;
  transition: color 0.25s, transform 0.25s;
  display: inline-flex;
  align-items: center;
  gap: 0.25rem;
}
.origin-orbit-link:hover {
  color: var(--deep-espresso);
  transform: translateX(2px);
}

/* Individual node wrapper */"""

assert target in css, "target not found in css"
css = css.replace(target, new_styles, 1)

with open('src/styles/responsive.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Successfully added planetary connection styles to responsive.css!")
