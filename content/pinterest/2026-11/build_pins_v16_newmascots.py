"""v16 pins (2026-11-20): Amazon pins with the new mascots Stash, Penny and Dot (SVG, no AI art). Light look, 1000x1500.
Products are the ones J checked on the live page (pins-v15-amazon.md). Product lines use only words from each
listing's title or highlights; checklists are general tips. Copy and links: pins-v16-newmascots.md.
Sums: 1..52 = 1,378; $1 a day for 2027 (365 days) = $365.
Usage: python3 content/pinterest/2026-11/build_pins_v16_newmascots.py
"""
import json, os, subprocess, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
POSES = f"{ROOT}/content/mascots-v2/poses"
TMP = tempfile.mkdtemp(prefix="cm-pins-v16-")
OUT = f"{HERE}/pins"; os.makedirs(OUT, exist_ok=True)
SIGN_CENTER = {"stash": (472, 75), "penny": (448, 75), "dot": (452, 95)}  # sign card centre in the pose SVG


def mascot(char, pose, sign=None):
    if pose != "sign":
        return f"{POSES}/{char}-{pose}.png"
    svg = open(f"{POSES}/{char}-sign.svg").read()
    x, y = SIGN_CENTER[char]
    size = 44 if len(sign) <= 5 else 34
    svg = svg.replace("</svg>", f'<text x="{x}" y="{y + size * 0.35}" font-family="Inter,Arial" font-weight="800" '
                                f'font-size="{size}" fill="#2E2B36" text-anchor="middle">{sign}</text></svg>')
    path = f"{TMP}/{char}-sign-{abs(hash(sign))}.svg"; open(path, "w").write(svg); return path


T = dict(bg="#FBF8F3", ink="#2E2B36", sub="#5E5A6B", muted="#8C8798", card="#FFFFFF", line="#E6E0D6",
         accent="#D9785B", hl="#C98A2E", check="#6E9B78", tag_bg="#6E9B78", tag_ink="#FFFFFF",
         env=["#F2B8A2", "#F5D98B", "#B9D4B5"], binder="#E9E1D4")

