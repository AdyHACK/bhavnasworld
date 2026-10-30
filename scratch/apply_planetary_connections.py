import sys
sys.stdout.reconfigure(encoding='utf-8')

# 1. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Update Nav Links
old_nav = """      <ul class="nav-links" id="nav-link-list" role="list">
        <li><a href="#hero" data-section="hero">Home</a></li>
        <li><a href="#universe" data-section="universe">Universe</a></li>
        <li><a href="#gallery" data-section="gallery">Gallery</a></li>
        <li><a href="#scrapbook" data-section="scrapbook">Scrapbook</a></li>
        <li><a href="#secret" data-section="secret">Surprise</a></li>
        <li><a href="#letter-section" data-section="letter-section">Letter</a></li>
      </ul>"""

new_nav = """      <ul class="nav-links" id="nav-link-list" role="list">
        <li><a href="#hero" data-section="hero">Home</a></li>
        <li><a href="#universe" data-section="universe">Universe</a></li>
        <li><a href="#gallery" data-section="gallery">Gallery <span class="nav-planet-tag">Terra</span></a></li>
        <li><a href="#scrapbook" data-section="scrapbook">Scrapbook <span class="nav-planet-tag">Ares</span></a></li>
        <li><a href="#mosaic" data-section="mosaic">Mosaic <span class="nav-planet-tag">Jove</span></a></li>
        <li><a href="#secret" data-section="secret">Surprise <span class="nav-planet-tag">Luna</span></a></li>
        <li><a href="#letter-section" data-section="letter-section">Letter <span class="nav-planet-tag">Chronos</span></a></li>
      </ul>"""

assert old_nav in html, "old_nav not found"
html = html.replace(old_nav, new_nav, 1)
print("Updated nav links with planetary indicators.")

