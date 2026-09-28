"""Bundle listing images: cover 1280x720, portrait 512x768, Gumroad thumb 600x600 (all exported at 2x by bundle.mjs)."""
import os
from mk import CSS, E, img, pill

PAGES = 28 + 32 + 22          # Can I Sell This? v3.2 + Can I Use This? v1.1 + Can I Resell This? v1.0
FOOT = "EDUCATIONAL RESOURCE, NOT LEGAL ADVICE · NOT AFFILIATED WITH ANY PLATFORM NAMED"
TITLES = "Can I Sell This?<br>Can I Use This?<br>Can I Resell This?"
C_SELL, C_USE, C_RES = img("canva-v3.2", 1), img("ai-v1.1", 1), img("resell-v1.0", 1)
EXTRA = """.bl-titles{font-size:25px;font-weight:bold;line-height:1.25}
.bl-meta{font-family:var(--sans);font-weight:bold;font-size:14px;letter-spacing:.12em;color:var(--muted);line-height:1.9}
.dots{display:flex;gap:10px}.dots span{width:24px;height:24px;border-radius:50%}"""


def page(w, h, body):
    css = CSS.replace("width:1280px;height:720px", f"width:{w}px;height:{h}px") + EXTRA
    return f'<!doctype html><html><head><meta charset="utf-8"><style>{css}</style></head><body><div class="frame">{body}</div></body></html>'


def stack(x, y, w, gap):
    return (f'<img class="pg" src="{C_SELL}" style="width:{w}px;left:{x - gap}px;top:{y + 26}px;transform:rotate(-7deg)">'
            f'<img class="pg" src="{C_USE}" style="width:{w}px;left:{x + gap}px;top:{y + 26}px;transform:rotate(7deg)">'
            f'<img class="pg" src="{C_RES}" style="width:{w + 20}px;left:{x}px;top:{y}px;transform:rotate(0deg)">')


def cover():
    stats = "".join(f'<div class="stat"><b>{a}</b>{b}</div>' for a, b in (("3", "TOOLKITS"), (str(PAGES), "PAGES IN TOTAL"), ("$29", "INSTEAD OF $45")))
    return page(1280, 720, f'''<div class="blob" style="right:-110px;top:-130px;width:760px;height:760px"></div>{stack(810, 80, 270, 105)}
<div class="cv-left" style="width:600px"><div class="brand">CHECKMAYBE · BUNDLE</div><h1 class="cv-title" style="font-size:66px">The Complete Toolkit Bundle</h1><div class="cv-rule"></div>
<div class="bl-titles">{TITLES}</div><p class="cv-val">Canva licences, AI content and resell rights: check all three before you list.</p>
<div class="stats">{stats}</div><div class="sigs">{pill("g")}{pill("a")}{pill("r")}</div></div>
<div class="foot"><span>{FOOT}</span><span>3 PDF TOOLKITS</span></div>''')


def portrait():
    return page(512, 768, f'''<div class="blob" style="right:-220px;top:auto;bottom:-240px;width:620px;height:620px"></div>
<div style="position:absolute;left:44px;top:40px;width:430px"><div class="brand" style="font-size:12px">CHECKMAYBE · BUNDLE</div>
<h1 class="cv-title" style="font-size:44px;margin-top:10px">The Complete Toolkit Bundle</h1><div class="cv-rule" style="margin:16px 0 14px;height:5px;width:52px"></div>
<div class="bl-titles" style="font-size:19px">{TITLES}</div><div class="bl-meta" style="font-size:12px;margin-top:14px">3 PDF TOOLKITS · {PAGES} PAGES<br>$29 INSTEAD OF $45</div></div>
{stack(190, 420, 150, 110)}''')


def thumb():
    return page(600, 600, f'''<div class="blob" style="right:-170px;top:auto;bottom:-190px;width:520px;height:520px"></div>
<div style="position:absolute;left:44px;top:40px;width:520px"><div class="brand" style="font-size:14px">CHECKMAYBE · BUNDLE</div>
<h1 class="cv-title" style="font-size:54px;margin-top:12px">The Complete Toolkit Bundle</h1><div class="cv-rule" style="margin:18px 0 16px;height:6px;width:56px"></div>
<div class="bl-titles" style="font-size:22px">{TITLES}</div><div class="bl-meta" style="margin-top:16px">3 PDF TOOLKITS · {PAGES} PAGES<br>$29 INSTEAD OF $45</div></div>
{stack(395, 330, 140, 85)}
<div class="dots" style="position:absolute;left:44px;bottom:44px"><span style="background:var(--green)"></span><span style="background:var(--gold)"></span><span style="background:var(--red)"></span></div>''')


if __name__ == "__main__":
    os.makedirs("img", exist_ok=True)
    for name, fn in (("bundle-cover", cover), ("bundle-portrait", portrait), ("bundle-thumb", thumb)):
        open(f"img/{name}.html", "w").write(fn())
    print("ok", PAGES)