PINS = [
    # Stash: cash stuffing, binders
    dict(id="az16", slug="cash-stuffing", char="stash", pose="happy", kicker="Cash stuffing on a budget",
         h1="Small paycheck?<br><em>Start with $20</em>",
         envs=[("Groceries", "$20"), ("Gas", "$20"), ("Fun money", "$10")], label="START SMALL, START THIS WEEK", steps=False,
         rows=[("Fill weekly, not monthly", "Smaller amounts, easier to stick to"),
               ("Coins count too", "Keep them in the envelope, not the car"),
               ("Round down when you plan", "Leftovers feel better than running short")],
         pick='A binder for it: <b>NICOOTH Budget Binder A6</b> (zipper cash envelopes)'),
    dict(id="az17", slug="cash-stuffing", char="stash", pose="thumbs", kicker="Sinking funds",
         h1="Sinking funds:<br><em>one envelope each</em>",
         envs=[("Christmas", "$50/mo"), ("Car repairs", "$40/mo"), ("Birthdays", "$25/mo")], label="SINKING FUNDS IN 3 STEPS", steps=True,
         rows=[("Pick costs that come once a year", "Gifts, car repairs, insurance, birthdays"),
               ("Divide by the months left", "$600 for Christmas over 12 months = $50 a month"),
               ("Fill it every payday", "So December isn't a surprise")],
         pick='12 envelopes and a calculator: <b>Nefeeko Budget Binder</b> (zipper envelopes, cash envelopes, calculator)'),
    dict(id="az18", slug="cash-stuffing", char="stash", pose="sign", sign="ZIP IT", kicker="Budget binder tip",
         h1="Coins falling out?<br><em>Get zipper pockets</em>",
         envs=[("Groceries", "$400"), ("Gas", "$160"), ("Fun money", "$80")], label="WHAT ZIPPER POCKETS FIX", steps=False,
         rows=[("Coins stay put", "Open-top envelopes leak change in your bag"),
               ("You can see what's left", "Clear pockets show the cash without counting"),
               ("Labels stop the mixing", "Grocery money stays grocery money")],
         pick='12 zipper pockets with labels: <b>Antner A6 Budget Binder</b> (zipper cash envelopes and labels)'),
    # Penny: savings challenges
    dict(id="az19", slug="savings-challenge", char="penny", pose="sign", sign="$365", kicker="New year savings",
         h1="$1 a day in 2027<br><em>is $365 by December 31</em>",
         envs=[("Jan 1", "$1"), ("Jun 30", "$181"), ("Dec 31", "$365")], label="THE EASIEST CHALLENGE", steps=False,
         rows=[("Put in $1 every day", "Cash in an envelope, not your wallet"),
               ("Missed a day? Add $2 tomorrow", "Catch up, don't start over"),
               ("Track it on a page", "Cross off each day")],
         pick='Envelopes and a tracker: <b>RONMONG 100 Envelopes Challenge Binder</b> (cash envelopes, tracker and budget sheets)'),
    dict(id="az20", slug="savings-challenge", char="penny", pose="surprised", kicker="52-week challenge",
         h1="52-week challenge:<br><em>$1,378 by year end</em>",
         envs=[("Week 1", "$1"), ("Week 26", "$26"), ("Week 52", "$52")], label="HOW IT ADDS UP", steps=False,
         rows=[("Week 1: $1, week 2: $2...", "Up to $52 in the last week"),
               ("Or start at $52 in January", "Big weeks first, while you're motivated"),
               ("All 52 weeks = $1,378", "1 + 2 + 3 ... + 52")],
         pick='A book for savings challenges: <b>APMFHO 100 Days Money Saving Challenge</b> (custom goals from $1,000 to $10,000)'),
    dict(id="az21", slug="savings-challenge", char="penny", pose="worried", kicker="Savings challenge",
         h1="Fell behind on your<br><em>savings challenge?</em>",
         envs=[("Filled", "41 of 100"), ("Saved so far", "$1,027"), ("Left to go", "59")], label="RESTART WITHOUT STARTING OVER", steps=True,
         rows=[("Count what's already filled", "That money is saved, keep it"),
               ("Skip the big numbers for now", "Fill the small ones first"),
               ("Set one envelope a week", "Slower still finishes")],
         pick='Envelopes and a tracker: <b>RONMONG 100 Envelopes Challenge Binder</b> (cash envelopes, tracker and budget sheets)'),
    # Dot: bills, due dates, planners
    dict(id="az22", slug="budget-planner", char="dot", pose="worried", kicker="Bills and paydays",
         h1="Bills due before payday?<br><em>Ask to move the date</em>",
         envs=[("Rent · 1st", "$1,200"), ("Card · 3rd", "$120"), ("Payday", "5th")], label="FIX THE TIMING", steps=True,
         rows=[("List bills by due date", "Next to your paydays"),
               ("Find the ones that land early", "Before the money arrives"),
               ("Call and ask to move it", "Many card issuers and utilities let you pick a due date")],
         pick='A bill organizer for it: <b>SOLIGT Budget Planner Monthly Bill Organizer</b> (undated, 12 pockets)'),
    dict(id="az23", slug="budget-planner", char="dot", pose="sign", sign="DUE", kicker="Pay later plans",
         h1="On pay-later plans?<br><em>Write every due date</em>",
         envs=[("Plan 1 · Dec 4", "$62"), ("Plan 2 · Dec 11", "$45"), ("Plan 3 · Dec 18", "$38")], label="ONE LIST FOR ALL YOUR PLANS", steps=False,
         rows=[("Every plan, every payment date", "Not just the first one"),
               ("Same week as rent? Flag it", "That's the week that gets tight"),
               ("Write the last payment date too", "So you know when it ends")],
         pick='An undated planner: <b>Taja Budget Planner</b> (undated budget book with expense tracker)'),
    dict(id="az24", slug="budget-planner", char="dot", pose="thumbs", kicker="Yearly subscriptions",
         h1="Yearly renewals?<br><em>Put them on one page</em>",
         envs=[("Streaming · Mar 2", "$139"), ("Cloud · Jul 15", "$99"), ("App · Oct 8", "$59")], label="BEFORE IT RENEWS", steps=True,
         rows=[("List every yearly renewal", "Check your email for receipts"),
               ("Write the date and the price", "Next to each one"),
               ("Decide two weeks before", "Keep it, switch plans, or cancel")],
         pick='An undated planner: <b>snootion Budget Planner</b> (undated monthly finance organizer with expense tracker)'),
]


