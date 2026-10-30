with open('src/styles/responsive.css', 'r', encoding='utf-8') as f:
    css = f.read()

t1 = """  /* Secret Envelope Section */
  .secret-envelope-wrapper {
    max-width: min(520px, 86vw) !important;
    margin: 110px auto 35px !important;
  }
  .secret-envelope {
    width: min(520px, 86vw) !important;
    height: min(320px, 52vw) !important;
  }
  .secret-card {
    min-height: 240px !important;
    padding: 1.8rem 1.6rem !important;
  }"""

r1 = """  /* Secret Envelope Section */
  .secret-envelope-wrap,
  .secret-envelope-wrapper {
    max-width: min(500px, 88vw) !important;
    margin: 115px auto 35px !important;
  }
  .secret-env-outer,
  .secret-envelope {
    width: 100% !important;
    height: min(280px, 50vw) !important;
  }
  .secret-card {
    min-height: 285px !important;
    padding: 1.8rem 1.6rem 1.4rem !important;
  }"""

t2 = """  /* Envelopes in Landscape */
  .secret-envelope-wrapper { max-width: 520px !important; margin: 90px auto 30px !important; }
  .envelope-wrapper { max-width: 540px !important; margin: 120px auto 40px !important; }"""

r2 = """  /* Envelopes in Landscape */
  .secret-envelope-wrap,
  .secret-envelope-wrapper { max-width: 500px !important; margin: 95px auto 30px !important; }
  .secret-env-outer,
  .secret-envelope { height: 260px !important; }
  .secret-card { min-height: 285px !important; padding: 1.8rem 1.8rem 1.4rem !important; }
  .envelope-wrapper { max-width: 540px !important; margin: 120px auto 40px !important; }"""

t3 = """  .secret-envelope-wrap { max-width: 90vw; margin-top: 75px; margin-bottom: 20px; }
  .secret-env-outer { height: 210px; }
  .secret-card { min-height: 220px; padding: 1.4rem 1.2rem; }"""

r3 = """  .secret-envelope-wrap { max-width: 92vw !important; margin-top: 85px !important; margin-bottom: 25px !important; }
  .secret-env-outer { height: 250px !important; }
  .secret-card { min-height: 275px !important; padding: 1.6rem 1.1rem 1.1rem !important; }
  .shayari-line { font-size: 0.94rem !important; line-height: 2.05 !important; }"""

css_norm = css.replace('\r\n', '\n')
t1_n = t1.replace('\r\n', '\n')
r1_n = r1.replace('\r\n', '\n')
t2_n = t2.replace('\r\n', '\n')
r2_n = r2.replace('\r\n', '\n')
t3_n = t3.replace('\r\n', '\n')
r3_n = r3.replace('\r\n', '\n')

css_norm = css_norm.replace(t1_n, r1_n, 1)
css_norm = css_norm.replace(t2_n, r2_n, 1)
css_norm = css_norm.replace(t3_n, r3_n, 1)

with open('src/styles/responsive.css', 'w', encoding='utf-8') as f:
    f.write(css_norm)

print("SUCCESS: media queries updated")
