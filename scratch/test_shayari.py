import subprocess
import time
import os
import json
import urllib.request
import socket
import base64
import sys

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

profile_dir = os.path.abspath("scratch/chrome_prof_shayari")
os.makedirs(profile_dir, exist_ok=True)
screenshot_dir = os.path.abspath("scratch/shayari_screenshots")
os.makedirs(screenshot_dir, exist_ok=True)

test_configs = [
    (1280, 800, "desktop_1280x800"),
    (768, 1024, "tablet_portrait_768x1024"),
    (1024, 768, "tablet_landscape_1024x768"),
    (390, 844, "mobile_390x844")
]

for w, h, label in test_configs:
    print(f"=== Testing {label} ({w}x{h}) ===")
    cmd = [
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        "--headless=new",
        "--remote-debugging-port=9261",
        "--disable-gpu",
        "--no-sandbox",
        f"--user-data-dir={profile_dir}",
        f"--window-size={w},{h}",
        "http://localhost:5173/"
    ]
    proc = subprocess.Popen(cmd)
    time.sleep(2.5)

    try:
        with urllib.request.urlopen("http://localhost:9261/json") as res:
            tabs = json.loads(res.read().decode('utf-8'))
        target_tab = [t for t in tabs if "5173" in t.get("url", "")][0]
        ws_host = "localhost"
        ws_port = 9261
        path = target_tab['webSocketDebuggerUrl'].split(f"{ws_host}:{ws_port}")[1]
        
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ws_host, ws_port))
        handshake = (
            f"GET {path} HTTP/1.1\r\n"
            f"Host: {ws_host}:{ws_port}\r\n"
            "Upgrade: websocket\r\n"
            "Connection: Upgrade\r\n"
            "Sec-WebSocket-Key: dGhlIHNhbXBsZSBub25jZQ==\r\n"
            "Sec-WebSocket-Version: 13\r\n\r\n"
        )
        s.sendall(handshake.encode('utf-8'))
        resp = s.recv(4096)
        
        def send_cdp(cmd_id, method, params=None):
            payload = json.dumps({"id": cmd_id, "method": method, "params": params or {}}).encode('utf-8')
            length = len(payload)
            mask = os.urandom(4)
            if length <= 125:
                header = bytes([0x81, 0x80 | length]) + mask
            elif length <= 65535:
                header = bytes([0x81, 0x80 | 126]) + length.to_bytes(2, 'big') + mask
            else:
                header = bytes([0x81, 0x80 | 127]) + length.to_bytes(8, 'big') + mask
                
            masked = bytearray(length)
            for i in range(length):
                masked[i] = payload[i] ^ mask[i % 4]
            s.sendall(header + masked)
            
            data = b""
            while True:
                chunk = s.recv(16384)
                data += chunk
                if b'"id":' + str(cmd_id).encode('utf-8') in data:
                    break
            
            idx = data.find(b'{"id":' + str(cmd_id).encode('utf-8'))
            if idx != -1:
                end_idx = data.rfind(b'}')
                return json.loads(data[idx:end_idx+1].decode('utf-8', errors='ignore'))
            return {}

        is_mobile = w <= 768
        send_cdp(1, "Emulation.setDeviceMetricsOverride", {
            "width": w,
            "height": h,
            "deviceScaleFactor": 1,
            "mobile": is_mobile
        })
        time.sleep(1)

        # Bypass intro screen and scroll to secret section
        send_cdp(2, "Runtime.evaluate", {
            "expression": """
            (() => {
                const intro = document.getElementById('intro');
                if (intro) intro.style.display = 'none';
                const main = document.getElementById('main-content');
                if (main) {
                    main.style.opacity = '1';
                    main.style.visibility = 'visible';
                }
                const sec = document.getElementById('secret');
                if (sec) {
                    sec.scrollIntoView({ behavior: 'instant', block: 'center' });
                }
            })()
            """
        })
        time.sleep(1)

        # Check before opening: shayari elements must have opacity 0 or be hidden
        check_before = send_cdp(3, "Runtime.evaluate", {
            "expression": """
            JSON.stringify((() => {
                const line1 = document.getElementById('shayari-line-1');
                const line1Style = line1 ? window.getComputedStyle(line1) : null;
                const card = document.getElementById('secret-card');
                const cardStyle = card ? window.getComputedStyle(card) : null;
                return {
                    line1Opacity: line1Style ? line1Style.opacity : null,
                    cardOpacity: cardStyle ? cardStyle.opacity : null,
                    cardActive: card ? card.classList.contains('is-active') : false
                };
            })())
            """,
            "returnByValue": True
        })
        val_before = check_before.get('result', {}).get('result', {}).get('value')
        print(f"[{label}] State BEFORE opening: {val_before}")

        # Trigger opening via seal click or reveal button
        send_cdp(4, "Runtime.evaluate", {
            "expression": """
            (() => {
                const seal = document.getElementById('secret-seal');
                if (seal) seal.click();
            })()
            """
        })

        # Wait for the full choreography to unfold (envelope open ~0.9s + settle + lines stagger ~3s + flourish ~0.7s = ~6s)
        time.sleep(6.2)

        # Check after opening
        check_after = send_cdp(5, "Runtime.evaluate", {
            "expression": """
            JSON.stringify((() => {
                const line1 = document.getElementById('shayari-line-1');
                const line4 = document.getElementById('shayari-line-4');
                const highlight = document.querySelector('.shayari-couplet--highlight');
                const flourish = document.getElementById('secret-flourish');
                const floral = document.getElementById('secret-floral');
                const divider = document.getElementById('secret-divider');
                
                return {
                    line1Opacity: line1 ? window.getComputedStyle(line1).opacity : null,
                    line1Length: line1 ? line1.textContent.length : 0,
                    line4Opacity: line4 ? window.getComputedStyle(line4).opacity : null,
                    line4Length: line4 ? line4.textContent.length : 0,
                    highlightClass: highlight ? highlight.className : null,
                    flourishOpacity: flourish ? window.getComputedStyle(flourish).opacity : null,
                    floralOpacity: floral ? window.getComputedStyle(floral).opacity : null,
                    dividerOpacity: divider ? window.getComputedStyle(divider).opacity : null
                };
            })())
            """,
            "returnByValue": True
        })
        val_after = check_after.get('result', {}).get('result', {}).get('value')
        print(f"[{label}] State AFTER opening: {val_after}")

        # Scroll secret section into view for clean crop
        send_cdp(6, "Runtime.evaluate", {
            "expression": """
            (() => {
                const sec = document.getElementById('secret');
                if (sec) sec.scrollIntoView({ behavior: 'instant', block: 'center' });
            })()
            """
        })
        time.sleep(0.5)

        # Capture screenshot of the secret section
        clip_res = send_cdp(7, "Runtime.evaluate", {
            "expression": """
            (() => {
                const sec = document.getElementById('secret');
                const r = sec.getBoundingClientRect();
                return {
                    x: Math.max(0, r.left),
                    y: Math.max(0, r.top + window.scrollY),
                    width: r.width,
                    height: r.height
                };
            })()
            """,
            "returnByValue": True
        })
        clip = clip_res.get('result', {}).get('result', {}).get('value')
        
        # Capture screenshot
        shot = send_cdp(8, "Page.captureScreenshot", {
            "format": "png",
            "clip": {
                "x": clip["x"],
                "y": clip["y"],
                "width": clip["width"],
                "height": clip["height"],
                "scale": 1
            }
        })
        b64 = shot.get('result', {}).get('data')
        if b64:
            out_file = os.path.join(screenshot_dir, f"{label}_secret_shayari.png")
            with open(out_file, "wb") as f:
                f.write(base64.b64decode(b64))
            print(f"Saved screenshot: {out_file}")

        s.close()
    finally:
        proc.terminate()
        proc.wait()

print("ALL TESTS COMPLETE!")
