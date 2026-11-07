"""Pinterest pins v2 (1000x1500, 2:3): receipt mascot + real product screen. October 2026.

Same products and made-up numbers as v1 (pins.md), new images so Pinterest sees fresh pins for the same links.
Mascot poses come from the receipt comics (content/2026-10-comic-02/03/art). Copy and links: pins.md, section v2.
Usage: python3 content/pinterest/2026-10/build_pins_v2.py
"""
import json, os, subprocess
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
P = f"{ROOT}/products"
ART = f"{ROOT}/content/2026-10-comic-02/art"
ART3 = f"{ROOT}/content/2026-10-comic-03/art"
TMP = "/tmp/cm-pins-v2"; os.makedirs(TMP, exist_ok=True)

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

def pin(kicker, title, receipt, receipt_top, shot, shot_style, pose, pose_style, tag):
    return (f'<div class="k"><b>CheckMaybe</b> · {kicker}</div><h1>{title}</h1>'
            f'<div class="receipt" style="top:{receipt_top}px"><div class="lab">THE RECEIPT</div><div class="t">{receipt}</div></div>'
            f'<div class="shot" style="{shot_style}"><img src="file://{TMP}/{shot}.png"></div>'
            f'<img class="pose" src="file://{pose}" style="{pose_style}">{tag}'
            '<div class="foot"><span>Made-up example · not financial advice</span><span>checkmaybe</span></div>')

PINS = {
    "r1-unroll-67": pin("Pay later", '<span style="font-size:100px">“Only $67<br>a month.”</span><br><em style="font-size:76px">Unroll the receipt.</em>',
        "24 × $67 = <i>$1,608</i> for a $1,200 phone.<br>That’s <i>$408 more</i>, about 29.8% APR.", 520,
        "bycpl", "left:64px;top:800px;width:380px", f"{ART}/unroll.jpg", "right:30px;top:820px;width:470px",
        '<span class="tag free">FREE GUIDE · 5 CHECKS</span>'),
    "r2-holiday-january": pin("Holiday budget", '<span style="font-size:92px">Four small<br>holiday plans.</span><br><em style="font-size:92px">One big January.</em>',
        "Four pay-in-4 plans land together:<br><i>$428.25</i> in January, 10.2% of the example income.", 520,
        "jan", "left:64px;top:820px;width:620px", f"{ART3}/gifts.jpg", "right:10px;top:860px;width:400px",
        '<span class="tag cta">HOLIDAY HIDDEN COST TRACKER</span>'),
    "r3-free-trial": pin("Free trials", '<span style="font-size:96px">Free until<br>the date</span><br><em style="font-size:96px">you forget.</em>',
        "Write down the <i>cancel-by date</i> the day you start. The tracker highlights trials before they bill.", 520,
        "hct", "left:64px;top:800px;width:600px", f"{ART3}/trial.jpg", "right:0px;top:880px;width:420px",
        '<span class="tag cta">HIDDEN COST TRACKER</span>'),
    "r4-zero-asterisk": pin("Debt payoff", '<span style="font-size:110px">“0% interest*”</span><br><em style="font-size:84px">Read the *.</em>',
        "When does the 0% end? It can change which debt you should pay off first.", 470,
        "compare", "left:64px;top:740px;width:640px", f"{ART}/asterisk.jpg", "right:10px;top:860px;width:450px",
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
