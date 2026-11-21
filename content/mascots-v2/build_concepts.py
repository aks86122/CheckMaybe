"""New mascot concepts (2026-11-20): hand-built SVG, no AI art. Flat, bold dark outline, orange limbs like the receipt.
Usage: python3 content/mascots-v2/build_concepts.py  -> concepts.png and one SVG per character.
"""
import os, subprocess, tempfile, json
HERE = os.path.dirname(os.path.abspath(__file__))
INK, ORANGE, YELLOW, CREAM, GREEN = "#2E2B36", "#F08A4B", "#F7C948", "#FFFDF8", "#74C69D"
S = 'stroke="%s" stroke-width="7" stroke-linejoin="round" stroke-linecap="round"' % INK

def face(cx, cy, mood="happy"):
    eyes = (f'<ellipse cx="{cx-34}" cy="{cy}" rx="20" ry="24" fill="#fff" {S}/><ellipse cx="{cx+34}" cy="{cy}" rx="20" ry="24" fill="#fff" {S}/>'
            f'<circle cx="{cx-30}" cy="{cy+4}" r="9" fill="{INK}"/><circle cx="{cx+38}" cy="{cy+4}" r="9" fill="{INK}"/>'
            f'<circle cx="{cx-27}" cy="{cy}" r="3" fill="#fff"/><circle cx="{cx+41}" cy="{cy}" r="3" fill="#fff"/>')
    brows = f'<path d="M{cx-52} {cy-34} q18 -12 34 -2" fill="none" {S}/><path d="M{cx+18} {cy-36} q18 -10 34 2" fill="none" {S}/>'
    mouth = (f'<path d="M{cx-32} {cy+38} q32 44 64 0 z" fill="{INK}" {S}/><path d="M{cx-16} {cy+56} q16 14 32 0" fill="#F28B8B"/>'
             f'<ellipse cx="{cx-64}" cy="{cy+34}" rx="16" ry="10" fill="#F6A6A6" opacity=".7"/><ellipse cx="{cx+64}" cy="{cy+34}" rx="16" ry="10" fill="#F6A6A6" opacity=".7"/>' if mood == "happy"
             else f'<path d="M{cx-18} {cy+46} q18 -10 36 0" fill="none" {S}/>')
    return eyes + brows + mouth

def limbs(x1, x2, y_arm, y_leg, xl1, xl2):
    arm = lambda x, d: f'<path d="M{x} {y_arm} q{d*40} 10 {d*60} -30" fill="none" stroke="{INK}" stroke-width="22" stroke-linecap="round"/><path d="M{x} {y_arm} q{d*40} 10 {d*60} -30" fill="none" stroke="{ORANGE}" stroke-width="12" stroke-linecap="round"/><circle cx="{x+d*62}" cy="{y_arm-32}" r="17" fill="{ORANGE}" {S}/>'
    leg = lambda x: f'<rect x="{x-9}" y="{y_leg}" width="18" height="44" rx="9" fill="{ORANGE}" {S}/><ellipse cx="{x+6}" cy="{y_leg+50}" rx="30" ry="15" fill="{ORANGE}" {S}/>'
    return arm(x1, -1) + arm(x2, 1) + leg(xl1) + leg(xl2)

def envelope():   # Stash: cash envelope with a zipper and a bill peeking out of the top
    bill = (f'<g transform="rotate(12 300 150)"><rect x="230" y="90" width="150" height="110" rx="10" fill="{GREEN}" {S}/>'
            f'<circle cx="305" cy="140" r="22" fill="none" stroke="{INK}" stroke-width="6"/>'
            f'<text x="305" y="150" font-family="Inter,Arial" font-weight="800" font-size="28" fill="{INK}" text-anchor="middle">$</text></g>')
    body = (f'<rect x="80" y="160" width="340" height="250" rx="22" fill="{CREAM}" {S}/>'
            f'<path d="M84 172 L250 290 L416 172" fill="none" {S}/>'
            f'<line x1="104" y1="380" x2="396" y2="380" stroke="{INK}" stroke-width="7" stroke-dasharray="12 10"/>'
            f'<rect x="392" y="366" width="22" height="30" rx="5" fill="{YELLOW}" {S}/>')
    return bill + limbs(84, 416, 330, 410, 190, 310) + body + face(250, 320)


