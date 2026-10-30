/* ═══════════════════════════════════════════════════════════════════
   HER LITTLE UNIVERSE — Main Application Engine v4 Premium
   Luxury Editorial × Cinematic × Interactive
   ═══════════════════════════════════════════════════════════════════ */

'use strict';

/* ────────────────────────────────────────────────────────────────
   STARFIELD CANVAS ENGINE
──────────────────────────────────────────────────────────────── */
class StarField {
  constructor(canvas, opts = {}) {
    this.canvas = canvas;
    this.ctx    = canvas.getContext('2d');
    this.stars  = [];
    this.raf    = null;
    this.opts   = {
      count:   opts.count   || 140,
      minSize: opts.minSize || 0.4,
      maxSize: opts.maxSize || 2.0,
      color:   opts.color   || '#8C6242',
      speed:   opts.speed   || 0.016,
      ...opts,
    };
    this.reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    this._resizeObserver = null;
    this._init();
  }

  _init() {
    this._resize();
    if (window.ResizeObserver) {
      this._resizeObserver = new ResizeObserver(() => this._resize());
      this._resizeObserver.observe(this.canvas.parentElement || document.body);
    } else {
      window.addEventListener('resize', () => this._resize(), { passive: true });
    }
    this.stars = Array.from({ length: this.opts.count }, () => this._makeStar());
    this.reduced ? this._drawStatic() : this._tick();
  }

  _resize() {
    const parent = this.canvas.parentElement;
    if (parent) {
      this.canvas.width  = parent.offsetWidth;
      this.canvas.height = parent.offsetHeight;
    } else {
      this.canvas.width  = window.innerWidth;
      this.canvas.height = window.innerHeight;
    }
    if (this.reduced) this._drawStatic();
  }

  _makeStar() {
    const w = this.canvas.width  || window.innerWidth;
    const h = this.canvas.height || window.innerHeight;
    return {
      x:     Math.random() * w,
      y:     Math.random() * h,
      size:  this.opts.minSize + Math.random() * (this.opts.maxSize - this.opts.minSize),
      alpha: 0.12 + Math.random() * 0.7,
      vx:    (Math.random() - 0.5) * 0.08,
      vy:    (Math.random() - 0.5) * 0.04,
      phase: Math.random() * Math.PI * 2,
      speed: this.opts.speed * (0.4 + Math.random() * 0.8),
    };
  }

  _rgba(alpha) {
    const c = this.opts.color;
    const r = parseInt(c.slice(1, 3), 16);
    const g = parseInt(c.slice(3, 5), 16);
    const b = parseInt(c.slice(5, 7), 16);
    return `rgba(${r},${g},${b},${Math.min(1, alpha).toFixed(3)})`;
  }

  _drawStatic() {
    const { ctx, canvas, stars } = this;
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    stars.forEach(s => {
      ctx.beginPath();
      ctx.arc(s.x, s.y, s.size, 0, Math.PI * 2);
      ctx.fillStyle = this._rgba(s.alpha * 0.5);
      ctx.fill();
    });
  }

  _tick() {
    const { ctx, canvas, stars } = this;
    const t = performance.now() / 1000;
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    stars.forEach(s => {
      const flicker = 0.5 + 0.5 * Math.sin(t * s.speed * 3.5 + s.phase);
      const a = s.alpha * (0.22 + 0.78 * flicker);

      ctx.beginPath();
      ctx.arc(s.x, s.y, s.size, 0, Math.PI * 2);
      ctx.fillStyle = this._rgba(a);
      ctx.fill();

      if (s.size > 1.3) {
        ctx.beginPath();
        ctx.arc(s.x, s.y, s.size * 2.6, 0, Math.PI * 2);
        ctx.fillStyle = this._rgba(a * 0.1);
        ctx.fill();
      }

      s.x += s.vx;
      s.y += s.vy;
      if (s.x < -4) s.x = canvas.width  + 4;
      if (s.x > canvas.width  + 4) s.x = -4;
      if (s.y < -4) s.y = canvas.height + 4;
      if (s.y > canvas.height + 4) s.y = -4;
    });
    this.raf = requestAnimationFrame(() => this._tick());
  }

  destroy() {
    if (this.raf) cancelAnimationFrame(this.raf);
    if (this._resizeObserver) this._resizeObserver.disconnect();
  }
}

/* ────────────────────────────────────────────────────────────────
   PARTICLE BURST
──────────────────────────────────────────────────────────────── */
function particleBurst(x, y, color = '#AE8157', count = 14) {
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  for (let i = 0; i < count; i++) {
    const el    = document.createElement('div');
    const angle = (i / count) * 360;
    const dist  = 40 + Math.random() * 60;
    const px    = Math.cos(angle * Math.PI / 180) * dist;
    const py    = Math.sin(angle * Math.PI / 180) * dist;
    const size  = 1.5 + Math.random() * 3.5;
    Object.assign(el.style, {
      position: 'fixed', left: `${x}px`, top: `${y}px`,
      width: `${size}px`, height: `${size}px`,
      background: color, borderRadius: '50%',
      pointerEvents: 'none', zIndex: '9998',
      '--px': `${px}px`, '--py': `${py}px`,
      animation: 'particle-burst 0.75s cubic-bezier(0.22,1,0.36,1) forwards',
    });
    document.body.appendChild(el);
    setTimeout(() => el.remove(), 850);
  }
}

/* ────────────────────────────────────────────────────────────────
   CUSTOM CURSOR
──────────────────────────────────────────────────────────────── */
class CustomCursor {
  constructor() {
    this.dot  = document.getElementById('cursor-dot');
    this.ring = document.getElementById('cursor-ring');
    if (!this.dot || !this.ring) return;
    if (window.matchMedia('(pointer: coarse)').matches) {
      [this.dot, this.ring].forEach(el => el.style.display = 'none');
      return;
    }
    this.mx = 0; this.my = 0;
    this.rx = 0; this.ry = 0;
    this.raf = null;

    document.addEventListener('mousemove', e => {
      this.mx = e.clientX; this.my = e.clientY;
      this.dot.style.left = `${e.clientX}px`;
      this.dot.style.top  = `${e.clientY}px`;
    }, { passive: true });

    const targets = 'button,a,[data-hover],input,label,.gallery-item,.scrap-card,.mosaic-tile,.universe-orb';
    document.addEventListener('mouseover', e => {
      if (e.target.closest(targets)) this._hover(true);
    });
    document.addEventListener('mouseout', e => {
      if (e.target.closest(targets)) this._hover(false);
    });

    this._loop();
  }

