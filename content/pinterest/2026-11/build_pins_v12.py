"""v12 pins (2026-11-07): Debt Payoff Planner Print tab. Light look (matches the printable), 1000x1500.
Screens are the real Print tab render with the made-up example debts. Copy and links: pins-v12.md.
Usage: python3 build_pins_v12.py
"""
import os, subprocess
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.abspath(os.path.join(HERE, "..", "..", "..", "products", "debt-payoff-planner", "images", "crops", "print_page.png"))
TMP = "/tmp/cm-pins-v12"; os.makedirs(TMP, exist_ok=True)
page = Image.open(SRC); W, H = page.size
page.save(f"{TMP}/full.png")
page.crop((0, int(H * .512), W, H)).save(f"{TMP}/debts.png")       # each-debt section
page.crop((0, 0, W, int(H * .302))).save(f"{TMP}/total.png")          # title + total boxes
img = lambda k, style: f'<div class="shot" style="{style}"><img src="file://{TMP}/{k}.png"></div>'
CSS = """*{box-sizing:border-box;margin:0;padding:0}html,body{width:1000px;height:1500px;overflow:hidden}
body{position:relative;padding:70px 64px;background:#FBF8F3;color:#2E2B36;font-family:"Liberation Sans","DejaVu Sans",sans-serif}
.k{font-size:24px;letter-spacing:.2em;font-weight:700;color:#8C8798;text-transform:uppercase}.k b{color:#6E9B78}
h1{font-weight:800;line-height:1.05;letter-spacing:-.015em}em{font-style:normal;color:#D98C8C}
.sub{color:#5E5A6B;line-height:1.35}
.shot{position:absolute;overflow:hidden;border-radius:14px;background:#fff;border:1px solid #E6E0D6;box-shadow:0 22px 60px rgba(46,43,54,.16)}
.shot img{display:block;width:100%}
.tag{display:inline-block;font-weight:800;border-radius:999px;padding:10px 24px;font-size:26px;background:#6E9B78;color:#fff}
.foot{position:absolute;left:64px;right:64px;bottom:40px;display:flex;justify-content:space-between;font-size:20px;letter-spacing:.12em;text-transform:uppercase;color:#8C8798}
"""
def pin(kicker, body):
    return (f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>'
            f'<div class="k">{kicker}</div>{body}<div class="foot"><span>Made-up example · not financial advice</span><span>checkmaybe</span></div></body></html>')
PINS = {
 "pt1-printable-real-numbers": pin("<b>CheckMaybe</b> · Debt payoff tracker",
    '<h1 style="font-size:78px;margin-top:40px">A printable debt tracker<br>with <em>your real numbers</em></h1>'
    '<div class="sub" style="font-size:32px;margin-top:22px">Built from your own payoff plan in Google Sheets.</div>'
    + img("full", "left:130px;top:410px;width:740px")),
 "pt2-color-a-box": pin("<b>CheckMaybe</b> · Debt payoff coloring page",
    '<h1 style="font-size:84px;margin-top:40px">Color one box<br>for every <em>10% paid off</em></h1>'
    '<div class="sub" style="font-size:32px;margin-top:22px">Each box is a real amount from your plan,<br>with your debts in payoff order.</div>'
    + img("debts", "left:64px;top:560px;width:872px")
    + '<div style="position:absolute;left:64px;top:1290px"><span class="tag">Google Sheets + printable</span></div>'),
 "pt3-debt-free-month": pin("<b>CheckMaybe</b> · Debt-free plan",
    '<h1 style="font-size:84px;margin-top:40px">Know the month<br>you\'ll be <em>debt-free</em></h1>'
    '<div class="sub" style="font-size:32px;margin-top:22px">Every 5% of your total, with the month your plan<br>gets there. Print it and color as you go.</div>'
    + img("total", "left:64px;top:600px;width:872px")
    + '<div style="position:absolute;left:64px;top:1080px;width:872px;font-size:30px;line-height:1.45;color:#5E5A6B">'
      '✓ Snowball, avalanche and 2 more orders compared<br>✓ 0% deadlines and early-payoff fees checked<br>✓ Change your debts and the page updates</div>'),
}
OUT = os.path.join(HERE, "pins"); os.makedirs(OUT, exist_ok=True)
for name, html in PINS.items():
    hp = f"{TMP}/{name}.html"; open(hp, "w").write(html)
    out = os.path.join(OUT, f"checkmaybe-pin-{name}.png")
    subprocess.run(["node", "-e", f"""const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch();const p=await b.newPage({{viewport:{{width:1000,height:1500}}}});await p.goto('file://{hp}');await p.waitForTimeout(400);await p.screenshot({{path:'{out}'}});await b.close();}})();"""], check=True)
    print("saved", out)
