"""Pinterest pins v4 (1000x1500, 2:3): Black Friday "is it really a deal?" for the Deal Check tab (Holiday Hidden Cost Tracker v1.1).

Same products and checked made-up numbers as v1/v2; seasonal poses in art/ (Canva AI, 2026-10-18, reference MAHYRYx0qyo).
Numbers are the made-up example rows of the Deal Check tab, checked by LibreOffice recalculation (2026-10-24).
Poses not used on any earlier pin. Copy, links and dates: pins.md, section v4.
Usage: python3 content/pinterest/2026-10/build_pins_v4.py
"""
import json, os, subprocess
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
P = f"{ROOT}/products"
ART = f"{ROOT}/content/2026-10-comic-02/art"
ART3 = f"{ROOT}/content/2026-10-comic-03/art"
TMP = "/tmp/cm-pins-v4"
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
.mini{position:absolute;left:64px;width:560px;background:#1C1E28;border:1px solid #33384F;border-radius:14px;padding:18px 22px;box-shadow:0 24px 70px rgba(0,0,0,.6)}
.mini table{width:100%;border-collapse:collapse;font-size:21px}.mini th{color:#9A98AC;font-weight:600;text-align:left;padding:6px 4px;font-size:16px;letter-spacing:.08em;text-transform:uppercase}
.mini td{padding:9px 4px;border-top:1px solid #2C2F3E}.mini td.r{text-align:right}.v{font-weight:800;border-radius:8px;padding:3px 8px;font-size:17px}.g{background:#1C3A2A;color:#74D39A}.b{background:#43202A;color:#E2687B}.y{background:#3D3218;color:#F7C948}
.foot{position:absolute;left:64px;right:64px;bottom:44px;display:flex;justify-content:space-between;font-size:19px;letter-spacing:.12em;text-transform:uppercase;color:#9A98AC}"""

def mini(rows, top, cols=("Item", "Sale", "Usual", "Verdict")):
    th = "".join(f"<th>{c}</th>" for c in cols)
    tr = "".join("<tr>" + "".join(f'<td class="{"r" if i in (1, 2) else ""}">{v}</td>' for i, v in enumerate(r)) + "</tr>" for r in rows)
    return f'<div class="mini" style="top:{top}px"><table><tr>{th}</tr>{tr}</table></div>'

def pin(kicker, title, receipt, receipt_top, table, pose, pose_style, tag, foot="Made-up example · not financial advice"):
    return (f'<div class="k"><b>CheckMaybe</b> · {kicker}</div><h1>{title}</h1>'
            f'<div class="receipt" style="top:{receipt_top}px"><div class="lab">THE RECEIPT</div><div class="t">{receipt}</div></div>'
            f'{table}<img class="pose" src="file://{pose}" style="{pose_style}">{tag}'
            f'<div class="foot"><span>{foot}</span><span>checkmaybe</span></div>')

V = lambda t, c: f'<span class="v {c}">{t}</span>'
TAG = '<span class="tag cta">DEAL CHECK · HOLIDAY TRACKER</span>'
PINS = {
    "bf1-really-a-deal": pin("Black Friday · Deal check", '<span style="font-size:96px">Black Friday<br>“deal”?</span><br><em style="font-size:76px">Check the usual price first.</em>',
        "Made-up example: headphones <i>$199</i>, usually $249 = <i>20%</i> below. An air fryer at $89, usually $89 = <i>not a deal</i>.", 560,
        mini([("Headphones", "$199", "$249", V("Real deal", "g")), ("Air fryer", "$89", "$89", V("Not a deal", "b")),
              ("Smart watch", "$279", "$299", V("Small deal", "y"))], 900),
        f"{ART}/tag.jpg", "right:0px;top:880px;width:400px", TAG),
    "bf2-checkout-price": pin("Black Friday · Deal check", '<span style="font-size:90px">The sale price<br>isn’t the</span><br><em style="font-size:90px">checkout price.</em>',
        "Made-up example: a <i>$159</i> robot vacuum + 8% tax + $15 shipping = <i>$186.72</i> at checkout.", 560,
        mini([("Sale price", "$159.00", "", ""), ("+ 8% tax", "$12.72", "", ""), ("+ shipping", "$15.00", "", ""),
              ("At checkout", "<b>$186.72</b>", "", "")], 860, cols=("", "", "", "")),
        f"{ROOT}/content/2026-10-comic-01/art/magnify.jpg", "right:0px;top:860px;width:420px", TAG),
    "bf3-deal-on-a-plan": pin("Black Friday · Deal check", '<span style="font-size:90px">A deal on a plan</span><br><em style="font-size:90px">can cost more.</em>',
        "Made-up example: a <i>$499</i> TV is $538.92 at checkout. On 12 × $49 it’s <i>$588</i>: <i>$49.08</i> more.", 520,
        mini([("Pay in full", "$538.92", "", ""), ("12 × $49", "$588.00", "", ""), ("Extra on the plan", "<b>$49.08</b>", "", V("Plan costs more", "b"))],
             860, cols=("", "", "", "")),
        f"{ART}/calc.jpg", "right:0px;top:860px;width:420px", TAG),
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