  _hover(on) {
    this.dot.classList.toggle('hovering', on);
    this.ring.classList.toggle('hovering', on);
  }

  _loop() {
    this.rx += (this.mx - this.rx) * 0.1;
    this.ry += (this.my - this.ry) * 0.1;
    this.ring.style.left = `${this.rx}px`;
    this.ring.style.top  = `${this.ry}px`;
    this.raf = requestAnimationFrame(() => this._loop());
  }

  destroy() { if (this.raf) cancelAnimationFrame(this.raf); }
}

/* ────────────────────────────────────────────────────────────────
   MAGNETIC BUTTONS
──────────────────────────────────────────────────────────────── */
function initMagneticButtons() {
  if (window.matchMedia('(pointer: coarse)').matches) return;
  document.querySelectorAll('.btn').forEach(btn => {
    btn.addEventListener('mousemove', e => {
      const r   = btn.getBoundingClientRect();
      const cx  = r.left + r.width  / 2;
      const cy  = r.top  + r.height / 2;
      const dx  = (e.clientX - cx) * 0.32;
      const dy  = (e.clientY - cy) * 0.32;
      btn.style.transform = `translate(${dx}px, ${dy}px) translateY(-2px)`;
    });
    btn.addEventListener('mouseleave', () => {
      btn.style.transform = '';
    });
  });
}

/* ────────────────────────────────────────────────────────────────
   SCROLL REVEAL OBSERVER
──────────────────────────────────────────────────────────────── */
function initRevealObserver() {
  const els = document.querySelectorAll('.reveal-up, .reveal-left, .reveal-right, .reveal-scale, .section-num');
  if (!els.length) return;

  const obs = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (!entry.isIntersecting) return;
      const el    = entry.target;
      const delay = parseInt(el.dataset.delay || '0', 10);
      el.style.setProperty('--reveal-delay', `${delay}ms`);
      setTimeout(() => el.classList.add('is-visible'), delay);
      obs.unobserve(el);
    });
  }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });

  els.forEach(el => obs.observe(el));
}

/* ────────────────────────────────────────────────────────────────
   ACTIVE NAV SECTION TRACKER
──────────────────────────────────────────────────────────────── */
function initSectionTracker() {
  const sections = ['hero','universe','gallery','scrapbook','mosaic','secret','letter-section','final-scene'];
  const navLinks = document.querySelectorAll('.nav-links a[data-section]');
  if (!navLinks.length) return;

  const obs = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (!entry.isIntersecting) return;
      const id = entry.target.id;
      navLinks.forEach(a => {
        a.classList.toggle('active', a.dataset.section === id);
      });
    });
  }, { threshold: 0.35 });

  sections.forEach(id => {
    const el = document.getElementById(id);
    if (el) obs.observe(el);
  });
}

