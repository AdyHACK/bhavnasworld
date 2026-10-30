import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

matches = list(re.finditer(r'</section>(\s*(?:<!--.*?-->\s*)*)<section', text, re.DOTALL))
print(f"Found {len(matches)} section transitions")
for i, m in enumerate(matches):
    print(f"--- Transition {i+1} ---")
    print(m.group(0)[:80])
