"""Listing images for Before You Click "Pay Later".

Usage: SHOTS=<dir with p01..p12.png from build_guide.mjs> python3 build_images.py
Writes images/gumroad/ (cover 2560x1440, thumb 1200x1200), images/beacons/ (1080x1080) and
images/instagram/ (5 slides, 1080x1350).
"""
import json, os, subprocess

SHOTS = os.path.abspath(os.environ["SHOTS"])
HERE = os.path.dirname(os.path.abspath(__file__))
TMP = "/tmp/bycpl-img"; os.makedirs(TMP, exist_ok=True)
pg = lambda n: f"file://{SHOTS}/p{n:02d}.png"

BASE = """*{box-sizing:border-box;margin:0;padding:0}
html,body{width:%dpx;height:%dpx;overflow:hidden}
body{background:#15171F;background-image:radial-gradient(ellipse at 85%% 0%%,rgba(240,138,75,.18),transparent 55%%);
color:#EDEBF5;font-family:"Liberation Sans","DejaVu Sans",Arial,sans-serif;position:relative;padding:%dpx}
.brand{font-size:%dpx;letter-spacing:.18em;font-weight:700;color:#9A98AE;text-transform:uppercase}.brand b{color:#F08A4B}
h1{font-weight:800;line-height:1.05;letter-spacing:-.01em}h1 em{font-style:normal;color:#F08A4B}
.sub{color:#9A98AE;line-height:1.35}
.free{display:inline-block;background:#5FD38D;color:#15171F;font-weight:800;border-radius:999px}
.pg{position:absolute;border-radius:10px;overflow:hidden;box-shadow:0 20px 60px rgba(0,0,0,.6);border:1px solid #33384F}
.pg img{display:block;width:100%%}
.ex{position:absolute;color:#9A98AE}
.card{background:#1E2130;border:1px solid #33384F;border-radius:16px}
.n{display:inline-flex;align-items:center;justify-content:center;border-radius:50%%;background:#F08A4B;color:#15171F;font-weight:800}
"""
def page(w, h, pad, brand, body):
    return (f'<!doctype html><html><head><meta charset="utf-8"><style>{BASE % (w, h, pad, brand)}</style></head><body>'
            f'<div class="brand"><b>CheckMaybe</b> · Free mini guide</div>{body}</body></html>')
shot = lambda n, style: f'<div class="pg" style="{style}"><img src="{pg(n)}"></div>'

COVER = page(1280, 720, 56, 15,
    '<h1 style="font-size:66px;margin-top:22px">Before You Click<br><em>"Pay Later"</em></h1>'
    '<div class="sub" style="font-size:24px;margin-top:18px;width:560px">5 checks in 5 minutes, before a small monthly payment becomes a bill you didn\'t see coming.</div>'
    '<div class="free" style="font-size:22px;padding:10px 22px;margin-top:26px">FREE · 12-page PDF</div>'
    + shot(1, "left:720px;top:70px;width:300px;transform:rotate(-4deg)") + shot(4, "left:900px;top:150px;width:300px;transform:rotate(3deg)"))
SQ = lambda w: page(w, w, round(w * .08), round(w * .025),
    f'<h1 style="font-size:{round(w*.105)}px;margin-top:{round(w*.03)}px">Before You<br>Click <em>"Pay<br>Later"</em></h1>'
    f'<div class="free" style="font-size:{round(w*.04)}px;padding:{round(w*.012)}px {round(w*.03)}px;margin-top:{round(w*.03)}px">FREE · 5 checks</div>'
    + shot(4, f"left:{round(w*.5)}px;top:{round(w*.42)}px;width:{round(w*.44)}px;transform:rotate(4deg)"))

IW, IH = 864, 1080
def ig(n, body):
    return page(IW, IH, 44, 16, f'<div class="ex" style="right:44px;top:44px;font-size:18px;font-weight:700">{n} / 5</div>' + body)