/* ────────────────────────────────────────────────────────────────
   NAVIGATION
──────────────────────────────────────────────────────────────── */
function initNav() {
  const nav     = document.getElementById('nav');
  const logo    = document.querySelector('.nav-logo');
  const links   = document.querySelector('.nav-links');
  const menuBtn = document.querySelector('.nav-menu-btn');
  if (!nav) return;

  let lastY   = 0;
  let ticking = false;

  window.addEventListener('scroll', () => {
    if (!ticking) {
      requestAnimationFrame(() => {
        const y = window.scrollY;
        nav.classList.toggle('scrolled', y > 50);
        if (logo) logo.classList.toggle('visible', y > 80);
        nav.style.transform = (y > lastY + 8 && y > 200) ? 'translateY(-100%)' : 'translateY(0)';
        lastY   = y;
        ticking = false;
      });
      ticking = true;
    }
  }, { passive: true });

  if (menuBtn && links) {
    menuBtn.addEventListener('click', () => {
      const open = menuBtn.classList.toggle('open');
      links.classList.toggle('open', open);
      menuBtn.setAttribute('aria-expanded', String(open));
    });
    links.querySelectorAll('a').forEach(a => {
      a.addEventListener('click', () => {
        menuBtn.classList.remove('open');
        links.classList.remove('open');
        menuBtn.setAttribute('aria-expanded', 'false');
      });
    });
  }

  document.querySelectorAll('a[href^="#"]').forEach(a => {
    a.addEventListener('click', e => {
      const target = document.querySelector(a.getAttribute('href'));
      if (target) {
        e.preventDefault();
        target.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    });
  });
}

/* ────────────────────────────────────────────────────────────────
   INTRO SCREEN
──────────────────────────────────────────────────────────────── */
function initIntro() {
  const intro    = document.getElementById('intro');
  const main     = document.getElementById('main-content');
  const enterBtn = document.getElementById('enter-btn');
  if (!intro || !enterBtn || !main) return;

  const reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  if (!reduced) {
    const lines   = intro.querySelectorAll('.intro-line');
    const btnWrap = intro.querySelector('.intro-btn-wrap');

    lines.forEach((line, i) => {
      line.style.cssText = 'opacity:0; transform:translateY(22px);';
      setTimeout(() => {
        line.style.cssText = 'transition:opacity 1.1s cubic-bezier(0.22,1,0.36,1),transform 1.1s cubic-bezier(0.22,1,0.36,1); opacity:1; transform:none;';
        line.classList.add('visible');
      }, 600 + i * 700);
    });

    if (btnWrap) {
      btnWrap.style.cssText = 'opacity:0; transform:translateY(18px);';
      setTimeout(() => {
        btnWrap.style.cssText = 'transition:opacity 0.9s ease,transform 0.9s cubic-bezier(0.22,1,0.36,1); opacity:1; transform:none;';
        btnWrap.classList.add('visible');
      }, 600 + 2 * 700 + 350);
    }
  }

  const doEnter = () => {
    const r = enterBtn.getBoundingClientRect();
    particleBurst(r.left + r.width / 2, r.top + r.height / 2, '#AE8157', 18);

    if (!reduced) {
      intro.style.transition = 'opacity 1.0s cubic-bezier(0.22,1,0.36,1), transform 1.0s cubic-bezier(0.22,1,0.36,1)';
      intro.style.opacity    = '0';
      intro.style.transform  = 'scale(1.04)';
      setTimeout(() => {
        intro.style.display  = 'none';
        document.body.style.overflow = '';
        main.classList.remove('hidden');
        main.style.opacity = '0';
        requestAnimationFrame(() => {
          main.style.transition = 'opacity 0.8s ease';
          main.style.opacity    = '1';
        });
        setTimeout(() => {
          initRevealObserver();
          initMagneticButtons();
          initSectionTracker();
        }, 120);
      }, 900);
    } else {
      intro.style.display = 'none';
      main.classList.remove('hidden');
      document.body.style.overflow = '';
      initRevealObserver();
    }
  };

  enterBtn.addEventListener('click', doEnter);
  setTimeout(() => { if (intro.style.display !== 'none') doEnter(); }, 14000);
}

/* ────────────────────────────────────────────────────────────────
   LIGHTBOX
──────────────────────────────────────────────────────────────── */
class Lightbox {
  constructor() {
    this.lb      = document.getElementById('lightbox');
    this.lbImg   = document.getElementById('lb-img');
    this.lbCap   = document.getElementById('lb-caption');
    this.lbCount = document.getElementById('lb-counter');
    this.prev    = document.getElementById('lb-prev');
    this.next    = document.getElementById('lb-next');
    this.close   = document.getElementById('lb-close');
    this.photos  = [];
    this.idx     = 0;
    this.scrollY = 0;
    if (!this.lb) return;
    this._bind();
  }

  open(photos, idx = 0) {
    this.photos  = photos;
    this.idx     = idx;
    this.scrollY = window.scrollY;
    this.lb.classList.add('open');
    document.body.style.overflow = 'hidden';
    this._show(idx);
    this.lb.focus();
  }

  _close() {
    this.lb.classList.remove('open');
    document.body.style.overflow = '';
    window.scrollTo({ top: this.scrollY, behavior: 'instant' });
  }

  _show(idx) {
    const p = this.photos[idx];
    if (!p) return;
    this.lbImg.classList.remove('loaded');
    this.lbImg.style.opacity = '0';
    this.lbImg.src = p.src || '';
    this.lbImg.alt = p.alt || 'Photograph';
    this.lbImg.onload  = () => { this.lbImg.style.opacity = '1'; this.lbImg.classList.add('loaded'); };
    this.lbImg.onerror = () => { this.lbImg.style.opacity = '0.2'; };
    if (this.lbCap)   this.lbCap.textContent  = p.caption || p.title || '';
    if (this.lbCount) this.lbCount.textContent = `${idx + 1} / ${this.photos.length}`;
    const atStart = idx === 0;
    const atEnd   = idx === this.photos.length - 1;
    this.prev.disabled      = atStart;
    this.prev.style.opacity = atStart ? '0.25' : '1';
    this.next.disabled      = atEnd;
    this.next.style.opacity = atEnd   ? '0.25' : '1';
  }

  _prev() { if (this.idx > 0)                   { this.idx--; this._show(this.idx); } }
  _next() { if (this.idx < this.photos.length-1) { this.idx++; this._show(this.idx); } }

  _bind() {
    this.close?.addEventListener('click', () => this._close());
    this.prev?.addEventListener('click',  () => this._prev());
    this.next?.addEventListener('click',  () => this._next());
    this.lb.addEventListener('click', e => { if (e.target === this.lb) this._close(); });
    document.addEventListener('keydown', e => {
      if (!this.lb?.classList.contains('open')) return;
      if (e.key === 'Escape')     { e.preventDefault(); this._close(); }
      if (e.key === 'ArrowLeft')  { e.preventDefault(); this._prev(); }
      if (e.key === 'ArrowRight') { e.preventDefault(); this._next(); }
    });
    let touchStartX = 0;
    this.lb.addEventListener('touchstart', e => { touchStartX = e.changedTouches[0].screenX; }, { passive: true });
    this.lb.addEventListener('touchend',   e => {
      const dx = e.changedTouches[0].screenX - touchStartX;
      if (Math.abs(dx) > 50) { dx < 0 ? this._next() : this._prev(); }
    }, { passive: true });
  }
}

/* ────────────────────────────────────────────────────────────────
   PHOTO ELEMENT BUILDER
──────────────────────────────────────────────────────────────── */
function buildPhotoEl(photo, context) {
  const wrapper = document.createElement('div');
  wrapper.style.cssText = 'position:absolute; inset:0; overflow:hidden;';

  const ph = document.createElement('div');
  ph.className = `photo-placeholder${context === 'scrap' ? ' warm' : ''}`;
  ph.innerHTML = `
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1" aria-hidden="true">
      <rect x="3" y="3" width="18" height="18" rx="2"/>
      <circle cx="8.5" cy="8.5" r="1.5"/>
      <polyline points="21 15 16 10 5 21"/>
    </svg>
    <span>${context === 'scrap' ? 'Photo' : 'Your photo'}</span>
  `;

  const img = document.createElement('img');
  img.className = 'img-cover';
  img.alt       = photo.alt || 'Personal photograph';
  img.loading   = 'lazy';
  img.decoding  = 'async';
  img.style.cssText = 'position:absolute; inset:0; opacity:0; transition:opacity 0.9s ease;';
  img.onload  = () => { img.style.opacity = '1'; ph.style.display = 'none'; };
  img.onerror = () => { img.style.display = 'none'; };
  img.src = photo.src;

  wrapper.appendChild(ph);
  wrapper.appendChild(img);
  return wrapper;
}

/* ────────────────────────────────────────────────────────────────
   GALLERY — Luxury Photography Exhibition
──────────────────────────────────────────────────────────────── */
function initGallery(lb, photos) {
  const grid = document.getElementById('gallery-grid');
  if (!grid) return;

  const gPhotos = photos.filter(p => p.section === 'gallery');
  if (!gPhotos.length) return;

  /* Layout cycles through varied sizes for editorial feel */
  const layouts = [
    'gallery-item--featured',  /* spans 6 cols × 2 rows — hero image */
    'gallery-item--medium',    /* spans 4 cols × 1 row */
    'gallery-item--small',     /* spans 4 cols × 1 row */
    'gallery-item--wide',      /* spans 8 cols × 1 row */
    'gallery-item--tall',      /* spans 4 cols × 2 rows */
    'gallery-item--medium',
  ];

  gPhotos.forEach((photo, i) => {
    const item = document.createElement('div');
    item.className = `gallery-item ${layouts[i % layouts.length]}`;
    item.setAttribute('role', 'listitem');
    item.setAttribute('data-hover', '1');
    item.tabIndex = 0;
    item.setAttribute('aria-label', `View photo: ${photo.title || photo.alt}`);

    item.appendChild(buildPhotoEl(photo, 'gallery'));

    const num = document.createElement('span');
    num.className   = 'gallery-num';
    num.textContent = String(i + 1).padStart(2, '0');
    item.appendChild(num);

    const cap = document.createElement('div');
    cap.className = 'gallery-caption';
    cap.innerHTML = `<p class="t-caption">${photo.caption || ''}</p>`;
    item.appendChild(cap);

    item.addEventListener('click', e => { particleBurst(e.clientX, e.clientY, '#AE8157', 8); lb.open(gPhotos, i); });
    item.addEventListener('keydown', e => {
      if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); lb.open(gPhotos, i); }
    });

    grid.appendChild(item);
  });
}

