with open('src/styles/responsive.css', 'r', encoding='utf-8') as f:
    css = f.read()

old_desktop_card = """/* Secret Keepsake Card */
.secret-card {
  position: absolute;
  top: 10px;
  left: 6%;
  right: 6%;
  min-height: 250px;
  background: #FFFDF9;
  border-radius: 2px;
  box-shadow: 0 16px 42px rgba(73, 50, 36, 0.16);
  padding: 1.8rem 1.6rem 1.4rem;
  box-sizing: border-box;
  opacity: 0;
  transform: translate3d(0, 0, 0) scale(0.96);
  pointer-events: none;
  will-change: transform, opacity;
  z-index: 10;
  text-align: center;
}

.secret-card.is-active {
  z-index: 50 !important;
  pointer-events: auto;
}

.secret-card-border {
  position: absolute;
  inset: 8px;
  border: 1px solid rgba(189, 149, 107, 0.35);
  pointer-events: none;
}

.secret-card-monogram {
  font-family: var(--font-nav);
  font-size: 0.46rem;
  letter-spacing: 0.28em;
  color: var(--soft-caramel);
  text-transform: uppercase;
  display: block;
  margin-bottom: 0.4rem;
}

.secret-card-title {
  font-family: var(--font-display);
  font-size: 1.45rem;
  font-style: italic;
  color: var(--deep-espresso);
  margin: 0 0 0.8rem;
}

.secret-message-text {
  font-family: var(--font-heading);
  font-size: 1.05rem;
  line-height: 1.85;
  color: #523D2D;
  margin: 0;
}

.secret-card-footer {
  margin-top: 1rem;
  color: var(--soft-caramel);
  font-size: 0.75rem;
  opacity: 0.6;
}

.secret-close-btn {
  position: absolute;
  top: 12px;
  right: 12px;
  width: 26px;
  height: 26px;
  border-radius: 50%;
  border: 1px solid rgba(189, 149, 107, 0.35);
  background: rgba(255, 253, 248, 0.9);
  color: var(--chestnut);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.7rem;
  cursor: pointer;
  z-index: 10;
  transition: all 0.25s ease;
}
.secret-close-btn:hover {
  background: var(--card-primary);
  color: var(--deep-espresso);
  transform: rotate(90deg) scale(1.1);
}"""

