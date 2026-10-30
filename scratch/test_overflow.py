import subprocess
import time
import os
import json
import urllib.request
import socket

profile_dir = os.path.abspath("scratch/chrome_prof_overflow")
os.makedirs(profile_dir, exist_ok=True)

viewports = [
    (768, 1024, "ipad_mini_portrait_768x1024"),
    (820, 1180, "ipad_air_portrait_820x1180"),
    (1024, 768, "ipad_landscape_1024x768")
]

for w, h, label in viewports:
    cmd = [
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        "--headless=new",
        "--remote-debugging-port=9258",
        "--disable-gpu",
        "--no-sandbox",
        f"--user-data-dir={profile_dir}",
        f"--window-size={w},{h}",
        "http://localhost:5173/"
    ]
    proc = subprocess.Popen(cmd)
    time.sleep(2.5)

    try:
        with urllib.request.urlopen("http://localhost:9258/json") as res:
            tabs = json.loads(res.read().decode('utf-8'))
        target_tab = [t for t in tabs if "5173" in t.get("url", "")][0]
        ws_host = "localhost"
        ws_port = 9258
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
            
            # Read response
            data = b""
            while True:
                chunk = s.recv(16384)
                data += chunk
                if b'"id":' + str(cmd_id).encode('utf-8') in data:
                    break
            
            # Strip websocket framing
            idx = data.find(b'{"id":' + str(cmd_id).encode('utf-8'))
            if idx != -1:
                end_idx = data.rfind(b'}')
                return json.loads(data[idx:end_idx+1].decode('utf-8', errors='ignore'))
            return {}

        send_cdp(1, "Emulation.setDeviceMetricsOverride", {
            "width": w,
            "height": h,
            "deviceScaleFactor": 1,
            "mobile": True
        })
        time.sleep(1)

        eval_res = send_cdp(2, "Runtime.evaluate", {
            "expression": """
            JSON.stringify((() => {
                const scrollW = document.documentElement.scrollWidth;
                const clientW = document.documentElement.clientWidth;
                const innerW = window.innerWidth;
                const bodyScrollW = document.body.scrollWidth;
                
                // Find any elements causing overflow if scrollW > innerW
                const overflowing = [];
                if (scrollW > innerW) {
                    const all = document.querySelectorAll('*');
                    all.forEach(el => {
                        const r = el.getBoundingClientRect();
                        if (r.right > innerW + 1) {
                            overflowing.push({ tag: el.tagName, id: el.id, cls: el.className, right: r.right });
                        }
                    });
                }
                
                return {
                    scrollW,
                    clientW,
                    innerW,
                    bodyScrollW,
                    hasHorizontalScroll: scrollW > innerW,
                    overflowCount: overflowing.length,
                    overflowing: overflowing.slice(0, 5)
                };
            })())
            """,
            "returnByValue": True
        })
        val = eval_res.get('result', {}).get('result', {}).get('value')
        print(f"[{label}] Result: {val}")
        s.close()
    finally:
        proc.terminate()
        proc.wait()
