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

os.makedirs("scratch/tablet_audit", exist_ok=True)

def audit_viewport(vp, port=9240):
    w, h, name = vp["w"], vp["h"], vp["name"]
    print(f"\n================ AUDITING {name} ({w}x{h}) ================")
    profile_dir = os.path.abspath(f"scratch/chrome_{name}")
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
                                out_name = f"scratch/tablet_audit/{name}_{sec_id}{suffix}.png"
                                with open(out_name, "wb") as f:
                                    f.write(base64.b64decode(b64))
                                print(f"  [Captured] {out_name}")
                                break
                except Exception:
                    break
        
        # Click enter
        send_cdp(1, "Runtime.evaluate", {"expression": "document.getElementById('enter-btn')?.click();"})
        time.sleep(1.2)
        
        # Check horizontal scroll
        check_overflow_js = """
        (() => {
            const docWidth = document.documentElement.scrollWidth;
            const winWidth = window.innerWidth;
            const overflowing = [];
            document.querySelectorAll('*').forEach(el => {
                if (el.scrollWidth > winWidth + 2) {
                    overflowing.push({
                        tag: el.tagName,
                        id: el.id,
                        className: el.className ? el.className.toString() : '',
                        scrollWidth: el.scrollWidth,
                        clientWidth: el.clientWidth
                    });
                }
            });
            return JSON.stringify({ docWidth, winWidth, hasHorizontalScroll: docWidth > winWidth, overflowing: overflowing.slice(0, 5) });
        })()
        """
        send_cdp(2, "Runtime.evaluate", {"expression": check_overflow_js})
        time.sleep(0.5)
        
        # Iterate sections and capture
        for sec in SECTIONS:
            scroll_js = f"document.getElementById('{sec}')?.scrollIntoView({{behavior: 'instant', block: 'start'}});"
            send_cdp(10, "Runtime.evaluate", {"expression": scroll_js})
            time.sleep(0.8)
            capture(sec)
            
        s.close()
    finally:
        proc.terminate()

for vp in VIEWPORTS:
    audit_viewport(vp, port=9240 + VIEWPORTS.index(vp))

print("\nAudit completed across all viewports!")
