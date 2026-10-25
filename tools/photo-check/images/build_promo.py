"""Square promo image (1080x1080) for the free Photo Check link (Beacons, link blocks). Usage: python3 build_promo.py"""
import os, subprocess, json
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
ART = f"{ROOT}/content/2026-10-comic-01/art/magnify.jpg"
CSS = """@import url('https://fonts.googleapis.com/css2?family=Inter:wght@500;600;800&family=IBM+Plex+Mono:wght@500&display=swap');
*{box-sizing:border-box;margin:0;padding:0}html,body{width:1080px;height:1080px;overflow:hidden}
body{position:relative;background:radial-gradient(ellipse 80% 45% at 60% -10%,#30255c 0%,transparent 75%),#080a11;color:#f3f4fb;font-family:Inter,sans-serif}
.k{position:absolute;left:72px;top:72px;font:500 24px 'IBM Plex Mono',monospace;letter-spacing:.14em;color:#a99dff}
h1{position:absolute;left:72px;top:130px;font-weight:800;font-size:112px;line-height:1.02;letter-spacing:-.04em}
h1 em{font-style:normal;background:linear-gradient(90deg,#c9bcff,#8fa2ff);-webkit-background-clip:text;color:transparent}
.sub{position:absolute;left:72px;top:390px;width:600px;font-size:34px;line-height:1.35;color:#b8bfd3}
.card{position:absolute;left:72px;top:540px;width:600px;background:#11141e;border:1px solid #3a3660;border-radius:24px;padding:30px 32px;box-shadow:0 30px 80px #0008}
.row{display:flex;justify-content:space-between;align-items:center;font-size:27px;padding:14px 0;border-top:1px solid #262a38}.row:first-child{border-top:0}
.c{font-weight:700;font-size:21px;border-radius:999px;padding:7px 14px;white-space:nowrap}.r{background:#39242e;color:#ff8f9d}.g{background:#17352f;color:#65d6b0}.a{background:#382d21;color:#f5c47d}
.pose{position:absolute;right:30px;bottom:150px;width:330px;-webkit-mask-image:radial-gradient(ellipse 50% 50% at center,#000 70%,transparent 100%);mask-image:radial-gradient(ellipse 50% 50% at center,#000 70%,transparent 100%)}
.tag{position:absolute;left:72px;bottom:72px;background:linear-gradient(135deg,#aa95ff,#6755e8);color:#fff;font-weight:800;font-size:28px;border-radius:999px;padding:16px 30px}
.note{position:absolute;right:72px;bottom:86px;font:500 20px 'IBM Plex Mono',monospace;letter-spacing:.06em;color:#9299ad;text-align:right}"""
BODY = f"""<div class="k">CHECKMAYBE · FREE TOOL</div>
<h1>Free<br><em>Photo Check</em></h1>
<div class="sub">See what your listing photo's file reveals before you post it.</div>
<div class="card"><div class="row"><span>AI marker</span><span class="c r">Found</span></div>
<div class="row"><span>Camera data</span><span class="c g">Original</span></div>
<div class="row"><span>Saved location</span><span class="c a">Remove first</span></div></div>
<img class="pose" src="file://{ART}">
<div class="tag">Check a photo</div>
<div class="note">RUNS IN YOUR BROWSER<br>PHOTOS NEVER UPLOADED</div>"""
src = "/tmp/cm-promo.html"; out = f"{HERE}/free-photo-check-1080.png"
open(src, "w").write(f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>{BODY}</body></html>')
js = f"""import {{ chromium }} from '/opt/node22/lib/node_modules/playwright/index.mjs';
const b = await chromium.launch(); const p = await b.newPage({{ viewport: {{ width: 1080, height: 1080 }} }});
await p.goto('file://{src}'); await p.waitForLoadState('networkidle'); await p.evaluate(() => document.fonts.ready);
await p.screenshot({{ path: {json.dumps(out)} }}); await b.close();"""
open("/tmp/cm-promo.mjs", "w").write(js); subprocess.run(["node", "/tmp/cm-promo.mjs"], check=True); print(out)
