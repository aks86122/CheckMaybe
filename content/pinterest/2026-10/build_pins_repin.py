"""Pinterest repin variants (1000x1500, 2:3): new image for every planned repin, so a repin is never the same picture.
Flipped layout (mascot left, product right), yellow accent, new headline; same links and checked made-up numbers.

Same products and checked made-up numbers as v1/v2; seasonal poses in art/ (Canva AI, 2026-10-18, reference MAHYRYx0qyo).
Copy, links and posting dates: pins.md, section "Repin variants".
Usage: python3 content/pinterest/2026-10/build_pins_repin.py
"""
import json, os, subprocess
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
P = f"{ROOT}/products"
ART = f"{ROOT}/content/2026-10-comic-02/art"
ART3 = f"{ROOT}/content/2026-10-comic-03/art"
TMP = "/tmp/cm-pins-repin"
SEA = f"{HERE}/art"; os.makedirs(TMP, exist_ok=True)

CUTS = {  # name: (source under products/, crop box in source pixels)
    "bycpl": ("before-you-click-pay-later/images/gumroad/before-you-click-pay-later-gumroad-cover.png", (1380, 100, 2560, 1440)),
    "hct": ("hidden-cost-tracker/images/gumroad/hidden-cost-tracker-gumroad-cover.png", (940, 580, 2460, 1440)),
    "jan": ("holiday-hidden-cost-tracker/images/crops/dash_month.png", (0, 0, 1540, 480)),
    "compare": ("debt-payoff-planner/images/crops/plan_compare.png", (0, 0, 1253, 315)),
    "gifts": ("holiday-hidden-cost-tracker/images/crops/gifts.png", (0, 0, 2600, 1300)),
}
for k, (src, box) in CUTS.items():
    Image.open(os.path.join(P, src)).crop(box).save(os.path.join(TMP, k + ".png"))

CSS = """@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
*{box-sizing:border-box;margin:0;padding:0}html,body{width:1000px;height:1500px;overflow:hidden}
body{position:relative;background:#15171F;color:#EDEBF5;font-family:Inter,"Liberation Sans",sans-serif}
.k{position:absolute;left:64px;top:64px;font-size:24px;letter-spacing:.18em;font-weight:600;color:#C9C7D8;text-transform:uppercase}.k b{color:#F08A4B}
h1{position:absolute;left:64px;right:64px;top:130px;font-weight:800;line-height:1.08}h1 em{font-style:normal;color:#F08A4B}
.receipt{position:absolute;left:64px;right:64px;background:#22202A;border:3px solid #F7C948;border-radius:26px;padding:34px 40px}
.lab{font-size:22px;font-weight:800;letter-spacing:.2em;color:#F7C948}.t{font-size:38px;font-weight:600;line-height:1.38;margin-top:12px}.t i{font-style:normal;color:#F7C948}
.shot{position:absolute;overflow:hidden;border-radius:14px;border:1px solid #33384F;box-shadow:0 24px 70px rgba(0,0,0,.6)}.shot img{display:block;width:100%}
.pose{position:absolute;-webkit-mask-image:radial-gradient(ellipse 50% 50% at center,#000 72%,transparent 100%);mask-image:radial-gradient(ellipse 50% 50% at center,#000 72%,transparent 100%)}
.tag{position:absolute;left:64px;bottom:110px;display:inline-block;font-weight:800;border-radius:999px;padding:12px 26px;font-size:26px;letter-spacing:.04em;color:#15171F}
.free{background:#5FD38D}.cta{background:#F08A4B}
h1 em{color:#F7C948}.receipt{border-color:#F08A4B}.lab{color:#F08A4B}.t i{color:#F08A4B}.k b{color:#F7C948}
.foot{position:absolute;left:64px;right:64px;bottom:44px;display:flex;justify-content:space-between;font-size:19px;letter-spacing:.12em;text-transform:uppercase;color:#9A98AC}"""

