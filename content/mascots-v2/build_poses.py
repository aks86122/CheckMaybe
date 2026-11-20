"""Poses for the new mascots (Stash, Penny, Dot): hand-built SVG, no AI art.
5 poses each: happy, thumbs, surprised, worried, sign. Transparent PNGs in poses/ (500x560) + poses-sheet.png.
Usage: python3 content/mascots-v2/build_poses.py
"""
import os, subprocess, tempfile, json

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = f"{HERE}/poses"; os.makedirs(OUT, exist_ok=True)
INK, ORANGE, YELLOW, CREAM, GREEN, RED = "#2E2B36", "#F08A4B", "#F7C948", "#FFFDF8", "#74C69D", "#E2687B"
S = 'stroke="%s" stroke-width="7" stroke-linejoin="round" stroke-linecap="round"' % INK


def face(cx, cy, mood):
    eye = lambda x, px: (f'<ellipse cx="{x}" cy="{cy}" rx="20" ry="24" fill="#fff" {S}/>'
                         f'<circle cx="{px}" cy="{cy + 4}" r="9" fill="{INK}"/><circle cx="{px + 3}" cy="{cy}" r="3" fill="#fff"/>')
    blush = (f'<ellipse cx="{cx - 64}" cy="{cy + 34}" rx="16" ry="10" fill="#F6A6A6" opacity=".7"/>'
             f'<ellipse cx="{cx + 64}" cy="{cy + 34}" rx="16" ry="10" fill="#F6A6A6" opacity=".7"/>')
    if mood == "wink":
        eyes = eye(cx - 34, cx - 30) + f'<path d="M{cx + 16} {cy + 4} q18 -16 36 0" fill="none" {S}/>'
    elif mood == "surprised":
        eyes = (f'<ellipse cx="{cx - 34}" cy="{cy - 4}" rx="22" ry="28" fill="#fff" {S}/><circle cx="{cx - 34}" cy="{cy - 2}" r="8" fill="{INK}"/>'
                f'<ellipse cx="{cx + 34}" cy="{cy - 4}" rx="22" ry="28" fill="#fff" {S}/><circle cx="{cx + 34}" cy="{cy - 2}" r="8" fill="{INK}"/>')
    else:
        eyes = eye(cx - 34, cx - 30) + eye(cx + 34, cx + 38)
    brows = {
        "worried": f'<path d="M{cx - 54} {cy - 30} q16 -14 34 -18" fill="none" {S}/><path d="M{cx + 20} {cy - 48} q18 4 34 18" fill="none" {S}/>',
        "surprised": f'<path d="M{cx - 54} {cy - 46} q18 -16 36 -4" fill="none" {S}/><path d="M{cx + 18} {cy - 50} q18 -12 36 4" fill="none" {S}/>',
    }.get(mood, f'<path d="M{cx - 52} {cy - 34} q18 -12 34 -2" fill="none" {S}/><path d="M{cx + 18} {cy - 36} q18 -10 34 2" fill="none" {S}/>')
    mouth = {
        "surprised": f'<ellipse cx="{cx}" cy="{cy + 52}" rx="16" ry="20" fill="{INK}" {S}/>',
        "worried": (f'<path d="M{cx - 24} {cy + 54} q12 -12 24 0 q12 12 24 0" fill="none" {S}/>'
                    f'<path d="M{cx + 82} {cy - 40} q-12 20 0 28 q12 -8 0 -28 z" fill="#8FC7F0" {S}/>'),
    }.get(mood, f'<path d="M{cx - 32} {cy + 38} q32 44 64 0 z" fill="{INK}" {S}/><path d="M{cx - 16} {cy + 56} q16 14 32 0" fill="#F28B8B"/>')
    return eyes + brows + mouth + ("" if mood == "worried" else blush)


def hand(x, y):
    return f'<circle cx="{x}" cy="{y}" r="17" fill="{ORANGE}" {S}/>'


def arm(x, y, d, kind):
    """d = -1 left, 1 right. Returns (svg, hand_xy)."""
    paths = {"wave": f"q{d*40} 10 {d*60} -30", "up": f"q{d*30} -20 {d*44} -80",
             "down": f"q{d*34} 24 {d*40} 70", "hold": f"q{d*40} -6 {d*56} -60"}
    p = paths[kind]
    xs = {"wave": (60, -30), "up": (44, -80), "down": (40, 70), "hold": (56, -60)}[kind]
    hx, hy = x + d * xs[0], y + xs[1]
    svg = (f'<path d="M{x} {y} {p}" fill="none" stroke="{INK}" stroke-width="22" stroke-linecap="round"/>'
           f'<path d="M{x} {y} {p}" fill="none" stroke="{ORANGE}" stroke-width="12" stroke-linecap="round"/>')
    return svg, (hx, hy)


def legs(xl1, xl2, y):
    leg = lambda x: f'<rect x="{x - 9}" y="{y}" width="18" height="44" rx="9" fill="{ORANGE}" {S}/><ellipse cx="{x + 6}" cy="{y + 50}" rx="30" ry="15" fill="{ORANGE}" {S}/>'
    return leg(xl1) + leg(xl2)


POSES = {  # name: (mood, left arm, right arm, extra)
    "happy": ("happy", "wave", "wave", None),
    "thumbs": ("wink", "down", "up", "thumb"),
    "surprised": ("surprised", "up", "up", None),
    "worried": ("worried", "down", "down", None),
    "sign": ("happy", "down", "hold", "sign"),
}


