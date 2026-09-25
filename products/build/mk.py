"""Generate listing images (cover / preview / featured) as HTML, 1280x720."""
import html
import os

E = lambda s: html.escape(s, quote=False)
MK = os.path.abspath("mk")

CSS = """
*{box-sizing:border-box;margin:0;padding:0}
:root{--bg:#ece1c4;--card:#f8f1de;--rule:#c7b287;--ink:#3b2a1e;--muted:#6b5a45;--bar:#2c1f15;--orange:#c25a1c;--gold:#a17a2e;--red:#c23c28;--green:#3f6b3a;--blue:#4a5a6a;
--serif:"Bitstream Charter","DejaVu Serif",serif;--sans:"Liberation Sans","DejaVu Sans",sans-serif}
html,body{width:1280px;height:720px;overflow:hidden;background:var(--bg);color:var(--ink);font-family:var(--serif)}
.frame{position:relative;width:1280px;height:720px;overflow:hidden;padding:56px 64px}
.brand{font-family:var(--sans);font-weight:bold;letter-spacing:.34em;font-size:15px;color:var(--orange)}
.kick{font-family:var(--sans);font-weight:bold;letter-spacing:.22em;font-size:13px;color:var(--muted)}
.foot{position:absolute;left:64px;right:64px;bottom:28px;display:flex;justify-content:space-between;font-family:var(--sans);font-size:12px;letter-spacing:.14em;color:var(--muted);border-top:1px solid var(--rule);padding-top:10px}
.pill{display:inline-flex;align-items:center;gap:8px;font-family:var(--sans);font-weight:bold;font-size:13px;letter-spacing:.08em;color:#fff;padding:7px 14px 7px 8px;border-radius:99px}
.pill i{font-style:normal;width:20px;height:20px;border-radius:50%;background:rgba(255,255,255,.25);display:inline-flex;align-items:center;justify-content:center;font-size:12px}
.g{background:var(--green)}.a{background:var(--gold)}.r{background:var(--red)}.v{background:var(--blue)}
.pg{position:absolute;box-shadow:0 18px 40px rgba(44,31,21,.28),0 2px 6px rgba(44,31,21,.18);border-radius:3px;background:#fff}
/* cover */
.cv-left{position:absolute;left:64px;top:64px;width:660px}
.cv-title{font-size:84px;line-height:1;font-weight:bold;margin-top:18px}
.cv-rule{width:72px;height:6px;background:var(--orange);margin:24px 0 20px}
.cv-sub{font-size:25px;font-weight:bold;line-height:1.2}
.cv-val{font-size:21px;color:var(--muted);margin-top:14px;line-height:1.4;max-width:560px}
.stats{display:flex;gap:12px;margin-top:30px}
.stat{background:var(--card);border:1px solid var(--rule);border-top:5px solid var(--orange);border-radius:6px;padding:12px 16px;font-family:var(--sans);font-weight:bold;font-size:14px;letter-spacing:.06em}
.stat:nth-child(2){border-top-color:var(--gold)}.stat:nth-child(3){border-top-color:var(--green)}
.stat b{display:block;font-family:var(--serif);font-size:26px;color:var(--orange);letter-spacing:0;margin-bottom:2px}
.sigs{display:flex;gap:10px;margin-top:26px}
.blob{position:absolute;right:-140px;top:-120px;width:760px;height:760px;border-radius:50%;background:#e3d3ae}
/* preview */
.pv-head{display:flex;justify-content:space-between;align-items:flex-end}
.pv-title{font-size:48px;font-weight:bold;line-height:1.05;margin-top:10px}
.pv-sub{font-size:19px;color:var(--muted);margin-top:10px;max-width:760px;line-height:1.4}
.pv-row{position:absolute;left:64px;right:64px;top:232px;display:grid;grid-template-columns:repeat(4,1fr);gap:26px}
.pv-item img{width:100%;display:block;border-radius:3px;box-shadow:0 12px 28px rgba(44,31,21,.25),0 2px 5px rgba(44,31,21,.15)}
.pv-cap{margin-top:14px;font-family:var(--sans);font-weight:bold;font-size:13px;letter-spacing:.14em;display:flex;align-items:center;gap:8px}
.pv-cap span{width:24px;height:24px;border-radius:50%;background:var(--orange);color:#fff;display:inline-flex;align-items:center;justify-content:center;font-size:12px;letter-spacing:0}
.pv-row{height:390px}.pv-item{overflow:visible}
/* featured */
.ft-left{position:absolute;left:64px;top:60px;width:520px}
.ft-title{font-size:40px;font-weight:bold;line-height:1.12;margin-top:14px}
.calls{margin-top:28px;display:flex;flex-direction:column;gap:16px}
.call{display:flex;gap:14px;align-items:center;background:var(--card);border:1px solid var(--rule);border-radius:8px;padding:12px 16px}
.num{width:34px;height:34px;border-radius:50%;background:var(--orange);color:#fff;font-family:var(--sans);font-weight:bold;font-size:17px;display:flex;align-items:center;justify-content:center;flex:none}
.call b{display:block;font-size:17px}
.call span{font-size:15px;color:var(--muted);line-height:1.35}
.crop{position:absolute;right:56px;top:52px;width:600px;height:600px;overflow:hidden;border-radius:6px;box-shadow:0 18px 40px rgba(44,31,21,.28),0 2px 6px rgba(44,31,21,.18);background:#fff}
.crop img{position:absolute;left:0;width:600px}
.crop::after{content:"";position:absolute;left:0;right:0;bottom:0;height:70px;background:linear-gradient(rgba(236,225,196,0),rgba(236,225,196,.95))}
.marker{position:absolute;width:34px;height:34px;border-radius:50%;background:var(--orange);color:#fff;font-family:var(--sans);font-weight:bold;font-size:17px;display:flex;align-items:center;justify-content:center;border:3px solid #fff;box-shadow:0 3px 8px rgba(0,0,0,.3)}
"""

