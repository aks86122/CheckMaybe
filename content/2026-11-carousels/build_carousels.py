"""Instagram carousels for the November pins and FB posts (1080x1350). Same look as content/2026-10-money-series.

deal-*  : "Is that Black Friday deal real?" (s3, pin bf3) -> Holiday Hidden Cost Tracker
print-* : Debt Payoff Planner Print tab (s4, pins pt1-pt3) -> Debt Payoff Planner

Numbers (made-up examples, from the s3/s4 posts and the sheets):
  headphones $199 vs usual $249 = 20.1% below usual; air fryer $89 vs usual $89 = no deal;
  robot vacuum $159 + 8% tax + $15 shipping = $186.72; TV $499 -> $538.92 at checkout (8% tax),
  12 x $49 = $588, $49.08 more, $50 discount.
  Print tab: example plan 19,150 to clear, 5 debts, debt-free Dec 2028; store card 0% ends, clear by May 2027.
Usage: python3 build_carousels.py
"""
import json, os, subprocess
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
PROD = os.path.abspath(os.path.join(HERE, "..", "..", "products"))
TMP = "/tmp/nov-carousels"; os.makedirs(TMP, exist_ok=True)
PRINT = os.path.join(PROD, "debt-payoff-planner/images/crops/print_page.png")
CUTS = {
    "print_top": (PRINT, (0, 0, 1173, 445)),
    "print_store": (PRINT, (0, 960, 1173, 1085)),
    "print_debts": (PRINT, (0, 780, 1173, 1518)),
    "print_why": (PRINT, (0, 470, 1173, 740)),
}
for k, (src, box) in CUTS.items():
    Image.open(src).crop(box).save(os.path.join(TMP, k + ".png"))
