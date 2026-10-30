# Script to generate the luxury background HTML snippets for each section

hero_bg = '''      <!-- ══════════════════════════════════════════════════════
           LUXURY BACKGROUND — HOMEPAGE / HERO
      ══════════════════════════════════════════════════════════ -->
      <div class="section-bg section-bg--hero" aria-hidden="true">
        <!-- Soft Dappled Sunlight Beam -->
        <div class="hero-sunbeam"></div>

        <!-- Botanical Corner Illustration — Top Left (Wild Olive Branch) -->
        <svg class="hero-botanical-tl" viewBox="0 0 160 160" fill="none">
          <path d="M 12 12 C 45 35, 75 75, 125 135" stroke="currentColor" stroke-width="0.9" stroke-linecap="round"/>
          <path d="M 38 32 C 48 20, 68 22, 62 38 C 56 50, 42 42, 38 32 Z" fill="currentColor" fill-opacity="0.12" stroke="currentColor" stroke-width="0.75"/>
          <path d="M 52 50 C 65 42, 82 46, 78 60 C 72 72, 58 64, 52 50 Z" fill="currentColor" fill-opacity="0.12" stroke="currentColor" stroke-width="0.75"/>
          <path d="M 72 74 C 88 66, 102 72, 98 86 C 92 98, 78 88, 72 74 Z" fill="currentColor" fill-opacity="0.12" stroke="currentColor" stroke-width="0.75"/>
          <path d="M 94 102 C 110 94, 126 100, 120 115 C 114 126, 100 116, 94 102 Z" fill="currentColor" fill-opacity="0.12" stroke="currentColor" stroke-width="0.75"/>
          <!-- Hanging Olive Berries -->
          <circle cx="48" cy="42" r="3" stroke="currentColor" stroke-width="0.75" fill="none"/>
          <circle cx="85" cy="78" r="3.2" stroke="currentColor" stroke-width="0.75" fill="none"/>
          <circle cx="106" cy="108" r="3.5" stroke="currentColor" stroke-width="0.75" fill="none"/>
        </svg>

        <!-- Botanical Corner Illustration — Bottom Right -->
        <svg class="hero-botanical-br" viewBox="0 0 160 160" fill="none">
          <path d="M 12 12 C 45 35, 75 75, 125 135" stroke="currentColor" stroke-width="0.9" stroke-linecap="round"/>
          <path d="M 38 32 C 48 20, 68 22, 62 38 C 56 50, 42 42, 38 32 Z" fill="currentColor" fill-opacity="0.12" stroke="currentColor" stroke-width="0.75"/>
          <path d="M 62 60 C 78 52, 95 58, 88 74 C 82 85, 68 76, 62 60 Z" fill="currentColor" fill-opacity="0.12" stroke="currentColor" stroke-width="0.75"/>
          <path d="M 88 95 C 105 88, 122 94, 115 110 C 108 122, 95 112, 88 95 Z" fill="currentColor" fill-opacity="0.12" stroke="currentColor" stroke-width="0.75"/>
          <circle cx="56" cy="52" r="3" stroke="currentColor" stroke-width="0.75" fill="none"/>
          <circle cx="98" cy="98" r="3.4" stroke="currentColor" stroke-width="0.75" fill="none"/>
        </svg>

        <!-- Vintage Editorial Watermark Medallion -->
        <svg class="hero-editorial-watermark" viewBox="0 0 320 320" fill="none">
          <circle cx="160" cy="160" r="150" stroke="currentColor" stroke-width="0.7" stroke-dasharray="2 3"/>
          <circle cx="160" cy="160" r="142" stroke="currentColor" stroke-width="1.2"/>
          <circle cx="160" cy="160" r="114" stroke="currentColor" stroke-width="0.8"/>
          <!-- Star studs -->
          <circle cx="160" cy="24" r="2" fill="currentColor"/>
          <circle cx="160" cy="296" r="2" fill="currentColor"/>
          <circle cx="24" cy="160" r="2" fill="currentColor"/>
          <circle cx="296" cy="160" r="2" fill="currentColor"/>
          <!-- Circular text path -->
          <path id="hero-seal-path" d="M 160 160 m -128, 0 a 128,128 0 1,1 256,0 a 128,128 0 1,1 -256,0" fill="none"/>
          <text font-family="'DM Sans', sans-serif" font-size="7.5" font-weight="500" letter-spacing="4" fill="currentColor">
            <textPath href="#hero-seal-path" startOffset="0%">
              ✦ HER LITTLE UNIVERSE ✦ COLLECTED MOMENTS • MCMXXIV •
            </textPath>
          </text>
          <!-- Center blossom motif -->
          <g transform="translate(160, 160)">
            <ellipse cx="0" cy="-24" rx="10" ry="20" stroke="currentColor" stroke-width="0.8" fill="none"/>
            <ellipse cx="0" cy="24" rx="10" ry="20" stroke="currentColor" stroke-width="0.8" fill="none"/>
            <ellipse cx="-24" cy="0" rx="20" ry="10" stroke="currentColor" stroke-width="0.8" fill="none"/>
            <ellipse cx="24" cy="0" rx="20" ry="10" stroke="currentColor" stroke-width="0.8" fill="none"/>
            <circle cx="0" cy="0" r="6" stroke="currentColor" stroke-width="0.9" fill="none"/>
            <circle cx="0" cy="0" r="2" fill="currentColor"/>
          </g>
        </svg>
      </div>'''

