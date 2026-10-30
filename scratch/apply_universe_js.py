import sys

with open('src/components/app.js', 'r', encoding='utf-8') as f:
    content = f.read()

start_marker = '/* ────────────────────────────────────────────────────────────────\n   INTERACTIVE UNIVERSE — 3D PREMIUM ORB SYSTEM\n──────────────────────────────────────────────────────────────── */'
if start_marker not in content:
    start_marker = '/* ────────────────────────────────────────────────────────────────\r\n   INTERACTIVE UNIVERSE — 3D PREMIUM ORB SYSTEM\r\n──────────────────────────────────────────────────────────────── */'

end_marker = 'function hexToRgb(hex) {'

idx_start = content.find(start_marker)
idx_end = content.find(end_marker)

if idx_start == -1 or idx_end == -1:
    print(f"Markers not found: idx_start={idx_start}, idx_end={idx_end}")
    sys.exit(1)

new_code = '''/* ────────────────────────────────────────────────────────────────
   REALISTIC 3D PLANETARY UNIVERSE — ASTRONOMICAL EXPLORATION
   Luxury Astronomical Solar System Visualization (Three.js WebGL)
──────────────────────────────────────────────────────────────── */
function initUniverse() {
  const canvas = document.getElementById('universe-3d-canvas');
  const section = document.getElementById('universe');
  if (!canvas || !section) return;

  if (typeof THREE === 'undefined') {
    console.warn('Three.js not found, skipping 3D planetary rendering');
    return;
  }

  // 1. Scene, Camera, Renderer
  const scene = new THREE.Scene();
  const width = section.offsetWidth || window.innerWidth;
  const height = section.offsetHeight || window.innerHeight;

  const camera = new THREE.PerspectiveCamera(45, width / height, 0.1, 100);
  camera.position.set(0, 0, 18);

  const renderer = new THREE.WebGLRenderer({
    canvas,
    alpha: true,
    antialias: true,
    powerPreference: 'high-performance',
  });
  renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 2));
  renderer.setSize(width, height);
  renderer.toneMapping = THREE.ACESFilmicToneMapping;
  renderer.toneMappingExposure = 1.08;

  // 2. Space Lighting
  // Directional Sun Light (creates natural terminator boundary across all planets)
  const sunLight = new THREE.DirectionalLight(0xfff6ea, 2.5);
  sunLight.position.set(-12, 8, 14);
  scene.add(sunLight);

  // Warm champagne/mocha ambient light (ensures shadowed hemisphere retains subtle detail)
  const ambientLight = new THREE.AmbientLight(0x72543c, 0.45);
  scene.add(ambientLight);

  // Delicate atmospheric rim light
  const rimLight = new THREE.DirectionalLight(0xdfc29d, 0.9);
  rimLight.position.set(10, -6, -8);
  scene.add(rimLight);

  // 3. Texture Loading
  const loader = new THREE.TextureLoader();
  const textures = {
    earth: loader.load('public/textures/planets/earth.webp'),
    earthClouds: loader.load('public/textures/planets/earth_clouds.webp'),
    mars: loader.load('public/textures/planets/mars.webp'),
    jupiter: loader.load('public/textures/planets/jupiter.webp'),
    moon: loader.load('public/textures/planets/moon.webp'),
    saturn: loader.load('public/textures/planets/saturn.webp'),
    saturnRing: loader.load('public/textures/planets/saturn_ring_topdown.png'),
  };

  // Helper: Atmospheric Rim Glow Mesh
  function createAtmosphereGlow(radius, colorRgb) {
    const geo = new THREE.SphereGeometry(radius * 1.045, 48, 48);
    const mat = new THREE.ShaderMaterial({
      vertexShader: `
        varying vec3 vNormal;
        void main() {
          vNormal = normalize(normalMatrix * normal);
          gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0);
        }
      `,
      fragmentShader: `
        varying vec3 vNormal;
        uniform vec3 uColor;
        uniform float uGlow;
        void main() {
          float intensity = pow(0.66 - dot(vNormal, vec3(0.0, 0.0, 1.0)), 2.3);
          gl_FragColor = vec4(uColor, 1.0) * intensity * uGlow;
        }
      `,
      uniforms: {
        uColor: { value: new THREE.Vector3(colorRgb[0], colorRgb[1], colorRgb[2]) },
        uGlow: { value: 0.85 },
      },
      blending: THREE.AdditiveBlending,
      side: THREE.BackSide,
      transparent: true,
      depthWrite: false,
    });
    return new THREE.Mesh(geo, mat);
  }

  // 4. Planets Definitions
  const planetConfigs = [
    {
      id: 'earth',
      name: 'THE GALLERY',
      href: '#gallery',
      radius: 1.25,
      pos: { x: -5.8, y: 2.3, z: 0 },
      rotSpeed: 0.0035,
      tiltZ: 23.4 * (Math.PI / 180),
      tiltX: 0.08,
      build(group) {
        // Earth Base Sphere
        const geo = new THREE.SphereGeometry(1.25, 64, 64);
        const mat = new THREE.MeshStandardMaterial({
          map: textures.earth,
          roughness: 0.62,
          metalness: 0.1,
        });
        const mesh = new THREE.Mesh(geo, mat);
        group.add(mesh);

        // Independent Rotating Clouds Layer
        const cloudGeo = new THREE.SphereGeometry(1.275, 64, 64);
        const cloudMat = new THREE.MeshStandardMaterial({
          map: textures.earthClouds,
          transparent: true,
          opacity: 0.72,
          blending: THREE.NormalBlending,
          depthWrite: false,
        });
        const cloudMesh = new THREE.Mesh(cloudGeo, cloudMat);
        group.add(cloudMesh);
        group.userData.cloudMesh = cloudMesh;

        // Rayleigh Cyan-Blue Atmosphere Glow
        const atmos = createAtmosphereGlow(1.25, [0.38, 0.68, 0.95]);
        group.add(atmos);
        group.userData.atmos = atmos;
      },
    },
    {
      id: 'mars',
      name: 'LITTLE MOMENTS',
      href: '#scrapbook',
      radius: 0.88,
      pos: { x: 5.5, y: 2.7, z: 0.4 },
      rotSpeed: 0.0030,
      tiltZ: 25.2 * (Math.PI / 180),
      tiltX: 0.06,
      build(group) {
        // Mars Cratered Terrain Sphere
        const geo = new THREE.SphereGeometry(0.88, 64, 64);
        const mat = new THREE.MeshStandardMaterial({
          map: textures.mars,
          roughness: 0.88,
          metalness: 0.04,
        });
        const mesh = new THREE.Mesh(geo, mat);
        group.add(mesh);

        // Terracotta Atmosphere Rim
        const atmos = createAtmosphereGlow(0.88, [0.92, 0.45, 0.28]);
        group.add(atmos);
        group.userData.atmos = atmos;
      },
    },
    {
      id: 'jupiter',
      name: 'THE SCRAPBOOK',
      href: '#scrapbook',
      radius: 1.68,
      pos: { x: 6.4, y: -2.1, z: -0.4 },
      rotSpeed: 0.0062,
      tiltZ: 3.1 * (Math.PI / 180),
      tiltX: 0.02,
      build(group) {
        // Jupiter Swirling Atmospheric Bands Sphere
        const geo = new THREE.SphereGeometry(1.68, 64, 64);
        const mat = new THREE.MeshStandardMaterial({
          map: textures.jupiter,
          roughness: 0.68,
          metalness: 0.02,
        });
        const mesh = new THREE.Mesh(geo, mat);
        group.add(mesh);

        // Warm Amber Atmosphere Rim
        const atmos = createAtmosphereGlow(1.68, [0.88, 0.72, 0.48]);
        group.add(atmos);
        group.userData.atmos = atmos;
      },
    },
    {
      id: 'moon',
      name: 'A LITTLE SECRET',
      href: '#secret',
      radius: 0.76,
      pos: { x: -5.6, y: -2.7, z: 0.7 },
      rotSpeed: 0.0020,
      tiltZ: 1.5 * (Math.PI / 180),
      tiltX: 0.02,
      build(group) {
        // Moon Cratered Basalt Surface (Sharp Shadows, No Atmosphere)
        const geo = new THREE.SphereGeometry(0.76, 64, 64);
        const mat = new THREE.MeshStandardMaterial({
          map: textures.moon,
          roughness: 0.96,
          metalness: 0.0,
        });
        const mesh = new THREE.Mesh(geo, mat);
        group.add(mesh);
      },
    },
    {
      id: 'saturn',
      name: 'ONE LAST THING',
      href: '#letter-section',
      radius: 1.32,
      pos: { x: 0.2, y: -4.1, z: 0.1 },
      rotSpeed: 0.0042,
      tiltZ: 26.7 * (Math.PI / 180),
      tiltX: 0.32,
      build(group) {
        // Saturn Gas Giant Sphere
        const geo = new THREE.SphereGeometry(1.32, 64, 64);
        const mat = new THREE.MeshStandardMaterial({
          map: textures.saturn,
          roughness: 0.72,
          metalness: 0.03,
        });
        const mesh = new THREE.Mesh(geo, mat);
        group.add(mesh);

        // Authentic 3D Tilted Ring System with Cassini Division
        const ringGeo = new THREE.PlaneGeometry(6.6, 6.6, 32, 32);
        const ringMat = new THREE.MeshStandardMaterial({
          map: textures.saturnRing,
          transparent: true,
          side: THREE.DoubleSide,
          opacity: 0.94,
          roughness: 0.55,
          metalness: 0.05,
          depthWrite: true,
        });
        const ringMesh = new THREE.Mesh(ringGeo, ringMat);
        ringMesh.rotation.x = Math.PI / 2.2;
        group.add(ringMesh);

        // Butterscotch Atmosphere Rim
        const atmos = createAtmosphereGlow(1.32, [0.92, 0.82, 0.62]);
        group.add(atmos);
        group.userData.atmos = atmos;
      },
    },
  ];

  // 5. Instantiate Planets & Hit Volumes
  const planets = [];
  const hitObjects = [];

  const isMobile = window.innerWidth <= 768;
  const isReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  planetConfigs.forEach((cfg, idx) => {
    const group = new THREE.Group();

    // Position & Tilt
    let px = cfg.pos.x;
    let py = cfg.pos.y;
    let pz = cfg.pos.z;

    // Mobile Responsive Layout (gentle vertical constellation alignment)
    if (isMobile) {
      const mobX = [-1.5, 1.5, -1.6, 1.4, 0.0];
      const mobY = [4.2, 2.1, 0.0, -2.1, -4.3];
      px = mobX[idx];
      py = mobY[idx];
      pz = 0;
    }

    group.position.set(px, py, pz);
    group.rotation.z = cfg.tiltZ;
    group.rotation.x = cfg.tiltX;

    cfg.build(group);
    scene.add(group);

    // Invisible Hit Volume for effortless clicking and hover
    const hitGeo = new THREE.SphereGeometry(cfg.radius * 1.35, 16, 16);
    const hitMat = new THREE.MeshBasicMaterial({ visible: false });
    const hitMesh = new THREE.Mesh(hitGeo, hitMat);
    hitMesh.position.set(px, py, pz);
    hitMesh.userData = { planetId: cfg.id, config: cfg, group };
    scene.add(hitMesh);
    hitObjects.push(hitMesh);

    const planetItem = {
      id: cfg.id,
      group,
      hitMesh,
      baseX: px,
      baseY: py,
      baseZ: pz,
      rotSpeed: cfg.rotSpeed,
      scale: 1.0,
      targetScale: 1.0,
      config: cfg,
      card: document.getElementById(`planet-card-${cfg.id}`),
    };

    planets.push(planetItem);
  });

  // Adjust camera for mobile
  if (isMobile) {
    camera.position.z = 22;
  }

  // 6. Interactive Raycasting & Hover / Click Handlers
  const raycaster = new THREE.Raycaster();
  const mouse = new THREE.Vector2(-9999, -9999);
  let hoveredPlanet = null;
  let targetCamX = 0;
  let targetCamY = 0;

  function updateHover(planetItem) {
    if (hoveredPlanet === planetItem) return;

    // Unhover previous
    if (hoveredPlanet) {
      hoveredPlanet.targetScale = 1.0;
      if (hoveredPlanet.group.userData.atmos) {
        hoveredPlanet.group.userData.atmos.material.uniforms.uGlow.value = 0.85;
      }
      hoveredPlanet.card?.classList.remove('is-hovered');
    }

    hoveredPlanet = planetItem;

    // Hover new
    if (hoveredPlanet) {
      hoveredPlanet.targetScale = 1.18;
      if (hoveredPlanet.group.userData.atmos) {
        hoveredPlanet.group.userData.atmos.material.uniforms.uGlow.value = 1.65;
      }
      hoveredPlanet.card?.classList.add('is-hovered');
      canvas.style.cursor = 'pointer';
    } else {
      canvas.style.cursor = 'grab';
    }
  }

  function handlePlanetClick(planetItem, clientX, clientY) {
    if (!planetItem) return;
    const cfg = planetItem.config;

    // Spawn celestial particle burst
    particleBurst(clientX, clientY, '#DFC29D', 18);

    // Smooth foreground camera move
    gsap.to(planetItem.group.scale, {
      x: 1.45, y: 1.45, z: 1.45,
      duration: 0.65,
      ease: 'power3.out',
      onComplete() {
        gsap.to(planetItem.group.scale, { x: 1.0, y: 1.0, z: 1.0, duration: 0.5, ease: 'power2.inOut' });
      }
    });

    // Smooth scroll to target destination
    setTimeout(() => {
      const tgt = document.querySelector(cfg.href);
      if (tgt) tgt.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }, 280);
  }

  // Canvas Mousemove Raycasting
  canvas.addEventListener('mousemove', e => {
    const rect = canvas.getBoundingClientRect();
    mouse.x = ((e.clientX - rect.left) / rect.width) * 2 - 1;
    mouse.y = -(((e.clientY - rect.top) / rect.height) * 2 - 1);

    // Subtle 3D camera parallax
    targetCamX = mouse.x * 0.75;
    targetCamY = mouse.y * 0.5;

    raycaster.setFromCamera(mouse, camera);
    const intersects = raycaster.intersectObjects(hitObjects);

    if (intersects.length > 0) {
      const hitId = intersects[0].object.userData.planetId;
      const found = planets.find(p => p.id === hitId);
      updateHover(found);
    } else {
      updateHover(null);
    }
  }, { passive: true });

  canvas.addEventListener('mouseleave', () => {
    mouse.set(-9999, -9999);
    targetCamX = 0;
    targetCamY = 0;
    updateHover(null);
  });

  // Canvas Click
  canvas.addEventListener('click', e => {
    const rect = canvas.getBoundingClientRect();
    mouse.x = ((e.clientX - rect.left) / rect.width) * 2 - 1;
    mouse.y = -(((e.clientY - rect.top) / rect.height) * 2 - 1);

    raycaster.setFromCamera(mouse, camera);
    const intersects = raycaster.intersectObjects(hitObjects);

    if (intersects.length > 0) {
      const hitId = intersects[0].object.userData.planetId;
      const found = planets.find(p => p.id === hitId);
      handlePlanetClick(found, e.clientX, e.clientY);
    }
  });

  // Card Hover & Click Handlers
  planets.forEach(p => {
    if (!p.card) return;

    p.card.addEventListener('mouseenter', () => updateHover(p));
    p.card.addEventListener('mouseleave', () => updateHover(null));

    p.card.addEventListener('click', e => {
      e.preventDefault();
      const rect = p.card.getBoundingClientRect();
      handlePlanetClick(p, rect.left + rect.width / 2, rect.top + rect.height / 2);
    });
  });

  // 7. Animation Loop with Viewport Culling
  let isRunning = false;
  let rafId = null;

  function tick() {
    if (!isRunning) return;

    const time = performance.now() * 0.001;

    // Slow planetary axial rotation
    planets.forEach((p, i) => {
      if (!isReduced) {
        p.group.rotation.y += p.rotSpeed;

        // Earth clouds independent atmospheric rotation
        if (p.group.userData.cloudMesh) {
          p.group.userData.cloudMesh.rotation.y += 0.0016;
        }

        // Harmonic spatial floating drift
        const phase = i * 1.35;
        p.group.position.y = p.baseY + Math.sin(time * 0.85 + phase) * 0.12;
        p.hitMesh.position.y = p.group.position.y;
      }

      // Smooth hover scale interpolation
      p.scale += (p.targetScale - p.scale) * 0.12;
      p.group.scale.set(p.scale, p.scale, p.scale);
    });

    // Camera parallax tilt
    if (!isReduced) {
      camera.position.x += (targetCamX - camera.position.x) * 0.05;
      camera.position.y += (targetCamY - camera.position.y) * 0.05;
      camera.lookAt(0, 0, 0);
    }

    renderer.render(scene, camera);
    rafId = requestAnimationFrame(tick);
  }

  function start() {
    if (isRunning) return;
    isRunning = true;
    tick();
  }

  function stop() {
    isRunning = false;
    if (rafId) {
      cancelAnimationFrame(rafId);
      rafId = null;
    }
  }

  // 8. IntersectionObserver (0% GPU when section is not visible)
  const obs = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        start();
      } else {
        stop();
      }
    });
  }, { threshold: 0.01, rootMargin: '100px 0px 100px 0px' });

  obs.observe(section);

  // 9. Resize Handling
  function onResize() {
    const w = section.offsetWidth || window.innerWidth;
    const h = section.offsetHeight || window.innerHeight;
    camera.aspect = w / h;
    camera.position.z = w <= 768 ? 22 : 18;
    camera.updateProjectionMatrix();
    renderer.setSize(w, h);
  }

  window.addEventListener('resize', onResize, { passive: true });

  // 10. Easter Egg Star Button
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
  section.appendChild(easterBtn);
}

'''

content = content[:idx_start] + new_code + content[idx_end:]
with open('src/components/app.js', 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully updated src/components/app.js with Realistic 3D Planetary Universe engine!")