/* ────────────────────────────────────────────────────────────────
   SCRAPBOOK — Vintage Journal with Varied Sizes
──────────────────────────────────────────────────────────────── */
function initScrapbook(lb, photos) {
  const grid = document.getElementById('scrapbook-grid');
  if (!grid) return;

  const sPhotos = photos.filter(p => p.section === 'scrapbook');
  if (!sPhotos.length) return;

  /* Size rotation: large → small → wide → medium → ... */
  const sizes = ['scrap-card--large', 'scrap-card--small', 'scrap-card--wide', 'scrap-card--medium'];
  /* Rotation: subtle alternating tilts */
  const rotations = ['-2.2deg', '1.8deg', '-1.0deg', '2.4deg', '-1.5deg'];
  /* Photo aspect ratios per size */
  const aspects   = ['4/3', '3/4', '16/9', '4/3'];

  sPhotos.forEach((photo, i) => {
    const card = document.createElement('div');
    const size = sizes[i % sizes.length];
    card.className = `scrap-card ${size}`;
    card.style.setProperty('--rotate', rotations[i % rotations.length]);
    card.setAttribute('role', 'listitem');
    card.tabIndex = 0;
    card.setAttribute('aria-label', `Open photo: ${photo.title || photo.alt}`);

    /* Photo area */
    const photoWrap = document.createElement('div');
    photoWrap.className = 'photo-area';
    const aspect = aspects[i % aspects.length];
    photoWrap.style.cssText = `position:relative; width:100%; aspect-ratio:${aspect}; overflow:hidden;`;
    photoWrap.appendChild(buildPhotoEl(photo, 'scrap'));
    card.appendChild(photoWrap);

    /* Caption */
    const label = document.createElement('p');
    label.className   = 'scrap-label';
    label.textContent = photo.caption || photo.title || '';
    card.appendChild(label);

    /* Handwritten annotation (first card only) */
    if (i === 0) {
      const note = document.createElement('span');
      note.className   = 'deco-annotation';
      note.textContent = '✦ a little memory';
      note.style.cssText = 'position:absolute; bottom:-14px; right:8px; font-size:0.78rem; transform:rotate(-3deg);';
      note.setAttribute('aria-hidden', 'true');
      card.appendChild(note);
    }

    card.addEventListener('click', e => { particleBurst(e.clientX, e.clientY, '#AE8157', 8); lb.open(sPhotos, i); });
    card.addEventListener('keydown', e => {
      if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); lb.open(sPhotos, i); }
    });

    grid.appendChild(card);
  });
}

/* ────────────────────────────────────────────────────────────────
   MOSAIC — Interactive Exhibition Wall
──────────────────────────────────────────────────────────────── */
function initMosaic(lb, photos) {
  const grid = document.getElementById('mosaic-grid');
  if (!grid) return;

  const mPhotos = photos.filter(p => p.section === 'mosaic' || p.section === 'gallery');
  if (!mPhotos.length) return;

  const tileClasses = [
    'mosaic-tile--large',
    'mosaic-tile',
    'mosaic-tile--tall',
    'mosaic-tile',
    'mosaic-tile--wide',
    'mosaic-tile',
    'mosaic-tile',
  ];

  mPhotos.forEach((photo, i) => {
    const tile = document.createElement('div');
    tile.className = `mosaic-tile ${tileClasses[i % tileClasses.length]}`;
    tile.setAttribute('role', 'listitem');
    tile.tabIndex = 0;
    tile.setAttribute('aria-label', `View photo: ${photo.title || photo.alt}`);

    tile.appendChild(buildPhotoEl(photo, 'mosaic'));

    const label = document.createElement('span');
    label.className   = 'mosaic-hover-label';
    label.textContent = photo.title || '';
    tile.appendChild(label);

    tile.addEventListener('click', e => { particleBurst(e.clientX, e.clientY, '#AE8157', 8); lb.open(mPhotos, i); });
    tile.addEventListener('keydown', e => {
      if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); lb.open(mPhotos, i); }
    });

    grid.appendChild(tile);
  });
}

