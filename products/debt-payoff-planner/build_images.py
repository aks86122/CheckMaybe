"""Debt Payoff Planner listing images. Crops in images/crops are real sheet renders (example rows)."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "build"))
from listing_images import Builder
PAL = dict(BG="#15171F", PANEL="#1E2130", PANEL2="#232739", LINE="#33384F", TXT="#EDEBF5", MUTED="#9A98AE", ACC="#F08A4B",
           RED="#FF6B6B", GREEN="#5FD38D", AMBER="#F2B544", BLUE="#8AB4FF", GLOW1="rgba(240,138,75,.16)", GLOW2="rgba(79,195,199,.10)")
B = Builder("debt-payoff-planner", "Debt Payoff Planner", PAL, os.path.join(HERE, "images", "crops"), os.path.join(HERE, "images"))
CHIPS = ('<div class="chips"><span class="chip o">4 payoff orders</span><span class="chip a">Early-payoff fees</span>'
         '<span class="chip r">0% deadlines</span><span class="chip g">Any currency</span></div>')
W, H = 1200, 900
ETSY = {
 "01-hero": B.page(W, H, '<h1>Snowball or avalanche?<br><em>Compare 4 payoff orders</em></h1>' + CHIPS
                   + '<div class="abs" style="left:56px;top:330px;width:440px"><ul class="inc">'
                     '<li>Debt-free date, interest and fees side by side</li><li>Early-payoff fees and lock-in periods</li>'
                     '<li>0% / deferred-interest deadlines</li><li>Behind-on-payments first</li><li>Only 4 things needed per debt</li></ul></div>'
                   + B.win("plan_full", "left:530px;top:300px;width:620px")),
 "02-compare": B.page(W, H, '<h1>Same debts, 4 orders.<br>See <em>which costs less</em></h1>'
                      '<div class="sub">Smart, Avalanche, Snowball and Cash-flow: debt-free month, total interest, early-payoff fees, first debt cleared.</div>'
                      + B.shot("plan_compare", "left:56px;top:380px;width:1088px")
                      + '<div class="abs card" style="left:56px;top:640px;width:1088px"><p><b class="r">Avalanche</b> pays the least interest on paper here, but misses the store card\'s 0% deadline. <b class="g">Smart</b> clears it in time.</p></div>'),
 "03-fee": B.page(W, H, '<h1>Early-payoff fee:<br><em>worth paying?</em></h1>'
                  '<div class="sub">The sheet compares the fee with the interest you\'d save. If the fee costs more, extra payments wait until it ends.</div>'
                  + B.shot("mydebts_check", "left:150px;top:330px;width:900px")
                  + '<div class="abs card" style="left:230px;top:700px;width:740px;text-align:center"><p style="font-size:24px">Car loan: <b class="a">$400 fee</b> vs about $1,317 interest at minimums<br>→ <b class="g">worth it, saves about $917</b></p></div>'),
 "04-deadlines": B.page(W, H, '<h1>0% deals have<br><em>a deadline</em></h1>'
                        '<div class="sub">Enter when the promo ends and the APR after it. Deferred interest? Smart clears it in time, and you get a warning if an order doesn\'t.</div>'
                        + B.shot("plan_order", "left:56px;top:400px;width:1088px") + B.shot("plan_checks", "left:200px;top:580px;width:800px")),
 "05-results": B.page(W, H, '<h1>Your <em>debt-free date</em>,<br>and what you save</h1>'
                      '<div class="sub">Interest and fees for your chosen order, compared with paying minimums only.</div>'
                      + B.shot("plan_kpi", "left:300px;top:350px;width:600px")),
 "06-schedule": B.page(W, H, '<h1>Month by month,<br><em>every debt</em></h1>'
                       '<div class="sub">Up to 12 debts and 30 years. Extra money rolls to the next debt when one is cleared.</div>'
                       + B.shot("schedule", "left:170px;top:350px;width:860px")),
 "07-rules": B.page(W, H, '<h1>Real contracts<br><em>have rules</em></h1>'
                    '<div class="abs" style="left:56px;top:270px;width:1088px;display:grid;grid-template-columns:1fr 1fr 1fr 1fr;gap:14px">'
                    '<div class="card"><h3 class="g">Allowed, no fee</h3><p>Extra money can go here any time. Blank counts as this.</p></div>'
                    '<div class="card"><h3 class="a">Allowed with a fee</h3><p>Fee vs interest saved: pay early only when it\'s worth it.</p></div>'
                    '<div class="card"><h3 class="b">Locked until a date</h3><p>Minimums only until it unlocks.</p></div>'
                    '<div class="card"><h3 class="r">Not sure</h3><p>Minimums only. Ask your lender, then change the rule.</p></div></div>'
                    + B.shot("mydebts_left", "left:200px;top:560px;width:800px")),
 "08-easy": B.page(W, H, '<h1>Only <em>4 things</em><br>needed per debt</h1>'
                   '<div class="abs" style="left:56px;top:300px;width:1088px;display:grid;grid-template-columns:repeat(4,1fr);gap:16px">'
                   '<div class="card"><h3>Name</h3></div><div class="card"><h3>Balance</h3></div><div class="card"><h3>APR</h3></div><div class="card"><h3>Minimum</h3></div></div>'
                   '<div class="abs" style="left:56px;top:430px;width:1088px"><ul class="inc">'
                   '<li>Everything else is optional: blank means no fee, no lock, no promo, not behind</li>'
                   '<li>Blank rows anywhere are fine</li><li>Works in any currency</li><li>One-time extra (bonus, tax refund) in the month you choose</li>'
                   '<li>Checks: budget below minimums, minimums that don\'t cover interest</li></ul></div>', example=False),
 "09-three-steps": B.page(W, H, '<h1>Ready in <em>3 steps</em></h1>'
                     '<div class="abs" style="left:56px;top:250px;width:1088px;display:grid;grid-template-columns:1fr 1fr 1fr;gap:20px">'
                     '<div class="card"><div class="num">1</div><h3>Make your copy</h3><p>Open the link in the PDF and press Make a copy. It saves to your own Google Drive.</p></div>'
                     '<div class="card"><div class="num">2</div><h3>List your debts</h3><p>Name, balance, APR, minimum. Add rules and promo dates if you have them.</p></div>'
                     '<div class="card"><div class="num">3</div><h3>Set your plan</h3><p>Monthly amount and payoff order. Compare all four.</p></div></div>'
                     + B.shot("plan_compare", "left:56px;top:580px;width:1088px")),
 "10-included": B.page(W, H, '<h1>What\'s <em>included</em></h1>'
                       '<div class="abs" style="left:56px;top:230px;width:580px"><ul class="inc">'
                       '<li>Google Sheets planner (copy link in the PDF)</li><li>Works in Excel too: File › Download › .xlsx</li>'
                       '<li>Tabs: Start Here, Plan, My Debts, Schedule</li><li>Up to 12 debts, 30-year schedule, 2 charts</li>'
                       '<li>4-page PDF guide</li><li>Digital download, nothing is shipped</li></ul>'
                       '<p style="font-size:16px;color:#6E6C80;margin-top:22px">Estimates only. Not financial advice. Example rows are made up.</p></div>'
                       + B.shot("dpp_guide1", "left:700px;top:200px;width:444px"), example=False),
}
for n, html in ETSY.items(): B.add("etsy", f"etsy-{n}", html, W, H, 2.5)
B.add("gumroad", "gumroad-cover", B.page(1280, 720, '<h1>Snowball or avalanche? <em>Compare 4 payoff orders</em></h1>' + CHIPS
      + B.win("plan_compare", "left:56px;top:360px;width:1168px")), 1280, 720, 2)
SQ = lambda w: B.page(w, w, f'<h1 style="font-size:{round(w*.11)}px">Debt Payoff<br><em>Planner</em></h1>'
                      f'<div class="sub" style="font-size:{round(w*.04)}px">4 orders · early-payoff fees · 0% deadlines</div>'
                      + B.win("plan_kpi", f"left:{round(w*.18)}px;top:{round(w*.5)}px;width:{round(w*.64)}px"))
B.add("gumroad", "gumroad-thumb", SQ(600), 600, 600, 2)
B.add("beacons", "beacons-product", SQ(540), 540, 540, 2)
B.render()
