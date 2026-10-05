"""Shared listing-image renderer (Etsy 10 × 4:3, Gumroad cover + thumb, Beacons square).

Each product script passes its palette, crops folder and page bodies. Crops are real renders of the sheet
(LibreOffice PDF at 300 dpi, example rows), so every image shows the actual product.
"""
import json, os, subprocess

CSS = """
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:%(w)dpx;height:%(h)dpx;overflow:hidden}
body{background:%(BG)s;background-image:radial-gradient(ellipse at 85%% 0%%,%(GLOW1)s,transparent 55%%),radial-gradient(ellipse at 0%% 100%%,%(GLOW2)s,transparent 50%%);
 color:%(TXT)s;font-family:"Liberation Sans","DejaVu Sans",Arial,sans-serif;position:relative;padding:%(pad)dpx}
.brand{font-size:%(bs)dpx;letter-spacing:.18em;font-weight:700;color:%(MUTED)s;text-transform:uppercase}
.brand b{color:%(ACC)s}
h1{font-size:%(h1)dpx;line-height:1.08;font-weight:800;margin-top:%(g)dpx;letter-spacing:-.01em}
h1 em{font-style:normal;color:%(ACC)s}
.sub{font-size:%(ss)dpx;color:%(MUTED)s;margin-top:%(g2)dpx;line-height:1.35}
.shot{border-radius:%(r)dpx;overflow:hidden;border:1px solid %(LINE)s;box-shadow:0 18px 50px rgba(0,0,0,.55);background:%(BG)s}
.shot img{display:block;width:100%%}
.win{border-radius:%(r)dpx;overflow:hidden;border:1px solid %(LINE)s;box-shadow:0 22px 60px rgba(0,0,0,.6);background:%(PANEL)s}
.win .bar{height:%(bar)dpx;display:flex;gap:%(dot)dpx;align-items:center;padding:0 %(dot)dpx;background:%(PANEL2)s}
.win .bar i{width:%(dot)dpx;height:%(dot)dpx;border-radius:50%%;background:%(LINE)s;display:block}
.win img{display:block;width:100%%}
.ex{position:absolute;z-index:9;right:%(pad)dpx;bottom:%(exb)dpx;font-size:%(xs)dpx;color:%(MUTED)s;letter-spacing:.06em;background:%(BG)s;padding:.35em .8em;border-radius:999px;border:1px solid %(LINE)s}
.chips{display:flex;flex-wrap:wrap;gap:%(cg)dpx;margin-top:%(g2)dpx}
.chip{font-size:%(cs)dpx;font-weight:700;padding:%(cp)dpx %(cp2)dpx;border-radius:999px;border:1px solid %(LINE)s;background:%(PANEL)s}
.o{color:%(ACC)s}.r{color:%(RED)s}.g{color:%(GREEN)s}.a{color:%(AMBER)s}.b{color:%(BLUE)s}
.card{background:%(PANEL)s;border:1px solid %(LINE)s;border-radius:%(r)dpx;padding:%(cpad)dpx}
.card h3{font-size:%(h3)dpx;margin-bottom:%(g3)dpx}
.card p{font-size:%(ps)dpx;color:%(MUTED)s;line-height:1.4}
.num{font-size:%(h3)dpx;font-weight:800;color:%(BG)s;background:%(ACC)s;width:%(nw)dpx;height:%(nw)dpx;border-radius:50%%;display:flex;align-items:center;justify-content:center;margin-bottom:%(g3)dpx}
ul.inc{list-style:none;font-size:%(ps)dpx;line-height:1.5}
ul.inc li{padding-left:1.3em;position:relative;margin-bottom:.35em}
ul.inc li:before{content:"✓";position:absolute;left:0;color:%(GREEN)s;font-weight:800}
.abs{position:absolute}
"""

class Builder:
    def __init__(self, slug, label, pal, crops, out_dir):
        self.slug, self.label, self.pal, self.crops, self.out = slug, label, pal, os.path.abspath(crops), os.path.abspath(out_dir)
        self.tmp = f"/tmp/{slug}-img"; os.makedirs(self.tmp, exist_ok=True); self.jobs = []

    def s(self, w, h):
        k = w / 1200
        v = dict(pad=56, bs=15, h1=58, g=14, ss=24, g2=14, r=14, bar=26, dot=11, exb=22, xs=13, cg=10, cs=17, cp=8, cp2=16,
                 cpad=26, h3=24, g3=10, ps=19, nw=40)
        d = {key: max(1, round(val * k)) for key, val in v.items()}; d.update(w=w, h=h); d.update(self.pal); return d

    def img(self, name): return f"file://{self.crops}/{name}.png"
    def shot(self, name, style): return f'<div class="shot abs" style="{style}"><img src="{self.img(name)}"></div>'
    def win(self, name, style): return f'<div class="win abs" style="{style}"><div class="bar"><i></i><i></i><i></i></div><img src="{self.img(name)}"></div>'

    def page(self, w, h, body, brand=True, example=True):
        top = f'<div class="brand"><b>CheckMaybe</b> · {self.label} · Google Sheets</div>' if brand else ""
        ex = '<div class="ex">Example data · not financial advice</div>' if example else ""
        return f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS % self.s(w, h)}</style></head><body>{top}{body}{ex}</body></html>'

    def add(self, folder, name, html, w, h, k):
        os.makedirs(os.path.join(self.out, folder), exist_ok=True)
        p = os.path.join(self.tmp, f"{folder}-{name}.html"); open(p, "w").write(html)
        self.jobs.append([p, os.path.join(self.out, folder, f"{self.slug}-{name}.png"), w, h, k])

    def render(self):
        js = f"""
import {{ chromium }} from '/opt/node22/lib/node_modules/playwright/index.mjs';
const jobs = {json.dumps(self.jobs)};
const b = await chromium.launch();
for (const [src, out, w, h, k] of jobs) {{
  const p = await b.newPage({{ viewport: {{ width: w, height: h }}, deviceScaleFactor: k }});
  await p.goto('file://' + src); await p.waitForLoadState('networkidle');
  const over = await p.evaluate(([W, H]) => [...document.querySelectorAll('.abs,h1,.sub,.chips')]
    .filter(e => {{ const r = e.getBoundingClientRect(); return r.right > W - 20 || r.bottom > H - 10; }}).map(e => e.className || e.tagName), [w, h]);
  await p.screenshot({{ path: out }}); console.log(out.split('/').pop(), over.length ? 'OVERFLOW ' + over.join(',') : 'OK');
  await p.close();
}}
await b.close();
"""
        f = os.path.join(self.tmp, "shoot.mjs"); open(f, "w").write(js)
        subprocess.run(["node", f], check=True)