/* ────────────────────────────────────────────────────────────────
   INTERACTIVE UNIVERSE — 3D PREMIUM ORB SYSTEM
──────────────────────────────────────────────────────────────── */
function initUniverse() {
  const container = document.getElementById('universe-nodes');
  if (!container) return;

  const nodes = [
    {
      label: 'THE GALLERY', href: '#gallery',
      gradient: 'radial-gradient(circle at 28% 24%, #F5DEB8 0%, #C8955C 38%, #8A5828 72%, #5C3510 100%)',
      glowColor: 'rgba(200,149,92,0.45)', shadowColor: 'rgba(90,52,16,0.45)',
      borderColor: 'rgba(180,130,80,0.55)', orbitColor: 'rgba(170,120,68,0.25)',
      orbitR: 62, size: 76, x: '14%', y: '30%', floatDir: 'y', floatDur: 7.2, floatDly: 0,
    },
    {
      label: 'LITTLE MOMENTS', href: '#scrapbook',
      gradient: 'radial-gradient(circle at 28% 24%, #FAE8CC 0%, #D9B48A 38%, #A07040 72%, #6E4820 100%)',
      glowColor: 'rgba(185,140,90,0.35)', shadowColor: 'rgba(80,50,20,0.38)',
      borderColor: 'rgba(195,155,105,0.5)', orbitColor: 'rgba(160,115,64,0.2)',
      orbitR: null, size: 46, x: '70%', y: '17%', floatDir: 'x', floatDur: 8.8, floatDly: 1.4,
    },
    {
      label: 'THE SCRAPBOOK', href: '#scrapbook',
      gradient: 'radial-gradient(circle at 28% 24%, #EDD5B2 0%, #BE8E60 38%, #7E5428 72%, #50300E 100%)',
      glowColor: 'rgba(190,142,96,0.4)', shadowColor: 'rgba(78,46,14,0.42)',
      borderColor: 'rgba(175,135,88,0.52)', orbitColor: 'rgba(150,112,70,0.22)',
      orbitR: 52, size: 62, x: '80%', y: '58%', floatDir: 'd', floatDur: 9.5, floatDly: 0.8,
    },
    {
      label: 'A LITTLE SECRET', href: '#secret',
      gradient: 'radial-gradient(circle at 28% 24%, #E8D0A8 0%, #A87848 38%, #6C4828 72%, #42280E 100%)',
      glowColor: 'rgba(168,120,72,0.35)', shadowColor: 'rgba(64,38,14,0.42)',
      borderColor: 'rgba(160,120,72,0.5)', orbitColor: 'rgba(130,95,58,0.2)',
      orbitR: null, size: 40, x: '11%', y: '65%', floatDir: 'x', floatDur: 10.2, floatDly: 2.1,
    },
    {
      label: 'ONE LAST THING', href: '#letter-section',
      gradient: 'radial-gradient(circle at 28% 24%, #FAE4C0 0%, #D4AA70 38%, #9C7040 72%, #623E18 100%)',
      glowColor: 'rgba(212,170,112,0.42)', shadowColor: 'rgba(96,60,22,0.42)',
      borderColor: 'rgba(196,152,96,0.55)', orbitColor: 'rgba(174,133,80,0.22)',
      orbitR: 58, size: 68, x: '46%', y: '74%', floatDir: 'y', floatDur: 8.0, floatDly: 1.6,
    },
  ];

  const isMobile  = window.innerWidth <= 768;
  const isReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  nodes.forEach((node, i) => {
    const wrap = document.createElement('div');
    wrap.className = 'universe-node';

    if (!isMobile) {
      wrap.style.cssText = `left:${node.x}; top:${node.y}; position:absolute;`;
      if (!isReduced) {
        const animName = { y: 'float-y', x: 'float-x', d: 'float-diagonal' }[node.floatDir] || 'float-y';
        wrap.style.animation = `${animName} ${node.floatDur}s ease-in-out ${node.floatDly}s infinite`;
      }
    }

    /* Orbit ring */
    if (node.orbitR && !isMobile) {
      const ringSize = (node.orbitR * 2) + node.size + 16;
      const ring = document.createElement('div');
      ring.className = 'universe-orbit-ring';
      ring.style.cssText = `
        width:${ringSize}px; height:${ringSize}px;
        border-color:${node.orbitColor};
        margin-left:-${ringSize/2}px; margin-top:-${ringSize/2}px;
        top:${node.size/2}px; left:${node.size/2}px;
        animation: orbit-spin ${22 + i * 5}s linear infinite;
      `;
      const dot = document.createElement('div');
      dot.className = 'universe-orbit-dot';
      dot.style.cssText = `width:4px;height:4px;background:${node.borderColor};box-shadow:0 0 8px ${node.glowColor};`;
      ring.appendChild(dot);
      wrap.appendChild(ring);
    }

    /* Orb */
    const orb = document.createElement('a');
    orb.href      = node.href;
    orb.className = 'universe-orb anim-orb-breathe';
    orb.setAttribute('aria-label', `Navigate to ${node.label}`);
    const s = node.size;
    orb.style.cssText = `
      width:${s}px; height:${s}px;
      background:${node.gradient};
      color:${node.borderColor};
      border:1px solid ${node.borderColor};
      box-shadow:
        inset 0 0 ${Math.round(s*.42)}px rgba(60,35,10,.35),
        inset ${Math.round(s*.07)}px ${Math.round(s*.07)}px ${Math.round(s*.18)}px rgba(255,248,225,.18),
        0 ${Math.round(s*.25)}px ${Math.round(s*.65)}px ${node.shadowColor},
        0 0 ${Math.round(s*.5)}px ${node.glowColor};
    `;

    /* Specular highlight */
    const hl = document.createElement('span');
    hl.className = 'orb-highlight';
    orb.appendChild(hl);

    /* Click */
    orb.addEventListener('click', e => {
      e.preventDefault();
      const rect = orb.getBoundingClientRect();
      particleBurst(rect.left + rect.width/2, rect.top + rect.height/2, '#AE8157', 14);
      const ripple = document.createElement('div');
      ripple.className = 'universe-ripple';
      ripple.style.cssText = `width:${s}px;height:${s}px;border-color:${node.borderColor};`;
      wrap.appendChild(ripple);
      setTimeout(() => ripple.remove(), 750);
      setTimeout(() => {
        const tgt = document.querySelector(node.href);
        if (tgt) tgt.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }, 300);
    });

    const labelEl = document.createElement('span');
    labelEl.className   = 'universe-label';
    labelEl.textContent = node.label;

    wrap.appendChild(orb);
    wrap.appendChild(labelEl);
    container.appendChild(wrap);
  });

  /* Easter egg dot */
  const easterBtn = document.createElement('button');
  easterBtn.id = 'easter-star';
  easterBtn.setAttribute('aria-label', 'A tiny hidden surprise');
  easterBtn.addEventListener('click', e => {
    const msg = document.getElementById('easter-msg');
    if (msg) {
      particleBurst(e.clientX, e.clientY, '#AE8157', 16);
      msg.classList.toggle('hidden');
    }
  });
  document.getElementById('universe')?.appendChild(easterBtn);
}