universe_bg = '''      <!-- ══════════════════════════════════════════════════════
           LUXURY BACKGROUND — UNIVERSE
      ══════════════════════════════════════════════════════════ -->
      <div class="section-bg section-bg--universe" aria-hidden="true">
        <!-- Grand Armillary Sphere Engraving -->
        <svg class="universe-armillary-svg" viewBox="0 0 600 600" fill="none">
          <!-- Concentric Celestial Rings -->
          <circle cx="300" cy="300" r="280" stroke="currentColor" stroke-width="0.75" stroke-dasharray="3 4"/>
          <circle cx="300" cy="300" r="268" stroke="currentColor" stroke-width="1.2"/>
          <circle cx="300" cy="300" r="220" stroke="currentColor" stroke-width="0.8"/>
          <circle cx="300" cy="300" r="160" stroke="currentColor" stroke-width="0.75" stroke-dasharray="2 3"/>
          <circle cx="300" cy="300" r="95" stroke="currentColor" stroke-width="0.8"/>
          <!-- Degree tick marks on outer ring -->
          <circle cx="300" cy="300" r="264" stroke="currentColor" stroke-width="0.6" stroke-dasharray="1 8"/>
          <!-- Tilted Ecliptic Oval -->
          <ellipse cx="300" cy="300" rx="268" ry="120" stroke="currentColor" stroke-width="0.9" transform="rotate(-25 300 300)"/>
          <ellipse cx="300" cy="300" rx="210" ry="85" stroke="currentColor" stroke-width="0.7" stroke-dasharray="2 3" transform="rotate(-25 300 300)"/>
          <!-- Celestial Coordinate Lines -->
          <line x1="300" y1="20" x2="300" y2="580" stroke="currentColor" stroke-width="0.6" stroke-dasharray="3 4"/>
          <line x1="20" y1="300" x2="580" y2="300" stroke="currentColor" stroke-width="0.6" stroke-dasharray="3 4"/>
          <line x1="102" y1="102" x2="498" y2="498" stroke="currentColor" stroke-width="0.5" stroke-dasharray="1 5"/>
          <line x1="102" y1="498" x2="498" y2="102" stroke="currentColor" stroke-width="0.5" stroke-dasharray="1 5"/>
          <!-- Logarithmic Golden Ratio Spiral -->
          <path d="M 300 300 Q 300 240, 360 240 Q 440 240, 440 340 Q 440 480, 260 480 Q 60 480, 60 260 Q 60 40, 320 40" stroke="currentColor" stroke-width="0.65" stroke-dasharray="2 3" fill="none"/>
        </svg>

        <!-- Constellation Star Chart Overlay -->
        <svg class="universe-chart-overlay" viewBox="0 0 1200 800" preserveAspectRatio="none" fill="none">
          <!-- Cygnus (Northern Cross) -->
          <g transform="translate(180, 160)">
            <polyline points="0,0 45,35 90,65 145,105" stroke="currentColor" stroke-width="0.6"/>
            <polyline points="15,65 45,35 75,10" stroke="currentColor" stroke-width="0.6"/>
            <circle cx="0" cy="0" r="2.5" fill="currentColor"/>
            <circle cx="45" cy="35" r="3.2" fill="currentColor"/>
            <circle cx="90" cy="65" r="2.2" fill="currentColor"/>
            <circle cx="145" cy="105" r="3" fill="currentColor"/>
            <circle cx="15" cy="65" r="2" fill="currentColor"/>
            <circle cx="75" cy="10" r="2" fill="currentColor"/>
            <text x="50" y="48" font-family="'Cormorant Garamond', serif" font-size="9" font-style="italic" letter-spacing="1" fill="currentColor" opacity="0.75">Deneb • Cygnus</text>
          </g>
          <!-- Cassiopeia -->
          <g transform="translate(860, 140)">
            <polyline points="0,40 35,0 70,30 110,5 145,45" stroke="currentColor" stroke-width="0.6"/>
            <circle cx="0" cy="40" r="2.2" fill="currentColor"/>
            <circle cx="35" cy="0" r="2.8" fill="currentColor"/>
            <circle cx="70" cy="30" r="2.5" fill="currentColor"/>
            <circle cx="110" cy="5" r="2.2" fill="currentColor"/>
            <circle cx="145" cy="45" r="2.6" fill="currentColor"/>
            <text x="40" y="22" font-family="'Cormorant Garamond', serif" font-size="9" font-style="italic" letter-spacing="1" fill="currentColor" opacity="0.75">Cassiopeia</text>
          </g>
          <!-- Lyra -->
          <g transform="translate(940, 560)">
            <polygon points="25,25 60,10 80,45 45,60" stroke="currentColor" stroke-width="0.55"/>
            <line x1="0" y1="0" x2="25" y2="25" stroke="currentColor" stroke-width="0.65"/>
            <circle cx="0" cy="0" r="3.8" fill="currentColor"/>
            <circle cx="25" cy="25" r="2.2" fill="currentColor"/>
            <circle cx="60" cy="10" r="2" fill="currentColor"/>
            <circle cx="80" cy="45" r="2" fill="currentColor"/>
            <circle cx="45" cy="60" r="2" fill="currentColor"/>
            <text x="8" y="-4" font-family="'Cormorant Garamond', serif" font-size="9" font-style="italic" letter-spacing="1" fill="currentColor" opacity="0.8">Vega • Lyra</text>
          </g>
        </svg>
      </div>'''

