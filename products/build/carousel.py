"""IG carousel slides, 1080x1350."""
import html, json
E = lambda s: html.escape(s, quote=False)
CSS = """*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1080px;height:1350px;overflow:hidden;background:#ece1c4;color:#3b2a1e;font-family:"Bitstream Charter","DejaVu Serif",serif}
.s{position:relative;width:1080px;height:1350px;padding:96px 92px;display:flex;flex-direction:column}
.top{display:flex;justify-content:space-between;align-items:center;font-family:"Liberation Sans",sans-serif;font-weight:bold;letter-spacing:.3em;font-size:22px}
.brand{color:#c25a1c}.num{color:#6b5a45;letter-spacing:.12em}
.body{flex:1;display:flex;flex-direction:column;justify-content:center;gap:40px}
.hook{font-size:92px;line-height:1.06;font-weight:bold;text-wrap:balance}
.rule{width:110px;height:10px;background:#c25a1c}
.sub{font-size:44px;line-height:1.3;color:#6b5a45;text-wrap:balance}
.label{font-family:"Liberation Sans",sans-serif;font-weight:bold;font-size:30px;letter-spacing:.22em;color:#fff;background:#2c1f15;align-self:flex-start;padding:14px 24px;border-radius:8px}
.meta{font-family:"Liberation Sans",sans-serif;font-size:28px;letter-spacing:.06em;color:#6b5a45}
.lead{font-size:42px;line-height:1.3}
.quote{background:#f8f1de;border:2px solid #c7b287;border-left:14px solid #c25a1c;border-radius:10px;padding:44px 48px;font-size:52px;line-height:1.32;font-weight:bold}
.note{font-size:34px;line-height:1.35;color:#6b5a45}
.big{font-size:70px;line-height:1.14;font-weight:bold;text-wrap:balance}
.checks{display:flex;flex-direction:column;gap:26px}
.check{display:flex;align-items:center;gap:28px;background:#f8f1de;border:2px solid #c7b287;border-radius:10px;padding:30px 34px;font-size:40px;line-height:1.28}
.box{width:46px;height:46px;border:4px solid #6b5a45;border-radius:6px;flex:none;background:#fffaf0}
.prod{background:#2c1f15;color:#f3e7cc;border-radius:12px;padding:48px}
.prod b{display:block;font-size:66px;line-height:1.05;margin-bottom:14px}
.prod span{font-size:36px;color:#e0c9a0}
.cta{font-family:"Liberation Sans",sans-serif;font-weight:bold;font-size:40px;letter-spacing:.08em;color:#c25a1c}
.foot{font-family:"Liberation Sans",sans-serif;font-size:22px;letter-spacing:.12em;color:#6b5a45;border-top:2px solid #c7b287;padding-top:22px;display:flex;justify-content:space-between}
.swipe{color:#c25a1c;font-weight:bold}
"""
def page(inner, i, n, foot_right):
    return f'''<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body><div class="s">
<div class="top"><span class="brand">CHECKMAYBE</span><span class="num">{i} / {n}</span></div>
<div class="body">{inner}</div>
<div class="foot"><span>EDUCATIONAL, NOT LEGAL ADVICE</span><span class="{'swipe' if i < n else ''}">{E(foot_right)}</span></div></div></body></html>'''
def quote(label, meta, lead, q, note=""):
    return (f'<div class="label">{E(label)}</div><div class="meta">{E(meta)}</div>'
            + (f'<div class="lead">{E(lead)}</div>' if lead else "")
            + f'<div class="quote">“{E(q)}”</div>' + (f'<div class="note">{E(note)}</div>' if note else ""))
SETS = {
 "resell-1-platform-rules": [
  '<div class="hook">Bought a pack with “resell rights”?</div><div class="rule"></div><div class="sub">Check the rules of the place you’ll sell it first.</div>',
  quote("GUMROAD", "Prohibited Products · last revised 16 Sep 2026", "The list of what’s not allowed includes:", "reselling private label rights products"),
  quote("BEACONS", "Community Standards · updated 22 Nov 2025", "", "In general, we do not allow resale; you cannot sell products you did not create."),
  quote("ETSY", "Creativity Standards · updated 10 Jun 2025", "Not “designed by a seller”:", "A bundle, collection, scan, or PDF of someone else’s work"),
  '<div class="big">“Buy once, rebrand, resell” can break the storefront’s rules before the licence even comes up.</div>',
  '<div class="big">Read the rules of the place you’ll sell, not only the licence you bought.</div><div class="rule"></div><div class="sub">Save this for your next purchase. Rules change, so check the current pages yourself.</div>',
 ],
 "resell-2-canva-packs": [
  '<div class="hook">Your resell pack is made in Canva?</div><div class="rule"></div><div class="sub">Read this line from Canva’s licence before you list it.</div>',
  quote("CANVA · §9 PROHIBITED USES", "Content License Agreement", "You can’t:", "sub-license, re-sell, rent, lend, assign, gift or otherwise transfer or distribute the Content or the rights granted under this Content License Agreement"),
  quote("CANVA · §9, SAME SECTION", "Content License Agreement", "You can’t:", "use or display Content in a manner that gives the impression that the Content was created by you"),
  '<div class="big">So “full resell rights, rebrand it as your own” can’t cover the Canva photos, graphics or fonts inside the pack.</div><div class="note">Narrow exception in §4A: handing a design to one client.</div>',
  '<div class="big" style="font-size:60px">Before you list:</div><div class="checks"><div class="check"><span class="box"></span>Which elements are Canva library content?</div><div class="check"><span class="box"></span>What label does each carry: Free, Pro, Education, Branded?</div><div class="check"><span class="box"></span>Could a buyer pull them out as files?</div></div>',
  '<div class="big" style="font-size:60px">20 seller scenarios like this one:</div><div class="prod"><b>Can I Sell This?</b><span>A commercial use toolkit for Canva sellers</span></div><div class="cta">LINK IN BIO →</div><div class="note">Not affiliated with Canva.</div>',
 ],
}
for name, slides in SETS.items():
    for i, inner in enumerate(slides, 1):
        open(f"car/{name}-{i}.html", "w").write(page(inner, i, len(slides), "SWIPE →" if i < len(slides) else "@CHECKMAYBETW"))
print("ok")
