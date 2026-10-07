"""Instagram carousels for the money series (1080x1350).

A  money-series-*  : traffic post, points to the free Before You Click "Pay Later" guide (post now)
B  holiday-*       : Holiday Hidden Cost Tracker launch (post on launch day, before 11/1)
C  planner-*       : Debt Payoff Planner launch (post on launch day)

Screens are the real sheet crops in products/*/images/crops (made-up example rows).
Numbers come from the listings and posts, checked in the sheets:
  phone $1,200 as 24 x $67 = $1,608, about 29.8% APR; holiday January $428.25 (10.2% of example income);
  console $499 as 6 x $89.50 about 25.7% APR; planner Avalanche 1,598.68 vs Smart 1,679.15 interest.
Usage: python3 build_carousels.py
"""
import json, os, subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
PROD = os.path.abspath(os.path.join(HERE, "..", "..", "products"))
TMP = "/tmp/money-carousels"; os.makedirs(TMP, exist_ok=True)
from PIL import Image
CUTS = {  # name: (source, box in source pixels) — zoom into the part a phone can read
    "jan_table": ("holiday-hidden-cost-tracker/images/crops/dash_month.png", (0, 0, 1540, 480)),
    "compare_2": ("debt-payoff-planner/images/crops/plan_compare.png", (0, 0, 1253, 315)),
    "checks_l": ("debt-payoff-planner/images/crops/plan_checks.png", (0, 0, 900, 373)),
    "gifts_top": ("holiday-hidden-cost-tracker/images/crops/gifts.png", (0, 0, 2600, 900)),
    "sched_top": ("debt-payoff-planner/images/crops/schedule.png", (60, 0, 1960, 700)),
}
for k, (src, box) in CUTS.items():
    Image.open(os.path.join(PROD, src)).crop(box).save(os.path.join(TMP, k + ".png"))
crop = lambda p: f"file://{TMP}/{p}.png" if p in CUTS else f"file://{PROD}/{p}"
HOL = "holiday-hidden-cost-tracker/images/crops/"
DPP = "debt-payoff-planner/images/crops/"

CSS = """*{box-sizing:border-box;margin:0;padding:0}
html,body{width:864px;height:1080px;overflow:hidden}
body{background:#15171F;background-image:radial-gradient(ellipse at 85% 0%,rgba(240,138,75,.18),transparent 55%);
color:#EDEBF5;font-family:"Liberation Sans","DejaVu Sans",Arial,sans-serif;position:relative;padding:44px}
.brand{font-size:16px;letter-spacing:.18em;font-weight:700;color:#9A98AE;text-transform:uppercase}.brand b{color:#F08A4B}
.pn{position:absolute;right:44px;top:44px;font-size:18px;font-weight:700;color:#9A98AE}
.k{font-size:22px;margin-top:30px;letter-spacing:.15em;font-weight:700;color:#9A98AE}
h1{font-weight:800;line-height:1.07;letter-spacing:-.01em}h1 em{font-style:normal;color:#F08A4B}
.sub{color:#9A98AE;line-height:1.38}
.card{background:#1E2130;border:1px solid #33384F;border-radius:16px}
.shot{position:absolute;border-radius:12px;overflow:hidden;box-shadow:0 20px 60px rgba(0,0,0,.6);border:1px solid #33384F}
.shot img{display:block;width:100%}
.free{display:inline-block;background:#5FD38D;color:#15171F;font-weight:800;border-radius:999px;font-size:17px;padding:5px 14px}
.soon{display:inline-block;border:1px solid #33384F;color:#9A98AE;font-weight:700;border-radius:999px;font-size:17px;padding:5px 14px}
.live{display:inline-block;background:#F08A4B;color:#15171F;font-weight:800;border-radius:999px;font-size:17px;padding:5px 14px}
ul{list-style:none}li{padding-left:1.3em;position:relative;margin-bottom:.45em}
li:before{content:"✓";position:absolute;left:0;color:#5FD38D;font-weight:800}
.r{color:#FF6B6B}.g{color:#5FD38D}.o{color:#F08A4B}
.foot{position:absolute;left:44px;bottom:24px;font-size:15px;color:#9A98AE}
.cta{position:absolute;left:0;right:0;bottom:60px;text-align:center;font-size:34px;font-weight:800;color:#F08A4B}
"""

