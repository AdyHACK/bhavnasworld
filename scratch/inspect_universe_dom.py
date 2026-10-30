import subprocess
import time
import os
import json
import urllib.request
import socket

profile_dir = os.path.abspath("scratch/chrome_profile_cdp2")
os.makedirs(profile_dir, exist_ok=True)

chrome_cmd = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    "--headless=new",
    "--remote-debugging-port=9223",
    "--disable-gpu",
    "--no-sandbox",
    f"--user-data-dir={profile_dir}",
    "--window-size=1400,1000",
    "http://localhost:5173/"
]

proc = subprocess.Popen(chrome_cmd)
time.sleep(2)

try:
    with urllib.request.urlopen("http://localhost:9223/json") as res:
        tabs = json.loads(res.read().decode('utf-8'))
    
    target_tab = None
    for tab in tabs:
        if "5173" in tab.get("url", ""):
            target_tab = tab
            break
            
    ws_host = "localhost"
    ws_port = 9223
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
    send_cdp(2, "Runtime.evaluate", {"expression": "document.getElementById('universe')?.scrollIntoView({block: 'start'});"})
    time.sleep(1.0)
    
    # Inspect elements
    js_inspect = """
    (() => {
        const u = document.getElementById('universe');
        const nodes = document.getElementById('universe-nodes');
        const cards = document.querySelectorAll('.universe-planet-card');
        const heading = document.querySelector('.universe-heading-area');
        const canvas = document.getElementById('universe-3d-canvas');
        
        return JSON.stringify({
            scroll: { scrollY: window.scrollY, innerHeight: window.innerHeight },
            universeRect: u ? u.getBoundingClientRect() : null,
            canvasRect: canvas ? canvas.getBoundingClientRect() : null,
            canvasZIndex: canvas ? window.getComputedStyle(canvas).zIndex : null,
            nodesRect: nodes ? nodes.getBoundingClientRect() : null,
            nodesStyles: nodes ? {
                display: window.getComputedStyle(nodes).display,
                opacity: window.getComputedStyle(nodes).opacity,
                zIndex: window.getComputedStyle(nodes).zIndex,
                visibility: window.getComputedStyle(nodes).visibility,
            } : null,
            cardsCount: cards.length,
            card0Rect: cards[0] ? cards[0].getBoundingClientRect() : null,
            card0Styles: cards[0] ? {
                display: window.getComputedStyle(cards[0]).display,
                opacity: window.getComputedStyle(cards[0]).opacity,
                visibility: window.getComputedStyle(cards[0]).visibility,
                top: window.getComputedStyle(cards[0]).top,
                left: window.getComputedStyle(cards[0]).left,
            } : null,
            headingRect: heading ? heading.getBoundingClientRect() : null
        });
    })()
    """
    send_cdp(3, "Runtime.evaluate", {"expression": js_inspect})
    
    data = b""
    s.settimeout(5.0)
    while True:
        try:
            chunk = s.recv(65536)
            if not chunk: break
            data += chunk
            if b'{"id":3' in data and b'"result":' in data:
                break
        except Exception:
            break
            
    # print parsed result
    idx = data.find(b'{"id":3')
    if idx != -1:
        end = data.find(b'\n', idx)
        # extract json
        raw = data[idx:].split(b'\n')[0]
        # find "value":
        v_idx = raw.find(b'"value":')
        if v_idx != -1:
            print("Inspection result:")
            val_str = raw[v_idx+8:].rstrip(b'}')
            # decode json string
            val_obj = json.loads(val_str.decode('utf-8'))
            print(json.dumps(json.loads(val_obj), indent=2))
            
    s.close()
finally:
    proc.terminate()