IG = {
    "01-hook": ig(1, '<h1 style="font-size:70px;margin-top:40px">Before you click<br><em>"pay later"</em>…</h1>'
                     '<div class="sub" style="font-size:30px;margin-top:24px">5 checks. 5 minutes.<br>A free guide I made →</div>'
                     + shot(1, "left:210px;top:470px;width:444px;transform:rotate(-3deg)")),
    "02-total": ig(2, '<div class="sub" style="font-size:22px;margin-top:30px;letter-spacing:.15em;font-weight:700">CHECK 1</div>'
                      '<h1 style="font-size:58px;margin-top:10px">What will I pay<br><em>in total?</em></h1>'
                      '<div class="card" style="margin-top:40px;padding:36px;font-size:36px;line-height:1.7">$67 × 24 = <b>$1,608</b><br>− price $1,200<br>= <b style="color:#FF6B6B">$408 extra</b></div>'
                      '<div class="sub" style="font-size:22px;margin-top:22px">Made-up example. That\'s about 29.8% APR.</div>'),
    "03-deferred": ig(3, '<div class="sub" style="font-size:22px;margin-top:30px;letter-spacing:.15em;font-weight:700">CHECK 3</div>'
                         '<h1 style="font-size:54px;margin-top:10px">When "0%" stops<br>being <em>0%</em></h1>'
                         '<div class="card" style="margin-top:36px;padding:32px;font-size:28px;line-height:1.5">"Deferred interest" / "no interest if paid in full":<br>'
                         '<span style="color:#9A98AE">if any balance is left when the promo ends, interest can go back to the day you bought it.</span></div>'
                         '<div class="sub" style="font-size:20px;margin-top:20px">Source: US CFPB. Check your own agreement.</div>'),
    "04-stack": ig(4, '<div class="sub" style="font-size:22px;margin-top:30px;letter-spacing:.15em;font-weight:700">CHECK 5</div>'
                      '<h1 style="font-size:58px;margin-top:10px">What else is<br><em>due that month?</em></h1>'
                      + shot(7, "left:44px;top:330px;width:776px")),
    "05-cta": ig(5, '<h1 style="font-size:64px;margin-top:40px">Get the <em>free</em><br>12-page guide</h1>'
                    '<div class="sub" style="font-size:26px;margin-top:20px">5 checks · a one-page summary ·<br>a fill-in list for all your plans</div>'
                    + shot(10, "left:250px;top:450px;width:364px;transform:rotate(3deg)")
                    + '<div style="position:absolute;left:0;right:0;bottom:56px;text-align:center;font-size:32px;font-weight:800;color:#F08A4B">Link in bio →</div>'
                    '<div class="ex" style="left:44px;bottom:24px;font-size:15px">Estimates only, not financial advice.</div>'),
}

jobs = []
def add(folder, name, html, w, h, k):
    os.makedirs(os.path.join(HERE, "images", folder), exist_ok=True)
    src = os.path.join(TMP, f"{folder}-{name}.html"); open(src, "w").write(html)
    jobs.append([src, os.path.join(HERE, "images", folder, f"before-you-click-pay-later-{name}.png"), w, h, k])

add("gumroad", "gumroad-cover", COVER, 1280, 720, 2)
add("gumroad", "gumroad-thumb", SQ(600), 600, 600, 2)
add("beacons", "beacons-product", SQ(540), 540, 540, 2)
for n, html in IG.items():
    add("instagram", f"ig-{n}", html, IW, IH, 1.25)

js = f"""import {{ chromium }} from '/opt/node22/lib/node_modules/playwright/index.mjs';
const jobs = {json.dumps(jobs)};
const b = await chromium.launch();
for (const [src, out, w, h, k] of jobs) {{
  const p = await b.newPage({{ viewport: {{ width: w, height: h }}, deviceScaleFactor: k }});
  await p.goto('file://' + src); await p.waitForLoadState('networkidle');
  await p.screenshot({{ path: out }}); console.log(out.split('/').pop()); await p.close();
}}
await b.close();"""
open(os.path.join(TMP, "shoot.mjs"), "w").write(js)
subprocess.run(["node", os.path.join(TMP, "shoot.mjs")], check=True)
