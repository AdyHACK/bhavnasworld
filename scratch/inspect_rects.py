import subprocess
import time
import os
import json
import urllib.request
import socket

profile_dir = os.path.abspath("scratch/chrome_profile_rects")
os.makedirs(profile_dir, exist_ok=True)

chrome_cmd = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    "--headless=new",
    "--remote-debugging-port=9234",
    "--disable-gpu",
    "--no-sandbox",
    f"--user-data-dir={profile_dir}",
    "--window-size=1400,1000",
    "http://localhost:5173/"
]

proc = subprocess.Popen(chrome_cmd)
time.sleep(2)

try:
    with urllib.request.urlopen("http://localhost:9234/json") as res:
        tabs = json.loads(res.read().decode('utf-8'))
    
    target_tab = [t for t in tabs if "5173" in t.get("url", "")][0]
    ws_host = "localhost"
    ws_port = 9234
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

    send_cdp(1, "Runtime.evaluate", {"expression": "document.getElementById('enter-btn')?.click();"})
    time.sleep(1.2)
    
    js = """
    (() => {
        const sb = document.getElementById('scrapbook');
        const container = sb.querySelector('.container');
        const grid = document.getElementById('scrapbook-grid');
        const edge = document.querySelector('.scrapbook-edge');
        const cards = Array.from(grid.querySelectorAll('.scrap-card'));
        
        return JSON.stringify({
            sb: {
                offsetTop: sb.offsetTop,
                offsetHeight: sb.offsetHeight,
                scrollHeight: sb.scrollHeight,
                computedHeight: window.getComputedStyle(sb).height,
                overflow: window.getComputedStyle(sb).overflow
            },
            container: {
                offsetTop: container.offsetTop,
                offsetHeight: container.offsetHeight
            },
            grid: {
                offsetTop: grid.offsetTop,
                offsetHeight: grid.offsetHeight,
                gridAutoRows: window.getComputedStyle(grid).gridAutoRows,
                gridTemplateColumns: window.getComputedStyle(grid).gridTemplateColumns,
                gridTemplateRows: window.getComputedStyle(grid).gridTemplateRows
            },
            edge: {
                offsetTop: edge ? edge.offsetTop : null,
                offsetHeight: edge ? edge.offsetHeight : null,
                position: edge ? window.getComputedStyle(edge).position : null,
                bottom: edge ? window.getComputedStyle(edge).bottom : null
            },
            cards: cards.map((c, i) => ({
                index: i,
                className: c.className,
                offsetTop: c.offsetTop,
                offsetHeight: c.offsetHeight,
                computedGridRow: window.getComputedStyle(c).gridRow,
                computedGridColumn: window.getComputedStyle(c).gridColumn
            }))
        });
    })()
    """
    send_cdp(2, "Runtime.evaluate", {"expression": js})
    
    data = b""
    s.settimeout(5.0)
    while True:
        try:
            chunk = s.recv(65536)
            if not chunk: break
            data += chunk
            if b'{"id":2' in data and b'"result":' in data:
                break
        except Exception:
            break
            
    idx = data.find(b'{"id":2')
    if idx != -1:
        raw = data[idx:].split(b'\n')[0]
        v_idx = raw.find(b'"value":')
        if v_idx != -1:
            val_str = raw[v_idx+8:].rstrip(b'}')
            val_obj = json.loads(val_str.decode('utf-8'))
            print("Layout data:")
            print(json.dumps(json.loads(val_obj), indent=2))
    s.close()
finally:
    proc.terminate()