new_desktop_card = """/* Secret Keepsake Card */
.secret-card {
  position: absolute;
  top: 8px;
  left: 4%;
  right: 4%;
  min-height: 295px;
  background: #FAF5EE;
  border-radius: 4px;
  box-shadow: 0 20px 52px rgba(73, 50, 36, 0.18), 0 2px 8px rgba(73, 50, 36, 0.08);
  padding: 2.1rem 2.2rem 1.6rem;
  box-sizing: border-box;
  opacity: 0;
  transform: translate3d(0, 0, 0) scale(0.96);
  pointer-events: none;
  will-change: transform, opacity;
  z-index: 10;
  text-align: center;
  border: 1px solid rgba(189, 149, 107, 0.38);
}

.secret-card.is-active {
  z-index: 50 !important;
  pointer-events: auto;
}

.secret-card-texture {
  position: absolute;
  inset: 0;
  border-radius: 4px;
  background-image: radial-gradient(rgba(189, 149, 107, 0.07) 1px, transparent 0);
  background-size: 8px 8px;
  opacity: 0.7;
  pointer-events: none;
}

.secret-card-border {
  position: absolute;
  inset: 7px;
  border: 1px solid rgba(189, 149, 107, 0.3);
  border-radius: 2px;
  pointer-events: none;
}

.secret-border-inner {
  position: absolute;
  inset: 3px;
  border: 0.8px dashed rgba(189, 149, 107, 0.22);
  border-radius: 1px;
  pointer-events: none;
}

.secret-corner-botanical {
  position: absolute;
  width: 18px;
  height: 18px;
}
.secret-corner--tl { top: 2px; left: 2px; }
.secret-corner--tr { top: 2px; right: 2px; transform: scaleX(-1); }
.secret-corner--bl { bottom: 2px; left: 2px; transform: scaleY(-1); }
.secret-corner--br { bottom: 2px; right: 2px; transform: scale(-1); }

/* Header with Tiny Decorative Floral Illustration */
.secret-card-header {
  position: relative;
  margin-bottom: 0.3rem;
}

.secret-floral-illustration {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-bottom: 0.45rem;
  opacity: 0;
  transform: translate3d(0, 8px, 0);
  will-change: transform, opacity;
}

.secret-floral-svg {
  width: 86px;
  height: 20px;
  overflow: visible;
}

.secret-card-monogram {
  font-family: var(--font-nav, 'DM Sans', sans-serif);
  font-size: 0.48rem;
  letter-spacing: 0.26em;
  color: var(--soft-caramel, #BD956B);
  text-transform: uppercase;
  display: block;
  margin-bottom: 0.4rem;
  opacity: 0;
  transform: translate3d(0, 6px, 0);
}

.secret-ornamental-divider {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.75rem;
  margin: 0.5rem auto 1.15rem;
  width: 70%;
  max-width: 200px;
  opacity: 0;
  transform: scaleX(0.5);
  transform-origin: center center;
  will-change: transform, opacity;
}

.secret-divider-line {
  flex: 1;
  height: 1px;
  background: linear-gradient(90deg, transparent, rgba(189, 149, 107, 0.45), transparent);
}

.secret-divider-star {
  font-size: 0.60rem;
  color: #BD956B;
  line-height: 1;
  text-shadow: 0 0 8px rgba(216, 185, 144, 0.5);
}

/* Shayari Body: Line by Line Devanagari Poetry */
.secret-shayari-body {
  margin: 0.2rem 0 0.8rem;
  text-align: center;
  position: relative;
}

.shayari-couplet {
  margin-bottom: 0.95rem;
  position: relative;
}

.shayari-couplet:last-child {
  margin-bottom: 0;
}

.shayari-line {
  font-family: 'Martel', 'Rozha One', 'Noto Serif Devanagari', 'Kokila', 'Mangal', 'Nirmala UI', serif;
  font-size: clamp(0.96rem, 2.3vw, 1.15rem);
  font-weight: 400;
  line-height: 2.15;
  letter-spacing: 0.025em;
  color: #442E20; /* Deep Mocha-Brown */
  margin: 0;
  padding: 0.1rem 0;
  opacity: 0;
  transform: translate3d(0, 14px, 0);
  will-change: transform, opacity;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-rendering: optimizeLegibility;
  white-space: normal;
  word-break: keep-all;
  overflow-wrap: break-word;
}

/* Subtle highlight on the final two lines */
.shayari-couplet--highlight {
  position: relative;
  padding: 0.25rem 0.6rem;
  border-radius: 4px;
  transition: background-color 0.8s ease, box-shadow 0.8s ease;
}

.shayari-couplet--highlight .shayari-line {
  color: #382214;
  font-weight: 450;
}

.shayari-couplet--highlight.is-highlighted {
  background-color: rgba(216, 185, 144, 0.14);
  box-shadow: 0 0 28px rgba(216, 185, 144, 0.25);
}

/* Footer & Delicate Decorative Flourish */
.secret-card-footer {
  margin-top: 1rem;
  display: flex;
  justify-content: center;
  align-items: center;
}

.secret-flourish-wrap {
  opacity: 0;
  transform: translate3d(0, 8px, 0) scale(0.9);
  will-change: transform, opacity;
}

.secret-bottom-flourish-svg {
  width: 95px;
  height: 15px;
  overflow: visible;
}

.secret-close-btn {
  position: absolute;
  top: 10px;
  right: 10px;
  width: 28px;
  height: 28px;
  border-radius: 50%;
  border: 1px solid rgba(189, 149, 107, 0.35);
  background: rgba(254, 250, 243, 0.92);
  color: var(--chestnut);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.75rem;
  cursor: pointer;
  z-index: 60;
  transition: all 0.28s cubic-bezier(0.22, 1, 0.36, 1);
  box-shadow: 0 2px 6px rgba(73, 50, 36, 0.1);
}

.secret-close-btn:hover {
  background: var(--card-primary);
  color: var(--deep-espresso);
  transform: rotate(90deg) scale(1.1);
  border-color: var(--champagne);
}"""

css_norm = css.replace('\r\n', '\n')
old_card_norm = old_desktop_card.replace('\r\n', '\n')
new_card_norm = new_desktop_card.replace('\r\n', '\n')

if old_card_norm in css_norm:
    css_norm = css_norm.replace(old_card_norm, new_card_norm, 1)
    with open('src/styles/responsive.css', 'w', encoding='utf-8') as f:
        f.write(css_norm)
    print("SUCCESS: secret-card replaced")
else:
    print("ERROR: old_card still not found")
