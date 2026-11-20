"""v15 pins (2026-11-20): first Amazon Associates pin (budget binder), dark and light versions, 1000x1500.

No Amazon product photos (Associates rules): own illustration, receipt mascot and text only.
Product named on the pin comes from its Amazon listing title only (SKYDUE Budget Binder: zipper envelopes,
cash envelopes, expense budget sheets). Checklist items are general buying tips, not product claims.
Usage: python3 content/pinterest/2026-11/build_pins_v15_amazon.py
"""
import json, os, subprocess, tempfile
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
ART = f"{ROOT}/content/2026-10-comic-02/art/check.jpg"
TMP = tempfile.mkdtemp(prefix="cm-pins-v15-")
OUT = f"{HERE}/pins"; os.makedirs(OUT, exist_ok=True)

# Mascot cut-out for the light version: key out the dark background connected to the edges.
im = Image.open(ART).convert("RGB")
key = im.copy()
from PIL import ImageDraw
for xy in [(0, 0), (im.width - 1, 0), (0, im.height - 1), (im.width - 1, im.height - 1)]:
    ImageDraw.floodfill(key, xy, (255, 0, 255), thresh=70)
rgba = im.convert("RGBA")
px, kp = rgba.load(), key.load()
for y in range(im.height):
    for x in range(im.width):
        if kp[x, y] == (255, 0, 255):
            px[x, y] = (0, 0, 0, 0)
rgba.save(f"{TMP}/mascot.png")

THEMES = {
    "dark": dict(bg="#15171F", ink="#EDEBF5", sub="#B9B7C9", muted="#9A98AC", card="#1C1E28", line="#33384F",
                 accent="#F08A4B", hl="#F7C948", check="#74D39A", tag_bg="#F08A4B", tag_ink="#15171F",
                 env=["#F08A4B", "#F7C948", "#74D39A", "#8FA7F0"], binder="#2A2D3A",
                 mascot=f"file://{ART}", mask=True),
    "light": dict(bg="#FBF8F3", ink="#2E2B36", sub="#5E5A6B", muted="#8C8798", card="#FFFFFF", line="#E6E0D6",
                  accent="#D9785B", hl="#C98A2E", check="#6E9B78", tag_bg="#6E9B78", tag_ink="#FFFFFF",
                  env=["#F2B8A2", "#F5D98B", "#B9D4B5", "#BFCBEF"], binder="#E9E1D4",
                  mascot=f"file://{TMP}/mascot.png", mask=False),
}