# Update Universe SVG Constellation and Destination Cards
old_constellation_and_nodes = """      <!-- SVG orbital ellipses & constellation paths -->
      <svg id="universe-constellation" class="universe-constellation-svg" aria-hidden="true"
           viewBox="0 0 100 100" preserveAspectRatio="none">
        <!-- Planetary Orbital Ellipses -->
        <ellipse cx="50" cy="50" rx="38" ry="26" fill="none" stroke="rgba(189,149,107,0.22)" stroke-width="0.35" stroke-dasharray="1.5 2.5" />
        <ellipse cx="50" cy="50" rx="46" ry="34" fill="none" stroke="rgba(189,149,107,0.18)" stroke-width="0.3" stroke-dasharray="2 3" />
        <ellipse cx="50" cy="50" rx="28" ry="18" fill="none" stroke="rgba(189,149,107,0.25)" stroke-width="0.35" stroke-dasharray="1 2" />
        <!-- Constellation Alignment Guide Lines -->
        <g id="constellation-paths" fill="none" stroke="rgba(189,149,107,0.24)" stroke-width="0.32">
          <line x1="22" y1="34" x2="78" y2="31" stroke-dasharray="1 3"/>
          <line x1="78" y1="31" x2="82" y2="65" stroke-dasharray="1.5 2.5"/>
          <line x1="82" y1="65" x2="51" y2="79" stroke-dasharray="1 3"/>
          <line x1="51" y1="79" x2="23" y2="69" stroke-dasharray="1.5 2.5"/>
          <line x1="23" y1="69" x2="22" y2="34" stroke-dasharray="1 3"/>
          <line x1="22" y1="34" x2="50" y2="50" stroke-dasharray="0.8 4"/>
          <line x1="78" y1="31" x2="50" y2="50" stroke-dasharray="0.8 4"/>
          <line x1="82" y1="65" x2="50" y2="50" stroke-dasharray="0.8 4"/>
          <line x1="23" y1="69" x2="50" y2="50" stroke-dasharray="0.8 4"/>
          <line x1="51" y1="79" x2="50" y2="50" stroke-dasharray="0.8 4"/>
        </g>
      </svg>

      <!-- Central decorative motif -->
      <div class="universe-center" aria-hidden="true">
        <div class="universe-center-ring universe-center-ring--outer anim-rotate-gentle"></div>
        <div class="universe-center-ring universe-center-ring--inner anim-orbit-reverse" style="--orbit-dur:38s;"></div>
        <p class="universe-center-title">
          <span class="universe-center-ornament">✦</span>
          <span id="universe-name">Bhavna's</span>
          <br>
          <em>little universe</em>
          <span class="universe-center-ornament">✦</span>
        </p>
      </div>

      <!-- Heading area -->
      <div class="universe-heading-area">
        <p class="t-eyebrow reveal-up" data-delay="100" style="--reveal-delay:100ms;
           color:var(--chestnut); display:block; text-align:center; opacity:0.85;">
          EXPLORE
        </p>
        <h2 class="t-h2 reveal-up" data-delay="220" style="--reveal-delay:220ms;
           color:var(--deep-espresso); font-weight:400; margin-top:0.6rem; text-align:center; opacity:0.9;">
          Choose your destination
        </h2>
      </div>

      <!-- Universe destination observatory cards -->
      <div id="universe-nodes" aria-label="Navigation destinations">
        <!-- Earth -->
        <a href="#gallery" class="universe-planet-card universe-planet-card--earth" data-planet="earth" id="planet-card-earth" aria-label="Navigate to The Gallery (Earth)">
          <div class="planet-card-pill">
            <span class="planet-pill-astronomy">TERRA • III</span>
            <span class="planet-pill-status">HABITABLE</span>
          </div>
          <div class="planet-card-title-wrap">
            <span class="planet-card-title">THE GALLERY</span>
            <span class="planet-card-arrow" aria-hidden="true">↗</span>
          </div>
          <p class="planet-card-meta">An exhibition of timeless portraits</p>
        </a>

        <!-- Mars -->
        <a href="#scrapbook" class="universe-planet-card universe-planet-card--mars" data-planet="mars" id="planet-card-mars" aria-label="Navigate to Little Moments (Mars)">
          <div class="planet-card-pill">
            <span class="planet-pill-astronomy">ARES • IV</span>
            <span class="planet-pill-status">TERRESTRIAL</span>
          </div>
          <div class="planet-card-title-wrap">
            <span class="planet-card-title">LITTLE MOMENTS</span>
            <span class="planet-card-arrow" aria-hidden="true">↗</span>
          </div>
          <p class="planet-card-meta">Quiet details & golden hours</p>
        </a>

        <!-- Jupiter -->
        <a href="#scrapbook" class="universe-planet-card universe-planet-card--jupiter" data-planet="jupiter" id="planet-card-jupiter" aria-label="Navigate to The Scrapbook (Jupiter)">
          <div class="planet-card-pill">
            <span class="planet-pill-astronomy">JOVE • V</span>
            <span class="planet-pill-status">GAS GIANT</span>
          </div>
          <div class="planet-card-title-wrap">
            <span class="planet-card-title">THE SCRAPBOOK</span>
            <span class="planet-card-arrow" aria-hidden="true">↗</span>
          </div>
          <p class="planet-card-meta">Keepsakes, notes & memories</p>
        </a>

        <!-- Moon -->
        <a href="#secret" class="universe-planet-card universe-planet-card--moon" data-planet="moon" id="planet-card-moon" aria-label="Navigate to A Little Secret (The Moon)">
          <div class="planet-card-pill">
            <span class="planet-pill-astronomy">LUNA • I</span>
            <span class="planet-pill-status">CRATER ARCHIVE</span>
          </div>
          <div class="planet-card-title-wrap">
            <span class="planet-card-title">A LITTLE SECRET</span>
            <span class="planet-card-arrow" aria-hidden="true">↗</span>
          </div>
          <p class="planet-card-meta">A hidden postal envelope</p>
        </a>

        <!-- Saturn -->
        <a href="#letter-section" class="universe-planet-card universe-planet-card--saturn" data-planet="saturn" id="planet-card-saturn" aria-label="Navigate to One Last Thing (Saturn)">
          <div class="planet-card-pill">
            <span class="planet-pill-astronomy">CHRONOS • VI</span>
            <span class="planet-pill-status">RINGED SYSTEM</span>
          </div>
          <div class="planet-card-title-wrap">
            <span class="planet-card-title">ONE LAST THING</span>
            <span class="planet-card-arrow" aria-hidden="true">↗</span>
          </div>
          <p class="planet-card-meta">A handcrafted personal letter</p>
        </a>
      </div>"""

