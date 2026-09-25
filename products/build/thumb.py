"""Square Gumroad thumbnails (600x600 CSS px, exported at 2x = 1200x1200)."""
import html, os
from mk import PRODUCTS, img
E = lambda s: html.escape(s, quote=False)
CSS = """*{box-sizing:border-box;margin:0;padding:0}
html,body{width:600px;height:600px;overflow:hidden;background:#ece1c4;color:#3b2a1e;font-family:"Bitstream Charter","DejaVu Serif",serif}
.f{position:relative;width:600px;height:600px;overflow:hidden;padding:46px 44px}
.blob{position:absolute;right:-150px;bottom:-170px;width:470px;height:470px;border-radius:50%;background:#e1cfa6}
.pg{position:absolute;width:215px;right:30px;bottom:-62px;transform:rotate(-6deg);box-shadow:0 14px 30px rgba(44,31,21,.3);border-radius:2px}
.brand{font-family:"Liberation Sans",sans-serif;font-weight:bold;letter-spacing:.3em;font-size:14px;color:#c25a1c}
h1{font-size:76px;line-height:.98;margin-top:16px;font-weight:bold}
.rule{width:56px;height:6px;background:#c25a1c;margin:20px 0 16px}
.sub{font-size:21px;font-weight:bold;line-height:1.22;max-width:300px}
.meta{margin-top:18px;font-family:"Liberation Sans",sans-serif;font-weight:bold;font-size:14px;letter-spacing:.1em;color:#6b5a45;line-height:1.7}
.dots{position:absolute;left:44px;bottom:44px;display:flex;gap:8px}
.dots span{width:22px;height:22px;border-radius:50%}
"""
SUB = {"canva-v3.1": ("Commercial use toolkit for Canva sellers", "27-PAGE PDF · 20 SCENARIOS"),
       "ai-v1.1": ("AI content commercial use toolkit", "32-PAGE PDF · 15 SCENARIOS")}
for p in PRODUCTS:
    sub, meta = SUB[p["id"]]
    t = p["title"].replace("This?", "<br>This?")
    open(f"img/{p['slug']}-thumb.html", "w").write(f'''<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body><div class="f">
<div class="blob"></div><img class="pg" src="{img(p["id"], 1)}">
<div class="brand">CHECKMAYBE</div><h1>{t}</h1><div class="rule"></div>
<div class="sub">{E(sub)}</div><div class="meta">{E(meta)}<br>V{E(p["version"])} · NOT LEGAL ADVICE</div>
<div class="dots"><span style="background:#3f6b3a"></span><span style="background:#a17a2e"></span><span style="background:#c23c28"></span></div>
</div></body></html>''')
print("ok")
