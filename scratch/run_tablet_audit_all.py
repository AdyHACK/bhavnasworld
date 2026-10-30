import subprocess
import time
import os
import json
import urllib.request
import base64
import socket

VIEWPORTS = [
    {"name": "ipad_mini_portrait_768x1024", "w": 768, "h": 1024},
    {"name": "ipad_air_portrait_820x1180", "w": 820, "h": 1180},
    {"name": "ipad_landscape_1024x768", "w": 1024, "h": 768}
]

SECTIONS = [
    "hero",
    "universe",
    "gallery",
    "scrapbook",
    "mosaic",
    "secret",
    "letter-section",
    "final-scene"
]

os.makedirs("scratch/tablet_audit_verified", exist_ok=True)

def audit(vp, port=9250):
    w, h, name = vp["w"], vp["h"], vp["name"]
    print(f"\n================ AUDITING {name} ({w}x{h}) ================")
    profile_dir = os.path.abspath(f"scratch/chrome_prof_{name}")
    os.makedirs(profile_dir, exist_ok=True)
    
    cmd = [
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        "--headless=new",
        f"--remote-debugging-port={port}",
        "--disable-gpu",
        "--no-sandbox",
        f"--user-data-dir={profile_dir}",
        f"--window-size={w},{h}",
        "http://localhost:5173/"
    ]
    proc = subprocess.Popen(cmd)
    time.sleep(2.5)
    
    try:
        with urllib.request.urlopen(f"http://localhost:{port}/json") as res:
            tabs = json.loads(res.read().decode('utf-8'))
        target_tab = [t for t in tabs if "5173" in t.get("url", "")][0]
        ws_host = "localhost"
        ws_port = port
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
                
            s.sendall(header + bytes(masked))
            
        def capture(sec_id, suffix=""):
            cid = int(time.time() * 1000) % 1000000
            send_cdp(cid, "Page.captureScreenshot", {"format": "png"})
            data = b""
            s.settimeout(6.0)
            while True:
                try:
                    chunk = s.recv(65536)
                    if not chunk: break
                    data += chunk
                    if f'{{"id":{cid}'.encode('utf-8') in data and b'"result":' in data and b'"data":' in data:
                        start = data.find(f'{{"id":{cid}'.encode('utf-8'))
                        idx = data.find(b'"data":"', start)
                        if idx != -1:
                            end = data.find(b'"', idx + 8)
                            if end != -1:
                                b64 = data[idx+8:end].decode('utf-8')
                                out_name = f"scratch/tablet_audit_verified/{name}_{sec_id}{suffix}.png"
                                with open(out_name, "wb") as f:
                                    f.write(base64.b64decode(b64))
                                print(f"  [Captured] {out_name}")
                                break
                except Exception:
                    break

        # Instantly dismiss intro
        dismiss_intro_js = """
        (() => {
            const intro = document.getElementById('intro');
            const main = document.getElementById('main-content');
            if (intro) intro.style.display = 'none';
            if (main) {
                main.classList.remove('hidden');
                main.style.opacity = '1';
            }
            document.querySelectorAll('.reveal-up, .reveal-left, .reveal-right, .reveal-scale, .section-num').forEach(el => {
                el.classList.add('is-visible');
            });
            window.dispatchEvent(new Event('resize'));
            return 'intro dismissed';
        })()
        """
        send_cdp(1, "Runtime.evaluate", {"expression": dismiss_intro_js})
        time.sleep(1.0)
        
        # Check horizontal overflow
        check_overflow_js = """
        (() => {
            const docWidth = document.documentElement.scrollWidth;
            const winWidth = window.innerWidth;
            return JSON.stringify({
                docWidth,
                winWidth,
                hasHorizontalScroll: docWidth > winWidth
            });
        })()
        """
        send_cdp(2, "Runtime.evaluate", {"expression": check_overflow_js})
        time.sleep(0.5)

        # Check universe 3D metrics
        check_universe_js = """
        (() => {
            const cards = Array.from(document.querySelectorAll('.universe-planet-card')).map(c => ({
                id: c.id,
                rect: c.getBoundingClientRect()
            }));
            const heading = document.querySelector('.universe-heading-area')?.getBoundingClientRect();
            return JSON.stringify({ cards, heading });
        })()
        """
        send_cdp(3, "Runtime.evaluate", {"expression": check_universe_js})
        time.sleep(0.5)

        # Iterate all sections and capture
        for sec in SECTIONS:
            scroll_js = f"document.getElementById('{sec}')?.scrollIntoView({{behavior: 'instant', block: 'start'}});"
            send_cdp(10, "Runtime.evaluate", {"expression": scroll_js})
            time.sleep(0.8)
            capture(sec)
            
        s.close()
    finally:
        proc.terminate()

for vp in VIEWPORTS:
    audit(vp, port=9250 + VIEWPORTS.index(vp))

print("\nAll tablet viewport audits completed successfully!")