def slide(label, n, total, body, foot="Made-up example. Estimates only, not financial advice."):
    return (f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>'
            f'<div class="brand"><b>CheckMaybe</b> · {label}</div><div class="pn">{n} / {total}</div>{body}'
            f'<div class="foot">{foot}</div></body></html>')
shot = lambda src, style: f'<div class="shot" style="{style}"><img src="{crop(src)}"></div>'

def series(label, slides):
    return [(name, slide(label, i + 1, len(slides), body, *extra)) for i, (name, body, *extra) in enumerate(slides)]

A = series("Money tools", [
    ("01-hook",
     '<h1 style="font-size:76px;margin-top:70px">“Only <em>$67</em><br>a month.”</h1>'
     '<div class="sub" style="font-size:34px;margin-top:34px">But what does it<br>really cost you?</div>'
     '<div class="card" style="margin-top:70px;padding:34px;font-size:30px;line-height:1.5">'
     'CheckMaybe now checks the fine print<br>on <b class="o">your money</b> too. Swipe →</div>'),
    ("02-math",
     '<div class="k">THE MATH NOBODY SHOWS YOU</div>'
     '<h1 style="font-size:58px;margin-top:10px">A $1,200 phone,<br>24 payments of $67</h1>'
     '<div class="card" style="margin-top:44px;padding:40px;font-size:40px;line-height:1.75">'
     '$67 × 24 = <b>$1,608</b><br>− price $1,200<br>= <b class="r">$408 extra</b></div>'
     '<div style="margin-top:34px;font-size:40px;font-weight:800">That’s about <span class="o">29.8% APR</span>.</div>'),
    ("03-stack",
     '<div class="k">THE MONTH IT ALL LANDS</div>'
     '<h1 style="font-size:56px;margin-top:10px">Four “small” holiday<br>plans = <em>$428.25</em><br>due in January</h1>'
     + shot("jan_table", "left:44px;top:420px;width:776px")
     + '<div class="sub" style="position:absolute;left:44px;top:700px;width:776px;font-size:26px">'
       'Pay-in-4, store financing and a monthly plan. Each one sounded fine on its own.</div>'),
    ("04-order",
     '<div class="k">PAYING IT OFF</div>'
     '<h1 style="font-size:54px;margin-top:10px">The cheapest order<br>on paper can <em>cost more</em></h1>'
     + shot("compare_2", "left:44px;top:330px;width:776px")
     + '<div class="card" style="position:absolute;left:44px;top:570px;width:776px;padding:30px;font-size:27px;line-height:1.5">'
       'Avalanche shows the least interest (1,598.68 vs 1,679.15), but it clears the store card <b class="r">after its 0% deal ends</b>, so back-interest could be added.</div>'),
    ("05-lineup",
     '<div class="k">THE MONEY TOOLS</div>'
     '<h1 style="font-size:54px;margin-top:10px">Same rule as always:<br><em>check first</em>, then decide.</h1>'
     '<div style="margin-top:40px;display:grid;gap:18px">'
     '<div class="card" style="padding:24px 28px"><span class="free">FREE</span><div style="font-size:30px;font-weight:800;margin-top:10px">Before You Click “Pay Later”</div><div class="sub" style="font-size:22px">5 checks in 5 minutes · 12-page PDF</div></div>'
     '<div class="card" style="padding:24px 28px"><span class="live">AVAILABLE NOW</span><div style="font-size:30px;font-weight:800;margin-top:10px">Hidden Cost Tracker</div><div class="sub" style="font-size:22px">Real APR, subscriptions, free trials · Google Sheets</div></div>'
     '<div class="card" style="padding:24px 28px"><span class="live">AVAILABLE NOW</span><div style="font-size:30px;font-weight:800;margin-top:10px">Holiday Hidden Cost Tracker</div><div class="sub" style="font-size:22px">Gifts, holiday plans, January totals</div></div>'
     '<div class="card" style="padding:24px 28px"><span class="live">AVAILABLE NOW</span><div style="font-size:30px;font-weight:800;margin-top:10px">Debt Payoff Planner</div><div class="sub" style="font-size:22px">4 payoff orders, early-payoff fees, 0% deadlines</div></div>'
     '</div>', "Not financial advice."),
    ("06-cta",
     '<h1 style="font-size:66px;margin-top:70px">Start with the<br><em>free</em> guide</h1>'
     '<div class="card" style="margin-top:50px;padding:36px;font-size:30px;line-height:1.5"><ul>'
     '<li>What will I pay in total?</li><li>Roughly what yearly rate is that?</li><li>What if I’m late, or don’t finish on time?</li>'
     '<li>When does the first payment leave?</li><li>What else is due that month?</li></ul></div>'
     '<div class="cta">Free · link in bio →</div>', "Estimates only, not financial advice."),
])

