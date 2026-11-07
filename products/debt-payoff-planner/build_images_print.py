"""Extra listing image for the Print tab (Gumroad gallery + Beacons). Run after build_images.py if crops change."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "build"))
from listing_images import Builder
PAL = dict(BG="#15171F", PANEL="#1E2130", PANEL2="#232739", LINE="#33384F", TXT="#EDEBF5", MUTED="#9A98AE", ACC="#F08A4B",
           RED="#FF6B6B", GREEN="#5FD38D", AMBER="#F2B544", BLUE="#8AB4FF", GLOW1="rgba(240,138,75,.16)", GLOW2="rgba(79,195,199,.10)")
B = Builder("debt-payoff-planner", "Debt Payoff Planner", PAL, os.path.join(HERE, "images", "crops"), os.path.join(HERE, "images"))
LEFT = ('<h1>Print it.<br><em>Color it.</em></h1>'
        '<div class="abs" style="left:56px;top:300px;width:520px"><ul class="inc">'
        '<li>A one-page color-in tracker built from your own plan</li>'
        '<li>Your debts in payoff order, your real amount in every box</li>'
        '<li>The month you\'ll reach every 5% of your total</li>'
        '<li>0% deadlines and lender notes under each debt</li>'
        '<li>Change your debts and the page updates</li></ul></div>')
B.add("gumroad", "gumroad-print", B.page(1280, 720, LEFT + B.shot("print_page", "left:700px;top:36px;width:480px")), 1280, 720, 2)
B.add("beacons", "beacons-print", B.page(1080, 1080, '<h1 style="font-size:84px">Print it.<br><em>Color it.</em></h1>'
      '<div class="sub" style="font-size:30px">Every box is your real number</div>'
      + B.shot("print_page", "left:305px;top:370px;width:470px")), 1080, 1080, 1)
B.render()
