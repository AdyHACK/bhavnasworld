import subprocess
import time
import os

profile_dir = os.path.abspath("scratch/chrome_profile")
os.makedirs(profile_dir, exist_ok=True)
screenshot_path = os.path.abspath("scratch/gallery_origin_preview.png")

cmd = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    "--headless=new",
    "--disable-gpu",
    "--no-sandbox",
    f"--user-data-dir={profile_dir}",
    "--window-size=1400,1000",
    "--virtual-time-budget=4000",
    f"--screenshot={screenshot_path}",
    "http://localhost:5173/#gallery"
]

res = subprocess.run(cmd, capture_output=True, text=True, timeout=15)
if os.path.exists(screenshot_path):
    print("Gallery screenshot captured! Size:", os.path.getsize(screenshot_path), "bytes")
else:
    print("Gallery screenshot failed.")
