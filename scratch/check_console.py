import urllib.request, json, socket, os, subprocess, time

profile_dir = os.path.abspath('scratch/chrome_prof_console')
os.makedirs(profile_dir, exist_ok=True)
cmd = [
    r'C:\Program Files\Google\Chrome\Application\chrome.exe',
    '--headless=new',
    '--remote-debugging-port=9263',
    '--disable-gpu',
    '--no-sandbox',
    f'--user-data-dir={profile_dir}',
    '--window-size=1280,800',
    'http://localhost:5173/'
]
proc = subprocess.Popen(cmd)
time.sleep(2)
try:
    with urllib.request.urlopen('http://localhost:9263/json') as res:
        tabs = json.loads(res.read().decode('utf-8'))
    target_tab = [t for t in tabs if '5173' in t.get('url', '')][0]
    ws_host = 'localhost'
    ws_port = 9263
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
    
    def send_cdp(cmd_id, method, params=None):
        payload = json.dumps({'id': cmd_id, 'method': method, 'params': params or {}}).encode('utf-8')
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
        data = b''
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

    # Check console errors
    res = send_cdp(1, 'Runtime.evaluate', {
        'expression': """(() => {
            return window.errors || [];
        })()""",
        'returnByValue': True
    })
    
    # Check if window._appLoaded or test if app.js had syntax errors
    syntax_check = send_cdp(2, 'Runtime.evaluate', {
        'expression': """(() => {
            return {
                HLU_CONTENT: typeof window.HLU_CONTENT,
                initSecretType: typeof initSecret,
                threeLoaded: typeof THREE
            };
        })()""",
        'returnByValue': True
    })
    print("CHECK:", syntax_check)
    s.close()
finally:
    proc.terminate()
    proc.wait()