gallery_bg = '''      <!-- ══════════════════════════════════════════════════════
           LUXURY BACKGROUND — GALLERY
      ══════════════════════════════════════════════════════════ -->
      <div class="section-bg section-bg--gallery" aria-hidden="true">
        <!-- Neoclassical Architectural Gallery Arches -->
        <svg class="gallery-arch-svg" viewBox="0 0 1200 900" preserveAspectRatio="none" fill="none">
          <!-- Central Arch Pair -->
          <path d="M 250 900 L 250 340 C 250 140, 550 140, 550 340 L 550 900" stroke="currentColor" stroke-width="0.8"/>
          <path d="M 265 900 L 265 345 C 265 160, 535 160, 535 345 L 535 900" stroke="currentColor" stroke-width="0.5" stroke-dasharray="3 3"/>
          <path d="M 650 900 L 650 340 C 650 140, 950 140, 950 340 L 950 900" stroke="currentColor" stroke-width="0.8"/>
          <path d="M 665 900 L 665 345 C 665 160, 935 160, 935 345 L 935 900" stroke="currentColor" stroke-width="0.5" stroke-dasharray="3 3"/>
          <!-- Keystone Flourishes -->
          <path d="M 390 190 L 410 190 L 405 215 L 395 215 Z" stroke="currentColor" stroke-width="0.75" fill="none"/>
          <path d="M 790 190 L 810 190 L 805 215 L 795 215 Z" stroke="currentColor" stroke-width="0.75" fill="none"/>
        </svg>

        <!-- French Rule Architectural Grid Framing -->
        <div class="gallery-french-rule-grid"></div>

        <!-- Catalog Margin Annotations -->
        <span class="gallery-margin-annotation gallery-margin-annotation--tl">EXPOSITION PRIVÉE • SALLE N° I</span>
        <span class="gallery-margin-annotation gallery-margin-annotation--br">ARCHIVE CATALOGUE • PLATE III</span>
      </div>'''

