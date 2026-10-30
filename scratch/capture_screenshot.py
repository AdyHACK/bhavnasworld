import subprocess
import time
import os

profile_dir = os.path.abspath("scratch/chrome_profile")
os.makedirs(profile_dir, exist_ok=True)
screenshot_path = os.path.abspath("scratch/universe_preview.png")

cmd = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    "--headless=new",
    "--disable-gpu",
    "--no-sandbox",
    f"--user-data-dir={profile_dir}",
    "--window-size=1400,1000",
    "--virtual-time-budget=4000",
    f"--screenshot={screenshot_path}",
    "http://localhost:5173/#universe"
]

print("Running command:", " ".join(cmd))
res = subprocess.run(cmd, capture_output=True, text=True, timeout=15)
print("Return code:", res.returncode)
print("Stdout:", res.stdout)
print("Stderr:", res.stderr)
if os.path.exists(screenshot_path):
    print("Screenshot captured successfully! Size:", os.path.getsize(screenshot_path), "bytes")
else:
    print("Screenshot failed to generate.")