function hexToRgb(hex) {
  const r = parseInt(hex.slice(1,3), 16);
  const g = parseInt(hex.slice(3,5), 16);
  const b = parseInt(hex.slice(5,7), 16);
  return `${r},${g},${b}`;
}

/* ────────────────────────────────────────────────────────────────
   SECRET SECTION — HANDCRAFTED 3D SURPRISE ENVELOPE
──────────────────────────────────────────────────────────────── */
function initSecret(content) {
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
}

/* ────────────────────────────────────────────────────────────────
   LETTER SECTION — HANDCRAFTED 3D ENVELOPE & VINTAGE STATIONERY
──────────────────────────────────────────────────────────────── */
function initLetter(content) {
  const openBtn     = document.getElementById('letter-open-btn');
  const envOuter    = document.getElementById('letter-env');
  const flap        = document.getElementById('letter-flap');
  const seal        = document.getElementById('letter-seal');
  const letterCard  = document.getElementById('letter-card');
  const closeBtn    = document.getElementById('letter-close-btn');
  const headingEl   = document.getElementById('letter-heading');
  const container   = document.getElementById('letter-paragraphs-container');
  const bodyEl      = document.getElementById('letter-body');
  const sigEl       = document.getElementById('letter-signature');
  const sigWrap     = document.getElementById('letter-signature-wrap');

  if (!envOuter || !letterCard) return;

  // 1. Populate Typography & Content
  if (headingEl && content?.letter?.heading) {
    headingEl.textContent = content.letter.heading;
  }

  const sigText = content?.closing?.signature || content?.letter?.signature || '— Aadi ✦';
  if (sigEl) {
    sigEl.textContent = sigText;
  }

  let paragraphs = [];
  const letterBodyText = content?.letter?.body || (bodyEl ? bodyEl.textContent : '');

  if (container && letterBodyText) {
    container.innerHTML = '';
    const rawParas = letterBodyText
      .split(/\n\s*\n/)
      .map(p => p.trim())
      .filter(Boolean);

    rawParas.forEach((pText, i) => {
      const p = document.createElement('p');
      p.className = `letter-para ${i === 0 ? 'letter-para--greeting' : ''}`;
      if (i === 0) p.id = 'letter-body';
      p.textContent = pText;
      container.appendChild(p);
      paragraphs.push(p);
    });
  } else if (bodyEl) {
    paragraphs = [bodyEl];
  }

  let isOpen = false;
  let isAnim = false;
  const reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  if (seal && typeof gsap !== 'undefined') {
    gsap.set(seal, { xPercent: -50, yPercent: -50, transformOrigin: 'center center' });
  }

  function openLetter(e) {
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
    const riseDistance = isMobile ? -170 : -230;

    if (typeof gsap !== 'undefined' && !reduced) {
      const tl = gsap.timeline({
        onComplete: () => {
          isOpen = true;
          isAnim = false;
          letterCard.classList.add('is-active');
          if (openBtn) {
            openBtn.innerHTML = 'Fold &amp; Close Note <span aria-hidden="true">✦</span>';
            openBtn.disabled = false;
            openBtn.style.opacity = '1';
          }
        }
      });

      // Step 2: Wax seal responds to click (press then pop)
      if (seal) {
        tl.to(seal, { scale: 0.9, duration: 0.14, ease: 'power2.in' })
          .to(seal, {
            scale: 1.15,
            opacity: 0,
            duration: 0.32,
            ease: 'power2.out',
            pointerEvents: 'none'
          }, '+=0.03');
      }

      // Step 3: Flap opens realistically in 3D around top crease (0 -> -180deg)
      if (flap) {
        tl.to(flap, {
          rotateX: -180,
          duration: 0.95,
          ease: 'power2.inOut',
          onUpdate: function() {
            if (this.progress() >= 0.5) {
              flap.style.zIndex = '2';
            } else {
              flap.style.zIndex = '30';
            }
          }
        }, '-=0.22');
      }

      // Step 4: Letter emerges cleanly in front of pocket (zIndex: 50) and slides out smoothly
      tl.set(letterCard, { zIndex: 50 }, '-=0.4')
        .fromTo(letterCard,
          { y: 0, scale: 0.96, opacity: 0 },
          {
            y: riseDistance,
            scale: 1,
            opacity: 1,
            duration: 0.95,
            ease: 'power3.out',
            boxShadow: '0 26px 64px rgba(73, 50, 36, 0.22), 0 6px 18px rgba(73, 50, 36, 0.1)'
          },
          '-=0.4'
        )

      // Step 6: Heading reveals itself
      .fromTo(headingEl,
        { opacity: 0, y: 14 },
        { opacity: 1, y: 0, duration: 0.52, ease: 'power2.out' },
        '-=0.15'
      )

      // Step 7: Paragraphs appear sequentially
      .fromTo(paragraphs,
        { opacity: 0, y: 12 },
        { opacity: 1, y: 0, stagger: 0.16, duration: 0.62, ease: 'power2.out' },
        '-=0.22'
      )

      // Step 8: Signature appears last
      .fromTo(sigWrap || sigEl,
        { opacity: 0, scale: 0.92, y: 10 },
        { opacity: 1, scale: 1, y: 0, duration: 0.72, ease: 'back.out(1.4)' },
        '-=0.15'
      );

    } else {
      // Graceful fallback for reduced motion or fallback
      if (flap) {
        flap.style.transform = 'rotateX(-180deg)';
        flap.style.zIndex = '2';
      }
      if (seal) {
        seal.style.opacity = '0';
        seal.style.pointerEvents = 'none';
      }
      if (letterCard) {
        letterCard.style.transform = `translate3d(0, ${riseDistance}px, 0) scale(1)`;
        letterCard.style.opacity = '1';
        letterCard.style.zIndex = '50';
        letterCard.classList.add('is-active');
      }
      if (headingEl) headingEl.style.opacity = '1';
      paragraphs.forEach(p => p.style.opacity = '1');
      if (sigWrap) sigWrap.style.opacity = '1';
      if (sigEl) sigEl.style.opacity = '1';
      isOpen = true;
      isAnim = false;
      if (openBtn) {
        openBtn.innerHTML = 'Fold &amp; Close Note <span aria-hidden="true">✦</span>';
        openBtn.disabled = false;
        openBtn.style.opacity = '1';
      }
    }
  }

  function closeLetter() {
    if (!isOpen || isAnim) return;
    isAnim = true;

    letterCard.classList.remove('is-active');

    if (typeof gsap !== 'undefined' && !reduced) {
      const closeTl = gsap.timeline({
        onComplete: () => {
          isOpen = false;
          isAnim = false;
          if (openBtn) {
            openBtn.innerHTML = 'Open the Note <span aria-hidden="true">✉</span>';
            openBtn.style.opacity = '1';
            openBtn.disabled = false;
          }
          if (seal) seal.style.transition = '';
          // Reset pristine state
          gsap.set(letterCard, { y: 0, scale: 0.96, opacity: 0, zIndex: 10 });
          gsap.set(envOuter, { y: 0 });
          if (flap) gsap.set(flap, { rotateX: 0, zIndex: 30 });
          if (seal) gsap.set(seal, { scale: 1, opacity: 1, xPercent: -50, yPercent: -50, pointerEvents: 'auto' });
          gsap.set([headingEl, ...paragraphs, sigWrap || sigEl], { opacity: 0, y: 0 });
        }
      });

      // 1. Text elements fade out gracefully
      closeTl.to([sigWrap || sigEl, ...paragraphs.slice().reverse(), headingEl], {
        opacity: 0,
        y: 8,
        duration: 0.28,
        stagger: 0.04,
        ease: 'power2.in'
      })

      // 2. Letter slides back down inside envelope pocket
      .to(letterCard, {
        y: 0,
        scale: 0.96,
        opacity: 0,
        duration: 0.65,
        ease: 'power3.in',
        onComplete: () => {
          letterCard.style.zIndex = '10';
        }
      }, '-=0.08')

      // 3. Flap folds back down in 3D (rotateX: -180 -> 0deg)
      .to(flap, {
        rotateX: 0,
        duration: 0.78,
        ease: 'power2.inOut',
        onUpdate: function() {
          if (this.progress() >= 0.5) {
            flap.style.zIndex = '30';
          } else {
            flap.style.zIndex = '2';
          }
        }
      }, '-=0.22')

      // 4. Wax seal returns and locks back into place
      .to(seal, {
        scale: 1,
        opacity: 1,
        pointerEvents: 'auto',
        duration: 0.42,
        ease: 'back.out(1.8)'
      }, '-=0.18');

    } else {
      // Graceful fallback
      if (letterCard) {
        letterCard.style.transform = 'translate3d(0, 0, 0) scale(0.96)';
        letterCard.style.opacity = '0';
        letterCard.style.zIndex = '10';
      }
      envOuter.style.transform = 'none';
      if (flap) {
        flap.style.transform = 'rotateX(0deg)';
        flap.style.zIndex = '30';
      }
      if (seal) {
        seal.style.opacity = '1';
        seal.style.pointerEvents = 'auto';
        seal.style.transition = '';
      }
      isOpen = false;
      isAnim = false;
      if (openBtn) {
        openBtn.innerHTML = 'Open the Note <span aria-hidden="true">✉</span>';
        openBtn.style.opacity = '1';
        openBtn.disabled = false;
      }
    }
  }

  // Event Listeners
  if (seal) {
    seal.addEventListener('click', openLetter);
    seal.addEventListener('keydown', e => {
      if (e.key === 'Enter' || e.key === ' ') {
        e.preventDefault();
        openLetter(e);
      }
    });
  }

  if (openBtn) {
    openBtn.addEventListener('click', () => {
      if (!isOpen) {
        openLetter();
      } else {
        closeLetter();
      }
    });
  }

  if (closeBtn) {
    closeBtn.addEventListener('click', e => {
      e.stopPropagation();
      closeLetter();
    });
  }

  // Clicking closed envelope triggers opening
  envOuter.addEventListener('click', e => {
    if (!isOpen && !isAnim && !e.target.closest('#letter-close-btn') && !e.target.closest('#letter-card')) {
      openLetter(e);
    }
  });
}