SIG = {"g": ("✓", "GREEN-LEANING"), "a": ("!", "AMBER"), "r": ("✕", "RED")}


def pill(c, label=None):
    i, l = SIG[c]
    return f'<span class="pill {c}"><i>{i}</i>{E(label or l)}</span>'


def doc(body):
    return f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body><div class="frame">{body}</div></body></html>'


def img(prod, n):
    return f"file://{MK}/{prod}-p{n:02d}.png"


def cover(p):
    stats = "".join(f'<div class="stat"><b>{E(a)}</b>{E(b)}</div>' for a, b in p["stats"])
    # page stack: two interior pages fanned behind the cover page
    w = 330; h = round(w * 842 / 595)
    stack = (f'<img class="pg" src="{img(p["id"], p["stack"][1])}" style="width:{w}px;left:790px;top:118px;transform:rotate(7deg)">'
             f'<img class="pg" src="{img(p["id"], p["stack"][0])}" style="width:{w}px;left:735px;top:96px;transform:rotate(-5deg)">'
             f'<img class="pg" src="{img(p["id"], 1)}" style="width:{w + 20}px;left:850px;top:70px;transform:rotate(1.5deg)">')
    return doc(f'''<div class="blob"></div>{stack}
<div class="cv-left"><div class="brand">CHECKMAYBE</div><h1 class="cv-title">{E(p["title"])}</h1><div class="cv-rule"></div>
<div class="cv-sub">{E(p["subtitle"])}</div><p class="cv-val">{E(p["value"])}</p>
<div class="stats">{stats}</div>
<div class="sigs">{pill("g")}{pill("a")}{pill("r")}</div></div>
<div class="foot"><span>{E(p["foot"])}</span><span>PDF TOOLKIT · V{E(p["version"])}</span></div>''')


def preview(p):
    items = "".join(f'<div class="pv-item"><img src="{img(p["id"], n)}"><div class="pv-cap"><span>{i + 1}</span>{E(c)}</div></div>'
                    for i, (n, c) in enumerate(p["preview"]))
    return doc(f'''<div class="pv-head"><div><div class="brand">CHECKMAYBE · {E(p["title"].upper())}</div><h1 class="pv-title">{E(p["pv_title"])}</h1>
<p class="pv-sub">{E(p["pv_sub"])}</p></div></div>
<div class="pv-row">{items}</div>
<div class="foot"><span>{E(p["foot"])}</span><span>{E(p["pages"])} PAGES · V{E(p["version"])}</span></div>''')