crop = lambda k: f"file://{TMP}/{k}.png" if k in CUTS else f"file://{k}"

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
.shot{position:absolute;border-radius:12px;overflow:hidden;box-shadow:0 20px 60px rgba(0,0,0,.6);border:1px solid #33384F;background:#fff}
.shot img{display:block;width:100%}
ul{list-style:none}li{padding-left:1.3em;position:relative;margin-bottom:.45em}
li:before{content:"✓";position:absolute;left:0;color:#5FD38D;font-weight:800}
.r{color:#FF6B6B}.g{color:#5FD38D}.o{color:#F08A4B}
.row{display:flex;justify-content:space-between}
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

DEAL = series("Black Friday · Deal check", [
    ("01-hook",
     '<h1 style="font-size:100px;margin-top:190px">Is that<br>Black Friday<br><em>deal</em> real?</h1>'
     '<div class="sub" style="font-size:40px;margin-top:60px">Three numbers tell you.<br>Takes two minutes →</div>'),
    ("02-usual",
     '<div class="k">NUMBER 1 · THE USUAL PRICE</div>'
     '<h1 style="font-size:54px;margin-top:10px">Compare with what it<br>normally sells for,<br>not the <em>crossed-out</em> price</h1>'
     '<div class="card" style="margin-top:80px;padding:44px;font-size:38px;line-height:1.8">'
     '<div class="row"><span>Headphones $199</span><span>usual $249</span></div><div class="g" style="font-weight:800">20.1% below usual: real deal</div>'
     '<div style="height:20px"></div>'
     '<div class="row"><span>Air fryer $89</span><span>usual $89</span></div><div class="r" style="font-weight:800">Not a deal, whatever the banner says</div></div>'),
    ("03-checkout",
     '<div class="k">NUMBER 2 · THE CHECKOUT PRICE</div>'
     '<h1 style="font-size:56px;margin-top:10px">Tax and shipping<br>come <em>after</em> you decide</h1>'
     '<div class="card" style="margin-top:80px;padding:48px;font-size:44px;line-height:1.8">'
     'Robot vacuum <b>$159</b><br>+ 8% tax + $15 shipping<br>= <b class="o">$186.72</b> at checkout</div>'
     '<div class="sub" style="font-size:34px;margin-top:50px">Still maybe a good price. But that’s the number to compare.</div>'),
    ("04-plan",
     '<div class="k">NUMBER 3 · THE PLAN TOTAL</div>'
     '<h1 style="font-size:56px;margin-top:10px">A deal on a plan<br>can <em>cost more</em></h1>'
     '<div class="card" style="margin-top:80px;padding:48px;font-size:42px;line-height:1.8">'
     'TV <b>$499</b> → <b>$538.92</b> at checkout<br>12 × $49 = <b>$588</b><br>'
     '<span class="r" style="font-weight:800">$49.08 more</span> for the same TV</div>'
     '<div class="sub" style="font-size:34px;margin-top:50px">That eats most of the $50 discount.</div>'),
    ("05-fourth",
     '<div class="k">THE CHECK THAT SAVES THE MOST</div>'
     '<h1 style="font-size:84px;margin-top:170px">Did you want it<br><em>before</em> the sale<br>started?</h1>'
     '<div class="sub" style="font-size:40px;margin-top:60px">If not, the cheapest version<br>is not buying it.</div>'),
    ("06-cta",
     '<h1 style="font-size:60px;margin-top:70px">Check your<br>whole list in<br><em>one sheet</em></h1>'
     '<div class="card" style="margin-top:44px;padding:34px;font-size:28px;line-height:1.45"><ul>'
     '<li>Deal Check tab: real deal, small deal, or not a deal</li><li>Plan total vs paying in full</li>'
     '<li>Gift budget per person</li><li>Your January payments in one number</li></ul></div>'
     '<div class="sub" style="font-size:26px;margin-top:26px">Holiday Hidden Cost Tracker · Google Sheets</div>'
     '<div class="cta">Link in bio →</div>', "Made-up example. Estimates only, not financial advice."),
])

PRINT_S = series("Debt Payoff Planner · Print", [
    ("01-hook",
     '<h1 style="font-size:70px;margin-top:60px">Most debt<br>printables give<br>every box <em>$100</em></h1>'
     '<div class="sub" style="font-size:32px;margin-top:34px">Your debts don’t work like that →</div>'
     + shot("print_top", "left:44px;top:560px;width:776px")),
    ("02-real",
     '<div class="k">MADE-UP EXAMPLE</div>'
     '<h1 style="font-size:54px;margin-top:10px">Every box is a<br><em>real amount</em> from<br>your own plan</h1>'
     + shot("print_debts", "left:94px;top:340px;width:676px")),
    ("03-month",
     '<div class="k">THE TOP OF THE PAGE</div>'
     '<h1 style="font-size:54px;margin-top:10px">See the <em>month</em> you’ll<br>reach every 5%</h1>'
     + shot("print_top", "left:44px;top:330px;width:776px")
     + '<div class="sub" style="position:absolute;left:44px;top:660px;width:776px;font-size:28px">'
       'Color one box each time you get there. Change a number in your plan and the page updates.</div>'),
    ("04-deadline",
     '<div class="k">WHY THE ORDER MATTERS</div>'
     '<h1 style="font-size:54px;margin-top:10px">A 0% deal that ends<br>can <em>flip</em> the order</h1>'
     + shot("print_store", "left:44px;top:340px;width:776px")
     + '<div class="card" style="position:absolute;left:44px;top:520px;width:776px;padding:32px;font-size:28px;line-height:1.5">'
       'Deferred interest: if any promo balance is left when the deal ends, interest can go back to the day you bought it. '
       'The plan puts this card <b class="g">before</b> its deadline.</div>'),
    ("05-why",
     '<div class="k">ROOM TO WRITE</div>'
     '<h1 style="font-size:56px;margin-top:10px">Your why, and how<br>you’ll <em>celebrate</em></h1>'
     + shot("print_why", "left:44px;top:340px;width:776px")
     + '<div class="sub" style="position:absolute;left:44px;top:620px;width:776px;font-size:28px">'
       'Print it, put it on the fridge, and color a box when you pay.</div>'),
    ("06-cta",
     '<h1 style="font-size:64px;margin-top:70px">Debt Payoff<br><em>Planner</em></h1>'
     '<div class="card" style="margin-top:40px;padding:34px;font-size:28px;line-height:1.45"><ul>'
     '<li>4 payoff orders side by side</li><li>Checks 0% deadlines and early-payoff fees</li>'
     '<li>One-page printable from your own numbers</li></ul></div>'
     '<div class="sub" style="font-size:26px;margin-top:26px">Google Sheets · also works in Excel</div>'
     '<div class="cta">Link in bio →</div>', "Estimates only. Your lender’s figures are the final word."),
])

jobs = []
for prefix, items in (("deal", DEAL), ("print", PRINT_S)):
    out = os.path.join(HERE, prefix); os.makedirs(out, exist_ok=True)
    for name, html in items:
        src = os.path.join(TMP, f"{prefix}-{name}.html"); open(src, "w").write(html)
        jobs.append([src, os.path.join(out, f"{prefix}-{name}.png")])

js = f"""const {{ chromium }} = require('playwright');
const jobs = {json.dumps(jobs)};
(async () => {{
const b = await chromium.launch();
for (const [src, out] of jobs) {{
  const p = await b.newPage({{ viewport: {{ width: 864, height: 1080 }}, deviceScaleFactor: 1.25 }});
  await p.goto('file://' + src); await p.waitForLoadState('networkidle');
  const over = await p.evaluate(() => [...document.querySelectorAll('h1,.card,.shot,.sub,.cta')]
    .filter(e => {{ const r = e.getBoundingClientRect(); return r.right > 844 || r.bottom > 1050; }}).map(e => e.className || e.tagName));
  await p.screenshot({{ path: out }}); console.log(out.split('/').pop(), over.length ? 'OVERFLOW ' + over.join(',') : 'OK');
  await p.close();
}}
await b.close();
}})();"""
open(os.path.join(TMP, "shoot.cjs"), "w").write(js)
subprocess.run(["node", os.path.join(TMP, "shoot.cjs")], check=True)