def pin(kicker, title, receipt, receipt_top, shot, shot_style, pose, pose_style, tag, foot="Made-up example · not financial advice"):
    return (f'<div class="k"><b>CheckMaybe</b> · {kicker}</div><h1>{title}</h1>'
            f'<div class="receipt" style="top:{receipt_top}px"><div class="lab">THE RECEIPT</div><div class="t">{receipt}</div></div>'
            f'<div class="shot" style="{shot_style}"><img src="file://{TMP}/{shot}.png"></div>'
            f'<img class="pose" src="file://{pose}" style="{pose_style}">{tag}'
            f'<div class="foot"><span>{foot}</span><span>checkmaybe</span></div>')

A3 = f"{ROOT}/content/2026-10-comic-03/art"

PINS = {  # mascot on the left, product on the right (mirror of v1–v3)
    "tg1b-black-friday-cart": pin("Black Friday · Pay later", '<span style="font-size:82px">The cart says $499.</span><br><em style="font-size:82px">The plan says $537.</em>',
        "Made-up example: 6 payments × $89.50 = <i>$537</i> for a $499 console, about 25.7% APR. Check the total, not the payment.", 440,
        "bycpl", "right:64px;top:800px;width:360px", f"{SEA}/bags.jpg", "left:10px;top:800px;width:460px",
        '<span class="tag free">FREE GUIDE · 5 CHECKS</span>'),
    "tg2b-black-friday-now-january-later": pin("Black Friday · Holiday budget", '<span style="font-size:96px">Black Friday now.</span><br><em style="font-size:96px">January later.</em>',
        "Made-up example: four holiday pay-in-4 plans land together, <i>$428.25</i> in January, 10.2% of the example income.", 420,
        "jan", "right:64px;top:780px;width:520px", f"{A3}/snow.jpg", "left:0px;top:760px;width:440px",
        '<span class="tag cta">HOLIDAY HIDDEN COST TRACKER</span>'),
    "h2b-gift-list-before-cart": pin("Christmas · Gift budget", '<span style="font-size:92px">Make the gift list</span><br><em style="font-size:92px">before the cart.</em>',
        "Budget per person, every pay-later due date and free-trial cancel-by dates, in one Google Sheet.", 420,
        "gifts", "right:64px;top:760px;width:560px", f"{A3}/gifts.jpg", "left:0px;top:780px;width:420px",
        '<span class="tag cta">HOLIDAY HIDDEN COST TRACKER</span>', "Example data · not financial advice"),
    "r4b-new-year-payoff-order": pin("New year · Debt payoff", '<span style="font-size:96px">New year,</span><br><span style="font-size:96px">new payoff plan?</span><br><em style="font-size:80px">Check the 0% dates first.</em>',
        "A 0% deal has an end date. It can change which debt you should pay off first.", 600,
        "compare", "right:64px;top:900px;width:540px", f"{A3}/calc.jpg", "left:10px;top:880px;width:420px",
        '<span class="tag cta">DEBT PAYOFF PLANNER</span>'),
}

jobs = []
for name, body in PINS.items():
    src = f"{TMP}/{name}.html"
    with open(src, "w") as f:
        f.write(f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>{body}</body></html>')
    jobs.append([src, f"{HERE}/pins/checkmaybe-pin-{name}.png"])

js = f"""import {{ chromium }} from '/opt/node22/lib/node_modules/playwright/index.mjs';
const jobs = {json.dumps(jobs)}; const b = await chromium.launch();
for (const [s, o] of jobs) {{
  const p = await b.newPage({{ viewport: {{ width: 1000, height: 1500 }} }});
  await p.goto('file://' + s); await p.waitForLoadState('networkidle'); await p.evaluate(() => document.fonts.ready);
  await p.screenshot({{ path: o }}); console.log(o.split('/').pop()); await p.close(); }}
await b.close();"""
with open(f"{TMP}/shoot.mjs", "w") as f:
    f.write(js)
subprocess.run(["node", f"{TMP}/shoot.mjs"], check=True)
