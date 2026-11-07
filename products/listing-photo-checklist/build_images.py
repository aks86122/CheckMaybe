"""Gumroad cover (1280x720 at 2x) and square thumbnail (1200x1200) for the free Listing Photo Checklist.
Reuses products/build/mk.py styles and page renders. Usage: python3 build_images.py"""
import os, sys, subprocess, json
HERE = os.path.dirname(os.path.abspath(__file__)); B = os.path.join(HERE, "..", "build")
sys.path.insert(0, B); os.chdir(B)
import pymupdf, mk
os.makedirs("mk", exist_ok=True)
d = pymupdf.open(os.path.join(HERE, "Listing-Photo-Checklist.pdf"))
for i, p in enumerate(d): p.get_pixmap(dpi=160).save(f"mk/photo-v1.0-p{i + 1:02d}.png")
P = {"id": "photo-v1.0", "title": "Listing Photo Checklist", "subtitle": "5 checks before you post a product photo",
     "value": "What your photo file tells marketplaces, platforms and buyers, and what to fix before you list. Free, with a free photo check tool.",
     "stats": [("FREE", "PDF"), ("5", "CHECKS"), ("1", "FREE TOOL")], "stack": [3, 2], "version": "1.0",
     "foot": "FREE EDUCATIONAL RESOURCE, NOT LEGAL ADVICE · NOT AFFILIATED WITH ETSY OR META"}
cover = mk.cover(P).replace('<div class="sigs"><span class="pill g">', '<div class="sigs" style="display:none"><span class="pill g">').replace("PDF TOOLKIT · V1.0", "FREE PDF · V1.0").replace('<h1 class="cv-title">', '<h1 class="cv-title" style="font-size:70px">')
w = 440
thumb = mk.doc(f'''<div class="blob" style="right:-260px;top:-200px"></div>
<img class="pg" src="{mk.img("photo-v1.0", 2)}" style="width:{w}px;left:700px;top:330px;transform:rotate(6deg)">
<img class="pg" src="{mk.img("photo-v1.0", 1)}" style="width:{w + 20}px;left:620px;top:280px;transform:rotate(-2deg)">
<div style="position:absolute;left:64px;top:80px;width:540px"><div class="brand">CHECKMAYBE · FREE</div>
<h1 class="cv-title" style="font-size:84px">Listing Photo Checklist</h1><div class="cv-rule"></div>
<div class="cv-sub" style="font-size:32px">5 checks before you post a product photo</div>
<div class="stats" style="margin-top:40px"><div class="stat"><b>FREE</b>PDF</div><div class="stat"><b>5</b>CHECKS</div></div></div>''').replace("width:1280px;height:720px", "width:1200px;height:1200px")
os.makedirs(os.path.join(HERE, "images"), exist_ok=True)
jobs = []
for name, html, W, H, s in [("listing-photo-checklist-gumroad-cover", cover, 1280, 720, 2), ("listing-photo-checklist-gumroad-thumb", thumb, 1200, 1200, 1)]:
    src = os.path.abspath(f"img/{name}.html"); os.makedirs("img", exist_ok=True); open(src, "w").write(html)
    jobs.append([src, os.path.join(HERE, "images", name + ".png"), W, H, s])
js = f"""import {{ chromium }} from '/opt/node22/lib/node_modules/playwright/index.mjs';
const b = await chromium.launch();
for (const [s, o, w, h, k] of {json.dumps(jobs)}) {{ const p = await b.newPage({{ viewport: {{ width: w, height: h }}, deviceScaleFactor: k }});
  await p.goto('file://' + s); await p.waitForLoadState('networkidle'); await p.screenshot({{ path: o }}); await p.close(); console.log(o.split('/').pop()); }}
await b.close();"""
open("/tmp/lpc-shot.mjs", "w").write(js); subprocess.run(["node", "/tmp/lpc-shot.mjs"], check=True)