def page(p):
    t = T
    css = f"""*{{box-sizing:border-box;margin:0;padding:0}}html,body{{width:1000px;height:1500px;overflow:hidden}}
body{{position:relative;background:{t['bg']};color:{t['ink']};font-family:Inter,"Liberation Sans",sans-serif}}
.k{{position:absolute;left:64px;top:64px;font-size:24px;letter-spacing:.18em;font-weight:600;color:{t['muted']};text-transform:uppercase}}.k b{{color:{t['accent']}}}
h1{{position:absolute;left:64px;right:64px;top:118px;font-size:72px;font-weight:800;line-height:1.06}}h1 em{{font-style:normal;color:{t['accent']}}}
.binder{{position:absolute;left:64px;top:330px;width:520px;height:330px;border-radius:28px;background:{t['binder']};border:3px solid {t['line']}}}
.ring{{position:absolute;left:22px;width:26px;height:26px;border-radius:50%;border:5px solid {t['muted']}}}
.env{{position:absolute;left:80px;width:410px;height:120px;border-radius:16px;padding:16px 24px;font-size:30px;font-weight:800;color:#2E2B36;box-shadow:0 10px 24px rgba(0,0,0,.18)}}
.zip{{position:absolute;left:24px;right:24px;bottom:22px;height:8px;border-radius:4px;background:repeating-linear-gradient(90deg,rgba(46,43,54,.55) 0 8px,transparent 8px 14px)}}
.amt{{position:absolute;right:24px;top:16px;font-size:26px;font-weight:600;opacity:.75}}
.pose{{position:absolute;right:10px;top:300px;width:400px}}
.card{{position:absolute;left:64px;right:64px;top:720px;background:{t['card']};border:2px solid {t['line']};border-radius:26px;padding:26px 40px;box-shadow:0 20px 60px rgba(0,0,0,.12)}}
.lab{{font-size:22px;font-weight:800;letter-spacing:.2em;color:{t['hl']};margin-bottom:6px}}
.row{{display:flex;gap:22px;align-items:flex-start;padding:14px 0;border-top:1px solid {t['line']}}}.row:nth-child(2){{border-top:0}}
.c{{flex:none;width:44px;height:44px;border-radius:50%;background:{t['check']};color:#fff;font-size:26px;font-weight:800;display:flex;align-items:center;justify-content:center}}
.q{{font-size:34px;font-weight:800}}.s{{font-size:24px;color:{t['sub']};margin-top:4px}}
.pick{{position:absolute;left:64px;right:64px;top:1262px;font-size:26px;color:{t['sub']};line-height:1.4}}.pick b{{color:{t['ink']}}}
.tag{{display:inline-block;margin-top:14px;font-weight:800;border-radius:999px;padding:10px 24px;font-size:24px;background:{t['tag_bg']};color:{t['tag_ink']}}}
.foot{{position:absolute;left:64px;right:64px;bottom:34px;display:flex;justify-content:space-between;font-size:17px;letter-spacing:.06em;color:{t['muted']}}}"""
    env_html = "".join(
        f'<div class="env" style="top:{40 + i * 90}px;background:{t["env"][i]}">{n}<span class="amt">{a}</span><div class="zip"></div></div>'
        for i, (n, a) in enumerate(p["envs"]))
    rings = "".join(f'<div class="ring" style="top:{60 + i * 90}px"></div>' for i in range(3))
    rows_html = "".join(
        f'<div class="row"><div class="c">{i + 1 if p["steps"] else "✓"}</div><div><div class="q">{q}</div><div class="s">{s}</div></div></div>'
        for i, (q, s) in enumerate(p["rows"]))
    img = mascot(p["char"], p["pose"], p.get("sign"))
    body = (f'<div class="k"><b>CheckMaybe</b> · {p["kicker"]}</div><h1>{p["h1"]}</h1>'
            f'<div class="binder">{rings}{env_html}</div><img class="pose" src="file://{img}">'
            f'<div class="card"><div class="lab">{p["label"]}</div>{rows_html}</div>'
            f'<div class="pick">{p["pick"]}<br><span class="tag">See it on Amazon</span></div>'
            f'<div class="foot"><span>As an Amazon Associate I earn from qualifying purchases. Example amounts.</span><span>checkmaybe</span></div>')
    return f'<!doctype html><html><head><meta charset="utf-8"><style>{css}</style></head><body>{body}</body></html>'


jobs = []
for p in PINS:
    src = f"{TMP}/{p['id']}.html"; open(src, "w").write(page(p))
    jobs.append([src, f"{OUT}/checkmaybe-pin-{p['id']}-{p['slug']}.png"])
js = f"""import {{ chromium }} from '/opt/node22/lib/node_modules/playwright/index.mjs';
const jobs = {json.dumps(jobs)}; const b = await chromium.launch();
for (const [s, o] of jobs) {{ const p = await b.newPage({{ viewport: {{ width: 1000, height: 1500 }} }});
  await p.goto('file://' + s); await p.evaluate(() => document.fonts.ready); await p.screenshot({{ path: o }}); console.log(o.split('/').pop()); await p.close(); }}
await b.close();"""
open(f"{TMP}/shoot.mjs", "w").write(js)
subprocess.run(["node", f"{TMP}/shoot.mjs"], check=True)