new_constellation_and_nodes = """      <!-- SVG orbital ellipses & constellation paths -->
      <svg id="universe-constellation" class="universe-constellation-svg" aria-hidden="true"
           viewBox="0 0 100 100" preserveAspectRatio="none">
        <!-- Planetary Orbital Ellipses -->
        <ellipse cx="50" cy="50" rx="38" ry="26" fill="none" stroke="rgba(189,149,107,0.25)" stroke-width="0.4" stroke-dasharray="1.5 2.5" />
        <ellipse cx="50" cy="50" rx="46" ry="34" fill="none" stroke="rgba(189,149,107,0.20)" stroke-width="0.3" stroke-dasharray="2 3" />
        <ellipse cx="50" cy="50" rx="28" ry="18" fill="none" stroke="rgba(189,149,107,0.28)" stroke-width="0.4" stroke-dasharray="1 2" />

        <!-- Direct Planet-to-Card Connecting Hairlines -->
        <!-- Earth line (planet ~18,33 to card ~12,38) -->
        <line x1="18" y1="33" x2="12" y2="38" stroke="rgba(189,149,107,0.45)" stroke-width="0.4" stroke-dasharray="1 2" class="planet-connector-line planet-connector-earth" />
        <circle cx="18" cy="33" r="0.6" fill="#DFC29D" opacity="0.8" />
        <!-- Mars line (planet ~80,25 to card ~86,26) -->
        <line x1="80" y1="25" x2="86" y2="26" stroke="rgba(189,149,107,0.45)" stroke-width="0.4" stroke-dasharray="1 2" class="planet-connector-line planet-connector-mars" />
        <circle cx="80" cy="25" r="0.6" fill="#DFC29D" opacity="0.8" />
        <!-- Jupiter line (planet ~82,67 to card ~86,68) -->
        <line x1="82" y1="67" x2="86" y2="68" stroke="rgba(189,149,107,0.45)" stroke-width="0.4" stroke-dasharray="1 2" class="planet-connector-line planet-connector-jupiter" />
        <circle cx="82" cy="67" r="0.6" fill="#DFC29D" opacity="0.8" />
        <!-- Moon line (planet ~18,71 to card ~12,72) -->
        <line x1="18" y1="71" x2="12" y2="72" stroke="rgba(189,149,107,0.45)" stroke-width="0.4" stroke-dasharray="1 2" class="planet-connector-line planet-connector-moon" />
        <circle cx="18" cy="71" r="0.6" fill="#DFC29D" opacity="0.8" />
        <!-- Saturn line (planet ~50,81 to card ~50,88) -->
        <line x1="50" y1="81" x2="50" y2="88" stroke="rgba(189,149,107,0.45)" stroke-width="0.4" stroke-dasharray="1 2" class="planet-connector-line planet-connector-saturn" />
        <circle cx="50" cy="81" r="0.6" fill="#DFC29D" opacity="0.8" />

        <!-- Inter-Planetary Constellation Journey Vector -->
        <g id="constellation-paths" fill="none" stroke="rgba(189,149,107,0.28)" stroke-width="0.35">
          <line x1="18" y1="33" x2="80" y2="25" stroke-dasharray="1 3"/>
          <line x1="80" y1="25" x2="82" y2="67" stroke-dasharray="1.5 2.5"/>
          <line x1="82" y1="67" x2="50" y2="81" stroke-dasharray="1 3"/>
          <line x1="50" y1="81" x2="18" y2="71" stroke-dasharray="1.5 2.5"/>
          <line x1="18" y1="71" x2="18" y2="33" stroke-dasharray="1 3"/>
          <!-- Central Sun Connections -->
          <line x1="18" y1="33" x2="50" y2="50" stroke-dasharray="0.8 4"/>
          <line x1="80" y1="25" x2="50" y2="50" stroke-dasharray="0.8 4"/>
          <line x1="82" y1="67" x2="50" y2="50" stroke-dasharray="0.8 4"/>
          <line x1="18" y1="71" x2="50" y2="50" stroke-dasharray="0.8 4"/>
          <line x1="50" y1="81" x2="50" y2="50" stroke-dasharray="0.8 4"/>
        </g>
      </svg>

      <!-- Central decorative motif -->
      <div class="universe-center" aria-hidden="true">
        <div class="universe-center-ring universe-center-ring--outer anim-rotate-gentle"></div>
        <div class="universe-center-ring universe-center-ring--inner anim-orbit-reverse" style="--orbit-dur:38s;"></div>
        <p class="universe-center-title">
          <span class="universe-center-ornament">✦</span>
          <span id="universe-name">Bhavna's</span>
          <br>
          <em>little universe</em>
          <span class="universe-center-ornament">✦</span>
        </p>
      </div>

      <!-- Heading area -->
      <div class="universe-heading-area">
        <p class="t-eyebrow reveal-up" data-delay="100" style="--reveal-delay:100ms;
           color:var(--chestnut); display:block; text-align:center; opacity:0.85;">
          INTERACTIVE SOLAR SYSTEM
        </p>
        <h2 class="t-h2 reveal-up" data-delay="220" style="--reveal-delay:220ms;
           color:var(--deep-espresso); font-weight:400; margin-top:0.6rem; text-align:center; opacity:0.9;">
          Choose your planetary destination
        </h2>
      </div>

      <!-- Universe destination observatory cards -->
      <div id="universe-nodes" aria-label="Navigation destinations">
        <!-- Earth -> Gallery -->
        <a href="#gallery" class="universe-planet-card universe-planet-card--earth" data-planet="earth" id="planet-card-earth" aria-label="Navigate to The Gallery (Earth)">
          <div class="planet-card-pill">
            <span class="planet-pill-astronomy">TERRA • III</span>
            <span class="planet-pill-status">HABITABLE WORLD</span>
          </div>
          <div class="planet-card-title-wrap">
            <span class="planet-card-title">THE GALLERY</span>
            <span class="planet-card-arrow" aria-hidden="true">↗</span>
          </div>
          <p class="planet-card-meta">Connected to Scene 03 • Photo Exhibition</p>
          <div class="planet-card-travel">TRAVEL TO WORLD ↓</div>
        </a>

        <!-- Mars -> Scrapbook -->
        <a href="#scrapbook" class="universe-planet-card universe-planet-card--mars" data-planet="mars" id="planet-card-mars" aria-label="Navigate to Little Moments (Mars)">
          <div class="planet-card-pill">
            <span class="planet-pill-astronomy">ARES • IV</span>
            <span class="planet-pill-status">TERRESTRIAL</span>
          </div>
          <div class="planet-card-title-wrap">
            <span class="planet-card-title">LITTLE MOMENTS</span>
            <span class="planet-card-arrow" aria-hidden="true">↗</span>
          </div>
          <p class="planet-card-meta">Connected to Scene 04 • Vintage Scrapbook</p>
          <div class="planet-card-travel">TRAVEL TO WORLD ↓</div>
        </a>

        <!-- Jupiter -> Mosaic -->
        <a href="#mosaic" class="universe-planet-card universe-planet-card--jupiter" data-planet="jupiter" id="planet-card-jupiter" aria-label="Navigate to The Photo Mosaic (Jupiter)">
          <div class="planet-card-pill">
            <span class="planet-pill-astronomy">JOVE • V</span>
            <span class="planet-pill-status">GAS GIANT</span>
          </div>
          <div class="planet-card-title-wrap">
            <span class="planet-card-title">PHOTO MOSAIC</span>
            <span class="planet-card-arrow" aria-hidden="true">↗</span>
          </div>
          <p class="planet-card-meta">Connected to Scene 05 • Exhibition Wall</p>
          <div class="planet-card-travel">TRAVEL TO WORLD ↓</div>
        </a>

        <!-- Moon -> Secret -->
        <a href="#secret" class="universe-planet-card universe-planet-card--moon" data-planet="moon" id="planet-card-moon" aria-label="Navigate to A Little Secret (The Moon)">
          <div class="planet-card-pill">
            <span class="planet-pill-astronomy">LUNA • I</span>
            <span class="planet-pill-status">CRATER ARCHIVE</span>
          </div>
          <div class="planet-card-title-wrap">
            <span class="planet-card-title">A LITTLE SECRET</span>
            <span class="planet-card-arrow" aria-hidden="true">↗</span>
          </div>
          <p class="planet-card-meta">Connected to Scene 06 • Surprise Envelope</p>
          <div class="planet-card-travel">TRAVEL TO WORLD ↓</div>
        </a>

        <!-- Saturn -> Letter -->
        <a href="#letter-section" class="universe-planet-card universe-planet-card--saturn" data-planet="saturn" id="planet-card-saturn" aria-label="Navigate to One Last Thing (Saturn)">
          <div class="planet-card-pill">
            <span class="planet-pill-astronomy">CHRONOS • VI</span>
            <span class="planet-pill-status">RINGED SYSTEM</span>
          </div>
          <div class="planet-card-title-wrap">
            <span class="planet-card-title">ONE LAST THING</span>
            <span class="planet-card-arrow" aria-hidden="true">↗</span>
          </div>
          <p class="planet-card-meta">Connected to Scene 07 • Handcrafted Letter</p>
          <div class="planet-card-travel">TRAVEL TO WORLD ↓</div>
        </a>
      </div>"""

