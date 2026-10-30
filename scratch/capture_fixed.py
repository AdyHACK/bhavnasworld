import subprocess
import time
import os
import json
import urllib.request
import base64
import socket

profile_dir = os.path.abspath("scratch/chrome_profile_cdp_fixed")
os.makedirs(profile_dir, exist_ok=True)

chrome_cmd = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    "--headless=new",
    "--remote-debugging-port=9228",
    "--disable-gpu",
    "--no-sandbox",
    f"--user-data-dir={profile_dir}",
    "--window-size=1400,1000",
    "http://localhost:5173/"
]

proc = subprocess.Popen(chrome_cmd)
time.sleep(2)

try:
    with urllib.request.urlopen("http://localhost:9228/json") as res:
        tabs = json.loads(res.read().decode('utf-8'))
    
    target_tab = [t for t in tabs if "5173" in t.get("url", "")][0]
    ws_host = "localhost"
    ws_port = 9228
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

    # Click enter
    send_cdp(1, "Runtime.evaluate", {"expression": "document.getElementById('enter-btn')?.click();"})
    time.sleep(1.2)
    
    # Scroll to universe
    send_cdp(2, "Runtime.evaluate", {"expression": "document.getElementById('universe')?.scrollIntoView({behavior: 'instant'});"})
    time.sleep(1.5)
    
    # Capture screenshot
    send_cdp(3, "Page.captureScreenshot", {"format": "png"})
    
    data = b""
    s.settimeout(5.0)
    while True:
        try:
            chunk = s.recv(65536)
            if not chunk: break
            data += chunk
            if b'{"id":3' in data and b'"result":' in data and b'"data":' in data:
                start = data.find(b'{"id":3')
                idx = data.find(b'"data":"', start)
                if idx != -1:
                    end = data.find(b'"', idx + 8)
                    if end != -1:
                        b64_data = data[idx+8:end].decode('utf-8')
                        img_bytes = base64.b64decode(b64_data)
                        out_path = os.path.abspath("scratch/universe_fixed.png")
                        with open(out_path, "wb") as f:
                            f.write(img_bytes)
                        print("Saved universe_fixed.png! Size:", len(img_bytes))
                        break
        except Exception:
            break
            
    s.close()
finally:
    proc.terminate()
