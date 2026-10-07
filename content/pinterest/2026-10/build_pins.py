"""Pinterest pins (1000x1500, 2:3) for CheckMaybe — October 2026.

Two looks, matching each product line: cream (seller toolkits, PDF look) and dark (money tools, sheet look).
Screens are cut from the existing product images (real renders, made-up example rows).
Copy, links, boards and posting order: pins.md. Usage: python3 build_pins.py
"""
import json, os, subprocess
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
P = os.path.abspath(os.path.join(HERE, "..", "..", "..", "products"))
TMP = "/tmp/cm-pins"; os.makedirs(TMP, exist_ok=True)

CUTS = {  # name: (source under products/, crop box in source pixels)
    "bycpl": ("before-you-click-pay-later/images/gumroad/before-you-click-pay-later-gumroad-cover.png", (1380, 100, 2560, 1440)),
    "hct": ("hidden-cost-tracker/images/gumroad/hidden-cost-tracker-gumroad-cover.png", (940, 580, 2460, 1440)),
    "jan": ("holiday-hidden-cost-tracker/images/crops/dash_month.png", (0, 0, 1540, 480)),
    "gifts": ("holiday-hidden-cost-tracker/images/crops/gifts.png", (0, 0, 2600, 1300)),
    "compare": ("debt-payoff-planner/images/crops/plan_compare.png", (0, 0, 1253, 315)),
    "sell": ("can-i-sell-this/images/can-i-sell-this-preview.png", (128, 460, 2432, 1235)),
    "use": ("can-i-use-this/images/can-i-use-this-preview.png", (128, 460, 2432, 1235)),
    "resell": ("can-i-resell-this/images/can-i-resell-this-preview.png", (128, 460, 2432, 1235)),
    "audit": ("free-audit/images/free-audit-cover.png", (1440, 100, 2432, 1240)),
    "bundle": ("bundle/images/bundle-portrait.png", (0, 820, 1024, 1536)),
}
for k, (src, box) in CUTS.items():
    Image.open(os.path.join(P, src)).crop(box).save(os.path.join(TMP, k + ".png"))
img = lambda k, style: f'<div class="shot" style="{style}"><img src="file://{TMP}/{k}.png"></div>'

BASE = """*{box-sizing:border-box;margin:0;padding:0}html,body{width:1000px;height:1500px;overflow:hidden}
body{position:relative;padding:70px 64px}
.shot{position:absolute;overflow:hidden;border-radius:14px}.shot img{display:block;width:100%}
.foot{position:absolute;left:64px;right:64px;bottom:40px;display:flex;justify-content:space-between;font-size:20px;letter-spacing:.12em;text-transform:uppercase}
ol{list-style:none;counter-reset:n}ol li{counter-increment:n;position:relative;padding-left:72px;margin-bottom:22px}
ol li:before{content:counter(n);position:absolute;left:0;top:-4px;width:50px;height:50px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-weight:800;font-size:28px}
"""
DARK = BASE + """body{background:#15171F;background-image:radial-gradient(ellipse at 85% 0%,rgba(240,138,75,.22),transparent 55%);color:#EDEBF5;font-family:"Liberation Sans","DejaVu Sans",sans-serif}
.k{font-size:24px;letter-spacing:.2em;font-weight:700;color:#9A98AE;text-transform:uppercase}.k b{color:#F08A4B}
h1{font-weight:800;line-height:1.04;letter-spacing:-.015em}em{font-style:normal;color:#F08A4B}
.sub{color:#B7B5C8;line-height:1.35}.r{color:#FF6B6B}.g{color:#5FD38D}
.card{background:#1E2130;border:1px solid #33384F;border-radius:20px}
.shot{border:1px solid #33384F;box-shadow:0 24px 70px rgba(0,0,0,.6)}
.tag{display:inline-block;font-weight:800;border-radius:999px;padding:10px 24px;font-size:26px}
.free{background:#5FD38D;color:#15171F}.cta{background:#F08A4B;color:#15171F}
.foot{color:#9A98AE}ol li:before{background:#F08A4B;color:#15171F}
"""
CREAM = BASE + """body{background:#ECE1C4;color:#3B2A1E;font-family:"Bitstream Charter","DejaVu Serif",serif}
.k{font-family:"Liberation Sans",sans-serif;font-size:24px;letter-spacing:.2em;font-weight:700;color:#C25A1C;text-transform:uppercase}
h1{font-weight:700;line-height:1.06;letter-spacing:-.01em}em{font-style:normal;color:#C25A1C}
.rule{width:90px;height:7px;background:#C25A1C;margin:30px 0}
.sub{color:#6B5A45;line-height:1.38}
.card{background:#F8F1DE;border:1.5px solid #C7B287;border-radius:16px}
.shot{border:1.5px solid #C7B287;box-shadow:0 18px 50px rgba(59,42,30,.25);background:#F8F1DE}
.tag{display:inline-block;font-family:"Liberation Sans",sans-serif;font-weight:800;border-radius:999px;padding:10px 24px;font-size:24px;letter-spacing:.06em;text-transform:uppercase}
.free{background:#3F6B3A;color:#fff}.cta{background:#C25A1C;color:#fff}
.pill{display:inline-block;font-family:"Liberation Sans",sans-serif;font-weight:800;color:#fff;border-radius:999px;padding:8px 18px;font-size:20px;margin-right:8px}
.foot{font-family:"Liberation Sans",sans-serif;color:#6B5A45}ol li:before{background:#C25A1C;color:#fff;font-family:"Liberation Sans",sans-serif}
"""

