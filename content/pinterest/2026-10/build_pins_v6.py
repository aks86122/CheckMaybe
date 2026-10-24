"""Pinterest pins v6 (1000x1500, 2:3): Etsy's October 2026 AI rules, 5 pain points -> Can I Use This? v1.2.

Wording from Etsy's official pages (pasted by the founder 2026-10-24): "Important updates to AI use on Etsy",
"What's Etsy's Stance on AI Creations?", "Listing Image Requirements" (all 22 Oct 2026). No numbers.
Copy, links and dates: pins.md, section v6. Usage: python3 content/pinterest/2026-10/build_pins_v6.py
"""
import json, os, subprocess
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
P = f"{ROOT}/products"
ART = f"{ROOT}/content/2026-10-comic-02/art"
ART3 = f"{ROOT}/content/2026-10-comic-03/art"
TMP = "/tmp/cm-pins-v6"
ART2 = f"{ROOT}/content/2026-10-comic-02/art"
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

def rows(items, top):
    tr = "".join(f'<tr><td>{a}</td><td style="text-align:right">{b}</td></tr>' for a, b in items)
    return f'<div class="mini" style="top:{top}px;width:620px"><table style="font-size:27px">{tr}</table></div>'

V = lambda t, c: f'<span class="v {c}" style="font-size:21px;white-space:nowrap">{t}</span>'
TAG = '<span class="tag cta">CAN I USE THIS? · AI TOOLKIT</span>'
FOOT = "Etsy policy summary · not legal advice"
POSE = "right:0px;top:1010px;width:300px"
PINS = {
    "et1-ai-patterns-recipes": pin("Etsy · AI rules, Oct 2026", '<span style="font-size:84px">AI-written patterns<br>and recipes are</span><br><em style="font-size:96px">out on Etsy.</em>',
        "Since 22 Oct 2026, Etsy doesn’t allow <i>AI&#8209;generated</i> patterns, recipes, project plans, manuals or <i>how&#8209;to e&#8209;books</i>. The instructions must be your own work.", 560,
        rows([("AI-written crochet pattern", V("Not allowed", "b")), ("AI-written recipe", V("Not allowed", "b")),
              ("Your own tested pattern", V("Show a real result", "y"))], 940),
        f"{ART1}/happy.jpg", POSE, TAG, foot=FOOT),
    "et2-disclose-ai": pin("Etsy · AI rules, Oct 2026", '<span style="font-size:96px">Made it with AI?</span><br><em style="font-size:84px">Say so in the description.</em>',
        "Etsy still allows items made with AI when you play a <i>clear creative role</i>. You must <i>disclose</i> AI use in the listing description and can’t call AI work handmade.", 560,
        rows([("Your own prompts and curation", V("Allowed", "g")), ("Item created with AI", V("Disclose it", "y")),
              ("AI work sold as handmade", V("Not allowed", "b"))], 940),
        f"{ART2}/check.jpg", POSE, TAG, foot=FOOT),
    "et3-digital-preview": pin("Etsy · Listing images, Oct 2026", '<span style="font-size:92px">Selling a<br>digital download?</span><br><em style="font-size:88px">Show what’s inside.</em>',
        "Etsy’s image rules: digital downloads should include a <i>visual preview or excerpt</i> of what buyers receive. Only items with nothing visual, like audio, can use representative images.", 620,
        rows([("Planner PDF", V("Real page preview", "y")), ("Printable wall art", V("Real file preview", "y")),
              ("Audio file", V("Representative image OK", "g"))], 1000),
        f"{ART2}/happy.jpg", "right:0px;top:1050px;width:280px", TAG, foot=FOOT),
    "et4-prompt-bundles": pin("Etsy · AI rules, Oct 2026", '<span style="font-size:96px">Prompt bundles</span><br><em style="font-size:88px">can’t be sold on Etsy.</em>',
        "Etsy prohibits selling <i>AI prompt bundles</i> on their own: prompts belong with the finished artwork. <i>Bot&#8209;generated</i> listings aren’t allowed either.", 560,
        rows([("Prompt bundle on its own", V("Not allowed", "b")), ("Bot-generated listings", V("Not allowed", "b")),
              ("AI art from your own prompts", V("Allowed, disclose", "y"))], 940),
        f"{ROOT}/content/2026-10-comic-03/art/check.jpg", POSE, TAG, foot=FOOT),
    "et5-one-unedited-photo": pin("Etsy · Listing images, Oct 2026", '<span style="font-size:84px">Edited every photo<br>with AI?</span><br><em style="font-size:84px">Keep one that isn’t.</em>',
        "Most Etsy listings now need <i>one unedited photo</i> of the actual item on a real background. If the item arrives materially different, <i>you may pay the refund</i>.", 620,
        rows([("One unedited photo", V("Required", "y")), ("New background on other photos", V("OK if accurate", "g")),
              ("Hiding flaws or damage", V("Not allowed", "b"))], 1000),
        f"{ROOT}/content/2026-10-comic-03/art/happy.jpg", "right:0px;top:1050px;width:280px", TAG, foot=FOOT),
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
