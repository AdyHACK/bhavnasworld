with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

target = """            <!-- Secret Keepsake Card (Slides out of envelope) -->
            <article id="secret-card" class="secret-card" aria-label="Secret discovery note">
              <button id="secret-close-btn" class="secret-close-btn" aria-label="Close secret note" title="Close note">✕</button>
              <div class="secret-card-border" aria-hidden="true"></div>
              <div class="secret-card-header">
                <span class="secret-card-monogram">✦ PRIVATE DISCOVERY ✦</span>
                <h3 class="secret-card-title">You found it. ✨</h3>
              </div>
              <div class="secret-card-body">
                <p id="secret-message-text" class="secret-message-text">
                  You found the little secret. ✨<br>
                  Some things are made to be discovered.
                </p>
              </div>
              <div class="secret-card-footer" aria-hidden="true">
                <span class="secret-star-flourish">✦ &nbsp; ★ &nbsp; ✦</span>
              </div>
            </article>"""

replacement = """            <!-- Secret Keepsake Card (Slides out of envelope) -->
            <article id="secret-card" class="secret-card" aria-label="Secret keepsake note">
              <button id="secret-close-btn" class="secret-close-btn" aria-label="Close secret note" title="Close note">
                <span class="close-icon">✕</span>
              </button>
              <div class="secret-card-texture" aria-hidden="true"></div>
              <div class="secret-card-border" aria-hidden="true">
                <div class="secret-border-inner">
                  <!-- Corner Botanical Accents -->
                  <svg class="secret-corner-botanical secret-corner--tl" viewBox="0 0 20 20" fill="none" aria-hidden="true">
                    <path d="M2 18 C 2 9, 9 2, 18 2 M 2 2 L 6 6" stroke="rgba(189,149,107,0.5)" stroke-width="0.8" stroke-linecap="round"/>
                  </svg>
                  <svg class="secret-corner-botanical secret-corner--tr" viewBox="0 0 20 20" fill="none" aria-hidden="true">
                    <path d="M2 18 C 2 9, 9 2, 18 2 M 2 2 L 6 6" stroke="rgba(189,149,107,0.5)" stroke-width="0.8" stroke-linecap="round"/>
                  </svg>
                  <svg class="secret-corner-botanical secret-corner--bl" viewBox="0 0 20 20" fill="none" aria-hidden="true">
                    <path d="M2 18 C 2 9, 9 2, 18 2 M 2 2 L 6 6" stroke="rgba(189,149,107,0.5)" stroke-width="0.8" stroke-linecap="round"/>
                  </svg>
                  <svg class="secret-corner-botanical secret-corner--br" viewBox="0 0 20 20" fill="none" aria-hidden="true">
                    <path d="M2 18 C 2 9, 9 2, 18 2 M 2 2 L 6 6" stroke="rgba(189,149,107,0.5)" stroke-width="0.8" stroke-linecap="round"/>
                  </svg>
                </div>
              </div>

              <!-- Header with Tiny Decorative Floral Illustration -->
              <header class="secret-card-header">
                <!-- Tiny Decorative Floral Illustration -->
                <div class="secret-floral-illustration" id="secret-floral" aria-hidden="true">
                  <svg class="secret-floral-svg" viewBox="0 0 100 24" fill="none">
                    <!-- Central Rose Bud Motif -->
                    <circle cx="50" cy="12" r="2.4" fill="#BD956B" opacity="0.85"/>
                    <path d="M50 8 C 47 4, 43 7, 45 11 C 48 10, 50 8, 50 8 Z" fill="#BD956B" opacity="0.6"/>
                    <path d="M50 8 C 53 4, 57 7, 55 11 C 52 10, 50 8, 50 8 Z" fill="#BD956B" opacity="0.6"/>
                    <!-- Graceful Botanical Vine & Leaves Stem Left -->
                    <path d="M44 12 C 34 11, 24 14, 10 12" stroke="#BD956B" stroke-width="0.85" stroke-linecap="round"/>
                    <path d="M30 11.8 C 28 8.5, 23 9.5, 25 12.8 C 27.5 12.5, 30 11.8, 30 11.8 Z" fill="#BD956B" opacity="0.45"/>
                    <path d="M20 12.2 C 18 15, 14 14, 15.5 11.5 C 17.5 11.8, 20 12.2, 20 12.2 Z" fill="#BD956B" opacity="0.45"/>
                    <circle cx="9" cy="12" r="1.2" fill="#BD956B" opacity="0.6"/>
                    <!-- Graceful Botanical Vine & Leaves Stem Right -->
                    <path d="M56 12 C 66 11, 76 14, 90 12" stroke="#BD956B" stroke-width="0.85" stroke-linecap="round"/>
                    <path d="M70 11.8 C 72 8.5, 77 9.5, 75 12.8 C 72.5 12.5, 70 11.8, 70 11.8 Z" fill="#BD956B" opacity="0.45"/>
                    <path d="M80 12.2 C 82 15, 86 14, 84.5 11.5 C 82.5 11.8, 80 12.2, 80 12.2 Z" fill="#BD956B" opacity="0.45"/>
                    <circle cx="91" cy="12" r="1.2" fill="#BD956B" opacity="0.6"/>
                  </svg>
                </div>

                <span class="secret-card-monogram">✦ EK EHSAAS • A PRIVATE DISCOVERY ✦</span>

                <!-- Small Ornamental Divider -->
                <div class="secret-ornamental-divider" id="secret-divider" aria-hidden="true">
                  <span class="secret-divider-line"></span>
                  <span class="secret-divider-star">✦</span>
                  <span class="secret-divider-line"></span>
                </div>
              </header>

              <!-- Shayari Body: Line by Line Devanagari Poetry -->
              <div class="secret-shayari-body" id="secret-shayari-body">
                <!-- Couplet 1 -->
                <div class="shayari-couplet shayari-couplet--1">
                  <p class="shayari-line shayari-line--1" id="shayari-line-1">कुछ लम्हे ख़ामोशी में भी, कहानी कह जाते हैं,</p>
                  <p class="shayari-line shayari-line--2" id="shayari-line-2">कुछ चेहरे बिना कोशिश के, मुस्कान दे जाते हैं।</p>
                </div>

                <!-- Couplet 2 (Subtly Highlighted) -->
                <div class="shayari-couplet shayari-couplet--2 shayari-couplet--highlight">
                  <p class="shayari-line shayari-line--3" id="shayari-line-3">तस्वीरों में क़ैद तो बस एक झलक होती है,</p>
                  <p class="shayari-line shayari-line--4" id="shayari-line-4">असल ख़ूबसूरती तो वो है, जो एहसास बन जाती है।</p>
                </div>
              </div>

              <!-- Stationery Footer & Delicate Decorative Flourish -->
              <footer class="secret-card-footer" id="secret-footer">
                <div class="secret-flourish-wrap" id="secret-flourish" aria-hidden="true">
                  <svg class="secret-bottom-flourish-svg" viewBox="0 0 120 18" fill="none">
                    <path d="M10 9 Q 35 3 60 9 Q 85 15 110 9" stroke="#BD956B" stroke-width="0.75" stroke-linecap="round" opacity="0.5"/>
                    <circle cx="60" cy="9" r="2.2" fill="#BD956B" opacity="0.8"/>
                    <circle cx="48" cy="9" r="1.3" fill="#BD956B" opacity="0.5"/>
                    <circle cx="72" cy="9" r="1.3" fill="#BD956B" opacity="0.5"/>
                  </svg>
                </div>
              </footer>
            </article>"""

# Normalize CRLF
content_norm = content.replace('\r\n', '\n')
target_norm = target.replace('\r\n', '\n')
replacement_norm = replacement.replace('\r\n', '\n')

if target_norm in content_norm:
    new_content = content_norm.replace(target_norm, replacement_norm, 1)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("SUCCESS: index.html updated")
else:
    print("ERROR: target not found")
