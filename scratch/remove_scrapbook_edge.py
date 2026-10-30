with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Remove the scrapbook-edge div
target_div = """      <!-- Torn-paper bottom edge transition -->
      <div class="scrapbook-edge" aria-hidden="true"></div>"""

target_div_crlf = target_div.replace('\n', '\r\n')

if target_div_crlf in html:
    html = html.replace(target_div_crlf, "")
    print("Found and removed scrapbook-edge div (CRLF)!")
elif target_div in html:
    html = html.replace(target_div, "")
    print("Found and removed scrapbook-edge div (LF)!")
else:
    print("Warning: target_div not found directly")

# 2. Also remove or comment the .scrapbook-edge CSS in index.html <style>
target_css = """    /* Scrapbook torn-paper edge */
    .scrapbook-edge {
      position: absolute;
      bottom: -1px; left: 0; right: 0;
      height: 56px;
      background: linear-gradient(180deg, #EBD8C0 0%, #F3E7D6 100%);
      clip-path: polygon(
        0% 100%,  2% 42%,  4% 72%,  6% 28%,  9% 58%,
        12% 18%, 15% 52%, 18% 14%, 21% 48%, 24% 22%,
        27% 58%, 30% 28%, 33% 62%, 36% 18%, 40% 52%,
        43% 16%, 46% 50%, 50% 20%, 54% 55%, 57% 22%,
        60% 58%, 63% 18%, 66% 52%, 69% 25%, 72% 60%,
        75% 20%, 78% 52%, 81% 28%, 84% 62%, 87% 22%,
        90% 55%, 93% 28%, 96% 60%, 98% 32%, 100% 48%,
        100% 100%
      );
      pointer-events: none;
      z-index: 2;
    }"""

target_css_crlf = target_css.replace('\n', '\r\n')
if target_css_crlf in html:
    html = html.replace(target_css_crlf, "    .scrapbook-edge { display: none !important; }")
    print("Found and neutralized scrapbook-edge CSS (CRLF)!")
elif target_css in html:
    html = html.replace(target_css, "    .scrapbook-edge { display: none !important; }")
    print("Found and neutralized scrapbook-edge CSS (LF)!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated index.html!")
