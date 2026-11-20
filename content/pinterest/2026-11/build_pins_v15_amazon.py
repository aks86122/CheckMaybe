"""v15 pins (2026-11-20): Amazon Associates pins for A6 budget binders, 1000x1500.

az1 comes in dark and light; az2 to az5 are light only (J 2026-11-20: light version, different copy,
same product type). No Amazon product photos (Associates rules): own illustration, receipt mascot, text.
Each product line uses only features named in that product's Amazon listing title. Checklists and steps
are general cash-stuffing tips, not product claims. Copy and links: pins-v15-amazon.md.
Usage: python3 content/pinterest/2026-11/build_pins_v15_amazon.py
"""
import json, os, subprocess, tempfile
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
A2, A3 = f"{ROOT}/content/2026-10-comic-02/art", f"{ROOT}/content/2026-10-comic-03/art"
TMP = tempfile.mkdtemp(prefix="cm-pins-v15-")
OUT = f"{HERE}/pins"; os.makedirs(OUT, exist_ok=True)


def cutout(src, name):
    """Key out the dark background connected to the edges, for the light pins."""
    im = Image.open(src).convert("RGB"); key = im.copy()
    for xy in [(0, 0), (im.width - 1, 0), (0, im.height - 1), (im.width - 1, im.height - 1)]:
        ImageDraw.floodfill(key, xy, (255, 0, 255), thresh=70)
    rgba = im.convert("RGBA"); px, kp = rgba.load(), key.load()
    for y in range(im.height):
        for x in range(im.width):
            if kp[x, y] == (255, 0, 255):
                px[x, y] = (0, 0, 0, 0)
    path = f"{TMP}/{name}.png"; rgba.save(path); return path


DARK = dict(bg="#15171F", ink="#EDEBF5", sub="#B9B7C9", muted="#9A98AC", card="#1C1E28", line="#33384F",
            accent="#F08A4B", hl="#F7C948", check="#74D39A", tag_bg="#F08A4B", tag_ink="#15171F",
            env=["#F08A4B", "#F7C948", "#74D39A", "#8FA7F0"], binder="#2A2D3A", mask=True)
LIGHT = dict(bg="#FBF8F3", ink="#2E2B36", sub="#5E5A6B", muted="#8C8798", card="#FFFFFF", line="#E6E0D6",
             accent="#D9785B", hl="#C98A2E", check="#6E9B78", tag_bg="#6E9B78", tag_ink="#FFFFFF",
             env=["#F2B8A2", "#F5D98B", "#B9D4B5", "#BFCBEF"], binder="#E9E1D4", mask=False)

