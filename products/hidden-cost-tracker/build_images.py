"""Hidden Cost Tracker listing images for Etsy, Gumroad and Beacons.

Usage: python3 build_images.py <crops_dir>
  <crops_dir> holds PNG crops of the real sheet (example rows):
    dash, kpi, upcoming, debts, phone_apr, donut, spend, apr, money, savecard, subs_left, guide1
  Dashboard/Debts crops come from the xlsx rendered at 400 dpi; subs_left is a Google Sheets
  screenshot (it shows the tick boxes). guide1 is page 1 of the buyer guide PDF.
Writes HTML to /tmp/hct-img and PNGs to images/etsy, images/gumroad, images/beacons.
"""
import json, os, subprocess, sys

SRC = os.path.abspath(sys.argv[1])
HERE = os.path.dirname(os.path.abspath(__file__))
TMP = "/tmp/hct-img"
os.makedirs(TMP, exist_ok=True)

CSS = """
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:%(w)dpx;height:%(h)dpx;overflow:hidden}
body{background:#15171F;background-image:radial-gradient(ellipse at 85%% 0%%,rgba(240,138,75,.16),transparent 55%%),radial-gradient(ellipse at 0%% 100%%,rgba(138,180,255,.10),transparent 50%%);
 color:#EDEBF5;font-family:"Liberation Sans","DejaVu Sans",Arial,sans-serif;position:relative;padding:%(pad)dpx}
.brand{font-size:%(bs)dpx;letter-spacing:.18em;font-weight:700;color:#9A98AE;text-transform:uppercase}
.brand b{color:#F08A4B}
h1{font-size:%(h1)dpx;line-height:1.08;font-weight:800;margin-top:%(g)dpx;letter-spacing:-.01em}
h1 em{font-style:normal;color:#F08A4B}
.sub{font-size:%(ss)dpx;color:#9A98AE;margin-top:%(g2)dpx;line-height:1.35}
.shot{border-radius:%(r)dpx;overflow:hidden;border:1px solid #33384F;box-shadow:0 18px 50px rgba(0,0,0,.55);background:#15171F}
.shot img{display:block;width:100%%}
.win{border-radius:%(r)dpx;overflow:hidden;border:1px solid #33384F;box-shadow:0 22px 60px rgba(0,0,0,.6);background:#1E2130}
.win .bar{height:%(bar)dpx;display:flex;gap:%(dot)dpx;align-items:center;padding:0 %(dot)dpx;background:#232739}
.win .bar i{width:%(dot)dpx;height:%(dot)dpx;border-radius:50%%;background:#33384F;display:block}
.win img{display:block;width:100%%}
.ex{position:absolute;z-index:9;right:%(pad)dpx;bottom:%(exb)dpx;font-size:%(xs)dpx;color:#9A98AE;letter-spacing:.06em;background:rgba(21,23,31,.92);padding:.35em .8em;border-radius:999px;border:1px solid #33384F}
.chips{display:flex;flex-wrap:wrap;gap:%(cg)dpx;margin-top:%(g2)dpx}
.chip{font-size:%(cs)dpx;font-weight:700;padding:%(cp)dpx %(cp2)dpx;border-radius:999px;border:1px solid #33384F;background:#1E2130}
.o{color:#F08A4B}.r{color:#FF6B6B}.g{color:#5FD38D}.a{color:#F2B544}.b{color:#8AB4FF}.p{color:#B18CFF}
.card{background:#1E2130;border:1px solid #33384F;border-radius:%(r)dpx;padding:%(cpad)dpx}
.card h3{font-size:%(h3)dpx;margin-bottom:%(g3)dpx}
.card p{font-size:%(ps)dpx;color:#9A98AE;line-height:1.4}
.num{font-size:%(h3)dpx;font-weight:800;color:#15171F;background:#F08A4B;width:%(nw)dpx;height:%(nw)dpx;border-radius:50%%;display:flex;align-items:center;justify-content:center;margin-bottom:%(g3)dpx}
ul.inc{list-style:none;font-size:%(ps)dpx;line-height:1.5}
ul.inc li{padding-left:1.3em;position:relative;margin-bottom:.35em}
ul.inc li:before{content:"✓";position:absolute;left:0;color:#5FD38D;font-weight:800}
.abs{position:absolute}
"""


