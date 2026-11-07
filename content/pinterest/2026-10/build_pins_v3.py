"""Pinterest pins v3 (1000x1500, 2:3): seasonal receipt mascot (Halloween, Thanksgiving / Black Friday). October 2026.

Same products and checked made-up numbers as v1/v2; seasonal poses in art/ (Canva AI, 2026-10-18, reference MAHYRYx0qyo).
Copy, links and posting dates: pins.md, section v3.
Usage: python3 content/pinterest/2026-10/build_pins_v3.py
"""
import json, os, subprocess
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
P = f"{ROOT}/products"
ART = f"{ROOT}/content/2026-10-comic-02/art"
ART3 = f"{ROOT}/content/2026-10-comic-03/art"
TMP = "/tmp/cm-pins-v3"
SEA = f"{HERE}/art"; os.makedirs(TMP, exist_ok=True)

CUTS = {  # name: (source under products/, crop box in source pixels)
    "bycpl": ("before-you-click-pay-later/images/gumroad/before-you-click-pay-later-gumroad-cover.png", (1380, 100, 2560, 1440)),
    "hct": ("hidden-cost-tracker/images/gumroad/hidden-cost-tracker-gumroad-cover.png", (940, 580, 2460, 1440)),
    "jan": ("holiday-hidden-cost-tracker/images/crops/dash_month.png", (0, 0, 1540, 480)),
    "compare": ("debt-payoff-planner/images/crops/plan_compare.png", (0, 0, 1253, 315)),
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
.foot{position:absolute;left:64px;right:64px;bottom:44px;display:flex;justify-content:space-between;font-size:19px;letter-spacing:.12em;text-transform:uppercase;color:#9A98AC}"""

def pin(kicker, title, receipt, receipt_top, shot, shot_style, pose, pose_style, tag, foot="Made-up example · not financial advice"):
    return (f'<div class="k"><b>CheckMaybe</b> · {kicker}</div><h1>{title}</h1>'
            f'<div class="receipt" style="top:{receipt_top}px"><div class="lab">THE RECEIPT</div><div class="t">{receipt}</div></div>'
            f'<div class="shot" style="{shot_style}"><img src="file://{TMP}/{shot}.png"></div>'
            f'<img class="pose" src="file://{pose}" style="{pose_style}">{tag}'
            f'<div class="foot"><span>{foot}</span><span>checkmaybe</span></div>')

PINS = {
    "hw1-zombie-subscriptions": pin("Halloween · Subscriptions", '<span style="font-size:104px">Zombie<br>subscriptions.</span><br><em style="font-size:70px">They come back every month.</em>',
        "Made-up example: 4 forgotten subscriptions = <i>$1,103.76</i> a year. Tick “Cancel it?” and the sheet adds it up.", 560,
        "hct", "left:64px;top:860px;width:560px", f"{SEA}/ghost.jpg", "right:10px;top:850px;width:440px",
        '<span class="tag cta">HIDDEN COST TRACKER</span>'),
    "hw2-trick-or-treat-0": pin("Halloween · Pay later", '<span style="font-size:92px">Trick or treat:</span><br><span style="font-size:100px">“0% interest*”</span><br><em style="font-size:84px">Read the *.</em>',
        "Look for “deferred interest”. If any balance is left when the promo ends, interest can go back to the day you bought it.", 600,
        "bycpl", "left:64px;top:930px;width:330px", f"{SEA}/pumpkin.jpg", "right:10px;top:920px;width:450px",
        '<span class="tag free">FREE GUIDE · 5 CHECKS</span>', "Educational · source: US CFPB · not financial advice"),
    "tg1-black-friday-pay-in-4": pin("Black Friday · Pay later", '<span style="font-size:100px">Black Friday<br>on pay-in-4?</span><br><em style="font-size:80px">Check the total first.</em>',
        "Made-up example: a $499 console as 6 × $89.50 = <i>$537</i>, about <i>25.7% APR</i>.", 560,
        "bycpl", "left:64px;top:820px;width:360px", f"{SEA}/bags.jpg", "right:10px;top:830px;width:460px",
        '<span class="tag free">FREE GUIDE · 5 CHECKS</span>'),
    "tg2-thanksgiving-january": pin("Thanksgiving · Holiday budget", '<span style="font-size:84px">Thanksgiving<br>week shopping</span><br><em style="font-size:84px">lands in January.</em>',
        "Made-up example: four holiday pay-in-4 plans = <i>$428.25</i> due in January, 10.2% of the example income.", 480,
        "jan", "left:64px;top:800px;width:540px", f"{SEA}/pie.jpg", "right:0px;top:770px;width:500px",
        '<span class="tag cta">HOLIDAY HIDDEN COST TRACKER</span>'),
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