PINS = [
    dict(id="az1", themes=["dark", "light"], art=f"{A2}/check.jpg", kicker="Cash stuffing",
         h1="Starting cash stuffing?<br><em>What your binder needs</em>",
         envs=[("Groceries", "$400"), ("Gas", "$160"), ("Fun money", "$80")],
         label="CHECK BEFORE YOU BUY", steps=False,
         rows=[("Zipper envelopes", "Coins and bills stay put"),
               ("Expense sheets", "Write down what you spend from each one"),
               ("One envelope per category", "Groceries, gas, fun money: decide before you spend"),
               ("Small enough to carry", "If it stays home, you'll pay by card instead")],
         pick='One that has the first two: <b>SKYDUE Budget Binder</b> (zipper envelopes, cash envelopes, expense sheets)'),
    dict(id="az2", themes=["light"], art=f"{A3}/check.jpg", kicker="Cash stuffing for beginners",
         h1="New to cash stuffing?<br><em>Start with 3 envelopes</em>",
         envs=[("Groceries", "$350"), ("Gas", "$120"), ("Eating out", "$60")],
         label="START SMALL", steps=False,
         rows=[("Pick 3 categories", "The ones where card spending gets away from you"),
               ("Set one amount each", "For the month, before you spend anything"),
               ("Only spend what's inside", "Empty envelope means wait until next month"),
               ("Add more later", "Once three feel easy, add gifts or personal care")],
         pick='A binder for it: <b>NICOOTH Budget Binder A6</b> (zipper cash envelopes)'),
    dict(id="az3", themes=["light"], art=f"{A2}/asterisk.jpg", kicker="Card spending",
         h1="Card bill higher<br><em>than you expected?</em>",
         envs=[("Groceries", "$400"), ("Takeout", "$80"), ("Shopping", "$100")],
         label="TRY ONE MONTH OF CASH", steps=False,
         rows=[("Pick the category that ran over", "Check last month's statement first"),
               ("Take that amount out in cash", "Put it in its own envelope"),
               ("Pay that category with cash only", "You can see what's left without an app"),
               ("Compare at the end of the month", "Same month on a card vs in cash")],
         pick='Envelopes with labels: <b>Antner A6 Budget Binder</b> (zipper cash envelopes and labels)'),
    dict(id="az4", themes=["light"], art=f"{A3}/calc.jpg", kicker="Payday routine",
         h1="Payday routine:<br><em>fill your envelopes</em>",
         envs=[("Groceries", "$200"), ("Gas", "$80"), ("Fun money", "$40")],
         label="EVERY PAYDAY, 4 STEPS", steps=True,
         rows=[("List this paycheck's categories", "Only the ones you'll pay in cash"),
               ("Write an amount next to each", "Add them up before you go to the bank"),
               ("Withdraw that total in cash", "Ask for small bills"),
               ("Fill each envelope and note it", "Amount in, date, what's left last time")],
         pick='A binder with a calculator: <b>Nefeeko Budget Binder</b> (zipper envelopes, cash envelopes, calculator)'),
    dict(id="az5", themes=["light"], art=f"{A2}/happy.jpg", kicker="Cash envelope rules",
         h1="Envelope empty?<br><em>That category is done</em>",
         envs=[("Groceries", "$12 left"), ("Gas", "$0 left"), ("Fun money", "$25 left")],
         label="3 RULES THAT MAKE IT WORK", steps=False,
         rows=[("Empty means done", "No borrowing from next month's envelope"),
               ("Moving money is a decision", "Take from fun money, not from rent"),
               ("Leftovers go somewhere on purpose", "Roll over or move to savings, and write it down")],
         pick='Zipper pockets with sheets: <b>Ginmlyda Budget Binder</b> (zipper PVC pockets, budget sheets, stickers and pen)'),
    # Savings challenge books (100 envelopes). Sums: 1..100 = 5,050; 1..50 = 1,275. Jan 1 + 99 days = Apr 10, 2027.
    dict(id="az6", slug="savings-challenge", themes=["light"], art=f"{A2}/unroll.jpg", kicker="100 envelope challenge",
         h1="100 envelopes,<br><em>$5,050 saved</em>",
         envs=[("Envelope #1", "$1"), ("Envelope #37", "$37"), ("Envelope #100", "$100")],
         label="HOW THE MATH WORKS", steps=False,
         rows=[("Each envelope has a number", "1 to 100: put in that many dollars"),
               ("Fill one when you can", "In any order, a small one on tight weeks"),
               ("All 100 filled = $5,050", "1 + 2 + 3 ... + 100")],
         pick='A book for it: <b>APMFHO 100 Days Money Saving Challenge</b> (100 envelopes, save $5,050 or $10,000)'),
    dict(id="az7", slug="savings-challenge", themes=["light"], art=f"{A3}/calc.jpg", kicker="Savings challenge",
         h1="$5,050 too much?<br><em>Do 50 envelopes</em>",
         envs=[("Envelope #1", "$1"), ("Envelope #25", "$25"), ("Envelope #50", "$50")],
         label="SMALLER VERSIONS", steps=False,
         rows=[("Envelopes 1 to 50", "$1,275 when they're all filled"),
               ("Envelopes 1 to 100", "$5,050 when they're all filled"),
               ("Pick the one you'll finish", "A finished small challenge beats a dropped big one")],
         pick='One with a tracker: <b>RONMONG 100 Envelopes Challenge Binder</b> (cash envelopes, tracker and budget sheets)'),
    dict(id="az8", slug="savings-challenge", themes=["light"], art=f"{A2}/check.jpg", kicker="100 envelope challenge",
         h1="One envelope a day,<br><em>100 days</em>",
         envs=[("Day 1 · #63", "$63"), ("Day 2 · #8", "$8"), ("Day 3 · #21", "$21")],
         label="HOW TO RUN IT", steps=True,
         rows=[("Pick a number you haven't filled", "Big on payday, small at month end"),
               ("Put in that many dollars", "Cash goes straight into the envelope"),
               ("Cross it off the tracker", "So you can see what's left")],
         pick='A book for it: <b>APMFHO 100 Days Money Saving Challenge</b> (100 envelopes, save $5,050 or $10,000)'),
    dict(id="az9", slug="savings-challenge", themes=["light"], art=f"{A3}/happy.jpg", kicker="New year savings",
         h1="Start January 1,<br><em>done by April 10</em>",
         envs=[("Jan 1", "Day 1"), ("Feb 28", "Day 59"), ("Apr 10", "Day 100")],
         label="100 DAYS IN 2027", steps=False,
         rows=[("One envelope a day", "100 envelopes, 100 days"),
               ("Miss a day? Keep going", "Just finish later than April 10"),
               ("$5,050 at the end", "If all 100 are filled")],
         pick='A book for it: <b>APMFHO 100 Days Money Saving Challenge</b> (100 envelopes, save $5,050 or $10,000)'),
    dict(id="az10", slug="savings-challenge", themes=["light"], art=f"{A2}/asterisk.jpg", kicker="Savings challenge",
         h1="Tight week?<br><em>Pick a small envelope</em>",
         envs=[("Payday week", "#88"), ("Normal week", "#40"), ("Tight week", "#3")],
         label="MATCH THE ENVELOPE TO THE WEEK", steps=False,
         rows=[("Big numbers on payday", "When the money is actually there"),
               ("Small numbers when it's tight", "Still counts, still crosses one off"),
               ("Never borrow back", "Taking cash out undoes the habit")],
         pick='One with a tracker: <b>RONMONG 100 Envelopes Challenge Binder</b> (cash envelopes, tracker and budget sheets)'),
    # Undated budget planners.
    dict(id="az11", slug="budget-planner", themes=["light"], art=f"{A2}/check.jpg", kicker="Budget planner",
         h1="Budget planner<br><em>that starts any month</em>",
         envs=[("Month 1", "February"), ("Month 2", "March"), ("Month 3", "April")],
         label="WHY UNDATED", steps=False,
         rows=[("Start the day you decide", "No waiting for January"),
               ("Skip a month, lose no pages", "Write the month in yourself"),
               ("Track what you spend", "Each month next to the plan")],
         pick='An undated one: <b>Taja Budget Planner</b> (undated budget book with expense tracker)'),
    dict(id="az12", slug="budget-planner", themes=["light"], art=f"{A3}/check.jpg", kicker="Bill calendar",
         h1="Bills on different days?<br><em>Put them on one page</em>",
         envs=[("Phone · 4th", "$65"), ("Car · 12th", "$310"), ("Card · 23rd", "$120")],
         label="ONE BILL CALENDAR", steps=False,
         rows=[("Write every due date", "Phone, car, cards, subscriptions"),
               ("Mark the paydays too", "See which bills land before payday"),
               ("Check it every Sunday", "So a due date never sneaks up on you")],
         pick='One with bill pockets: <b>SOLIGT Budget Planner Monthly Bill Organizer</b> (undated, 12 pockets)'),
    dict(id="az13", slug="budget-planner", themes=["light"], art=f"{A3}/calc.jpg", kicker="January budget reset",
         h1="January budget reset:<br><em>4 numbers first</em>",
         envs=[("Take-home pay", "$3,800"), ("Fixed bills", "$1,950"), ("Debt minimums", "$680")],
         label="WRITE THESE BEFORE ANYTHING ELSE", steps=True,
         rows=[("Take-home pay", "What actually lands in your account"),
               ("Fixed bills", "Rent, insurance, phone"),
               ("Debt minimums", "Every card and loan"),
               ("What's left", "That's the budget for everything else")],
         pick='An undated one: <b>Taja Budget Planner</b> (undated budget book with expense tracker)'),
    dict(id="az14", slug="budget-planner", themes=["light"], art=f"{A2}/tag.jpg", kicker="Bill organizer",
         h1="Paper bills piling up?<br><em>One pocket a month</em>",
         envs=[("January", "pocket 1"), ("February", "pocket 2"), ("March", "pocket 3")],
         label="KEEP IT SIMPLE", steps=False,
         rows=[("Paid it? Into this month's pocket", "Receipt or bill, nothing else"),
               ("Need it later? It's by month", "Taxes, returns, disputes"),
               ("New year, empty pockets", "Box last year's and start again")],
         pick='One with 12 pockets: <b>SOLIGT Budget Planner Monthly Bill Organizer</b> (undated, 12 pockets)'),
    dict(id="az15", slug="budget-planner", themes=["light"], art=f"{A3}/gifts.jpg", kicker="Weekly money check",
         h1="A 10-minute<br><em>weekly money check</em>",
         envs=[("Spent this week", "$412"), ("Left this month", "$860"), ("Bills next week", "$185")],
         label="EVERY SUNDAY", steps=True,
         rows=[("Add up this week's spending", "Card, cash, apps"),
               ("Compare with what's left", "For the rest of the month"),
               ("Look at next week's bills", "So nothing surprises you")],
         pick='An undated one: <b>Taja Budget Planner</b> (undated budget book with expense tracker)'),
]