scrapbook_bg = '''      <!-- ══════════════════════════════════════════════════════
           LUXURY BACKGROUND — SCRAPBOOK
      ══════════════════════════════════════════════════════════ -->
      <div class="section-bg section-bg--scrapbook" aria-hidden="true">
        <!-- Herbarium Pressed Fern (Left Side) -->
        <svg class="scrapbook-herbarium-left" viewBox="0 0 200 460" fill="none">
          <path d="M 100 450 C 95 380, 85 240, 115 20" stroke="currentColor" stroke-width="1.1" stroke-linecap="round"/>
          <!-- Frond Pinnae Left & Right -->
          <g stroke="currentColor" stroke-width="0.75" fill="currentColor" fill-opacity="0.10">
            <path d="M 96 390 C 65 380, 40 370, 30 380 C 45 395, 75 398, 95 394 Z"/>
            <path d="M 98 390 C 130 380, 155 372, 165 382 C 150 396, 120 398, 99 393 Z"/>
            <path d="M 92 330 C 60 318, 35 308, 25 318 C 42 334, 72 336, 91 333 Z"/>
            <path d="M 95 330 C 128 318, 158 310, 168 320 C 152 335, 122 338, 96 333 Z"/>
            <path d="M 88 270 C 58 258, 32 248, 24 258 C 40 274, 68 276, 87 273 Z"/>
            <path d="M 92 270 C 124 258, 150 250, 160 260 C 145 274, 118 276, 93 273 Z"/>
            <path d="M 87 210 C 60 198, 38 190, 30 198 C 45 212, 70 214, 86 212 Z"/>
            <path d="M 90 210 C 120 198, 142 192, 150 200 C 136 213, 112 215, 91 212 Z"/>
            <path d="M 92 150 C 70 140, 52 134, 46 142 C 58 154, 78 155, 91 152 Z"/>
            <path d="M 94 150 C 118 140, 136 135, 142 143 C 130 155, 110 156, 95 152 Z"/>
            <path d="M 98 90 C 82 82, 68 78, 64 84 C 74 94, 88 95, 97 92 Z"/>
            <path d="M 100 90 C 118 82, 132 78, 136 84 C 126 94, 112 95, 101 92 Z"/>
          </g>
          <!-- Handwritten Herbarium Label -->
          <text x="25" y="445" font-family="'Cormorant Garamond', serif" font-size="10" font-style="italic" fill="currentColor" opacity="0.65">Herbarium Horti • Specimen N° 24</text>
        </svg>

        <!-- Herbarium Wild Rose (Right Side) -->
        <svg class="scrapbook-herbarium-right" viewBox="0 0 220 440" fill="none">
          <path d="M 110 430 C 115 350, 125 210, 90 20" stroke="currentColor" stroke-width="1.1" stroke-linecap="round"/>
          <!-- Rose Leaves -->
          <g stroke="currentColor" stroke-width="0.75" fill="currentColor" fill-opacity="0.10">
            <path d="M 112 370 C 145 358, 172 364, 178 376 C 160 390, 132 385, 114 374 Z"/>
            <path d="M 108 340 C 75 328, 48 334, 42 346 C 60 360, 88 355, 106 344 Z"/>
            <path d="M 116 270 C 150 258, 178 262, 185 275 C 166 290, 136 284, 118 274 Z"/>
            <path d="M 104 230 C 70 216, 42 222, 36 235 C 55 250, 84 244, 102 233 Z"/>
            <!-- Rosehip / Flower bud at top -->
            <path d="M 88 45 C 72 25, 108 25, 92 45 Z" fill="currentColor" fill-opacity="0.18"/>
            <ellipse cx="90" cy="55" rx="12" ry="16" fill="currentColor" fill-opacity="0.14"/>
          </g>
          <text x="35" y="425" font-family="'Cormorant Garamond', serif" font-size="10" font-style="italic" fill="currentColor" opacity="0.65">Rosa Canina • Collectio Botanica</text>
        </svg>

        <!-- Vintage French Postmark Cancellation (Top Right) -->
        <svg class="scrapbook-postal-mark" viewBox="0 0 140 140" fill="none">
          <circle cx="70" cy="70" r="62" stroke="currentColor" stroke-width="1.2"/>
          <circle cx="70" cy="70" r="54" stroke="currentColor" stroke-width="0.75" stroke-dasharray="2 2"/>
          <!-- Wavy cancellation lines -->
          <path d="M -40 50 Q -20 40 0 50 Q 20 60 40 50" stroke="currentColor" stroke-width="0.9" fill="none"/>
          <path d="M -40 70 Q -20 60 0 70 Q 20 80 40 70" stroke="currentColor" stroke-width="0.9" fill="none"/>
          <path d="M -40 90 Q -20 80 0 90 Q 20 100 40 90" stroke="currentColor" stroke-width="0.9" fill="none"/>
          <!-- Circular Postmark Typography -->
          <path id="scrap-post-path" d="M 70 70 m -46, 0 a 46,46 0 1,1 92,0 a 46,46 0 1,1 -92,0" fill="none"/>
          <text font-family="'DM Sans', sans-serif" font-size="6.5" font-weight="600" letter-spacing="2.2" fill="currentColor">
            <textPath href="#scrap-post-path" startOffset="5%">
              ★ POSTES DE PARIS ★ ARCHIVE 1924
            </textPath>
          </text>
          <text x="70" y="74" font-family="'Cormorant Garamond', serif" font-size="11" font-weight="600" text-anchor="middle" fill="currentColor">15 OCT</text>
        </svg>

        <!-- Vintage Airmail Boxed Cachet (Bottom Left) -->
        <svg class="scrapbook-postal-mark scrapbook-postal-mark--alt" viewBox="0 0 130 65" fill="none">
          <rect x="3" y="3" width="124" height="59" rx="3" stroke="currentColor" stroke-width="1.2"/>
          <rect x="7" y="7" width="116" height="51" stroke="currentColor" stroke-width="0.6" stroke-dasharray="2 2"/>
          <text x="65" y="28" font-family="'DM Sans', sans-serif" font-size="8.5" font-weight="700" letter-spacing="3" text-anchor="middle" fill="currentColor">PAR AVION</text>
          <text x="65" y="46" font-family="'Cormorant Garamond', serif" font-size="8" font-style="italic" letter-spacing="1.5" text-anchor="middle" fill="currentColor">Poste Restante • Service Spécial</text>
        </svg>
      </div>'''