assert old_constellation_and_nodes in html, "old_constellation_and_nodes not found"
html = html.replace(old_constellation_and_nodes, new_constellation_and_nodes, 1)
print("Updated Universe constellation connectors and cards.")

# 3. Add Planetary Origin Badges into Section 01: Gallery
target_gallery = '<span class="section-num">01</span>'
repl_gallery = """<span class="section-num">01</span>

          <!-- Planetary Connection: Earth (Terra • III) -->
          <div class="section-planet-origin reveal-up" data-delay="30">
            <span class="origin-planet-icon origin-planet-icon--earth" aria-hidden="true"></span>
            <span class="origin-planet-tag">DESTINATION 01 • TERRA (EARTH)</span>
            <span class="origin-sep">✦</span>
            <a href="#universe" class="origin-orbit-link">Return to Solar Orbit ↑</a>
          </div>"""
assert target_gallery in html, "target_gallery not found"
html = html.replace(target_gallery, repl_gallery, 1)

# 4. Add Planetary Origin Badges into Section 02: Scrapbook
target_scrap = '<span class="section-num" style="color:var(--chestnut); opacity:0.72;">02</span>'
repl_scrap = """<span class="section-num" style="color:var(--chestnut); opacity:0.72;">02</span>

          <!-- Planetary Connection: Mars (Ares • IV) -->
          <div class="section-planet-origin reveal-up" data-delay="30">
            <span class="origin-planet-icon origin-planet-icon--mars" aria-hidden="true"></span>
            <span class="origin-planet-tag">DESTINATION 02 • ARES (MARS)</span>
            <span class="origin-sep">✦</span>
            <a href="#universe" class="origin-orbit-link">Return to Solar Orbit ↑</a>
          </div>"""