def coin():       # Penny: a coin with a rim and a small $ stamp
    body = (f'<circle cx="250" cy="280" r="150" fill="{YELLOW}" {S}/><circle cx="250" cy="280" r="122" fill="none" stroke="#C9971F" stroke-width="8" stroke-dasharray="4 14"/>'
            f'<text x="250" y="190" font-family="Inter,Arial" font-weight="800" font-size="46" fill="#C9971F" text-anchor="middle">$</text>')
    return limbs(108, 392, 330, 420, 200, 300) + body + face(250, 290)

def calendar():   # Dot: a tear-off calendar page with rings and a due-date circle
    body = (f'<rect x="100" y="140" width="300" height="300" rx="24" fill="{CREAM}" {S}/>'
            f'<path d="M100 164 a24 24 0 0 1 24 -24 h252 a24 24 0 0 1 24 24 v56 h-300 z" fill="{ORANGE}" {S}/>'
            f'<rect x="160" y="112" width="18" height="56" rx="9" fill="#fff" {S}/><rect x="322" y="112" width="18" height="56" rx="9" fill="#fff" {S}/>'
            f'<circle cx="352" cy="400" r="26" fill="none" stroke="#E2687B" stroke-width="7"/><text x="352" y="410" font-family="Inter,Arial" font-weight="800" font-size="28" fill="{INK}" text-anchor="middle">15</text>')
    return limbs(104, 396, 350, 440, 200, 300) + body + face(250, 320)

CHARS = [("stash", "Stash", "Cash envelope", "Cash stuffing, budget binders, envelope rules", envelope()),
         ("penny", "Penny", "Coin", "Savings challenges, sinking funds, money kept", coin()),
         ("dot", "Dot", "Calendar page", "Bills and due dates, pay-later dates, budget planners", calendar())]

svgs = {}
for key, name, what, use, g in CHARS:
    svg = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 520" width="500" height="520">{g}</svg>'
    open(f"{HERE}/{key}.svg", "w").write(svg); svgs[key] = svg
cards = "".join(f'<div class="c"><div class="art">{svgs[k]}</div><h2>{n}</h2><div class="w">{w}</div><div class="u">{u}</div></div>' for k, n, w, u, _ in CHARS)
html = f'''<!doctype html><html><head><meta charset="utf-8"><style>
body{{margin:0;width:1800px;height:900px;background:#FBF8F3;font-family:Inter,Arial;color:{INK};display:flex;flex-direction:column;align-items:center}}
h1{{font-size:44px;margin:40px 0 10px}}.row{{display:flex;gap:40px}}.c{{width:540px;background:#fff;border:2px solid #E6E0D6;border-radius:28px;padding:20px;text-align:center}}
.art svg{{width:440px;height:458px}}h2{{margin:6px 0 2px;font-size:40px}}.w{{font-size:24px;color:{ORANGE};font-weight:700}}.u{{font-size:22px;color:#5E5A6B;margin-top:6px}}
</style></head><body><h1>CheckMaybe new mascots: concepts</h1><div class="row">{cards}</div></body></html>'''
tmp = tempfile.mkdtemp(prefix="cm-mascots-"); open(f"{tmp}/s.html", "w").write(html)
js = f"""import {{ chromium }} from '/opt/node22/lib/node_modules/playwright/index.mjs';
const b = await chromium.launch(); const p = await b.newPage({{ viewport: {{ width: 1800, height: 900 }} }});
await p.goto('file://{tmp}/s.html'); await p.screenshot({{ path: '{HERE}/concepts.png' }}); await b.close();"""
open(f"{tmp}/s.mjs", "w").write(js); subprocess.run(["node", f"{tmp}/s.mjs"], check=True); print("concepts.png")
