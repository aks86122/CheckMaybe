"""Debt Toolkit Bundle: Gumroad cover/thumb, Beacons square and one Etsy hero. Crops are real sheet renders."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "build"))
from listing_images import Builder
PAL = dict(BG="#15171F", PANEL="#1E2130", PANEL2="#232739", LINE="#33384F", TXT="#EDEBF5", MUTED="#9A98AE", ACC="#F08A4B",
           RED="#FF6B6B", GREEN="#5FD38D", AMBER="#F2B544", BLUE="#8AB4FF", GLOW1="rgba(240,138,75,.16)", GLOW2="rgba(224,176,90,.12)")
B = Builder("debt-toolkit-bundle", "Debt Toolkit Bundle", PAL, os.path.join(HERE, "images", "crops"), os.path.join(HERE, "images"))
CHIPS = ('<div class="chips"><span class="chip r">Hidden Cost Tracker</span><span class="chip o">Debt Payoff Planner</span>'
         '<span class="chip a">Holiday edition</span><span class="chip g">Save $7</span></div>')
STACK = lambda x, y, w: (B.win("hct_kpi", f"left:{x}px;top:{y}px;width:{w}px")
                         + B.win("plan_compare", f"left:{x + 40}px;top:{y + round(w*.30)}px;width:{w}px")
                         + B.win("dash_month", f"left:{x + 80}px;top:{y + round(w*.47)}px;width:{w}px"))
B.add("etsy", "etsy-01-hero", B.page(1200, 900, '<h1>The <em>Debt Toolkit</em>:<br>3 Google Sheets, one price</h1>' + CHIPS
      + '<div class="abs" style="left:56px;top:330px;width:420px"><ul class="inc"><li>See what every debt and subscription really costs</li>'
        '<li>Plan the payoff order, fees and 0% deadlines included</li><li>Holiday gifts and January bills</li>'
        '<li>$22 separately, <b style="color:#5FD38D">$15 together</b></li></ul></div>' + STACK(480, 300, 600)), 1200, 900, 2.5)
B.add("gumroad", "gumroad-cover", B.page(1280, 720, '<h1>The <em>Debt Toolkit</em></h1><div class="sub">3 Google Sheets, one price · $22 separately, $15 together</div>' + CHIPS
      + STACK(660, 275, 480)), 1280, 720, 2)
SQ = lambda w: B.page(w, w, f'<h1 style="font-size:{round(w*.11)}px">Debt<br><em>Toolkit</em></h1>'
                      f'<div class="sub" style="font-size:{round(w*.04)}px">3 trackers · $22 → $15</div>' + STACK(round(w*.06), round(w*.44), round(w*.62)))
B.add("gumroad", "gumroad-thumb", SQ(600), 600, 600, 2)
B.add("beacons", "beacons-product", SQ(540), 540, 540, 2)
B.render()