mosaic_bg = '''      <!-- ══════════════════════════════════════════════════════
           LUXURY BACKGROUND — MOSAIC
      ══════════════════════════════════════════════════════════ -->
      <div class="section-bg section-bg--mosaic" aria-hidden="true">
        <!-- Layered Organic Parchment Silhouettes -->
        <div class="mosaic-organic-blob-1"></div>
        <div class="mosaic-organic-blob-2"></div>

        <!-- Refined Architectural Drafting Compass & Golden Spiral -->
        <svg class="mosaic-architectural-svg" viewBox="0 0 800 800" fill="none">
          <!-- Golden Ratio Rectangles & Golden Spiral -->
          <rect x="100" y="100" width="600" height="371" stroke="currentColor" stroke-width="0.8"/>
          <rect x="100" y="100" width="371" height="371" stroke="currentColor" stroke-width="0.6" stroke-dasharray="3 3"/>
          <rect x="471" y="100" width="229" height="229" stroke="currentColor" stroke-width="0.6"/>
          <rect x="471" y="329" width="142" height="142" stroke="currentColor" stroke-width="0.6"/>
          <path d="M 471 471 A 371 371 0 0 1 100 100" stroke="currentColor" stroke-width="0.9" fill="none"/>
          <path d="M 471 100 A 229 229 0 0 1 700 329" stroke="currentColor" stroke-width="0.8" fill="none"/>
          <path d="M 700 329 A 142 142 0 0 1 558 471" stroke="currentColor" stroke-width="0.75" fill="none"/>
          <!-- Diagonal drafting projection guidelines -->
          <line x1="50" y1="750" x2="750" y2="50" stroke="currentColor" stroke-width="0.5" stroke-dasharray="2 4"/>
          <line x1="50" y1="50" x2="750" y2="750" stroke="currentColor" stroke-width="0.5" stroke-dasharray="2 4"/>
          <!-- Architectural Compass Axis Rings -->
          <circle cx="400" cy="400" r="320" stroke="currentColor" stroke-width="0.6" stroke-dasharray="1 6"/>
          <circle cx="400" cy="400" r="260" stroke="currentColor" stroke-width="0.7"/>
          <circle cx="400" cy="400" r="180" stroke="currentColor" stroke-width="0.5" stroke-dasharray="2 3"/>
          <circle cx="400" cy="400" r="3" fill="currentColor"/>
          <!-- Architectural Caption -->
          <text x="105" y="90" font-family="'DM Sans', sans-serif" font-size="7.5" font-weight="500" letter-spacing="2" fill="currentColor" opacity="0.65">SECTION 03 • ELEVATION ARCHIVE — N 48° 51' 24"</text>
        </svg>
      </div>'''