assert target_scrap in html, "target_scrap not found"
html = html.replace(target_scrap, repl_scrap, 1)

# 5. Add Planetary Origin Badges into Section 03: Mosaic
target_mosaic = '<span class="section-num">03</span>'
repl_mosaic = """<span class="section-num">03</span>

          <!-- Planetary Connection: Jupiter (Jove • V) -->
          <div class="section-planet-origin reveal-up" data-delay="30">
            <span class="origin-planet-icon origin-planet-icon--jupiter" aria-hidden="true"></span>
            <span class="origin-planet-tag">DESTINATION 03 • JOVE (JUPITER)</span>
            <span class="origin-sep">✦</span>
            <a href="#universe" class="origin-orbit-link">Return to Solar Orbit ↑</a>
          </div>"""
assert target_mosaic in html, "target_mosaic not found"
html = html.replace(target_mosaic, repl_mosaic, 1)

# 6. Add Planetary Origin Badges into Section 04: Secret
target_secret = '<span class="section-num">04</span>'
repl_secret = """<span class="section-num">04</span>

        <!-- Planetary Connection: The Moon (Luna • I) -->
        <div class="section-planet-origin reveal-up" data-delay="30" style="margin-left:auto; margin-right:auto;">
          <span class="origin-planet-icon origin-planet-icon--moon" aria-hidden="true"></span>
          <span class="origin-planet-tag">DESTINATION 04 • LUNA (THE MOON)</span>
          <span class="origin-sep">✦</span>
          <a href="#universe" class="origin-orbit-link">Return to Solar Orbit ↑</a>
        </div>"""
assert target_secret in html, "target_secret not found"
html = html.replace(target_secret, repl_secret, 1)

# 7. Add Planetary Origin Badges into Section 05: Letter
target_letter = '<span class="section-num">05</span>'
repl_letter = """<span class="section-num">05</span>

        <!-- Planetary Connection: Saturn (Chronos • VI) -->
        <div class="section-planet-origin reveal-up" data-delay="30" style="margin-left:auto; margin-right:auto;">
          <span class="origin-planet-icon origin-planet-icon--saturn" aria-hidden="true"></span>
          <span class="origin-planet-tag">DESTINATION 05 • CHRONOS (SATURN)</span>
          <span class="origin-sep">✦</span>
          <a href="#universe" class="origin-orbit-link">Return to Solar Orbit ↑</a>
        </div>"""
assert target_letter in html, "target_letter not found"
html = html.replace(target_letter, repl_letter, 1)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Successfully updated index.html with all planetary connections!")