B = series("Holiday Hidden Cost Tracker", [
    ("01-hook",
     '<h1 style="font-size:74px;margin-top:70px">Holiday gifts<br>on pay-in-4?</h1>'
     '<h1 style="font-size:74px;margin-top:20px"><em>January</em> gets<br>the bill.</h1>'
     '<div class="sub" style="font-size:32px;margin-top:40px">Add it up before you check out →</div>'
     + shot(HOL + "dash_kpi.png", "left:44px;top:760px;width:776px")),
    ("02-plans",
     '<div class="k">MADE-UP EXAMPLE</div>'
     '<h1 style="font-size:56px;margin-top:10px">Four plans.<br>None felt like a lot.</h1>'
     '<div class="card" style="margin-top:40px;padding:34px;font-size:28px;line-height:1.75">'
     'Smart watch · pay-in-4 · <b>$69.75</b> / 2 weeks<br>Flights · pay-in-4 · <b>$105</b> / 2 weeks<br>'
     'TV · store financing · <b>$59</b> / month<br>Game console · monthly plan · <b>$89.50</b> / month</div>'),
    ("03-january",
     '<div class="k">LINE UP THE DUE DATES</div>'
     '<h1 style="font-size:58px;margin-top:10px">January:<br><em>$428.25</em> in one month</h1>'
     '<div class="sub" style="font-size:26px;margin-top:16px">That’s 10.2% of the example income, on top of the usual bills.</div>'
     + shot("jan_table", "left:44px;top:440px;width:776px")),
    ("04-apr",
     '<div class="k">THE REAL RATE</div>'
     '<h1 style="font-size:56px;margin-top:10px">“Only $89.50 a month”</h1>'
     '<div class="card" style="margin-top:40px;padding:38px;font-size:38px;line-height:1.7">'
     '$499 console<br>6 × $89.50 = <b>$537</b><br>≈ <b class="r">25.7% APR</b></div>'
     '<div class="sub" style="font-size:26px;margin-top:26px">Enter the price, the payment and the number of payments. The sheet works out the rate.</div>'),
    ("05-inside",
     '<div class="k">WHAT’S INSIDE</div>'
     '<h1 style="font-size:54px;margin-top:10px">One sheet for the<br>whole season</h1>'
     '<div class="card" style="margin-top:36px;padding:34px;font-size:28px;line-height:1.45"><ul>'
     '<li>Gift list with a budget per person</li><li>Every holiday plan with its due dates</li>'
     '<li>Real APR and extra cost of each plan</li><li>Month-by-month totals and share of income</li>'
     '<li>Free trials with cancel-by dates</li></ul></div>'
     + shot("gifts_top", "left:44px;top:740px;width:776px;height:270px")),
    ("06-cta",
     '<h1 style="font-size:64px;margin-top:70px">Holiday<br>Hidden Cost<br><em>Tracker</em></h1>'
     '<div class="sub" style="font-size:30px;margin-top:30px">Google Sheets · your copy lives<br>in your own Drive</div>'
     + shot(HOL + "dash_full.png", "left:232px;top:520px;width:400px;transform:rotate(3deg)")
     + '<div class="cta">Link in bio →</div>', "Estimates only, not financial advice."),
])