def scale(w, h):
    k = w / 1200
    v = dict(w=w, h=h, pad=56, bs=15, h1=58, g=14, ss=24, g2=14, r=14, bar=26, dot=11, exb=22, xs=13,
             cg=10, cs=17, cp=8, cp2=16, cpad=26, h3=24, g3=10, ps=19, nw=40)
    return {key: (val if key in ("w", "h") else max(1, round(val * k))) for key, val in v.items()}


def img(name):
    return f"file://{SRC}/{name}.png"


def page(w, h, body, brand=True, example=True):
    s = scale(w, h)
    top = '<div class="brand"><b>CheckMaybe</b> · Hidden Cost Tracker · Google Sheets</div>' if brand else ""
    ex = '<div class="ex">Example data · not financial advice</div>' if example else ""
    return f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS % s}</style></head><body>{top}{body}{ex}</body></html>'


def win(name, style):
    return f'<div class="win abs" style="{style}"><div class="bar"><i></i><i></i><i></i></div><img src="{img(name)}"></div>'


def shot(name, style):
    return f'<div class="shot abs" style="{style}"><img src="{img(name)}"></div>'


CHIPS = ('<div class="chips"><span class="chip r">Real APR</span><span class="chip a">Free-trial countdown</span>'
         '<span class="chip g">Debt-free date</span><span class="chip b">Google Sheets + Excel</span></div>')

# ---- Etsy: 4:3, rendered 1200x900 CSS px at 2.5x = 3000x2250 ----
W, H = 1200, 900
ETSY = {
    "01-hero": page(W, H, '<h1>See what your debts &amp;<br>subscriptions <em>really cost</em></h1>' + CHIPS
                   + win("dash", "left:330px;top:300px;width:820px")),
    "02-real-apr": page(W, H, '<h1>That $1,200 phone plan?<br><em>About 29.8% APR</em></h1>'
                       '<div class="sub">Enter the monthly payment and number of payments. The sheet works out the real yearly rate.</div>'
                       + shot("phone_apr", "left:130px;top:320px;width:940px")),
    "03-kpis": page(W, H, '<h1><em>8 numbers</em> that show where<br>your money goes each month</h1>'
                   + shot("kpi", "left:56px;top:300px;width:1088px")),
    "04-pay-first": page(W, H, '<h1>Know which debt<br>to <em>pay off first</em></h1>'
                        '<div class="sub">Debts ranked by real APR, with HIGH / CHECK / OK flags.</div>'
                        + shot("debts", "left:56px;top:330px;width:560px") + shot("apr", "left:650px;top:300px;width:494px")),
    "05-free-trials": page(W, H, '<h1>Never miss a<br><em>free-trial cancel-by</em> date</h1>'
                          '<div class="sub">Next charges and trial countdowns, updated every day.</div>'
                          + shot("upcoming", "left:240px;top:330px;width:720px")),
    "06-cancel-it": page(W, H, '<h1>Tick <em>“Cancel it?”</em><br>see your yearly savings</h1>'
                        + shot("subs_left", "left:56px;top:260px;width:720px")
                        + shot("savecard", "left:810px;top:420px;width:334px")),
    "07-charts": page(W, H, '<h1>Charts that <em>update</em><br>as you type</h1>'
                     + shot("donut", "left:56px;top:290px;width:500px") + shot("spend", "left:590px;top:290px;width:554px")
                     + shot("apr", "left:330px;top:560px;width:540px")),
    "08-money-map": page(W, H, '<h1>Your monthly <em>money map</em></h1>'
                        '<div class="sub">Take-home pay, what is already spoken for, and what is left.</div>'
                        + shot("money", "left:56px;top:300px;width:540px") + shot("donut", "left:630px;top:300px;width:514px")),
    "09-three-steps": page(W, H, '<h1>Ready in <em>3 steps</em></h1>'
                          '<div class="abs" style="left:56px;top:250px;width:1088px;display:grid;grid-template-columns:1fr 1fr 1fr;gap:20px">'
                          '<div class="card"><div class="num">1</div><h3>Make your copy</h3><p>Open the link in the PDF and press <b style="color:#EDEBF5">Make a copy</b>. It saves to your own Google Drive.</p></div>'
                          '<div class="card"><div class="num">2</div><h3>Add your numbers</h3><p>Monthly take-home pay in Settings, then your debts and subscriptions.</p></div>'
                          '<div class="card"><div class="num">3</div><h3>Read the Dashboard</h3><p>Real APR, free trials, savings and your debt-free date fill in on their own.</p></div></div>'
                          + win("dash", "left:300px;top:520px;width:600px")),
    "10-included": page(W, H, '<h1>What\'s <em>included</em></h1>'
                        '<div class="abs" style="left:56px;top:230px;width:560px"><ul class="inc">'
                        '<li>Google Sheets tracker (copy link in the PDF)</li><li>Works in Excel too: File › Download › .xlsx</li>'
                        '<li>Tabs: Dashboard, Debts &amp; Installments, Subscriptions, Settings, How to Use</li>'
                        '<li>Room for 20 debts and 30 subscriptions</li><li>Dark theme, tick boxes, filters, 3 charts</li>'
                        '<li>4-page PDF guide</li><li>Digital download, nothing is shipped</li></ul>'
                        '<p style="font-size:16px;color:#6E6C80;margin-top:22px">Estimates only. Not financial advice. Example rows are made up.</p></div>'
                        + shot("guide1", "left:700px;top:200px;width:444px"), example=False),
}

