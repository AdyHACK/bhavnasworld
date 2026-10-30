import urllib.request, json, socket, os, subprocess, time

profile_dir = os.path.abspath('scratch/chrome_prof_debug')
os.makedirs(profile_dir, exist_ok=True)
cmd = [
    r'C:\Program Files\Google\Chrome\Application\chrome.exe',
    '--headless=new',
    '--remote-debugging-port=9262',
    '--disable-gpu',
    '--no-sandbox',
    f'--user-data-dir={profile_dir}',
    '--window-size=1280,800',
    'http://localhost:5173/'
]
proc = subprocess.Popen(cmd)
time.sleep(2)
try:
    with urllib.request.urlopen('http://localhost:9262/json') as res:
        tabs = json.loads(res.read().decode('utf-8'))
    target_tab = [t for t in tabs if '5173' in t.get('url', '')][0]
    ws_host = 'localhost'
    ws_port = 9262
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
    send_cdp(1, 'Console.enable')
    send_cdp(2, 'Runtime.enable')

    # Remove intro
    res_open = send_cdp(3, 'Runtime.evaluate', {
        'expression': """(() => {
            const intro = document.getElementById('intro');
            if (intro) intro.style.display = 'none';
            const main = document.getElementById('main-content');
            if (main) { main.style.opacity = '1'; main.style.visibility = 'visible'; }
            
            // Try clicking the reveal button
            const btn = document.getElementById('secret-reveal-btn');
            const seal = document.getElementById('secret-seal');
            console.log('reveal-btn found:', !!btn, 'seal found:', !!seal);
            if (btn) btn.click();
            return { btnFound: !!btn, sealFound: !!seal };
        })()""",
        'returnByValue': True
    })
    print("res_open:", res_open)

    time.sleep(6)
    
    res = send_cdp(4, 'Runtime.evaluate', {
        'expression': """JSON.stringify((() => {
            const card = document.getElementById('secret-card');
            const line1 = document.getElementById('shayari-line-1');
            const line4 = document.getElementById('shayari-line-4');
            const seal = document.getElementById('secret-seal');
            return {
                cardStyle: card ? card.getAttribute('style') : null,
                cardClass: card ? card.className : null,
                line1Style: line1 ? line1.getAttribute('style') : null,
                line4Style: line4 ? line4.getAttribute('style') : null,
                sealStyle: seal ? seal.getAttribute('style') : null
            };
        })())""",
        'returnByValue': True
    })
    print('DEBUG RESULT:', res.get('result', {}).get('result', {}).get('value'))
    s.close()
finally:
    proc.terminate()
    proc.wait()
