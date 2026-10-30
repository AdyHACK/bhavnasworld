import subprocess
import time
import os
import json
import urllib.request
import socket

profile_dir = os.path.abspath("scratch/chrome_profile_rules")
os.makedirs(profile_dir, exist_ok=True)

chrome_cmd = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    "--headless=new",
    "--remote-debugging-port=9225",
    "--disable-gpu",
    "--no-sandbox",
    f"--user-data-dir={profile_dir}",
    "--window-size=1400,1000",
    "http://localhost:5173/"
]

proc = subprocess.Popen(chrome_cmd)
time.sleep(2)

try:
    with urllib.request.urlopen("http://localhost:9225/json") as res:
        tabs = json.loads(res.read().decode('utf-8'))
    
    target_tab = [t for t in tabs if "5173" in t.get("url", "")][0]
    ws_host = "localhost"
    ws_port = 9225
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
        
    js = """
    (() => {
        const el = document.getElementById('universe-nodes');
        const rules = [];
        for (const sheet of document.styleSheets) {
            try {
                for (const rule of sheet.cssRules) {
                    if (rule.selectorText && el.matches(rule.selectorText)) {
                        rules.push({
                            sheet: sheet.href,
                            selector: rule.selectorText,
                            cssText: rule.cssText
                        });
                    }
                }
            } catch(e) {}
        }
        return JSON.stringify(rules);
    })()
    """
    send_cdp(1, "Runtime.evaluate", {"expression": js})
    
    data = b""
    s.settimeout(5.0)
    while True:
        try:
            chunk = s.recv(65536)
            if not chunk: break
            data += chunk
            if b'{"id":1' in data and b'"result":' in data:
                break
        except Exception:
            break
            
    idx = data.find(b'{"id":1')
    if idx != -1:
        raw = data[idx:].split(b'\n')[0]
        v_idx = raw.find(b'"value":')
        if v_idx != -1:
            val_str = raw[v_idx+8:].rstrip(b'}')
            val_obj = json.loads(val_str.decode('utf-8'))
            print("Matched rules for #universe-nodes:")
            print(json.dumps(json.loads(val_obj), indent=2))
    s.close()
finally:
    proc.terminate()
