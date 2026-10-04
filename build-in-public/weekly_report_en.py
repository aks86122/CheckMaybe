"""CheckMaybe build-in-public weekly report card, English (1080x1440, IG carousel 3:4).

Usage: python3 weekly_report_en.py weeks/2026-W41.json  ->  weeks/2026-W41.png
Every number comes from the JSON; fields left as null render as "—". Never estimate.
"""
import json, os, subprocess, sys
src = os.path.abspath(sys.argv[1]); out = src.rsplit(".", 1)[0] + ".png"
d = json.load(open(src))
def v(x, unit=""):
    if x is None: return "—"
    if isinstance(x, (int, float)): return f"{x:,.0f}{unit}" if float(x).is_integer() else f"{x:,.1f}{unit}"
    return str(x)
pl = None if d.get("income") is None or d.get("spend") is None else d["income"] - d["spend"]
plc = "#7CE38B" if (pl or 0) > 0 else ("#FF8A8A" if (pl or 0) < 0 else "#F08A4B")
tiles = [("Time in", v(d.get("hours"), " h")), ("Spent", v(d.get("spend"), " USD")),
         ("Page views", v(d.get("page_views"))), ("Sales", v(d.get("sales"))),
         ("Free downloads", v(d.get("free_downloads"))), ("Revenue (paid out)", v(d.get("income"), " USD")),
         ("Reel views", v(d.get("views"))), ("New followers", v(d.get("new_followers")))]
T = "".join(f'<div class="t"><div class="k">{k}</div><div class="n">{n}</div></div>' for k, n in tiles)
notes = "".join(f"<li>{x}</li>" for x in d.get("notes", []))
html = f"""<!doctype html><html><head><meta charset="utf-8"><style>
@import url('https://fonts.googleapis.com/css2?family=Inter+Tight:wght@500;700;900&display=swap');
*{{margin:0;padding:0;box-sizing:border-box}}body{{width:720px;height:960px;background:#15171F;color:#fff;font-family:"Inter Tight",system-ui,sans-serif;padding:48px 44px;position:relative}}
.tag{{color:#F08A4B;font-weight:700;letter-spacing:.12em;font-size:18px}}h1{{font-size:44px;font-weight:900;margin-top:10px}}.d{{color:#AEB6C8;font-size:20px;margin-top:6px}}
.pl{{margin-top:26px;background:rgba(255,255,255,.06);border:2px solid #F08A4B;border-radius:22px;padding:18px 26px;display:flex;justify-content:space-between;align-items:center}}
.pl .k{{font-size:22px;color:#AEB6C8}}.pl .n{{font-size:52px;font-weight:900;color:{plc}}}
.g{{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:18px}}.t{{background:rgba(255,255,255,.06);border-radius:16px;padding:14px 18px}}
.t .k{{font-size:17px;color:#AEB6C8}}.t .n{{font-size:30px;font-weight:900;margin-top:2px}}
ul{{margin-top:20px;padding-left:26px;font-size:20px;line-height:1.6;color:#E6E8EF}}
.f{{position:absolute;left:44px;right:44px;bottom:32px;font-size:15px;color:#7F89A3;display:flex;justify-content:space-between}}
</style></head><body><div class="tag">CHECKMAYBE · BUILDING IN PUBLIC</div><h1>{d['title']}</h1><div class="d">{d['period']}</div>
<div class="pl"><div class="k">Net this week<br><span style="font-size:15px">revenue − spend</span></div><div class="n">{v(pl, ' 元')}</div></div>
<div class="g">{T}</div><ul>{notes}</ul><div class="f"><span>Real numbers only. Fees and refunds already deducted.</span><span>Check before you pay.</span></div></body></html>"""
h = out.replace(".png", ".html"); open(h, "w").write(html)
js = f"""import {{ chromium }} from '/opt/node22/lib/node_modules/playwright/index.mjs';
const b=await chromium.launch();const p=await b.newPage({{viewport:{{width:720,height:960}},deviceScaleFactor:1.5}});
await p.goto('file://{h}',{{waitUntil:'networkidle'}});await p.evaluate(()=>document.fonts.ready);await p.screenshot({{path:'{out}'}});await b.close();"""
m = out.replace(".png", ".mjs"); open(m, "w").write(js); subprocess.run(["node", m], check=True)
os.remove(h); os.remove(m); print(out)
