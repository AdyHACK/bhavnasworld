with open('src/components/app.js', 'r', encoding='utf-8') as f:
    content = f.read()

target = """function initSecret(content) {
  const revealBtn = document.getElementById('secret-reveal-btn');
  const envOuter  = document.getElementById('secret-envelope');
  const flap      = document.getElementById('secret-flap');
  const seal      = document.getElementById('secret-seal');
  const card      = document.getElementById('secret-card');
  const closeBtn  = document.getElementById('secret-close-btn');
  const msgText   = document.getElementById('secret-message-text');

  if (!envOuter || !card) return;

  if (msgText && content?.secret?.message) {
    msgText.innerHTML = content.secret.message;
  }

  let isOpen = false;
  let isAnim = false;
  const reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  if (seal && typeof gsap !== 'undefined') {
    gsap.set(seal, { xPercent: -50, yPercent: -50, transformOrigin: 'center center' });
  }

  function openSecret(e) {
    if (isOpen || isAnim) return;
    isAnim = true;

    if (seal) seal.style.transition = 'none';

    if (e && e.clientX) {
      particleBurst(e.clientX, e.clientY, '#D8B990', 16);
    } else if (seal) {
      const rect = seal.getBoundingClientRect();
      particleBurst(rect.left + rect.width / 2, rect.top + rect.height / 2, '#D8B990', 16);
    }

    const isMobile = window.innerWidth <= 768;
    const riseDist = isMobile ? -130 : -160;

    if (typeof gsap !== 'undefined' && !reduced) {
      const tl = gsap.timeline({
        onComplete: () => {
          isOpen = true;
          isAnim = false;
          card.classList.add('is-active');
          if (revealBtn) {
            revealBtn.innerHTML = 'Fold &amp; Close <span aria-hidden="true">✦</span>';
          }
        }
      });

      // 1. Wax seal compression and pop
      if (seal) {
        tl.to(seal, { scale: 0.9, duration: 0.14, ease: 'power2.in' })
          .to(seal, { scale: 1.15, opacity: 0, duration: 0.3, ease: 'power2.out', pointerEvents: 'none' }, '+=0.02');
      }

      // 2. 3D flap rotation backward (0 -> -180deg)
      if (flap) {
        tl.to(flap, {
          rotateX: -180,
          duration: 0.85,
          ease: 'power2.inOut',
          onUpdate: function() {
            if (this.progress() >= 0.5) {
              flap.style.zIndex = '2';
            } else {
              flap.style.zIndex = '30';
            }
          }
        }, '-=0.2');
      }

      // 3. Card emerges cleanly in front of pocket (zIndex: 50) and slides up
      tl.set(card, { zIndex: 50 }, '-=0.4')
        .fromTo(card,
          { y: 0, scale: 0.96, opacity: 0 },
          {
            y: riseDist,
            scale: 1,
            opacity: 1,
            duration: 0.9,
            ease: 'power3.out',
            boxShadow: '0 24px 60px rgba(73, 50, 36, 0.22)'
          },
          '-=0.4'
        );

    } else {
      // Fallback
      if (flap) { flap.style.transform = 'rotateX(-180deg)'; flap.style.zIndex = '2'; }
      if (seal) { seal.style.opacity = '0'; seal.style.pointerEvents = 'none'; }
      card.style.transform = `translate3d(0, ${riseDist}px, 0) scale(1)`;
      card.style.opacity = '1';
      card.style.zIndex = '50';
      card.classList.add('is-active');
      isOpen = true;
      isAnim = false;
      if (revealBtn) revealBtn.innerHTML = 'Fold &amp; Close <span aria-hidden="true">✦</span>';
    }
  }

  function closeSecret() {
    if (!isOpen || isAnim) return;
    isAnim = true;

    card.classList.remove('is-active');

    if (typeof gsap !== 'undefined' && !reduced) {
      const closeTl = gsap.timeline({
        onComplete: () => {
          isOpen = false;
          isAnim = false;
          if (revealBtn) {
            revealBtn.innerHTML = 'Take a Look <span aria-hidden="true">✦</span>';
          }
          if (seal) seal.style.transition = '';
          gsap.set(card, { y: 0, scale: 0.96, opacity: 0, zIndex: 10 });
          gsap.set(envOuter, { y: 0 });
          if (flap) gsap.set(flap, { rotateX: 0, zIndex: 30 });
          if (seal) gsap.set(seal, { scale: 1, opacity: 1, xPercent: -50, yPercent: -50, pointerEvents: 'auto' });
        }
      });

      // 1. Card slides back into pocket
      closeTl.to(card, {
        y: 0,
        scale: 0.96,
        opacity: 0,
        duration: 0.6,
        ease: 'power3.in',
        onComplete: () => { card.style.zIndex = '10'; }
      })

      // 2. Flap folds back down
      .to(flap, {
        rotateX: 0,
        duration: 0.75,
        ease: 'power2.inOut',
        onUpdate: function() {
          if (this.progress() >= 0.5) {
            flap.style.zIndex = '30';
          } else {
            flap.style.zIndex = '2';
          }
        }
      }, '-=0.2')

      // 3. Wax seal returns
      .to(seal, {
        scale: 1,
        opacity: 1,
        pointerEvents: 'auto',
        duration: 0.38,
        ease: 'back.out(1.8)'
      }, '-=0.15');

    } else {
      // Fallback
      card.style.transform = 'translate3d(0, 0, 0) scale(0.96)';
      card.style.opacity = '0';
      card.style.zIndex = '10';
      envOuter.style.transform = 'none';
      if (flap) { flap.style.transform = 'rotateX(0deg)'; flap.style.zIndex = '30'; }
      if (seal) { seal.style.opacity = '1'; seal.style.pointerEvents = 'auto'; }
      isOpen = false;
      isAnim = false;
      if (revealBtn) revealBtn.innerHTML = 'Take a Look <span aria-hidden="true">✦</span>';
    }
  }

  // Event handlers
  if (seal) {
    seal.addEventListener('click', openSecret);
    seal.addEventListener('keydown', e => {
      if (e.key === 'Enter' || e.key === ' ') {
        e.preventDefault();
        openSecret(e);
      }
    });
  }

  if (revealBtn) {
    revealBtn.addEventListener('click', e => {
      if (!isOpen) {
        openSecret(e);
      } else {
        closeSecret();
      }
    });
  }

  if (closeBtn) {
    closeBtn.addEventListener('click', e => {
      e.stopPropagation();
      closeSecret();
    });
  }

  envOuter.addEventListener('click', e => {
    if (!isOpen && !isAnim && !e.target.closest('#secret-close-btn') && !e.target.closest('#secret-card')) {
      openSecret(e);
    }
  });
}"""

