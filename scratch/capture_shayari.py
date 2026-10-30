import urllib.request, json, socket, os, subprocess, time, base64

profile_dir = os.path.abspath('scratch/chrome_prof_shot')
os.makedirs(profile_dir, exist_ok=True)
screenshot_dir = os.path.abspath("scratch/shayari_screenshots")
os.makedirs(screenshot_dir, exist_ok=True)

test_configs = [
    (1280, 800, "desktop_1280x800"),
    (768, 1024, "tablet_portrait_768x1024"),
    (820, 1180, "tablet_portrait_820x1180"),
    (1024, 768, "tablet_landscape_1024x768"),
    (390, 844, "mobile_390x844")
]

for w, h, label in test_configs:
    cmd = [
        r'C:\Program Files\Google\Chrome\Application\chrome.exe',
        '--headless=new',
        '--remote-debugging-port=9267',
        '--disable-gpu',
        '--no-sandbox',
        f'--user-data-dir={profile_dir}',
        f'--window-size={w},{h}',
        'http://localhost:5173/'
    ]
    proc = subprocess.Popen(cmd)
    time.sleep(2)
    try:
        with urllib.request.urlopen('http://localhost:9267/json') as res:
            tabs = json.loads(res.read().decode('utf-8'))
        target_tab = [t for t in tabs if '5173' in t.get('url', '')][0]
        ws_host = 'localhost'
        ws_port = 9267
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
                chunk = s.recv(32768)
                data += chunk
                if b'"id":' + str(cmd_id).encode('utf-8') in data:
                    break
            idx = data.find(b'{"id":' + str(cmd_id).encode('utf-8'))
            if idx != -1:
                end_idx = data.rfind(b'}')
                return json.loads(data[idx:end_idx+1].decode('utf-8', errors='ignore'))
            return {}

        is_mobile = w <= 768
        send_cdp(1, 'Emulation.setDeviceMetricsOverride', {
            'width': w, 'height': h, 'deviceScaleFactor': 1, 'mobile': is_mobile
        })
        time.sleep(1)

        # Hide intro, scroll into view
        send_cdp(2, 'Runtime.evaluate', {
            'expression': """(() => {
                const intro = document.getElementById('intro');
                if (intro) intro.style.display = 'none';
                const main = document.getElementById('main-content');
                if (main) { main.style.opacity = '1'; main.style.visibility = 'visible'; }
                const sec = document.getElementById('secret');
                if (sec) sec.scrollIntoView({ behavior: 'instant', block: 'center' });
            })()"""
        })
        time.sleep(1)

        # Click wax seal to open
        send_cdp(3, 'Runtime.evaluate', {
            'expression': """(() => {
                const seal = document.getElementById('secret-seal');
                if (seal) seal.click();
            })()"""
        })

        # Wait 8.5 seconds for complete sequence to settle
        time.sleep(8.5)

        # Check full state
        res_state = send_cdp(4, 'Runtime.evaluate', {
            'expression': """JSON.stringify((() => {
                const line1 = document.getElementById('shayari-line-1');
                const line2 = document.getElementById('shayari-line-2');
                const line3 = document.getElementById('shayari-line-3');
                const line4 = document.getElementById('shayari-line-4');
                const highlight = document.querySelector('.shayari-couplet--highlight');
                const flourish = document.getElementById('secret-flourish');
                const floral = document.getElementById('secret-floral');
                const divider = document.getElementById('secret-divider');
                const card = document.getElementById('secret-card');
                
                return {
                    line1Opacity: line1 ? window.getComputedStyle(line1).opacity : null,
                    line2Opacity: line2 ? window.getComputedStyle(line2).opacity : null,
                    line3Opacity: line3 ? window.getComputedStyle(line3).opacity : null,
                    line4Opacity: line4 ? window.getComputedStyle(line4).opacity : null,
                    flourishOpacity: flourish ? window.getComputedStyle(flourish).opacity : null,
                    floralOpacity: floral ? window.getComputedStyle(floral).opacity : null,
                    dividerOpacity: divider ? window.getComputedStyle(divider).opacity : null,
                    isHighlighted: highlight ? highlight.classList.contains('is-highlighted') : false,
                    cardActive: card ? card.classList.contains('is-active') : false
                };
            })())""",
            'returnByValue': True
        })
        print(f"[{label}] COMPLETE STATE:", res_state.get('result', {}).get('result', {}).get('value'))

        # Capture viewport screenshot
        shot = send_cdp(5, 'Page.captureScreenshot', { 'format': 'png' })
        b64 = shot.get('result', {}).get('data')
        if b64:
            out_path = os.path.join(screenshot_dir, f"{label}_secret_shayari.png")
            with open(out_path, 'wb') as f:
                f.write(base64.b64decode(b64))
            print(f"Saved: {out_path}")

        s.close()
    finally:
        proc.terminate()
        proc.wait()

print("ALL CAPTURES COMPLETED SUCCESSFULLY!")
