import sys

with open('src/styles/responsive.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Target lines 2594 to the end
target_marker = "/* ════════════════════════════════════════════════\n   RESPONSIVE — TABLET\n════════════════════════════════════════════════ */"

if target_marker not in css:
    target_marker = "/* ════════════════════════════════════════════════\r\n   RESPONSIVE — TABLET\r\n════════════════════════════════════════════════ */"

assert target_marker in css, "Target marker not found in responsive.css"

idx = css.find(target_marker)
base_css = css[:idx]

new_responsive_css = """/* ════════════════════════════════════════════════
   COMPREHENSIVE TABLET & RESPONSIVE ARCHITECTURE
   Tailored compositions for 768x1024, 820x1180, 1024x768
════════════════════════════════════════════════ */

/* Common touch and tablet baseline (max-width: 1024px) */
@media (max-width: 1024px) {
  #cursor-dot, #cursor-ring {
    display: none !important;
  }
  * {
    cursor: auto !important;
  }
  button, a, .btn, .wax-seal, .universe-planet-card, .scrap-card, .gallery-item {
    cursor: pointer !important;
  }

  /* Universal section clearance */
  .section {
    padding: var(--s-12) 0;
  }

  /* Lightbox touch optimization */
  .lb-btn {
    width: 48px !important;
    height: 48px !important;
    font-size: 1.4rem !important;
    background: rgba(243, 231, 214, 0.92) !important;
    box-shadow: 0 4px 16px rgba(73, 50, 36, 0.22) !important;
  }
  #lb-prev { left: 1rem !important; }
  #lb-next { right: 1rem !important; }
  .lightbox-close { top: 1rem !important; right: 1rem !important; width: 44px !important; height: 44px !important; }
}

/* ────────────────────────────────────────────────────────────
   1. TABLET PORTRAIT COMPOSITIONS (768x1024, 820x1180)
   iPad Mini, iPad Air, iPad Pro 11", standard tablets
──────────────────────────────────────────────────────────── */
@media (min-width: 600px) and (max-width: 960px) and (orientation: portrait),
       (min-width: 768px) and (max-width: 850px) {

  /* Tablet Nav with Slide-out Drawer */
  #nav {
    padding: 0.9rem 1.8rem;
  }
  .nav-menu-btn {
    display: flex !important;
  }
  .nav-links {
    position: fixed !important;
    top: 0 !important;
    right: -100% !important;
    height: 100vh !important;
    width: min(340px, 82vw) !important;
    flex-direction: column !important;
    justify-content: center !important;
    align-items: flex-start !important;
    background: rgba(248, 241, 231, 0.98) !important;
    backdrop-filter: blur(24px) !important;
    -webkit-backdrop-filter: blur(24px) !important;
    padding: 3rem 2.2rem !important;
    gap: 1.2rem !important;
    transition: right 0.42s cubic-bezier(0.22, 1, 0.36, 1) !important;
    box-shadow: -6px 0 40px rgba(73, 50, 36, 0.18) !important;
    z-index: 9999 !important;
  }
  .nav-links.open {
    right: 0 !important;
  }
  .nav-links a {
    font-size: 0.90rem !important;
    letter-spacing: 0.16em !important;
    padding: 0.5rem 0 !important;
    width: 100% !important;
    border-bottom: 1px dashed rgba(189, 149, 107, 0.22) !important;
  }
  .nav-planet-tag {
    font-size: 0.60rem !important;
    margin-left: 0.6rem !important;
    padding: 0.12rem 0.45rem !important;
  }

  /* Hero Section: Intentional Editorial Tablet Spread */
  .hero-layout {
    display: grid !important;
    grid-template-columns: 1.05fr 0.95fr !important;
    min-height: 100vh !important;
    min-height: 100svh !important;
    align-items: center !important;
  }
  .hero-left {
    padding: 4rem 1.6rem 3.5rem 2.2rem !important;
  }
  .hero-heading {
    font-size: clamp(2.3rem, 4.8vw, 3.5rem) !important;
    line-height: 1.06 !important;
  }
  .hero-sub {
    font-size: 0.90rem !important;
    max-width: 360px !important;
  }
  .hero-right {
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    padding: 3rem 2.2rem 3rem 0.8rem !important;
    height: 100% !important;
  }
  .hero-frame {
    width: 100% !important;
    max-width: 340px !important;
    max-height: 72vh !important;
    aspect-ratio: 3/4 !important;
    box-shadow: var(--shadow-card), 0 20px 48px rgba(73, 50, 36, 0.14) !important;
  }
  .hero-frame img {
    object-fit: cover !important;
    object-position: 50% 20% !important;
  }
  .hero-vertical-label {
    left: 0.8rem !important;
    font-size: 0.50rem !important;
  }
  .hero-num {
    bottom: 2rem !important;
    right: 2rem !important;
    font-size: 3rem !important;
    opacity: 0.12 !important;
  }

  /* 3D Planetary Universe: Perimeter Composition (Zero Planet Overlap) */
  #universe {
    height: 100vh !important;
    min-height: 100vh !important;
    overflow: hidden !important;
    position: relative !important;
  }
  #universe-nodes {
    position: absolute !important;
    inset: 0 !important;
    z-index: 7 !important;
    pointer-events: none !important;
    display: block !important;
  }
  .universe-heading-area {
    position: absolute !important;
    top: 4.8rem !important;
    left: 50% !important;
    transform: translateX(-50%) !important;
    z-index: 6 !important;
    text-align: center !important;
    width: 90% !important;
    max-width: 440px !important;
  }
  .universe-heading-area .t-eyebrow {
    font-size: 0.56rem !important;
    letter-spacing: 0.24em !important;
  }
  .universe-heading-area .t-h2 {
    font-size: clamp(1.4rem, 2.8vw, 1.95rem) !important;
    margin-top: 0.4rem !important;
  }
  .universe-center {
    position: absolute !important;
    top: 52% !important;
    left: 50% !important;
    transform: translate(-50%, -50%) !important;
    z-index: 4 !important;
    text-align: center !important;
  }
  .universe-center-title {
    font-size: 0.68rem !important;
    letter-spacing: 0.26em !important;
  }
  .universe-center-ring--outer {
    width: 150px !important;
    height: 150px !important;
    margin-left: -75px !important;
    margin-top: -75px !important;
  }
  .universe-center-ring--inner {
    width: 90px !important;
    height: 90px !important;
    margin-left: -45px !important;
    margin-top: -45px !important;
  }
  .universe-constellation-svg {
    display: block !important;
    position: absolute !important;
    inset: 0 !important;
    z-index: 3 !important;
    width: 100% !important;
    height: 100% !important;
  }
  .universe-scroll-hint {
    position: absolute !important;
    bottom: 1.6rem !important;
    left: 50% !important;
    transform: translateX(-50%) !important;
    z-index: 6 !important;
    display: flex !important;
  }

  /* Observatory Cards Tablet Perimeter Styling */
  .universe-planet-card {
    position: absolute !important;
    pointer-events: auto !important;
    max-width: 195px !important;
    width: auto !important;
    padding: 0.52rem 0.80rem !important;
    border-radius: 10px !important;
    z-index: 8 !important;
    box-shadow: 0 6px 20px rgba(78, 46, 14, 0.12), inset 0 1px 0 rgba(255, 255, 255, 0.95) !important;
  }
  .universe-planet-card .planet-card-title {
    font-size: 0.72rem !important;
  }
  .universe-planet-card .planet-pill-astronomy {
    font-size: 0.50rem !important;
  }
  .universe-planet-card .planet-pill-status {
    font-size: 0.44rem !important;
  }
  .universe-planet-card .planet-card-meta {
    font-size: 0.55rem !important;
    line-height: 1.3 !important;
  }
  .universe-planet-card .planet-card-travel {
    font-size: 0.48rem !important;
  }
  .universe-planet-card--earth   { left: 4% !important; top: 22% !important; transform: none !important; }
  .universe-planet-card--mars    { right: 4% !important; top: 20% !important; transform: none !important; }
  .universe-planet-card--moon    { left: 4% !important; top: 62% !important; transform: none !important; }
  .universe-planet-card--jupiter { right: 4% !important; top: 64% !important; transform: none !important; }
  .universe-planet-card--saturn  { left: 50% !important; top: auto !important; bottom: 3% !important; transform: translateX(-50%) !important; }

  /* Gallery Section: 2-Column Balanced Exhibition */
  .gallery-grid {
    display: grid !important;
    grid-template-columns: repeat(2, 1fr) !important;
    grid-auto-rows: minmax(240px, 300px) !important;
    gap: 16px !important;
  }
  .gallery-item--featured {
    grid-column: span 2 !important;
    grid-row: span 1 !important;
    max-height: 440px !important;
  }
  .gallery-item--wide,
  .gallery-item--tall,
  .gallery-item--medium,
  .gallery-item--small {
    grid-column: span 1 !important;
    grid-row: span 1 !important;
  }

  /* Scrapbook Section: 2-Column Vintage Layout */
  .scrapbook-grid {
    display: grid !important;
    grid-template-columns: repeat(2, 1fr) !important;
    grid-auto-rows: minmax(220px, auto) !important;
    gap: 20px !important;
    padding-bottom: var(--s-8) !important;
  }
  .scrap-card--large {
    grid-column: span 1 !important;
    grid-row: span 1 !important;
  }
  .scrap-card--small {
    grid-column: span 1 !important;
    grid-row: span 1 !important;
  }
  .scrap-card--wide {
    grid-column: span 2 !important;
    grid-row: span 1 !important;
    max-width: 640px !important;
    margin: 0 auto !important;
    width: 100% !important;
  }

  /* Mosaic Section: 2-Column Wall of Memories */
  .mosaic-grid {
    display: grid !important;
    grid-template-columns: repeat(2, 1fr) !important;
    grid-auto-rows: minmax(200px, 240px) !important;
    gap: 12px !important;
  }
  .mosaic-tile--featured,
  .mosaic-tile--large {
    grid-column: span 2 !important;
  }
  .mosaic-tile--wide,
  .mosaic-tile--tall,
  .mosaic-tile {
    grid-column: span 1 !important;
  }

  /* Secret Envelope Section */
  .secret-envelope-wrapper {
    max-width: min(520px, 86vw) !important;
    margin: 110px auto 35px !important;
  }
  .secret-envelope {
    width: min(520px, 86vw) !important;
    height: min(320px, 52vw) !important;
  }
  .secret-card {
    min-height: 240px !important;
    padding: 1.8rem 1.6rem !important;
  }

  /* Handcrafted Letter Section */
  .envelope-wrapper {
    max-width: min(540px, 88vw) !important;
    margin: 140px auto 45px !important;
  }
  .envelope {
    width: min(540px, 88vw) !important;
    height: min(340px, 54vw) !important;
  }
  .letter-stationery {
    width: min(500px, 86vw) !important;
    padding: 2.2rem 2.4rem !important;
  }
  .letter-para {
    font-size: 0.98rem !important;
    line-height: 1.85 !important;
  }

  /* Final Cinematic Section */
  #final-scene {
    padding: 4.5rem 1.6rem 5.5rem !important;
    min-height: auto !important;
  }
  .final-scene-content {
    max-width: 520px !important;
    margin: 0 auto !important;
  }
  .final-heading {
    font-size: clamp(2.2rem, 5vw, 3.2rem) !important;
  }
  .final-photo-frame {
    max-width: 380px !important;
    width: 78vw !important;
    margin: 1.5rem auto 2rem !important;
  }
}

/* ────────────────────────────────────────────────────────────
   2. TABLET LANDSCAPE COMPOSITIONS (1024x768)
   iPad Landscape, 10" - 12" widescreen tablets
──────────────────────────────────────────────────────────── */
@media (min-width: 961px) and (max-width: 1100px) and (orientation: landscape),
       (min-width: 900px) and (max-width: 1040px) {

  /* Compact Desktop Nav for Landscape Tablet */
  #nav {
    padding: 0.8rem 1.6rem;
  }
  .nav-menu-btn {
    display: none !important;
  }
  .nav-links {
    display: flex !important;
    position: static !important;
    height: auto !important;
    width: auto !important;
    background: transparent !important;
    backdrop-filter: none !important;
    box-shadow: none !important;
    padding: 0 !important;
    gap: 0.75rem !important;
  }
  .nav-links a {
    font-size: 0.58rem !important;
    letter-spacing: 0.18em !important;
  }
  .nav-planet-tag {
    font-size: 0.48rem !important;
    padding: 0.05rem 0.25rem !important;
    margin-left: 0.2rem !important;
  }

  /* Hero Section: Landscape Tablet Spread */
  .hero-layout {
    display: grid !important;
    grid-template-columns: 1.15fr 0.85fr !important;
    min-height: 100vh !important;
    align-items: center !important;
  }
  .hero-left {
    padding: 3.5rem 2rem 3rem 3.5rem !important;
  }
  .hero-heading {
    font-size: clamp(2.5rem, 4.2vw, 3.8rem) !important;
  }
  .hero-right {
    padding: 2.5rem 3.5rem 2.5rem 1rem !important;
  }
  .hero-frame {
    max-height: 75vh !important;
    aspect-ratio: 4/5 !important;
  }

  /* 3D Planetary Universe: Landscape Tablet Composition */
  #universe {
    height: 100vh !important;
    min-height: 100vh !important;
    overflow: hidden !important;
    position: relative !important;
  }
  #universe-nodes {
    position: absolute !important;
    inset: 0 !important;
    z-index: 7 !important;
    pointer-events: none !important;
    display: block !important;
  }
  .universe-heading-area {
    position: absolute !important;
    top: 3.5rem !important;
    left: 50% !important;
    transform: translateX(-50%) !important;
    z-index: 6 !important;
    text-align: center !important;
    width: 90% !important;
    max-width: 480px !important;
  }
  .universe-heading-area .t-h2 {
    font-size: 1.8rem !important;
  }
  .universe-planet-card {
    position: absolute !important;
    pointer-events: auto !important;
    max-width: 190px !important;
    padding: 0.45rem 0.75rem !important;
    border-radius: 10px !important;
    z-index: 8 !important;
  }
  .universe-planet-card--earth   { left: 3% !important; top: 30% !important; transform: none !important; }
  .universe-planet-card--mars    { right: 3% !important; top: 22% !important; transform: none !important; }
  .universe-planet-card--moon    { left: 3% !important; top: 66% !important; transform: none !important; }
  .universe-planet-card--jupiter { right: 3% !important; top: 64% !important; transform: none !important; }
  .universe-planet-card--saturn  { left: 50% !important; top: auto !important; bottom: 2% !important; transform: translateX(-50%) !important; }

  /* Gallery, Scrapbook, Mosaic Landscape */
  .gallery-grid {
    grid-template-columns: repeat(12, 1fr) !important;
    grid-auto-rows: 220px !important;
    gap: 12px !important;
  }
  .gallery-item--featured { grid-column: span 6 !important; }
  .gallery-item--wide { grid-column: span 6 !important; }

  .scrapbook-grid {
    grid-template-columns: repeat(12, 1fr) !important;
    grid-auto-rows: minmax(210px, auto) !important;
    gap: 16px !important;
  }
  .scrap-card--large { grid-column: span 5 !important; grid-row: span 2 !important; }
  .scrap-card--small { grid-column: span 3 !important; grid-row: span 1 !important; }
  .scrap-card--wide  { grid-column: span 7 !important; grid-row: span 2 !important; }

  .mosaic-grid {
    grid-template-columns: repeat(12, 1fr) !important;
    grid-auto-rows: 190px !important;
    gap: 8px !important;
  }

  /* Envelopes in Landscape */
  .secret-envelope-wrapper { max-width: 520px !important; margin: 90px auto 30px !important; }
  .envelope-wrapper { max-width: 540px !important; margin: 120px auto 40px !important; }
}

/* ────────────────────────────────────────────────────────────
   3. MOBILE PHONES (max-width: 599px)
──────────────────────────────────────────────────────────── */
@media (max-width: 599px) {
  /* Nav */
  .nav-menu-btn { display: flex !important; }
  .nav-links {
    position: fixed;
    top: 0; right: -100%;
    height: 100vh;
    width: min(280px, 85vw);
    flex-direction: column;
    justify-content: center;
    background: rgba(243, 231, 214, 0.97);
    backdrop-filter: blur(20px);
    padding: var(--s-8) var(--s-6);
    gap: var(--s-4);
    transition: right 0.45s var(--ease-out);
    box-shadow: -4px 0 30px rgba(73, 50, 36, 0.12);
  }
  .nav-links.open { right: 0; }
  .nav-links a { font-size: 0.82rem; }
  #nav { padding: 0.8rem 1rem; }

  /* Hero — stacked */
  .hero-layout { grid-template-columns: 1fr; min-height: 100svh; }
  .hero-left {
    order: 2;
    padding: var(--s-8) var(--s-4);
    background: var(--cream);
  }
  .hero-right {
    order: 1;
    height: 48svh;
    min-height: 300px;
  }
  .hero-vertical-label { display: none; }
  .hero-num { display: none; }
  .hero-annotation { display: none; }
  .hero-heading { font-size: clamp(2.2rem, 8vw, 3.2rem); }

  /* Universe — vertical scroll stack */
  #universe { min-height: auto; height: auto; padding: 2rem 0 3rem; }
  #universe-nodes {
    position: relative;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 0.9rem;
    padding: var(--s-6) var(--s-4) var(--s-10);
    z-index: 7;
  }
  .universe-planet-card {
    position: static !important;
    width: 100% !important;
    max-width: 330px !important;
    transform: none !important;
  }
  .universe-orbit-ring { display: none; }
  .universe-center { position: static; transform: none; margin: var(--s-8) auto 0; padding: 0 var(--s-4); }
  .universe-heading-area { position: static; transform: none; padding: var(--s-8) var(--s-4) 0; }
  .universe-constellation-svg { display: none; }
  .universe-scroll-hint { display: none; }

  /* Content Grids */
  .gallery-grid, .scrapbook-grid, .mosaic-grid {
    grid-template-columns: 1fr !important;
    grid-auto-rows: 240px !important;
  }
  .gallery-item--featured, .gallery-item--wide, .gallery-item,
  .scrap-card--large, .scrap-card--wide, .scrap-card,
  .mosaic-tile--large, .mosaic-tile--wide, .mosaic-tile {
    grid-column: span 1 !important;
    grid-row: span 1 !important;
  }

  /* Envelope & Letter */
  .letter-envelope-wrap { max-width: 94vw; margin-top: 110px; margin-bottom: 25px; }
  .letter-env-outer { height: 260px; }
  .letter-card { padding: 1.8rem 1.4rem; min-height: 440px; }
  .letter-heading { font-size: 1.55rem; }
  .letter-para { font-size: 0.95rem; line-height: 1.9; }

  .secret-envelope-wrap { max-width: 90vw; margin-top: 75px; margin-bottom: 20px; }
  .secret-env-outer { height: 210px; }
  .secret-card { min-height: 220px; padding: 1.4rem 1.2rem; }

  .final-photo-frame { max-width: 320px; }
  #lb-prev { left: 0.4rem; width: 36px; height: 36px; }
  #lb-next { right: 0.4rem; width: 36px; height: 36px; }
  .lightbox-close { top: -2.5rem; }
}
"""

with open('src/styles/responsive.css', 'w', encoding='utf-8') as f:
    f.write(base_css + new_responsive_css)

print("Successfully injected comprehensive tablet & responsive rules into responsive.css!")