/* ────────────────────────────────────────────────────────────────
   FINAL SCENE
──────────────────────────────────────────────────────────────── */
function initFinalScene(lb, content, photos) {
  const finalPhoto = document.getElementById('final-photo');
  const finalPh    = document.getElementById('final-photo-placeholder');
  const replayBtn  = document.getElementById('explore-again-btn');

  const finalPhotos = photos.filter(p => p.section === 'final');
  if (finalPhotos.length && finalPhoto) {
    const fp = finalPhotos[0];
    finalPhoto.src = fp.src;
    finalPhoto.alt = fp.alt || 'Closing photograph';
    finalPhoto.onload  = () => { finalPhoto.style.opacity = '1'; if (finalPh) finalPh.style.opacity = '0'; };
    finalPhoto.onerror = () => { if (finalPh) finalPh.style.display = 'flex'; };
  }

  if (replayBtn) {
    replayBtn.addEventListener('click', e => {
      particleBurst(e.clientX, e.clientY, '#AE8157', 14);
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }
}

/* ────────────────────────────────────────────────────────────────
   AUDIO TOGGLE
──────────────────────────────────────────────────────────────── */
function initAudio() {
  const audioEl  = document.getElementById('bg-audio');
  const audioBtn = document.getElementById('audio-btn');
  if (!audioEl || !audioBtn) return;
  let playing = false;
  let synthTimer = null;
  let audioCtx = null;

  function playSynthChime() {
    try {
      if (!audioCtx) audioCtx = new (window.AudioContext || window.webkitAudioContext)();
      if (audioCtx.state === 'suspended') audioCtx.resume();
      const notes = [261.63, 329.63, 392.00, 523.25, 659.25]; // Warm C-major pentatonic
      const freq = notes[Math.floor(Math.random() * notes.length)];
      const osc = audioCtx.createOscillator();
      const gain = audioCtx.createGain();
      osc.type = 'sine';
      osc.frequency.setValueAtTime(freq, audioCtx.currentTime);
      gain.gain.setValueAtTime(0, audioCtx.currentTime);
      gain.gain.linearRampToValueAtTime(0.06, audioCtx.currentTime + 1.2);
      gain.gain.exponentialRampToValueAtTime(0.0001, audioCtx.currentTime + 4.5);
      osc.connect(gain);
      gain.connect(audioCtx.destination);
      osc.start();
      osc.stop(audioCtx.currentTime + 4.6);
    } catch (_) {}
  }

  audioBtn.addEventListener('click', () => {
    if (playing) {
      if (audioEl) audioEl.pause();
      if (synthTimer) { clearInterval(synthTimer); synthTimer = null; }
      audioBtn.textContent = '♪';
      audioBtn.setAttribute('aria-label', 'Play ambient music');
      audioBtn.classList.remove('playing');
    } else {
      audioBtn.textContent = '⏸';
      audioBtn.setAttribute('aria-label', 'Pause ambient music');
      audioBtn.classList.add('playing');
      const p = audioEl ? audioEl.play() : Promise.reject();
      p.catch(() => {
        playSynthChime();
        if (!synthTimer) {
          synthTimer = setInterval(playSynthChime, 3200);
        }
      });
    }
    playing = !playing;
  });
}

/* ────────────────────────────────────────────────────────────────
   STARFIELD LAZY INIT — section canvases
──────────────────────────────────────────────────────────────── */
function initSectionCanvases() {
  const introCanvas    = document.getElementById('intro-canvas');
  const universeCanvas = document.getElementById('universe-canvas');
  const secretCanvas   = document.getElementById('secret-canvas');
  const finalCanvas    = document.getElementById('final-canvas');

  let universeSF, finalSF;

  /* Intro starfield — visible immediately */
  const introSF = introCanvas
    ? new StarField(introCanvas, { count: 150, color: '#9E7248', maxSize: 1.8, speed: 0.014 })
    : null;

  const sectionCanvasMap = [
    { id: 'universe',    canvas: universeCanvas, color: '#7A5030', count: 145, minSize: 0.5, maxSize: 2.0, speed: 0.016, ref: r => universeSF = r },
    { id: 'secret',      canvas: secretCanvas,   color: '#8C6238', count: 80,  minSize: 0.4, maxSize: 1.6, speed: 0.012, ref: () => {} },
    { id: 'final-scene', canvas: finalCanvas,    color: '#966840', count: 100, minSize: 0.4, maxSize: 1.8, speed: 0.015, ref: r => finalSF = r },
  ];

  const lazyObs = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (!entry.isIntersecting) return;
      const map = sectionCanvasMap.find(m => m.id === entry.target.id);
      if (!map || !map.canvas) return;
      const sf = new StarField(map.canvas, {
        count: map.count, color: map.color,
        minSize: map.minSize, maxSize: map.maxSize, speed: map.speed,
      });
      map.ref(sf);
      lazyObs.unobserve(entry.target);
    });
  }, { threshold: 0.01 });

  sectionCanvasMap.forEach(m => {
    const el = document.getElementById(m.id);
    if (el) lazyObs.observe(el);
  });
}