secret_bg = '''      <!-- ══════════════════════════════════════════════════════
           LUXURY BACKGROUND — SURPRISE / SECRET
      ══════════════════════════════════════════════════════════ -->
      <div class="section-bg section-bg--secret" aria-hidden="true">
        <!-- Postal Chevron Borders -->
        <div class="secret-postal-chevrons"></div>
        <div class="secret-postal-chevrons secret-postal-chevrons--bottom"></div>

        <!-- Ambient Candlelight Halo behind Envelope -->
        <div class="secret-ambient-aura"></div>

        <!-- Heraldic Secret Seal Watermark -->
        <svg class="secret-seal-watermark-svg" viewBox="0 0 360 360" fill="none">
          <circle cx="180" cy="180" r="170" stroke="currentColor" stroke-width="1.2"/>
          <circle cx="180" cy="180" r="162" stroke="currentColor" stroke-width="0.6" stroke-dasharray="2 3"/>
          <circle cx="180" cy="180" r="128" stroke="currentColor" stroke-width="0.8"/>
          <!-- Circular Latin Motto -->
          <path id="secret-watermark-path" d="M 180 180 m -142, 0 a 142,142 0 1,1 284,0 a 142,142 0 1,1 -284,0" fill="none"/>
          <text font-family="'DM Sans', sans-serif" font-size="7.2" font-weight="600" letter-spacing="3.2" fill="currentColor">
            <textPath href="#secret-watermark-path" startOffset="4%">
              ✦ SIGILLUM SECRETI • AD USUM PRIVATUM • MCMXXIV ✦
            </textPath>
          </text>
          <!-- 8-Point Compass Star in Center -->
          <g transform="translate(180, 180)">
            <polygon points="0,-70 12,-16 70,0 16,12 0,70 -12,16 -70,0 -16,-12" stroke="currentColor" stroke-width="0.85" fill="currentColor" fill-opacity="0.08"/>
            <polygon points="0,-48 8,-12 48,0 12,8 0,48 -8,12 -48,0 -12,-8" transform="rotate(45)" stroke="currentColor" stroke-width="0.65" fill="none"/>
            <circle cx="0" cy="0" r="7" stroke="currentColor" stroke-width="0.8" fill="none"/>
            <circle cx="0" cy="0" r="2.5" fill="currentColor"/>
          </g>
        </svg>
      </div>'''