def limbs_for(pose, ax1, ax2, ay, lx1, lx2, ly):
    mood, la, ra, extra = POSES[pose]
    lsvg, lh = arm(ax1, ay, -1, la)
    rsvg, rh = arm(ax2, ay, 1, ra)
    top = hand(*lh) + hand(*rh)
    if extra == "thumb":
        top += f'<rect x="{rh[0] - 7}" y="{rh[1] - 40}" width="14" height="30" rx="7" fill="{ORANGE}" {S}/>' + hand(*rh)
    if extra == "sign":
        top = hand(*lh) + (f'<rect x="{rh[0] - 10}" y="{rh[1] - 150}" width="14" height="150" rx="6" fill="#C9A27A" {S}/>'
                           f'<rect x="{rh[0] - 80}" y="{rh[1] - 250}" width="160" height="110" rx="14" fill="#fff" {S}/>') + hand(*rh)
    return lsvg + rsvg + legs(lx1, lx2, ly), top, mood


def stash(pose):
    under, top, mood = limbs_for(pose, 84, 416, 330, 190, 310, 410)
    bill = (f'<g transform="rotate(12 300 150)"><rect x="230" y="90" width="150" height="110" rx="10" fill="{GREEN}" {S}/>'
            f'<circle cx="305" cy="140" r="22" fill="none" stroke="{INK}" stroke-width="6"/>'
            f'<text x="305" y="150" font-family="Inter,Arial" font-weight="800" font-size="28" fill="{INK}" text-anchor="middle">$</text></g>')
    body = (f'<rect x="80" y="160" width="340" height="250" rx="22" fill="{CREAM}" {S}/>'
            f'<path d="M84 172 L250 290 L416 172" fill="none" {S}/>'
            f'<line x1="104" y1="392" x2="396" y2="392" stroke="{INK}" stroke-width="7" stroke-dasharray="12 10"/>'
            f'<rect x="392" y="378" width="22" height="30" rx="5" fill="{YELLOW}" {S}/>')
    return bill + under + body + face(250, 316, mood) + top


def penny(pose):
    under, top, mood = limbs_for(pose, 108, 392, 330, 200, 300, 420)
    body = (f'<circle cx="250" cy="280" r="150" fill="{YELLOW}" {S}/><circle cx="250" cy="280" r="122" fill="none" stroke="#C9971F" stroke-width="8" stroke-dasharray="4 14"/>'
            f'<text x="250" y="190" font-family="Inter,Arial" font-weight="800" font-size="46" fill="#C9971F" text-anchor="middle">$</text>')
    return under + body + face(250, 290, mood) + top


def dot(pose):
    under, top, mood = limbs_for(pose, 104, 396, 350, 200, 300, 440)
    body = (f'<rect x="100" y="140" width="300" height="300" rx="24" fill="{CREAM}" {S}/>'
            f'<path d="M100 164 a24 24 0 0 1 24 -24 h252 a24 24 0 0 1 24 24 v56 h-300 z" fill="{ORANGE}" {S}/>'
            f'<rect x="160" y="112" width="18" height="56" rx="9" fill="#fff" {S}/><rect x="322" y="112" width="18" height="56" rx="9" fill="#fff" {S}/>'
            f'<circle cx="352" cy="400" r="26" fill="none" stroke="{RED}" stroke-width="7"/>'
            f'<text x="352" y="410" font-family="Inter,Arial" font-weight="800" font-size="28" fill="{INK}" text-anchor="middle">15</text>')
    return under + body + face(250, 320, mood) + top


CHARS = {"stash": stash, "penny": penny, "dot": dot}
VB = "-70 -140 640 700"  # room for raised arms and the sign
tmp = tempfile.mkdtemp(prefix="cm-poses-")
jobs = []
for c, fn in CHARS.items():
    for p in POSES:
        svg = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{VB}" width="500" height="547">{fn(p)}</svg>'
        open(f"{OUT}/{c}-{p}.svg", "w").write(svg)
        html = f'<!doctype html><html><head><style>html,body{{margin:0;background:transparent}}</style></head><body>{svg}</body></html>'
        open(f"{tmp}/{c}-{p}.html", "w").write(html)
        jobs.append([f"{tmp}/{c}-{p}.html", f"{OUT}/{c}-{p}.png"])
cells = "".join(f'<div class="c"><img src="file://{OUT}/{c}-{p}.svg"><div>{c} · {p}</div></div>' for c in CHARS for p in POSES)
open(f"{tmp}/sheet.html", "w").write(
    '<!doctype html><html><head><style>body{margin:0;width:1500px;background:#FBF8F3;font-family:Inter,Arial;display:flex;flex-wrap:wrap;padding:20px;box-sizing:border-box}'
    '.c{width:292px;text-align:center;font-size:20px;color:#5E5A6B}.c img{width:260px}</style></head><body>' + cells + '</body></html>')
js = f"""import {{ chromium }} from '/opt/node22/lib/node_modules/playwright/index.mjs';
const jobs = {json.dumps(jobs)}; const b = await chromium.launch();
for (const [s, o] of jobs) {{ const p = await b.newPage({{ viewport: {{ width: 500, height: 547 }} }});
  await p.goto('file://' + s); await p.screenshot({{ path: o, omitBackground: true }}); await p.close(); }}
const p = await b.newPage({{ viewport: {{ width: 1500, height: 1000 }} }}); await p.goto('file://{tmp}/sheet.html');
await p.screenshot({{ path: '{HERE}/poses-sheet.png', fullPage: true }}); await b.close();"""
open(f"{tmp}/r.mjs", "w").write(js)
subprocess.run(["node", f"{tmp}/r.mjs"], check=True)
print(len(jobs), "poses")
