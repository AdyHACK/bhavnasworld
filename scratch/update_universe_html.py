import sys

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add three.min.js script tag
three_script = '  <!-- 0. Three.js for Realistic 3D Planetary Universe -->\n  <script src="public/vendor/three.min.js"></script>\n'
target_script = '  <!-- 1. Content config -->'
if target_script in content and 'three.min.js' not in content:
    content = content.replace(target_script, three_script + target_script, 1)
    print("Added Three.js script tag.")
else:
    print("Three.js script tag already present or target not found.")

# 2. Update universe section content
old_universe_block = """      <!-- Ambient glow -->
      <div class="universe-glow-center" aria-hidden="true"></div>

      <!-- SVG constellation lines (drawn by JS) -->
      <svg id="universe-constellation" class="universe-constellation-svg" aria-hidden="true"
           viewBox="0 0 100 100" preserveAspectRatio="none">
        <g id="constellation-paths" fill="none" stroke="rgba(189,149,107,0.22)" stroke-width="0.3">
          <line x1="20" y1="35" x2="50" y2="78" />
          <line x1="50" y1="78" x2="82" y2="62" />
          <line x1="20" y1="35" x2="72" y2="22" />
          <line x1="72" y1="22" x2="82" y2="62" />
          <line x1="14" y1="70" x2="50" y2="78" />
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

      <!-- Universe nodes (JS populated) -->
      <div id="universe-nodes" aria-label="Navigation destinations"></div>"""

new_universe_block = """      <!-- Ambient glow -->
      <div class="universe-glow-center" aria-hidden="true"></div>

      <!-- 3D Realistic Planetary Universe Canvas -->
      <canvas id="universe-3d-canvas" aria-label="Interactive 3D Planetary Universe"></canvas>

      <!-- SVG orbital ellipses & constellation paths -->
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

# Test match with LF and CRLF
if old_universe_block in content:
    content = content.replace(old_universe_block, new_universe_block, 1)
    print("Replaced universe block (LF).")
elif old_universe_block.replace('\n', '\r\n') in content:
    content = content.replace(old_universe_block.replace('\n', '\r\n'), new_universe_block.replace('\n', '\r\n'), 1)
    print("Replaced universe block (CRLF).")
else:
    print("Could not find exact old_universe_block. Inspecting...")
    idx = content.find('universe-nodes')
    print("Context around universe-nodes:")
    print(content[idx-300:idx+200])
    raise AssertionError("old_universe_block not matched")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully updated index.html with 3D canvas and destination cards!")