letter_bg = '''      <!-- ══════════════════════════════════════════════════════
           LUXURY BACKGROUND — LETTER
      ══════════════════════════════════════════════════════════ -->
      <div class="section-bg section-bg--letter" aria-hidden="true">
        <!-- Writing-Desk Candlelight Illumination -->
        <div class="letter-desk-light"></div>

        <!-- Grand Blind-Embossed Stationery Crest Watermark -->
        <svg class="letter-stationery-crest-svg" viewBox="0 0 500 500" fill="none">
          <!-- Outer Laurel Wreath -->
          <g stroke="currentColor" stroke-width="0.8" fill="currentColor" fill-opacity="0.09">
            <!-- Left laurel branch -->
            <path d="M 250 430 C 130 430, 80 320, 80 230 C 80 140, 150 70, 230 65"/>
            <!-- Right laurel branch -->
            <path d="M 250 430 C 370 430, 420 320, 420 230 C 420 140, 350 70, 270 65"/>
            <!-- Laurel Leaves -->
            <ellipse cx="100" cy="300" rx="14" ry="7" transform="rotate(-40 100 300)"/>
            <ellipse cx="85" cy="240" rx="14" ry="7" transform="rotate(-15 85 240)"/>
            <ellipse cx="100" cy="180" rx="14" ry="7" transform="rotate(15 100 180)"/>
            <ellipse cx="140" cy="120" rx="14" ry="7" transform="rotate(40 140 120)"/>
            <ellipse cx="400" cy="300" rx="14" ry="7" transform="rotate(40 400 300)"/>
            <ellipse cx="415" cy="240" rx="14" ry="7" transform="rotate(15 415 240)"/>
            <ellipse cx="400" cy="180" rx="14" ry="7" transform="rotate(-15 400 180)"/>
            <ellipse cx="360" cy="120" rx="14" ry="7" transform="rotate(-40 360 120)"/>
          </g>
          <!-- Central Cartouche Frame -->
          <circle cx="250" cy="240" r="110" stroke="currentColor" stroke-width="1.2"/>
          <circle cx="250" cy="240" r="102" stroke="currentColor" stroke-width="0.6" stroke-dasharray="2 3"/>
          <circle cx="250" cy="240" r="80" stroke="currentColor" stroke-width="0.75"/>
          <!-- Radiant Starburst at Top -->
          <path d="M 250 110 L 250 85 M 250 110 L 260 92 M 250 110 L 240 92" stroke="currentColor" stroke-width="0.8"/>
          <!-- Center Monogram -->
          <text x="250" y="248" font-family="'Playfair Display', serif" font-size="28" font-style="italic" text-anchor="middle" fill="currentColor" letter-spacing="3">✦ B ✦</text>
          <!-- Latin Motto Ribbon at Bottom -->
          <path d="M 160 380 Q 250 365 340 380 Q 250 395 160 380 Z" stroke="currentColor" stroke-width="0.75" fill="none"/>
          <text x="250" y="388" font-family="'DM Sans', sans-serif" font-size="7" font-weight="500" letter-spacing="2" text-anchor="middle" fill="currentColor">SCRIPTUM EX CORDE • PERPETUO MANET</text>
        </svg>

        <!-- Classical Acanthus Corner Flourishes -->
        <svg class="letter-corner-flourish letter-corner-flourish--tl" viewBox="0 0 100 100" fill="none">
          <path d="M 12 88 C 12 40, 40 12, 88 12" stroke="currentColor" stroke-width="1"/>
          <path d="M 12 60 C 12 30, 30 12, 60 12" stroke="currentColor" stroke-width="0.6" stroke-dasharray="2 2"/>
          <path d="M 12 12 Q 28 28 44 12 Q 28 28 12 44" stroke="currentColor" stroke-width="0.8" fill="none"/>
          <circle cx="12" cy="12" r="2.5" fill="currentColor"/>
        </svg>
        <svg class="letter-corner-flourish letter-corner-flourish--tr" viewBox="0 0 100 100" fill="none">
          <path d="M 12 88 C 12 40, 40 12, 88 12" stroke="currentColor" stroke-width="1"/>
          <path d="M 12 60 C 12 30, 30 12, 60 12" stroke="currentColor" stroke-width="0.6" stroke-dasharray="2 2"/>
          <path d="M 12 12 Q 28 28 44 12 Q 28 28 12 44" stroke="currentColor" stroke-width="0.8" fill="none"/>
          <circle cx="12" cy="12" r="2.5" fill="currentColor"/>
        </svg>
        <svg class="letter-corner-flourish letter-corner-flourish--bl" viewBox="0 0 100 100" fill="none">
          <path d="M 12 88 C 12 40, 40 12, 88 12" stroke="currentColor" stroke-width="1"/>
          <path d="M 12 60 C 12 30, 30 12, 60 12" stroke="currentColor" stroke-width="0.6" stroke-dasharray="2 2"/>
          <path d="M 12 12 Q 28 28 44 12 Q 28 28 12 44" stroke="currentColor" stroke-width="0.8" fill="none"/>
          <circle cx="12" cy="12" r="2.5" fill="currentColor"/>
        </svg>
        <svg class="letter-corner-flourish letter-corner-flourish--br" viewBox="0 0 100 100" fill="none">
          <path d="M 12 88 C 12 40, 40 12, 88 12" stroke="currentColor" stroke-width="1"/>
          <path d="M 12 60 C 12 30, 30 12, 60 12" stroke="currentColor" stroke-width="0.6" stroke-dasharray="2 2"/>
          <path d="M 12 12 Q 28 28 44 12 Q 28 28 12 44" stroke="currentColor" stroke-width="0.8" fill="none"/>
          <circle cx="12" cy="12" r="2.5" fill="currentColor"/>
        </svg>
      </div>'''

