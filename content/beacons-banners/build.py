"""Beacons section banners (3:2, 1800x1200) on the founder's Unsplash photos. One photo, one short title, one line.
Photos stay in the scratchpad (Unsplash License: free commercial use, attribution not required). Usage: python3 build.py"""
import json, os, subprocess
U = "/tmp/claude-0/-home-user-Website-Landing-Complete/327d6f94-e741-55c1-861f-29b9141070b9/scratchpad/unsplash/full"
HERE = os.path.dirname(os.path.abspath(__file__)); TMP = "/tmp/cm-banners"; os.makedirs(TMP, exist_ok=True)
CSS = """*{box-sizing:border-box;margin:0;padding:0}html,body{width:900px;height:600px;overflow:hidden}
body{position:relative;color:#fff;font-family:"Liberation Sans","DejaVu Sans",Arial,sans-serif}
.bg{position:absolute;inset:0;background-size:cover}
.ov{position:absolute;inset:0;background:linear-gradient(90deg,rgba(13,14,20,.82) 0%,rgba(13,14,20,.55) 45%,rgba(13,14,20,.05) 80%)}
.txt{position:absolute;left:56px;bottom:64px;right:300px}
.brand{position:absolute;left:56px;top:44px;font-size:15px;letter-spacing:.22em;font-weight:700;color:rgba(255,255,255,.85)}.brand b{color:#F08A4B}
.k{font-size:16px;letter-spacing:.2em;font-weight:700;color:#F08A4B;margin-bottom:12px}
h1{font-size:64px;font-weight:800;line-height:1.05;text-shadow:0 2px 18px rgba(0,0,0,.45)}
p{font-size:23px;color:rgba(255,255,255,.88);margin-top:16px;line-height:1.4}
.bar{width:48px;height:4px;background:#F08A4B;border-radius:2px;margin-bottom:22px}"""
B = [  # name, photo, background-position, kicker, title, line
 ("01-home", "nica-lorber-FTj49uatPMc", "center 60%", "START HERE", "Check the<br>fine print.", "Before you sell, buy or pay later."),
 ("02-free", "emma-swoboda-iFWGdUOAHIA", "center 55%", "FREE", "Start free.", "Two short checklists to try first."),
 ("03-sellers", "kal-luu-8isKycuUkkc", "center 40%", "FOR SELLERS", "Can I sell<br>this?", "Templates, fonts, AI and resell rights."),
 ("04-money", "timo-volz-Ha6n8MNgEbQ", "center", "FOR YOUR MONEY", "What will this<br>really cost?", "Pay later, hidden costs and debt payoff."),
 ("05-about", "jack-brind-eV7WTlVcydg", "right center", "WHO'S BEHIND IT", "Made in<br>Taipei.", "Plain-English checklists by J."),
 ("06-chinese", "markus-winkler-yHbEL72j0jc", "center", "中文", "中文說明", "Traditional Chinese guide to CheckMaybe."),
]
jobs = []
for name, photo, pos, k, h, p in B:
    html = (f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>'
            f'<div class="bg" style="background-image:url(\'file://{U}/{photo}-unsplash.jpg\');background-position:{pos}"></div><div class="ov"></div>'
            f'<div class="brand"><b>CheckMaybe</b></div><div class="txt"><div class="bar"></div><div class="k">{k}</div><h1>{h}</h1><p>{p}</p></div></body></html>')
    src = f"{TMP}/{name}.html"; open(src, "w").write(html); jobs.append([src, os.path.join(HERE, f"banner-{name}.jpg")])
js = f"""import {{ chromium }} from '/opt/node22/lib/node_modules/playwright/index.mjs';
const jobs = {json.dumps(jobs)}; const b = await chromium.launch();
for (const [s, o] of jobs) {{ const p = await b.newPage({{ viewport: {{ width: 900, height: 600 }}, deviceScaleFactor: 2 }});
  await p.goto('file://' + s); await p.waitForLoadState('networkidle'); await p.screenshot({{ path: o, type: 'jpeg', quality: 88 }}); console.log(o.split('/').pop()); await p.close(); }}
await b.close();"""
open(f"{TMP}/s.mjs", "w").write(js); subprocess.run(["node", f"{TMP}/s.mjs"], check=True)