/* ────────────────────────────────────────────────────────────────
   HERO PHOTO LOAD
──────────────────────────────────────────────────────────────── */
function initHero(content) {
  const heroBg = document.getElementById('hero-bg');
  if (!heroBg || !content?.hero?.photo?.src) return;
  heroBg.alt = content.hero.photo.alt || 'Hero photograph';
  heroBg.onload  = () => heroBg.classList.add('loaded');
  heroBg.onerror = () => {};
  heroBg.src     = content.hero.photo.src;
}

/* ────────────────────────────────────────────────────────────────
   CONTENT INJECTION FROM siteContent
──────────────────────────────────────────────────────────────── */
function applyContent(content) {
  const set = (id, text) => { const el = document.getElementById(id); if (el && text) el.textContent = text; };
  const setHtml = (id, html) => { const el = document.getElementById(id); if (el && html) el.innerHTML = html; };

  /* Intro */
  set('intro-line-1', content.introduction?.firstLine);
  set('intro-line-2', content.introduction?.secondLine);

  /* Hero */
  set('hero-eyebrow', content.hero?.eyebrow);
  if (content.hero?.heading) {
    const el = document.getElementById('hero-heading');
    if (el) { el.innerHTML = content.hero.heading.replace(/\n/g, '<br>'); }
  }
  set('hero-subheading', content.hero?.subheading);

  /* Universe name */
  const univName = document.getElementById('universe-name');
  if (univName && content.siteTitle) {
    const name = content.siteTitle.replace(/\s*(little\s*universe|her\s*little\s*universe)/i, '').trim() || "Bhavna's";
    univName.textContent = name;
  }

  /* Gallery */
  set('gallery-eyebrow', content.gallery?.eyebrow);

  /* Letter */
  set('letter-teaser',     content.letter?.teaser);
  set('letter-sub-teaser', content.letter?.subTeaser);
  set('letter-heading',    content.letter?.heading);
  set('letter-body',       content.letter?.body);

  /* Final */
  set('final-heading',   content.closing?.heading);
  set('final-body',      content.closing?.body);
  set('final-signature', content.closing?.signature);

  /* Secret */
  set('secret-teaser',       content.secret?.teaser);
  set('secret-message-text', content.secret?.message);
}

/* ════════════════════════════════════════════════════════════════
   BOOT
════════════════════════════════════════════════════════════════ */
(function boot() {
  const content = window.HLU_CONTENT || window.siteContent || {};
  const photos  = content.photos || [];

  /* Apply all text content first */
  applyContent(content);

  /* Init everything */
  initNav();
  initAudio();
  initSectionCanvases();

  const cursor = new CustomCursor();
  const lb     = new Lightbox();

  /* Hero photo */
  initHero(content);

  /* Wait for DOM to settle, then init components */
  requestAnimationFrame(() => {
    initGallery(lb, photos);
    initScrapbook(lb, photos);
    initMosaic(lb, photos);
    initUniverse();
    initSecret(content);
    initLetter(content);
    initFinalScene(lb, content, photos);
    initIntro();
  });
})();