C = series("Debt Payoff Planner", [
    ("01-hook",
     '<h1 style="font-size:76px;margin-top:70px">Snowball<br>or avalanche?</h1>'
     '<div class="sub" style="font-size:34px;margin-top:34px">Check the <b class="o">fine print</b> first.<br>It can change the answer →</div>'
     + shot(DPP + "plan_kpi.png", "left:170px;top:560px;width:524px")),
    ("02-trap",
     '<div class="k">MADE-UP EXAMPLE</div>'
     '<h1 style="font-size:54px;margin-top:10px">Least interest on paper<br>≠ <em>cheapest</em></h1>'
     + shot("compare_2", "left:44px;top:300px;width:776px")
     + '<div class="card" style="position:absolute;left:44px;top:530px;width:776px;padding:32px;font-size:28px;line-height:1.5">'
       'Avalanche: 1,598.68 interest. But it clears the store card <b class="r">after its 0% deal ends</b>, so back-interest could be added.<br><br>'
       'Smart: 1,679.15, and the store card is cleared <b class="g">in time</b>.</div>'),
    ("03-skip",
     '<div class="k">WHAT MOST CALCULATORS SKIP</div>'
     '<h1 style="font-size:54px;margin-top:10px">Your loans have<br><em>rules</em></h1>'
     '<div class="card" style="margin-top:40px;padding:36px;font-size:30px;line-height:1.5"><ul>'
     '<li>A fee for paying early</li><li>Locked until a date</li><li>0% deals with deferred interest</li>'
     '<li>Payments you’re already behind on</li><li>“Not sure”: mark it and ask your lender</li></ul></div>'),
    ("04-checks",
     '<div class="k">IT CHECKS YOUR PLAN</div>'
     '<h1 style="font-size:54px;margin-top:10px">Smart order:<br>behind first, then 0%<br>deadlines, then <em>highest APR</em></h1>'
     + shot("checks_l", "left:44px;top:440px;width:776px")),
    ("05-compare",
     '<div class="k">WHAT’S INSIDE</div>'
     '<h1 style="font-size:54px;margin-top:10px">4 orders,<br>side by side</h1>'
     '<div class="card" style="margin-top:36px;padding:34px;font-size:28px;line-height:1.45"><ul>'
     '<li>Smart, Avalanche, Snowball, Cash-flow</li><li>Debt-free month, interest and fees for each</li>'
     '<li>One-time extra payment (bonus, tax refund)</li><li>Room for 12 debts, 30-year schedule</li></ul></div>'
     + shot("sched_top", "left:44px;top:700px;width:776px;height:300px")),
    ("06-cta",
     '<h1 style="font-size:64px;margin-top:70px">Debt Payoff<br><em>Planner</em></h1>'
     '<div class="sub" style="font-size:30px;margin-top:30px">Google Sheets · also works in Excel</div>'
     + shot(DPP + "plan_full.png", "left:212px;top:440px;width:440px;transform:rotate(3deg)")
     + '<div class="cta">Link in bio →</div>', "Estimates only. Your lender’s figures are the final word."),
])

jobs = []
for prefix, items in (("money-series", A), ("holiday", B), ("planner", C)):
    out = os.path.join(HERE, prefix); os.makedirs(out, exist_ok=True)
    for name, html in items:
        src = os.path.join(TMP, f"{prefix}-{name}.html"); open(src, "w").write(html)
        jobs.append([src, os.path.join(out, f"{prefix}-{name}.png")])

js = f"""import {{ chromium }} from '/opt/node22/lib/node_modules/playwright/index.mjs';
const jobs = {json.dumps(jobs)};
const b = await chromium.launch();
for (const [src, out] of jobs) {{
  const p = await b.newPage({{ viewport: {{ width: 864, height: 1080 }}, deviceScaleFactor: 1.25 }});
  await p.goto('file://' + src); await p.waitForLoadState('networkidle');
  const over = await p.evaluate(() => [...document.querySelectorAll('h1,.card,.shot,.sub,.cta')]
    .filter(e => {{ const r = e.getBoundingClientRect(); return r.right > 844 || r.bottom > 1050; }}).map(e => e.className || e.tagName));
  await p.screenshot({{ path: out }}); console.log(out.split('/').pop(), over.length ? 'OVERFLOW ' + over.join(',') : 'OK');
  await p.close();
}}
await b.close();"""
open(os.path.join(TMP, "shoot.mjs"), "w").write(js)
subprocess.run(["node", os.path.join(TMP, "shoot.mjs")], check=True)