# ---- Gumroad: cover 1280x720 at 2x; thumbnail 600x600 at 2x. Beacons: 540x540 at 2x = 1080 ----
GUM_COVER = page(1280, 720, '<h1>See what your debts &amp; subscriptions <em>really cost</em></h1>' + CHIPS
                 + win("dash", "left:470px;top:290px;width:760px"))
SQUARE = lambda w: page(w, w, f'<h1 style="font-size:{round(w*.12)}px">Hidden Cost<br><em>Tracker</em></h1>'
                        f'<div class="sub" style="font-size:{round(w*.042)}px">Real APR · free trials · debt-free date</div>'
                        + win("dash", f"left:{round(w*.06)}px;top:{round(w*.5)}px;width:{round(w*.88)}px"))

jobs = []
def add(folder, name, html, w, h, k):
    os.makedirs(os.path.join(HERE, "images", folder), exist_ok=True)
    p = os.path.join(TMP, f"{folder}-{name}.html")
    open(p, "w").write(html)
    jobs.append([p, os.path.join(HERE, "images", folder, f"hidden-cost-tracker-{name}.png"), w, h, k])

for n, html in ETSY.items():
    add("etsy", f"etsy-{n}", html, W, H, 2.5)
add("gumroad", "gumroad-cover", GUM_COVER, 1280, 720, 2)
add("gumroad", "gumroad-thumb", SQUARE(600), 600, 600, 2)
add("beacons", "beacons-product", SQUARE(540), 540, 540, 2)

js = f"""
import {{ chromium }} from '/opt/node22/lib/node_modules/playwright/index.mjs';
const jobs = {json.dumps(jobs)};
const b = await chromium.launch();
for (const [src, out, w, h, k] of jobs) {{
  const p = await b.newPage({{ viewport: {{ width: w, height: h }}, deviceScaleFactor: k }});
  await p.goto('file://' + src); await p.waitForLoadState('networkidle');
  const over = await p.evaluate(([W, H]) => [...document.querySelectorAll('.abs,h1,.sub,.chips')]
    .filter(e => {{ const r = e.getBoundingClientRect(); return r.right > W - 20 || r.bottom > H - 10; }}).map(e => e.className || e.tagName), [w, h]);
  await p.screenshot({{ path: out }}); console.log(out.split('/').pop(), over.length ? 'OVERFLOW ' + over.join(',') : 'OK');
  await p.close();
}}
await b.close();
"""
open(os.path.join(TMP, "shoot.mjs"), "w").write(js)
subprocess.run(["node", os.path.join(TMP, "shoot.mjs")], check=True,
               env={**os.environ, "NODE_PATH": "/opt/node22/lib/node_modules"})