def page(t):
    mask = ("-webkit-mask-image:radial-gradient(ellipse 50% 50% at center,#000 70%,transparent 100%);"
            "mask-image:radial-gradient(ellipse 50% 50% at center,#000 70%,transparent 100%);") if t["mask"] else ""
    css = f"""*{{box-sizing:border-box;margin:0;padding:0}}html,body{{width:1000px;height:1500px;overflow:hidden}}
body{{position:relative;background:{t['bg']};color:{t['ink']};font-family:Inter,"Liberation Sans",sans-serif}}
.k{{position:absolute;left:64px;top:64px;font-size:24px;letter-spacing:.18em;font-weight:600;color:{t['muted']};text-transform:uppercase}}.k b{{color:{t['accent']}}}
h1{{position:absolute;left:64px;right:64px;top:118px;font-size:72px;font-weight:800;line-height:1.06}}h1 em{{font-style:normal;color:{t['accent']}}}
.binder{{position:absolute;left:64px;top:330px;width:520px;height:330px;border-radius:28px;background:{t['binder']};border:3px solid {t['line']}}}
.ring{{position:absolute;left:22px;width:26px;height:26px;border-radius:50%;border:5px solid {t['muted']}}}
.env{{position:absolute;left:80px;width:410px;height:120px;border-radius:16px;padding:16px 24px;font-size:30px;font-weight:800;color:#2E2B36;box-shadow:0 10px 24px rgba(0,0,0,.18)}}
.zip{{position:absolute;left:24px;right:24px;bottom:22px;height:8px;border-radius:4px;background:repeating-linear-gradient(90deg,rgba(46,43,54,.55) 0 8px,transparent 8px 14px)}}
.amt{{position:absolute;right:24px;top:16px;font-size:26px;font-weight:600;opacity:.75}}
.pose{{position:absolute;right:40px;top:320px;width:330px;{mask}}}
.card{{position:absolute;left:64px;right:64px;top:720px;background:{t['card']};border:2px solid {t['line']};border-radius:26px;padding:26px 40px;box-shadow:0 20px 60px rgba(0,0,0,.18)}}
.lab{{font-size:22px;font-weight:800;letter-spacing:.2em;color:{t['hl']};margin-bottom:6px}}
.row{{display:flex;gap:22px;align-items:flex-start;padding:14px 0;border-top:1px solid {t['line']}}}.row:nth-child(2){{border-top:0}}
.c{{flex:none;width:44px;height:44px;border-radius:50%;background:{t['check']};color:#fff;font-size:28px;font-weight:800;display:flex;align-items:center;justify-content:center}}
.q{{font-size:34px;font-weight:800}}.s{{font-size:24px;color:{t['sub']};margin-top:4px}}
.pick{{position:absolute;left:64px;right:64px;top:1230px;font-size:26px;color:{t['sub']};line-height:1.4}}.pick b{{color:{t['ink']}}}
.tag{{display:inline-block;margin-top:14px;font-weight:800;border-radius:999px;padding:10px 24px;font-size:24px;background:{t['tag_bg']};color:{t['tag_ink']}}}
.foot{{position:absolute;left:64px;right:64px;bottom:34px;display:flex;justify-content:space-between;font-size:17px;letter-spacing:.06em;color:{t['muted']}}}"""
    envs = [("Groceries", "$400"), ("Gas", "$160"), ("Fun money", "$80")]
    env_html = "".join(
        f'<div class="env" style="top:{40 + i * 90}px;background:{t["env"][i]}">{n}<span class="amt">{a}</span><div class="zip"></div></div>'
        for i, (n, a) in enumerate(envs))
    rings = "".join(f'<div class="ring" style="top:{60 + i * 90}px"></div>' for i in range(3))
    rows = [("Zipper envelopes", "Coins and bills stay put"),
            ("Expense sheets", "Write down what you spend from each one"),
            ("One envelope per category", "Groceries, gas, fun money: decide before you spend"),
            ("Small enough to carry", "If it stays home, you'll pay by card instead")]
    rows_html = "".join(f'<div class="row"><div class="c">✓</div><div><div class="q">{q}</div><div class="s">{s}</div></div></div>' for q, s in rows)
    body = (f'<div class="k"><b>CheckMaybe</b> · Cash stuffing</div>'
            f'<h1>Starting cash stuffing?<br><em>What your binder needs</em></h1>'
            f'<div class="binder">{rings}{env_html}</div>'
            f'<img class="pose" src="{t["mascot"]}">'
            f'<div class="card"><div class="lab">CHECK BEFORE YOU BUY</div>{rows_html}</div>'
            f'<div class="pick">One that has the first two: <b>SKYDUE Budget Binder</b> (zipper envelopes, cash envelopes, expense sheets)<br><span class="tag">See it on Amazon</span></div>'
            f'<div class="foot"><span>As an Amazon Associate I earn from qualifying purchases. Example amounts.</span><span>checkmaybe</span></div>')
    return f'<!doctype html><html><head><meta charset="utf-8"><style>{css}</style></head><body>{body}</body></html>'


jobs = []
for name, t in THEMES.items():
    src = f"{TMP}/az1-{name}.html"
    open(src, "w").write(page(t))
    jobs.append([src, f"{OUT}/checkmaybe-pin-az1-budget-binder-{name}.png"])
js = f"""import {{ chromium }} from '/opt/node22/lib/node_modules/playwright/index.mjs';
const jobs = {json.dumps(jobs)}; const b = await chromium.launch();
for (const [s, o] of jobs) {{ const p = await b.newPage({{ viewport: {{ width: 1000, height: 1500 }} }});
  await p.goto('file://' + s); await p.evaluate(() => document.fonts.ready); await p.screenshot({{ path: o }}); console.log(o.split('/').pop()); await p.close(); }}
await b.close();"""
open(f"{TMP}/shoot.mjs", "w").write(js)
subprocess.run(["node", f"{TMP}/shoot.mjs"], check=True)