def page(p, t, mascot):
    mask = ("-webkit-mask-image:radial-gradient(ellipse 50% 50% at center,#000 70%,transparent 100%);"
            "mask-image:radial-gradient(ellipse 50% 50% at center,#000 70%,transparent 100%);") if t["mask"] else ""
    css = f"""*{{box-sizing:border-box;margin:0;padding:0}}html,body{{width:1000px;height:1500px;overflow:hidden}}
body{{position:relative;background:{t['bg']};color:{t['ink']};font-family:Inter,"Liberation Sans",sans-serif}}
.k{{position:absolute;left:64px;top:64px;font-size:24px;letter-spacing:.18em;font-weight:600;color:{t['muted']};text-transform:uppercase}}.k b{{color:{t['accent']}}}
h1{{position:absolute;left:64px;right:64px;top:118px;font-size:72px;font-weight:800;line-height:1.06}}h1 em{{font-style:normal;color:{t['accent']}}}
.binder{{position:absolute;left:64px;top:330px;width:520px;height:330px;border-radius:28px;background:{t['binder']};border:3px solid {t['line']}}}
.ring{{position:absolute;left:22px;width:26px;height:26px;border-radius:50%;border:5px solid {t['muted']}}}
.env{{position:absolute;left:80px;width:410px;height:120px;border-radius:16px;padding:16px 24px;font-size:30px;font-weight:800;color:#2E2B36;box-shadow:0 10px 24px rgba(0,0,0,.18)}}
.zip{{position:absolute;left:24px;right:24px;bottom:22px;height:8px;border-radius:4px;background:repeating-linear-gradient(90deg,rgba(46,43,54,.55) 0 8px,transparent 8px 14px)}}
.amt{{position:absolute;right:24px;top:16px;font-size:26px;font-weight:600;opacity:.75}}
.pose{{position:absolute;right:40px;top:320px;width:330px;{mask}}}
.card{{position:absolute;left:64px;right:64px;top:720px;background:{t['card']};border:2px solid {t['line']};border-radius:26px;padding:26px 40px;box-shadow:0 20px 60px rgba(0,0,0,.18)}}
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
    body = (f'<div class="k"><b>CheckMaybe</b> · {p["kicker"]}</div><h1>{p["h1"]}</h1>'
            f'<div class="binder">{rings}{env_html}</div><img class="pose" src="file://{mascot}">'
            f'<div class="card"><div class="lab">{p["label"]}</div>{rows_html}</div>'
            f'<div class="pick">{p["pick"]}<br><span class="tag">See it on Amazon</span></div>'
            f'<div class="foot"><span>As an Amazon Associate I earn from qualifying purchases. Example amounts.</span><span>checkmaybe</span></div>')
    return f'<!doctype html><html><head><meta charset="utf-8"><style>{css}</style></head><body>{body}</body></html>'


jobs = []
for p in PINS:
    for th in p["themes"]:
        t = DARK if th == "dark" else LIGHT
        mascot = p["art"] if th == "dark" else cutout(p["art"], p["id"])
        src = f"{TMP}/{p['id']}-{th}.html"
        open(src, "w").write(page(p, t, mascot))
        name = f"checkmaybe-pin-{p['id']}-{p.get('slug', 'budget-binder')}" + (f"-{th}" if p["id"] == "az1" else "")
        jobs.append([src, f"{OUT}/{name}.png"])
js = f"""import {{ chromium }} from '/opt/node22/lib/node_modules/playwright/index.mjs';
const jobs = {json.dumps(jobs)}; const b = await chromium.launch();
for (const [s, o] of jobs) {{ const p = await b.newPage({{ viewport: {{ width: 1000, height: 1500 }} }});
  await p.goto('file://' + s); await p.evaluate(() => document.fonts.ready); await p.screenshot({{ path: o }}); console.log(o.split('/').pop()); await p.close(); }}
await b.close();"""
open(f"{TMP}/shoot.mjs", "w").write(js)
subprocess.run(["node", f"{TMP}/shoot.mjs"], check=True)
