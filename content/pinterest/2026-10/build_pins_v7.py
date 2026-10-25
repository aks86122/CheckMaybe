"""Pinterest pins v7 (1000x1500, 2:3): free Photo Check tool (checkmaybe-photo-check.pages.dev).

Facts from our own tests (tools/photo-check/README.md). Copy and links: pins.md, section v7. Usage: python3 content/pinterest/2026-10/build_pins_v7.py
"""
import json, os, subprocess
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
P = f"{ROOT}/products"
ART = f"{ROOT}/content/2026-10-comic-02/art"
ART3 = f"{ROOT}/content/2026-10-comic-03/art"
TMP = "/tmp/cm-pins-v7"
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

POSE = "right:0px;top:1010px;width:300px"
V = lambda t, c: f'<span class="v {c}" style="font-size:21px;white-space:nowrap">{t}</span>'
TAG = '<span class="tag free">FREE TOOL · PHOTO CHECK</span>'
FOOT = "Runs in your browser · photos never uploaded"
PINS = {
    "pc1-ai-marker-in-file": pin("Free tool · Photo Check", '<span style="font-size:88px">Your image file<br>may already say</span><br><em style="font-size:110px">“made with AI.”</em>',
        "Many AI tools write a <i>hidden marker</i> into the file, and Instagram and Facebook read it. Check what your file says <i>before you post or list it</i>.", 600,
        rows([("Image saved from ChatGPT", V("AI marker found", "b")), ("Photo from your camera roll", V("Camera data", "g")),
              ("Photo saved from a chat app", V("Data removed", "y"))], 960),
        f"{ART1}/magnify.jpg", POSE, TAG, foot=FOOT),
    "pc2-location-in-photo": pin("Free tool · Photo Check", '<span style="font-size:96px">Posting a photo<br>of your item?</span><br><em style="font-size:84px">Check what the file<br>gives away.</em>',
        "A phone photo can carry <i>where it was taken</i>, the camera, the date and the <i>editing app</i>. Anyone who downloads the original file can read them.", 690,
        rows([("Saved location", V("Remove before posting", "b")), ("Editing app named", V("Check first", "y")),
              ("Camera data only", V("Fine for most listings", "g"))], 1040),
        f"{ART1}/shock.jpg", "right:0px;top:1080px;width:260px", TAG, foot=FOOT),
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
