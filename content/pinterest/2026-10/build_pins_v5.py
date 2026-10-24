"""Pinterest pins v5 (1000x1500, 2:3): new topics for W44 (volume plan topics 2, 6, 7).

mt1 minimum payment trap -> Debt Payoff Planner; sb1 compare subscriptions by the year -> Hidden Cost Tracker;
tv1 holiday travel fees -> Holiday Hidden Cost Tracker. Numbers are the products' made-up example rows,
LibreOffice recalculation 2026-10-24 (planner: Minimums only interest 7,135.07, plan 1,679.15, save 5,455.92;
credit card 4,800 at 24.49%, 120 minimum, interest if minimums only 5,265.69, 84 payments by independent simulation;
tracker: photo app 22.99/month = 275.88/yr, VPN 59.88/yr = 4.99/month, meal kit 59.99/week = 3,119.48/yr).
Poses not used on any earlier pin (shock, think, checklist). Copy, links and dates: pins.md, section v5.
Usage: python3 content/pinterest/2026-10/build_pins_v5.py
"""
import json, os, subprocess
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
P = f"{ROOT}/products"
ART = f"{ROOT}/content/2026-10-comic-02/art"
ART3 = f"{ROOT}/content/2026-10-comic-03/art"
TMP = "/tmp/cm-pins-v5"
ART1 = f"{ROOT}/content/2026-10-comic-01/art"
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

def mini2(rows, top, cols):  # money in columns 2 and 4, text left in 1 and 3
    th = "".join(f'<th style="text-align:{"right" if i in (1, 3) else "left"}">{c}</th>' for i, c in enumerate(cols))
    tr = "".join("<tr>" + "".join(f'<td style="text-align:{"right" if i in (1, 3) else "left"};padding-left:{"22px" if i == 2 else "4px"}">{v}</td>' for i, v in enumerate(r)) + "</tr>" for r in rows)
    return f'<div class="mini" style="top:{top}px"><table><tr>{th}</tr>{tr}</table></div>'

V = lambda t, c: f'<span class="v {c}">{t}</span>'
PINS = {
    "mt1-minimum-payment-trap": pin("Debt payoff · Minimum payments", '<span style="font-size:96px">Minimum payment,</span><br><em style="font-size:96px">maximum interest.</em>',
        "Made-up example: a <i>$4,800</i> card at 24.49% APR, paying only the <i>$120</i> minimum: about <i>7 years</i> and <i>$5,265.69</i> in interest.", 560,
        mini([("Minimums only, 5 debts", "$7,135.07", "", ""), ("With a payoff order", "$1,679.15", "", ""),
              ("Interest you save", "<b>$5,455.92</b>", "", V("Plan", "g"))], 960, cols=("Total interest", "", "", "")),
        f"{ART1}/shock.jpg", "right:0px;top:960px;width:350px", '<span class="tag cta">DEBT PAYOFF PLANNER</span>'),
    "sb1-subscriptions-by-the-year": pin("Subscriptions · Monthly or yearly", '<span style="font-size:96px">Monthly or yearly?</span><br><em style="font-size:84px">Compare by the year.</em>',
        "Made-up example: a photo app at <i>$22.99</i> a month is <i>$275.88</i> a year. A meal kit at $59.99 a week is <i>$3,119.48</i> a year.", 560,
        mini2([("Photo app", "$22.99", "Monthly", "$275.88"), ("VPN", "$59.88", "Yearly", "$59.88"),
              ("Meal kit", "$59.99", "Weekly", "<b>$3,119.48</b>")], 940, cols=("Item", "Price", "Billing", "Per year")),
        f"{ART1}/think.jpg", "right:0px;top:960px;width:350px", '<span class="tag cta">HIDDEN COST TRACKER</span>'),
    "tv1-holiday-travel-fees": pin("Holiday travel · Before you book", '<span style="font-size:92px">Holiday travel:</span><br><em style="font-size:84px">the fare isn’t the trip.</em>',
        "Before you book, add what the fare leaves out: <i>checked bags</i>, <i>seat choice</i>, <i>resort fees</i>, <i>airport parking</i>. Then plan the total, not the fare.", 560,
        mini([("Fare", "", "", V("Listed", "g")), ("Checked bags", "", "", V("Add", "y")), ("Seat choice", "", "", V("Add", "y")),
              ("Resort fee", "", "", V("Add", "y")), ("Airport parking", "", "", V("Add", "y"))], 920, cols=("Trip cost", "", "", "")),
        f"{ART1}/checklist.jpg", "right:0px;top:1040px;width:330px", '<span class="tag cta">HOLIDAY HIDDEN COST TRACKER</span>', foot="Checklist · not financial advice"),
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