def pin(css, kicker, body, foot):
    return (f'<!doctype html><html><head><meta charset="utf-8"><style>{css}</style></head><body>'
            f'<div class="k">{kicker}</div>{body}<div class="foot"><span>{foot}</span><span>checkmaybe</span></div></body></html>')
D = lambda kicker, body, foot="Made-up example · not financial advice": pin(DARK, kicker, body, foot)
C = lambda kicker, body, foot="Educational resource · not legal advice": pin(CREAM, kicker, body, foot)

PINS = {
    # ---- money tools (dark) ----
    "m1-67-a-month": D("<b>CheckMaybe</b> · Pay later",
        '<h1 style="font-size:104px;margin-top:60px">“Only <em>$67</em><br>a month”</h1>'
        '<div class="sub" style="font-size:40px;margin-top:30px">is about <b class="r">29.8% APR</b><br>on a $1,200 phone.</div>'
        '<div class="card" style="margin-top:60px;padding:46px;font-size:48px;line-height:1.7">$67 × 24 = <b>$1,608</b><br>− price $1,200<br>= <b class="r">$408 extra</b></div>'
        '<div style="margin-top:70px"><span class="tag free">FREE GUIDE</span> <span class="sub" style="font-size:30px;margin-left:12px">5 checks before you click</span></div>'),
    "m2-5-checks": D("<b>CheckMaybe</b> · Free guide",
        '<h1 style="font-size:82px;margin-top:50px">5 checks before<br>you click<br><em>“pay later”</em></h1>'
        '<ol style="margin-top:60px;font-size:38px;line-height:1.3">'
        '<li>What will I pay in total?</li><li>Roughly what yearly rate is that?</li><li>What if I’m late, or don’t finish on time?</li>'
        '<li>When does the first payment leave?</li><li>What else is due that month?</li></ol>'
        '<div style="margin-top:40px"><span class="tag free">FREE · 12-PAGE PDF</span></div>', "Estimates only · not financial advice"),
    "m3-deferred": D("<b>CheckMaybe</b> · Pay later",
        '<h1 style="font-size:96px;margin-top:60px">When “0%”<br>stops being<br><em>0%</em></h1>'
        '<div class="card" style="margin-top:60px;padding:46px;font-size:38px;line-height:1.45">Look for <b>“deferred interest”</b> or <b>“no interest if paid in full”</b>.<br><br>'
        '<span class="sub">If any balance is left when the promo ends, interest can go back to the <b class="r">day you bought it</b>.</span></div>'
        '<div class="sub" style="font-size:26px;margin-top:30px">Source: US CFPB. Read your own agreement.</div>'
        '<div style="margin-top:50px"><span class="tag free">FREE GUIDE</span> <span class="sub" style="font-size:30px;margin-left:12px">Before You Click “Pay Later”</span></div>',
        "Educational · not financial advice"),
    "m4-free-guide": D("<b>CheckMaybe</b> · Free mini guide",
        '<h1 style="font-size:92px;margin-top:50px">Before You Click<br><em>“Pay Later”</em></h1>'
        '<div class="sub" style="font-size:36px;margin-top:26px">5 checks in 5 minutes · one-page summary · fill-in list for all your plans</div>'
        + img("bycpl", "left:120px;top:620px;width:760px;border:none;box-shadow:none")
        + '<div style="position:absolute;left:64px;bottom:110px"><span class="tag free">FREE · 12-PAGE PDF</span></div>'),
    "m5-hct": D("<b>CheckMaybe</b> · Google Sheets",
        '<h1 style="font-size:84px;margin-top:50px">What is this<br>monthly payment<br><em>really costing me?</em></h1>'
        '<div class="sub" style="font-size:34px;margin-top:26px">Real APR on every plan · subscriptions · free-trial cancel-by dates</div>'
        + img("hct", "left:64px;top:690px;width:872px")
        + '<div style="position:absolute;left:64px;bottom:110px"><span class="tag cta">HIDDEN COST TRACKER</span></div>'),
    "m6-subscriptions": D("<b>CheckMaybe</b> · Subscriptions",
        '<h1 style="font-size:92px;margin-top:60px">4 subscriptions<br>you forgot =<br><em>$1,103.76</em> a year</h1>'
        '<div class="sub" style="font-size:36px;margin-top:30px">Tick “Cancel it?” and the sheet adds up the yearly saving.</div>'
        + img("hct", "left:64px;top:760px;width:872px")
        + '<div style="position:absolute;left:64px;bottom:110px"><span class="tag cta">HIDDEN COST TRACKER</span></div>'),
    "h1-january": D("<b>CheckMaybe</b> · Holiday budget",
        '<h1 style="font-size:92px;margin-top:60px">Holiday gifts<br>on pay-in-4?<br><em>January</em> gets the bill.</h1>'
        '<div class="sub" style="font-size:36px;margin-top:30px">Four “small” plans = <b class="r">$428.25</b> due in one month.</div>'
        + img("jan", "left:64px;top:760px;width:872px")
        + '<div style="position:absolute;left:64px;bottom:110px"><span class="tag cta">HOLIDAY HIDDEN COST TRACKER</span></div>'),
    "h2-gift-tracker": D("<b>CheckMaybe</b> · Google Sheets",
        '<h1 style="font-size:84px;margin-top:50px">Christmas gift list<br>+ budget +<br><em>pay-later plans</em></h1>'
        '<div class="sub" style="font-size:34px;margin-top:26px">Budget per person · every due date · real APR · free-trial cancel-by dates</div>'
        + img("gifts", "left:64px;top:700px;width:872px")
        + '<div style="position:absolute;left:64px;bottom:110px"><span class="tag cta">HOLIDAY HIDDEN COST TRACKER</span></div>'),
    "p1-snowball": D("<b>CheckMaybe</b> · Debt payoff",
        '<h1 style="font-size:90px;margin-top:60px">Snowball or<br>avalanche?<br><em>Check the fees first.</em></h1>'
        '<div class="sub" style="font-size:34px;margin-top:30px">Early-payoff fees and 0% deadlines can change which order costs less.</div>'
        + img("compare", "left:64px;top:780px;width:872px")
        + '<div class="card" style="position:absolute;left:64px;top:1030px;width:872px;padding:30px;font-size:30px;line-height:1.4">'
          'Avalanche: least interest on paper, but it clears the store card <b class="r">after its 0% deal ends</b>.</div>'
        + '<div style="position:absolute;left:64px;bottom:110px"><span class="tag cta">DEBT PAYOFF PLANNER</span></div>'),
    # ---- seller toolkits (cream) ----
    "s1-canva": C("CheckMaybe · Can I Sell This?",
        '<h1 style="font-size:86px;margin-top:50px">Made it in Canva.<br>Can you <em>sell</em> it?</h1><div class="rule"></div>'
        '<div class="sub" style="font-size:34px">A printable, a mug, an editable template, a client logo: four different licence situations.</div>'
        '<div style="margin-top:34px"><span class="pill" style="background:#3F6B3A">GREEN-LEANING</span><span class="pill" style="background:#A17A2E">AMBER</span><span class="pill" style="background:#C23C28">RED</span></div>'
        + img("sell", "left:64px;top:820px;width:872px")
        + '<div style="position:absolute;left:64px;bottom:110px"><span class="tag cta">28-page toolkit · official clauses cited</span></div>',
        "Not legal advice · not affiliated with Canva"),
    "s2-ai": C("CheckMaybe · Can I Use This?",
        '<h1 style="font-size:84px;margin-top:50px">Selling something<br>made with <em>AI</em>?</h1><div class="rule"></div>'
        '<div class="sub" style="font-size:34px;margin-bottom:26px">Run the 5 checks first:</div>'
        '<ol style="font-size:36px;line-height:1.2"><li><b>Tool</b>: does your plan allow commercial use?</li><li><b>Output</b>: what rights do you get?</li>'
        '<li><b>Input</b>: what did you upload?</li><li><b>Use</b>: where and how will you sell it?</li><li><b>Verify</b>: what must you disclose?</li></ol>'
        + img("use", "left:64px;top:1050px;width:872px;height:290px"),
        "Not legal advice · independent resource"),
    "s3-resell": C("CheckMaybe · Can I Resell This?",
        '<h1 style="font-size:84px;margin-top:50px">Buying a pack with<br><em>“resell rights”</em>?</h1><div class="rule"></div>'
        '<div class="sub" style="font-size:36px">PLR, MRR, resell rights: the licence text decides, not the label. Check 7 things before you pay, and again before you list.</div>'
        + img("resell", "left:64px;top:800px;width:872px")
        + '<div style="position:absolute;left:64px;bottom:110px"><span class="tag cta">22-page buyer’s checklist</span></div>',
        "Not legal advice · not affiliated with any platform"),
    "s4-audit": C("CheckMaybe · Free checklist",
        '<h1 style="font-size:80px;margin-top:50px">5 questions before<br>you list <em>any</em><br>digital product</h1><div class="rule"></div>'
        '<ol style="font-size:38px;line-height:1.2"><li>What went into it?</li><li>Which licence covers each piece?</li><li>What exactly am I selling?</li>'
        '<li>Where will I sell it?</li><li>What must I disclose?</li></ol>'
        + img("audit", "left:600px;top:1000px;width:330px;transform:rotate(4deg);border:none;box-shadow:none;background:none")
        + '<div style="position:absolute;left:64px;bottom:110px"><span class="tag free">FREE · 6-page PDF</span></div>'),
    "s5-bundle": C("CheckMaybe · Bundle",
        '<h1 style="font-size:84px;margin-top:50px">Can I sell this?<br>Can I use this?<br><em>Can I resell this?</em></h1><div class="rule"></div>'
        '<div class="sub" style="font-size:36px">Canva, AI content and resell rights: 3 PDF toolkits, 82 pages, every answer tied to the official source.</div>'
        + img("bundle", "left:64px;top:840px;width:872px;height:500px;border:none")
        + '<div style="position:absolute;left:64px;bottom:110px"><span class="tag cta">$29 instead of $45</span></div>'),
}

