import urllib.request, json, socket, os, subprocess, time, base64

profile_dir = os.path.abspath('scratch/chrome_prof_mob')
os.makedirs(profile_dir, exist_ok=True)
screenshot_dir = os.path.abspath("scratch/shayari_screenshots")

cmd = [
    r'C:\Program Files\Google\Chrome\Application\chrome.exe',
    '--headless=new',
    '--remote-debugging-port=9271',
    '--disable-gpu',
    '--no-sandbox',
    f'--user-data-dir={profile_dir}',
    '--window-size=390,844',
    'http://localhost:5173/'
]
proc = subprocess.Popen(cmd)
time.sleep(2)
try:
    with urllib.request.urlopen('http://localhost:9271/json') as res:
        tabs = json.loads(res.read().decode('utf-8'))
    target_tab = [t for t in tabs if '5173' in t.get('url', '')][0]
    ws_host = 'localhost'
    ws_port = 9271
    path = target_tab['webSocketDebuggerUrl'].split(f'{ws_host}:{ws_port}')[1]
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ws_host, ws_port))
    handshake = (
        f'GET {path} HTTP/1.1\r\n'
        f'Host: {ws_host}:{ws_port}\r\n'
        'Upgrade: websocket\r\n'
        'Connection: Upgrade\r\n'
        'Sec-WebSocket-Key: dGhlIHNhbXBsZSBub25jZQ==\r\n'
        'Sec-WebSocket-Version: 13\r\n\r\n'
    )
    s.sendall(handshake.encode('utf-8'))
    resp = s.recv(4096)
    
    def send_cdp_eval(cmd_id, expr):
        payload = json.dumps({'id': cmd_id, 'method': 'Runtime.evaluate', 'params': {'expression': expr, 'returnByValue': True}}).encode('utf-8')
        length = len(payload)
        mask = os.urandom(4)
        header = bytes([0x81, 0x80 | 126]) + length.to_bytes(2, 'big') + mask
        masked = bytearray(length)
        for i in range(length):
            masked[i] = payload[i] ^ mask[i % 4]
        s.sendall(header + masked)
        s.settimeout(6.0)
        while True:
            chunk = s.recv(16384)
            if f'{{"id":{cmd_id}'.encode('utf-8') in chunk:
                break

    # Device metrics
    payload = json.dumps({'id': 1, 'method': 'Emulation.setDeviceMetricsOverride', 'params': {'width': 390, 'height': 844, 'deviceScaleFactor': 1, 'mobile': True}}).encode('utf-8')
    length = len(payload)
    mask = os.urandom(4)
    header = bytes([0x81, 0x80 | 126]) + length.to_bytes(2, 'big') + mask
    masked = bytearray(length)
    for i in range(length):
        masked[i] = payload[i] ^ mask[i % 4]
    s.sendall(header + masked)
    time.sleep(0.5)

    # Dismiss intro
    send_cdp_eval(2, """(() => {
        const intro = document.getElementById('intro');
        const main = document.getElementById('main-content');
        if (intro) intro.style.display = 'none';
        if (main) { main.classList.remove('hidden'); main.style.opacity = '1'; }
        document.querySelectorAll('.reveal-up, .reveal-left, .reveal-right, .reveal-scale').forEach(el => {
            el.classList.add('is-visible');
        });
        const sec = document.getElementById('secret');
        if (sec) sec.scrollIntoView({ behavior: 'instant', block: 'center' });
    })()""")
    time.sleep(0.8)

    # Open
    send_cdp_eval(3, "document.getElementById('secret-seal')?.click()")
    time.sleep(8.5)

    # Center
    send_cdp_eval(4, "document.getElementById('secret-envelope-wrap')?.scrollIntoView({ behavior: 'instant', block: 'center' })")
    time.sleep(0.8)

    # Capture
    cid = 999
    payload = json.dumps({'id': cid, 'method': 'Page.captureScreenshot', 'params': {'format': 'png'}}).encode('utf-8')
    length = len(payload)
    mask = os.urandom(4)
    header = bytes([0x81, 0x80 | length]) + mask
    masked = bytearray(length)
    for i in range(length):
        masked[i] = payload[i] ^ mask[i % 4]
    s.sendall(header + masked)

    data = b''
    s.settimeout(10.0)
    while True:
        chunk = s.recv(65536)
        if not chunk: break
        data += chunk
        start = data.find(f'{{"id":{cid}'.encode('utf-8'))
        if start != -1:
            idx = data.find(b'"data":"', start)
            if idx != -1:
                end = data.find(b'"', idx + 8)
                if end != -1:
                    b64 = data[idx+8:end].decode('utf-8')
                    out_path = os.path.join(screenshot_dir, "mobile_390x844_secret_shayari.png")
                    with open(out_path, 'wb') as f:
                        f.write(base64.b64decode(b64))
                    print(f"Captured: {out_path}")
                    break
    s.close()
finally:
    proc.terminate()
    proc.wait()