replacement = """function initSecret(content) {
  const revealBtn = document.getElementById('secret-reveal-btn');
  const envOuter  = document.getElementById('secret-envelope');
  const flap      = document.getElementById('secret-flap');
  const seal      = document.getElementById('secret-seal');
  const card      = document.getElementById('secret-card');
  const closeBtn  = document.getElementById('secret-close-btn');

  // Hindi Shayari & Ornament Elements
  const floralEl         = document.getElementById('secret-floral');
  const monogramEl       = card ? card.querySelector('.secret-card-monogram') : null;
  const dividerEl        = document.getElementById('secret-divider');
  const line1            = document.getElementById('shayari-line-1');
  const line2            = document.getElementById('shayari-line-2');
  const line3            = document.getElementById('shayari-line-3');
  const line4            = document.getElementById('shayari-line-4');
  const highlightCouplet = card ? card.querySelector('.shayari-couplet--highlight') : null;
  const flourishEl       = document.getElementById('secret-flourish');

  if (!envOuter || !card) return;

  // Populate shayari lines if custom content passed
  if (content?.secret?.shayari && Array.isArray(content.secret.shayari)) {
    const lines = [line1, line2, line3, line4];
    content.secret.shayari.forEach((txt, i) => {
      if (lines[i] && txt) lines[i].textContent = txt;
    });
  }

  let isOpen = false;
  let isAnim = false;
  const reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  function resetShayari() {
    if (typeof gsap === 'undefined') return;
    if (floralEl) gsap.set(floralEl, { opacity: 0, y: 10 });
    if (monogramEl) gsap.set(monogramEl, { opacity: 0, y: 8 });
    if (dividerEl) gsap.set(dividerEl, { opacity: 0, scaleX: 0.4, transformOrigin: 'center center' });
    [line1, line2, line3, line4].forEach(l => {
      if (l) gsap.set(l, { opacity: 0, y: 16, textShadow: 'none', color: '#442E20' });
    });
    if (highlightCouplet) {
      highlightCouplet.classList.remove('is-highlighted');
      gsap.set(highlightCouplet, { backgroundColor: 'transparent', boxShadow: 'none' });
    }
    if (flourishEl) gsap.set(flourishEl, { opacity: 0, y: 10, scale: 0.88, transformOrigin: 'center center' });
  }

  // Ensure initial pristine hidden state before envelope opens
  resetShayari();

  if (seal && typeof gsap !== 'undefined') {
    gsap.set(seal, { xPercent: -50, yPercent: -50, transformOrigin: 'center center' });
  }

  function openSecret(e) {
    if (isOpen || isAnim) return;
    isAnim = true;

    if (seal) seal.style.transition = 'none';

    if (e && e.clientX) {
      particleBurst(e.clientX, e.clientY, '#D8B990', 16);
    } else if (seal) {
      const rect = seal.getBoundingClientRect();
      particleBurst(rect.left + rect.width / 2, rect.top + rect.height / 2, '#D8B990', 16);
    }

    const isMobile = window.innerWidth <= 768;
    const riseDist = isMobile ? -145 : -190;

    if (typeof gsap !== 'undefined' && !reduced) {
      const tl = gsap.timeline({
        onComplete: () => {
          isOpen = true;
          isAnim = false;
          card.classList.add('is-active');
          if (revealBtn) {
            revealBtn.innerHTML = 'Fold &amp; Close <span aria-hidden="true">✦</span>';
          }
        }
      });

      // Step 1: Wax seal compression and pop
      if (seal) {
        tl.to(seal, { scale: 0.9, duration: 0.14, ease: 'power2.in' })
          .to(seal, { scale: 1.15, opacity: 0, duration: 0.3, ease: 'power2.out', pointerEvents: 'none' }, '+=0.02');
      }

      // Step 2: 3D flap opens completely backward around top crease (0 -> -180deg)
      if (flap) {
        tl.to(flap, {
          rotateX: -180,
          duration: 0.88,
          ease: 'power2.inOut',
          onUpdate: function() {
            if (this.progress() >= 0.5) {
              flap.style.zIndex = '2';
            } else {
              flap.style.zIndex = '30';
            }
          }
        }, '-=0.2');
      }

      // Step 3: Letter emerges cleanly in front of pocket (zIndex: 50) and slides out smoothly
      tl.set(card, { zIndex: 50 }, '-=0.4')
        .fromTo(card,
          { y: 0, scale: 0.96, opacity: 0 },
          {
            y: riseDist,
            scale: 1,
            opacity: 1,
            duration: 0.92,
            ease: 'power3.out',
            boxShadow: '0 24px 60px rgba(73, 50, 36, 0.22), 0 4px 14px rgba(73, 50, 36, 0.1)'
          },
          '-=0.4'
        );

      // Step 4: Tiny floral illustration & monogram reveal
      if (floralEl) {
        tl.to(floralEl, { opacity: 1, y: 0, duration: 0.55, ease: 'power2.out' }, '+=0.08');
      }
      if (monogramEl) {
        tl.to(monogramEl, { opacity: 1, y: 0, duration: 0.45, ease: 'power2.out' }, '-=0.25');
      }

      // Step 5: Introduce the small ornamental divider
      if (dividerEl) {
        tl.to(dividerEl, { opacity: 1, scaleX: 1, duration: 0.58, ease: 'power2.out' }, '-=0.15');
      }

      // Step 6: Reveal the shayari one line at a time with gentle upward movement & opacity
      if (line1) {
        tl.to(line1, { opacity: 1, y: 0, duration: 0.72, ease: 'power2.out' }, '+=0.12');
      }
      if (line2) {
        tl.to(line2, { opacity: 1, y: 0, duration: 0.72, ease: 'power2.out' }, '+=0.2');
      }

      // Poetic breathing pause between couplets
      tl.to({}, { duration: 0.32 });

      if (line3) {
        tl.to(line3, { opacity: 1, y: 0, duration: 0.72, ease: 'power2.out' });
      }
      if (line4) {
        tl.to(line4, { opacity: 1, y: 0, duration: 0.72, ease: 'power2.out' }, '+=0.2');
      }

      // Step 7: Highlight the final two lines subtly
      if (highlightCouplet) {
        tl.to(highlightCouplet, {
          backgroundColor: 'rgba(216, 185, 144, 0.14)',
          boxShadow: '0 0 28px rgba(216, 185, 144, 0.25)',
          duration: 0.8,
          ease: 'power2.out',
          onStart: () => { highlightCouplet.classList.add('is-highlighted'); }
        }, '+=0.15');
      }
      if (line3 && line4) {
        tl.to([line3, line4], {
          color: '#2E190E',
          textShadow: '0 0 16px rgba(216, 185, 144, 0.42), 0 1px 1px rgba(255, 255, 255, 0.6)',
          duration: 0.8,
          ease: 'power2.out'
        }, '<');
      }

      // Step 8: Finish with a delicate decorative flourish
      if (flourishEl) {
        tl.to(flourishEl, {
          opacity: 1,
          y: 0,
          scale: 1,
          duration: 0.65,
          ease: 'back.out(1.7)'
        }, '+=0.12');
      }

    } else {
      // Graceful fallback for reduced motion
      if (flap) { flap.style.transform = 'rotateX(-180deg)'; flap.style.zIndex = '2'; }
      if (seal) { seal.style.opacity = '0'; seal.style.pointerEvents = 'none'; }
      card.style.transform = `translate3d(0, ${riseDist}px, 0) scale(1)`;
      card.style.opacity = '1';
      card.style.zIndex = '50';
      card.classList.add('is-active');

      if (floralEl) { floralEl.style.opacity = '1'; floralEl.style.transform = 'none'; }
      if (monogramEl) { monogramEl.style.opacity = '1'; monogramEl.style.transform = 'none'; }
      if (dividerEl) { dividerEl.style.opacity = '1'; dividerEl.style.transform = 'none'; }
      [line1, line2, line3, line4].forEach(l => {
        if (l) { l.style.opacity = '1'; l.style.transform = 'none'; }
      });
      if (highlightCouplet) {
        highlightCouplet.classList.add('is-highlighted');
      }
      if (flourishEl) { flourishEl.style.opacity = '1'; flourishEl.style.transform = 'none'; }

      isOpen = true;
      isAnim = false;
      if (revealBtn) revealBtn.innerHTML = 'Fold &amp; Close <span aria-hidden="true">✦</span>';
    }
  }

  function closeSecret() {
    if (!isOpen || isAnim) return;
    isAnim = true;

    card.classList.remove('is-active');

    if (typeof gsap !== 'undefined' && !reduced) {
      const closeTl = gsap.timeline({
        onComplete: () => {
          isOpen = false;
          isAnim = false;
          if (revealBtn) {
            revealBtn.innerHTML = 'Take a Look <span aria-hidden="true">✦</span>';
          }
          if (seal) seal.style.transition = '';
          gsap.set(card, { y: 0, scale: 0.96, opacity: 0, zIndex: 10 });
          gsap.set(envOuter, { y: 0 });
          if (flap) gsap.set(flap, { rotateX: 0, zIndex: 30 });
          if (seal) gsap.set(seal, { scale: 1, opacity: 1, xPercent: -50, yPercent: -50, pointerEvents: 'auto' });
          resetShayari();
        }
      });

      // Quick graceful fade out of shayari elements
      const elementsToFade = [floralEl, monogramEl, dividerEl, line1, line2, line3, line4, highlightCouplet, flourishEl].filter(Boolean);
      if (elementsToFade.length) {
        closeTl.to(elementsToFade, {
          opacity: 0,
          duration: 0.22,
          ease: 'power2.in'
        });
      }

      // 1. Card slides back into pocket
      closeTl.to(card, {
        y: 0,
        scale: 0.96,
        opacity: 0,
        duration: 0.55,
        ease: 'power3.in',
        onComplete: () => { card.style.zIndex = '10'; }
      }, '-=0.08')

      // 2. Flap folds back down
      .to(flap, {
        rotateX: 0,
        duration: 0.7,
        ease: 'power2.inOut',
        onUpdate: function() {
          if (this.progress() >= 0.5) {
            flap.style.zIndex = '30';
          } else {
            flap.style.zIndex = '2';
          }
        }
      }, '-=0.18')

      // 3. Wax seal returns
      .to(seal, {
        scale: 1,
        opacity: 1,
        pointerEvents: 'auto',
        duration: 0.35,
        ease: 'back.out(1.8)'
      }, '-=0.15');

    } else {
      // Fallback
      card.style.transform = 'translate3d(0, 0, 0) scale(0.96)';
      card.style.opacity = '0';
      card.style.zIndex = '10';
      envOuter.style.transform = 'none';
      if (flap) { flap.style.transform = 'rotateX(0deg)'; flap.style.zIndex = '30'; }
      if (seal) { seal.style.opacity = '1'; seal.style.pointerEvents = 'auto'; }
      resetShayari();
      isOpen = false;
      isAnim = false;
      if (revealBtn) revealBtn.innerHTML = 'Take a Look <span aria-hidden="true">✦</span>';
    }
  }

  // Event handlers
  if (seal) {
    seal.addEventListener('click', openSecret);
    seal.addEventListener('keydown', e => {
      if (e.key === 'Enter' || e.key === ' ') {
        e.preventDefault();
        openSecret(e);
      }
    });
  }

  if (revealBtn) {
    revealBtn.addEventListener('click', e => {
      if (!isOpen) {
        openSecret(e);
      } else {
        closeSecret();
      }
    });
  }

  if (closeBtn) {
    closeBtn.addEventListener('click', e => {
      e.stopPropagation();
      closeSecret();
    });
  }

  envOuter.addEventListener('click', e => {
    if (!isOpen && !isAnim && !e.target.closest('#secret-close-btn') && !e.target.closest('#secret-card')) {
      openSecret(e);
    }
  });
}"""

content_norm = content.replace('\r\n', '\n')
target_norm = target.replace('\r\n', '\n')
replacement_norm = replacement.replace('\r\n', '\n')

if target_norm in content_norm:
    new_content = content_norm.replace(target_norm, replacement_norm, 1)
    with open('src/components/app.js', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("SUCCESS: app.js updated")
else:
    print("ERROR: target not found in app.js")