jobs = []
out = os.path.join(HERE, "pins"); os.makedirs(out, exist_ok=True)
for name, html in PINS.items():
    src = os.path.join(TMP, name + ".html"); open(src, "w").write(html)
    jobs.append([src, os.path.join(out, f"checkmaybe-pin-{name}.png")])
js = f"""import {{ chromium }} from '/opt/node22/lib/node_modules/playwright/index.mjs';
const jobs = {json.dumps(jobs)};
const b = await chromium.launch();
for (const [src, o] of jobs) {{
  const p = await b.newPage({{ viewport: {{ width: 1000, height: 1500 }} }});
  await p.goto('file://' + src); await p.waitForLoadState('networkidle');
  const over = await p.evaluate(() => [...document.querySelectorAll('h1,.card,.shot,.sub,ol,.tag')]
    .filter(e => {{ const r = e.getBoundingClientRect(); return r.right > 990 || r.bottom > 1440; }}).map(e => e.className || e.tagName));
  await p.screenshot({{ path: o }}); console.log(o.split('/').pop(), over.length ? 'OVERFLOW ' + over.join(',') : 'OK'); await p.close();
}}
await b.close();"""
open(os.path.join(TMP, "shoot.mjs"), "w").write(js)
subprocess.run(["node", os.path.join(TMP, "shoot.mjs")], check=True)