final_bg = '''      <!-- ══════════════════════════════════════════════════════
           LUXURY BACKGROUND — FINAL SCENE
      ══════════════════════════════════════════════════════════ -->
      <div class="section-bg section-bg--final" aria-hidden="true">
        <!-- Cinematic Golden Spotlight Halo -->
        <div class="final-cinematic-halo"></div>

        <!-- Celestial Starlight Ring -->
        <svg class="final-starlight-ring-svg" viewBox="0 0 500 500" fill="none">
          <circle cx="250" cy="250" r="240" stroke="currentColor" stroke-width="0.75" stroke-dasharray="2 4"/>
          <circle cx="250" cy="250" r="228" stroke="currentColor" stroke-width="1.1"/>
          <circle cx="250" cy="250" r="185" stroke="currentColor" stroke-width="0.6"/>
          <!-- Starburst markers around circumference -->
          <g stroke="currentColor" stroke-width="0.7">
            <line x1="250" y1="5" x2="250" y2="25"/>
            <line x1="250" y1="475" x2="250" y2="495"/>
            <line x1="5" y1="250" x2="25" y2="250"/>
            <line x1="475" y1="250" x2="495" y2="250"/>
          </g>
          <!-- Tiny Stars -->
          <circle cx="250" cy="22" r="2" fill="currentColor"/>
          <circle cx="250" cy="478" r="2" fill="currentColor"/>
          <circle cx="22" cy="250" r="2" fill="currentColor"/>
          <circle cx="478" cy="250" r="2" fill="currentColor"/>
        </svg>
      </div>'''

print("All section background templates generated successfully!")
