import sys

with open('src/components/app.js', 'r', encoding='utf-8') as f:
    code = f.read()

# Let's inspect lines 955-1015
target_section = """  const isMobile = window.innerWidth <= 768;
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
  }"""

replacement_section = """  const isReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // Responsive Celestial Coordinate Calculator
  function getPlanetCoordinates(w, h, idx) {
    const isPortrait = h > w;
    if (w <= 600) {
      // Mobile vertical alignment
      const mobX = [-1.3, 1.3, -1.4, 1.3, 0.0];
      const mobY = [4.2, 2.1, 0.0, -2.1, -4.3];
      return { x: mobX[idx], y: mobY[idx], z: 0 };
    }
    if (isPortrait && w <= 960) {
      // Tablet Portrait (768x1024, 820x1180, iPad Mini, iPad Air, iPad Pro)
      // Intentional vertical oval constellation with clean perimeter framing
      const tabPortX = [-2.8, 2.8, 3.1, -2.9, 0.0];
      const tabPortY = [3.2, 3.6, -1.6, -2.2, -5.2];
      return { x: tabPortX[idx], y: tabPortY[idx], z: 0.1 };
    }
    if (w <= 1100) {
      // Tablet Landscape (1024x768)
      const tabLandX = [-5.0, 4.8, 5.4, -4.8, 0.2];
      const tabLandY = [2.0, 2.4, -1.9, -2.2, -3.8];
      return { x: tabLandX[idx], y: tabLandY[idx], z: 0.1 };
    }
    // Desktop (> 1100px)
    return { x: planetConfigs[idx].pos.x, y: planetConfigs[idx].pos.y, z: planetConfigs[idx].pos.z };
  }

  function getCameraZ(w, h) {
    const aspect = w / h;
    if (w <= 600) return 22;
    if (aspect < 1.0) {
      // Portrait tablet: dynamically scale Z so horizontal extent comfortably fits +-3.2 units
      return Math.max(19, Math.min(23, Math.round(14.2 / aspect)));
    }
    if (w <= 1100) return 17;
    return 18;
  }

  const initialW = section.offsetWidth || window.innerWidth;
  const initialH = section.offsetHeight || window.innerHeight;
  camera.position.z = getCameraZ(initialW, initialH);

  planetConfigs.forEach((cfg, idx) => {
    const group = new THREE.Group();
    const coords = getPlanetCoordinates(initialW, initialH, idx);
    let px = coords.x;
    let py = coords.y;
    let pz = coords.z;

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
  });"""

target_onresize = """  // 9. Resize Handling
  function onResize() {
    const w = section.offsetWidth || window.innerWidth;
    const h = section.offsetHeight || window.innerHeight;
    camera.aspect = w / h;
    camera.position.z = w <= 768 ? 22 : 18;
    camera.updateProjectionMatrix();
    renderer.setSize(w, h);
  }"""

replacement_onresize = """  // 9. Resize Handling (Tablet & Desktop Dynamic Repositioning)
  function onResize() {
    const w = section.offsetWidth || window.innerWidth;
    const h = section.offsetHeight || window.innerHeight;
    camera.aspect = w / h;
    camera.position.z = getCameraZ(w, h);
    camera.updateProjectionMatrix();
    renderer.setSize(w, h);

    // Dynamically glide planets to their responsive compositions
    planets.forEach((p, idx) => {
      const coords = getPlanetCoordinates(w, h, idx);
      p.baseX = coords.x;
      p.baseY = coords.y;
      p.baseZ = coords.z;
      p.group.position.x = coords.x;
      p.group.position.z = coords.z;
      p.hitMesh.position.x = coords.x;
      p.hitMesh.position.z = coords.z;
    });
  }"""

code_norm = code.replace('\r\n', '\n')
target_section_norm = target_section.replace('\r\n', '\n')
replacement_section_norm = replacement_section.replace('\r\n', '\n')

assert target_section_norm in code_norm, "Target section not found"
code_norm = code_norm.replace(target_section_norm, replacement_section_norm, 1)

target_onresize_norm = target_onresize.replace('\r\n', '\n')
replacement_onresize_norm = replacement_onresize.replace('\r\n', '\n')

assert target_onresize_norm in code_norm, "Target onresize not found"
code_norm = code_norm.replace(target_onresize_norm, replacement_onresize_norm, 1)

with open('src/components/app.js', 'w', encoding='utf-8') as f:
    f.write(code_norm)

print("Successfully updated Three.js planet positions & resize handling in app.js!")