def featured(p):
    f = p["featured"]
    top, W = f["crop_top"], f.get("width", 600)
    ph = W * 842 / 595
    calls = "".join(f'<div class="call"><div class="num">{i + 1}</div><div><b>{E(t)}</b><span>{E(s)}</span></div></div>'
                    for i, (t, s, _) in enumerate(f["calls"]))
    marks = "".join(f'<div class="marker" style="left:{round(x * W) - 17}px;top:{round((y - top) * ph) - 17}px">{i + 1}</div>'
                    for i, (_, _, (x, y)) in enumerate(f["calls"]))
    return doc(f'''<div class="ft-left"><div class="kick">INSIDE {E(p["title"].upper())}</div><h1 class="ft-title">{E(f["title"])}</h1>
<div class="calls">{calls}</div></div>
<div class="crop" style="width:{W}px"><img src="{img(p["id"], f["page"])}" style="top:{-round(top * ph)}px;width:{W}px">{marks}</div>
<div class="foot"><span>{E(p["foot"])}</span><span>PAGE {f["page"]} OF {E(p["pages"])}</span></div>''')


PRODUCTS = [
    {"id": "canva-v3.1", "slug": "can-i-sell-this", "title": "Can I Sell This?", "subtitle": "A Commercial Use Toolkit for Canva Sellers",
     "value": "Check a Canva-made product against the official license rules before you list it — first-pass signals, not guesses.",
     "stats": [("27", "PAGE PDF"), ("20", "SELLER SCENARIOS"), ("SEP 2026", "SOURCES VERIFIED")],
     "stack": [10, 5], "version": "3.1", "pages": "27",
     "foot": "EDUCATIONAL RESOURCE, NOT LEGAL ADVICE · NOT AFFILIATED WITH CANVA",
     "pv_title": "Look inside the toolkit",
     "pv_sub": "A decision path, a quick map, 20 traffic-light seller scenarios, Etsy checks, a pre-publish checklist and worksheets.",
     "preview": [(4, "DECISION PATH"), (5, "QUICK MAP"), (10, "20 SCENARIOS"), (20, "PRE-PUBLISH CHECKLIST")],
     "featured": {"page": 10, "crop_top": 0.07, "title": "Every scenario gets a signal — and the reason behind it",
                  "calls": [("A traffic-light signal", "GREEN-LEANING, AMBER or RED. A first-pass signal, never a guarantee.", (0.70, 0.176)),
                            ("The reason, with the clause", "Each answer cites the official source, e.g. CLA §5.", (0.045, 0.25)),
                            ("A marketplace check", "Etsy’s own-design rule, built into the checklist.", (0.045, 0.394)),
                            ("What could change it", "The edge cases that flip the answer to AMBER or RED.", (0.045, 0.455))]}},
    {"id": "ai-v1.1", "slug": "can-i-use-this", "title": "Can I Use This?", "subtitle": "AI Content Commercial Use Toolkit",
     "value": "Know what to check before you sell anything you made with AI tools — platform terms, inputs, outputs and marketplace rules.",
     "stats": [("32", "PAGE PDF"), ("5", "AI TOOL SNAPSHOTS"), ("15", "SCENARIOS")],
     "stack": [24, 7], "version": "1.1", "pages": "32",
     "foot": "EDUCATIONAL RESOURCE, NOT LEGAL ADVICE · NOT AFFILIATED WITH ANY AI PROVIDER",
     "pv_title": "Look inside the toolkit",
     "pv_sub": "A quick decision map, AI tool terms snapshots, 15 real-world scenarios, a before-you-sell checklist and worksheets.",
     "preview": [(5, "DECISION MAP"), (7, "AI TOOL SNAPSHOTS"), (24, "15 SCENARIOS"), (28, "BEFORE-YOU-SELL CHECKLIST")],
     "featured": {"page": 24, "crop_top": 0.045, "width": 520, "title": "Some answers are a clear no — and the toolkit says so",
                  "calls": [("A clear signal", "Selling AI prompt bundles: NOT ALLOWED ON ETSY.", (0.645, 0.14)),
                            ("Grounded in the official rule", "Etsy’s Creativity Standards, quoted and cited.", (0.486, 0.525)),
                            ("The same five checks", "Platform, input, output, third-party rights and intended use.", (0.045, 0.44)),
                            ("Concrete next steps", "What to do before you publish, in plain language.", (0.045, 0.745))]}},
]

if __name__ == "__main__":
    os.makedirs("img", exist_ok=True)
    for p in PRODUCTS:
        for kind, fn in (("cover", cover), ("preview", preview), ("featured", featured)):
            open(f"img/{p['slug']}-{kind}.html", "w").write(fn(p))
    print("ok")
