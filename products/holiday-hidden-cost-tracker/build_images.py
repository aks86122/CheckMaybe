"""Holiday Hidden Cost Tracker listing images. Crops in images/crops are real sheet renders (example rows)."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "build"))
from listing_images import Builder
PAL = dict(BG="#101A14", PANEL="#17251D", PANEL2="#1F3127", LINE="#2C4436", TXT="#F3EFE4", MUTED="#A9B5AC", ACC="#E0B05A",
           RED="#E2687B", GREEN="#74D39A", AMBER="#E0B05A", BLUE="#8AB4FF", GLOW1="rgba(224,176,90,.16)", GLOW2="rgba(226,104,123,.12)")
B = Builder("holiday-hidden-cost-tracker", "Holiday Hidden Cost Tracker", PAL, os.path.join(HERE, "images", "crops"), os.path.join(HERE, "images"))
CHIPS = ('<div class="chips"><span class="chip r">January bills</span><span class="chip o">Gift budget</span>'
         '<span class="chip a">Real APR</span><span class="chip g">Free-trial countdown</span></div>')
W, H = 1200, 900
ETSY = {
 "01-hero": B.page(W, H, '<h1>What the holidays will<br><em>still cost you in January</em></h1>' + CHIPS + B.win("dash_full", "left:600px;top:300px;width:540px")
                   + '<div class="abs" style="left:56px;top:330px;width:500px"><ul class="inc">'
                     '<li>Gift budget: planned, spent, left</li><li>Every pay-in-4 and store plan added up by month</li>'
                     '<li>Real APR hidden in "small" monthly prices</li><li>Free-trial cancel-by dates</li><li>Google Sheets + Excel</li></ul></div>'),
 "02-january": B.page(W, H, '<h1>See <em>January\'s bill</em><br>before you check out</h1>'
                      '<div class="sub">Every holiday payment plan, added up month by month, as a share of your take-home pay.</div>'
                      + B.shot("dash_month", "left:56px;top:350px;width:1088px")),
 "03-budget": B.page(W, H, '<h1>Your holiday money<br><em>at a glance</em></h1>'
                     '<div class="sub">Budget, spent, left, gifts sorted, what\'s due next month and the month after.</div>'
                     + B.shot("dash_kpi", "left:56px;top:360px;width:1088px")),
 "04-real-apr": B.page(W, H, '<h1>That 6 × $89.50 console?<br><em>About 25.7% APR</em></h1>'
                       '<div class="sub">Enter the price, the payment and how many payments. The sheet works out the extra cost and the real yearly rate.</div>'
                       + B.shot("payments_left", "left:130px;top:370px;width:940px")),
 "05-gifts": B.page(W, H, '<h1>Every person, every gift,<br><em>one list</em></h1>'
                    '<div class="sub">Budget vs actual, how you paid, and which gifts are on a payment plan.</div>'
                    + B.shot("gifts", "left:130px;top:350px;width:940px")),
 "06-trials": B.page(W, H, '<h1>Cancel holiday free trials<br><em>before they charge</em></h1>'
                     '<div class="sub">Cancel-by date, countdown and the yearly cost if you keep it.</div>'
                     + B.shot("trials", "left:80px;top:360px;width:1040px")),
 "07-ranked": B.page(W, H, '<h1>Payment plans ranked<br>by <em>real APR</em></h1>'
                     '<div class="sub">HIGH / CHECK / OK flags, what\'s still to buy, and how you paid for gifts.</div>'
                     + B.shot("dash_lower", "left:200px;top:340px;width:800px")),
 "08-three-steps": B.page(W, H, '<h1>Ready in <em>3 steps</em></h1>'
                     '<div class="abs" style="left:56px;top:250px;width:1088px;display:grid;grid-template-columns:1fr 1fr 1fr;gap:20px">'
                     '<div class="card"><div class="num">1</div><h3>Make your copy</h3><p>Open the link in the PDF and press Make a copy. It saves to your own Google Drive.</p></div>'
                     '<div class="card"><div class="num">2</div><h3>Settings</h3><p>Holiday budget, monthly take-home pay, first month to plan.</p></div>'
                     '<div class="card"><div class="num">3</div><h3>Add gifts &amp; plans</h3><p>The dashboard, charts and January total fill in on their own.</p></div></div>'
                     + B.shot("dash_kpi", "left:150px;top:560px;width:900px")),
 "09-pair": B.page(W, H, '<h1>Pair it with<br><em>Hidden Cost Tracker</em></h1>'
                   '<div class="sub">The all-year version: debts, installments and subscriptions.</div>'
                   '<div class="abs" style="left:56px;top:360px;width:1088px;display:grid;grid-template-columns:1fr 1fr;gap:20px">'
                   '<div class="card"><h3>Holiday edition</h3><p>Gifts, holiday payment plans, January bills, holiday free trials.</p></div>'
                   '<div class="card"><h3>Hidden Cost Tracker</h3><p>All debts and installments with real APR, subscriptions, debt-free date.</p></div></div>'
                   '<div class="abs card" style="left:330px;top:600px;width:540px;text-align:center"><h3 class="o" style="font-size:34px">Both for $12</h3><p>Look for the bundle in the shop.</p></div>', example=False),
 "10-included": B.page(W, H, '<h1>What\'s <em>included</em></h1>'
                       '<div class="abs" style="left:56px;top:230px;width:580px"><ul class="inc">'
                       '<li>Google Sheets tracker (copy link in the PDF)</li><li>Works in Excel too: File › Download › .xlsx</li>'
                       '<li>Tabs: Dashboard, Gift List, Holiday Payments, Free Trials, Settings, How to Use</li>'
                       '<li>Dark green &amp; gold theme, charts, filters, colour tags</li><li>4-page PDF guide</li><li>Digital download, nothing is shipped</li></ul>'
                       '<p style="font-size:16px;color:#7E8C82;margin-top:22px">Estimates only. Not financial advice. Example rows are made up.</p></div>'
                       + B.shot("hol_guide1", "left:700px;top:200px;width:444px"), example=False),
}
for n, html in ETSY.items(): B.add("etsy", f"etsy-{n}", html, W, H, 2.5)
B.add("gumroad", "gumroad-cover", B.page(1280, 720, '<h1>What the holidays will <em>still cost you in January</em></h1>' + CHIPS
      + B.win("dash_month", "left:440px;top:330px;width:790px")), 1280, 720, 2)
SQ = lambda w: B.page(w, w, f'<h1 style="font-size:{round(w*.105)}px">Holiday Hidden<br><em>Cost Tracker</em></h1>'
                      f'<div class="sub" style="font-size:{round(w*.04)}px">Gift budget · January bills · real APR</div>'
                      + B.win("dash_kpi", f"left:{round(w*.06)}px;top:{round(w*.55)}px;width:{round(w*.88)}px"))
B.add("gumroad", "gumroad-thumb", SQ(600), 600, 600, 2)
B.add("beacons", "beacons-product", SQ(540), 540, 540, 2)
B.render()
