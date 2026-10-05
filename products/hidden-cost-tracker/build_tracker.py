"""Hidden Cost Tracker (dark theme): debts & installments with real-APR back-calc, subscriptions with
free-trial cancel-by dates, and a dashboard of monthly committed money.

Builds hidden-cost-tracker-prototype.xlsx. For the Google Sheets version, import the file, save it as a
Google Sheet, then run sheets_polish.gs once (checkboxes, slicers, native dark charts)."""
import datetime as dt
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.formatting.rule import FormulaRule, CellIsRule
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.chart import BarChart, DoughnutChart, Reference
from openpyxl.chart.label import DataLabelList
from openpyxl.chart.series import DataPoint
from openpyxl.chart.shapes import GraphicalProperties
from openpyxl.chart.text import RichText
from openpyxl.drawing.line import LineProperties
from openpyxl.drawing.text import Paragraph, ParagraphProperties, CharacterProperties
from openpyxl.comments import Comment

BG, PANEL, PANEL2, INPUT, INPUT2, LINE, HEAD = "15171F", "1E2130", "232739", "262A3D", "2C3147", "33384F", "10121A"
TXT, MUTED, BLUE, ORANGE, RED, AMBER, GREEN, TEAL = "EDEBF5", "9A98AE", "8AB4FF", "F08A4B", "FF6B6B", "F2B544", "5FD38D", "4FC3C7"
PURPLE, PINK = "B18CFF", "F06BC8"
CHIP = {"purple": (PURPLE, "2E2250"), "pink": (PINK, "3D1B35"), "teal": (TEAL, "16373A"), "amber": (AMBER, "4A3A15"),
        "green": (GREEN, "173A28"), "red": (RED, "4A1D22"), "blue": (BLUE, "1C2B4A"), "orange": (ORANGE, "4A2A18"),
        "grey": ("B8B6C8", "2F3242")}
F = lambda c=TXT, b=False, s=10, i=False, strike=False: Font(name="Arial", color=c, bold=b, size=s, italic=i, strike=strike)
# Conditional-format fonts: colour/bold only. Font name or size in a dxf makes desktop Excel 'repair' styles.xml and drop all formatting.
FD = lambda c=TXT, b=False, *_a, **_k: Font(color=c, bold=b)
fill = lambda c: PatternFill("solid", fgColor=c)
thin = Side(style="thin", color=LINE); BOX = Border(left=thin, right=thin, top=thin, bottom=thin)
CUR, PCT, DATE = '$#,##0.00;($#,##0.00);"-"', '0.0%;-0.0%;"-"', 'mmm d, yyyy'
DAYS = '[=0]"Today";[=1]"Tomorrow";0" days"'

wb = Workbook()
def sheet(name, widths, first=False, rows=40, cols=12):
    ws = wb.active if first else wb.create_sheet(name)
    ws.title = name; ws.sheet_view.showGridLines = False
    for col, w in widths.items(): ws.column_dimensions[col].width = w
    for r in range(1, rows + 1):
        for c in range(1, cols + 1): ws.cell(r, c).fill = fill(BG)
    return ws

def title(ws, text, sub=None):
    ws["B2"] = text; ws["B2"].font = F(TXT, True, 18)
    ws.row_dimensions[2].height = 30
    if sub: ws["B3"] = sub; ws["B3"].font = F(MUTED, False, 10, True)

def header(ws, row, col, labels, color=ORANGE):
    for i, l in enumerate(labels):
        c = ws.cell(row, col + i, l.upper()); c.font = F(color, True, 8); c.fill = fill(HEAD)
        c.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        c.border = Border(left=thin, right=thin, top=thin, bottom=Side(style="medium", color=color))
    ws.row_dimensions[row].height = 34

def cell(ws, ref, v, fmt=None, inp=False, bold=False, color=None, align="left", band=False, size=10):
    c = ws[ref]; c.value = v; c.border = BOX
    c.fill = fill((INPUT2 if band else INPUT) if inp else (PANEL2 if band else PANEL))
    c.font = F(color or TXT, bold, size)
    c.alignment = Alignment(horizontal=align, vertical="center")
    if fmt: c.number_format = fmt
    return c

def chips(ws, rng, mapping):
    """Colour-coded 'chip' look for drop-down values (conditional formatting, works in Excel and Sheets)."""
    for v, name in mapping.items():
        fg, bg = CHIP[name]
        ws.conditional_formatting.add(rng, CellIsRule(operator="equal", formula=[f'"{v}"'], fill=fill(bg), font=FD(fg, True, 9)))

def listdv(ws, src, rng):
    v = DataValidation(type="list", formula1=src, allow_blank=True); ws.add_data_validation(v); v.add(rng)

# ---------------- Settings ----------------
st = sheet("Settings", {"A": 3, "B": 34, "C": 16, "D": 18, "E": 16, "F": 40}, rows=24, cols=7)
title(st, "Settings", "Blue-header cells are yours to edit.")
header(st, 4, 2, ["Setting", "Value"], BLUE); header(st, 4, 4, ["What it does"], MUTED)
st.merge_cells("D4:F4")
rows = [("Monthly take-home income", 4200, CUR, "Your income after tax, per month."),
        ("High-cost APR (red flag)", 0.20, PCT, "Any debt at or above this APR is flagged HIGH."),
        ("Check APR (amber flag)", 0.10, PCT, "At or above this APR is flagged CHECK."),
        ("Warn me this many days ahead", 7, "0", "Trials and bills due within this many days are highlighted."),
        ("Today's date", "=TODAY()", DATE, "Updates automatically. Every date calculation uses it.")]
for i, (lab, val, fmt, note) in enumerate(rows):
    r = 5 + i
    cell(st, f"B{r}", lab); cell(st, f"C{r}", val, fmt, inp=(i < 4), align="right", color=BLUE if i < 4 else MUTED)
    st.merge_cells(f"D{r}:F{r}"); st[f"D{r}"] = note; st[f"D{r}"].font = F(MUTED, False, 9, True)
    st.row_dimensions[r].height = 22
INCOME, RED_APR, AMB_APR, WARN, TODAY = "Settings!$C$5", "Settings!$C$6", "Settings!$C$7", "Settings!$C$8", "Settings!$C$9"
header(st, 12, 2, ["Debt types", "Billing", "Categories", "Paid with"], MUTED)
lists = {"B": ["Credit card", "Loan", "Installment", "BNPL", "Family / friend", "Other"],
         "C": ["Weekly", "Monthly", "Quarterly", "Yearly"],
         "D": ["Streaming", "Software", "Fitness", "Shopping", "News", "Cloud", "Food", "Education", "Other"],
         "E": ["Credit card", "Debit card", "PayPal", "Apple Pay", "Google Pay", "Bank transfer", "Other"]}
for col, items in lists.items():
    for j in range(9):
        cell(st, f"{col}{13 + j}", items[j] if j < len(items) else None, inp=True, color=TXT, band=j % 2 == 1)
st["F13"] = "Rename or add items here and the drop-downs follow."; st["F13"].font = F(MUTED, False, 9, True)
DEBT_TYPES, BILLING, CATS, PAID = "=Settings!$B$13:$B$18", "=Settings!$C$13:$C$16", "=Settings!$D$13:$D$21", "=Settings!$E$13:$E$21"

# ---------------- Debts ----------------
de = sheet("Debts & Installments", {"A": 3, "B": 24, "C": 14, "D": 13, "E": 12, "F": 11, "G": 10, "H": 12, "I": 13,
                                    "J": 11, "K": 11, "L": 13, "M": 13, "N": 13, "O": 14, "P": 10, "Q": 10, "R": 10, "S": 4}, rows=27, cols=20)
title(de, "Debts & Installments")
de["M2"] = "BLUE headers: you fill in   ·   ORANGE headers: calculated for you"; de["M2"].font = F(MUTED, False, 8, True)
de.row_dimensions[4].height = 40                                           # room for the Sheets slicers
cols = ["Name", "Type", "Original amount", "Monthly payment", "Total payments", "Payments made", "Stated APR (if known)",
        "Balance now (if known)", "Real APR", "Payments left", "Balance (est.)", "Still to pay", "Interest still to pay",
        "Debt-free date", "Avalanche order", "Snowball order", "Flag"]
header(de, 5, 2, cols[:8], BLUE); header(de, 5, 10, cols[8:], ORANGE)
sample = [("Credit card", "Credit card", None, 120, None, None, 0.2499, 3200),
          ("Store credit card", "Credit card", None, 40, None, None, 0.2999, 850),
          ("Car loan", "Loan", None, 330, None, None, 0.069, 14500),
          ("Student loan", "Loan", None, 110, None, None, 0.055, 9800),
          ("Phone installment plan", "Installment", 1200, 67, 24, 6, None, None),
          ("Sofa store financing", "Installment", 2000, 105, 24, 3, None, None),
          ("Laptop pay-in-4", "BNPL", 800, 200, 4, 1, None, None),
          ("Loan from family", "Family / friend", None, 100, None, None, 0, 1500)]
N0, N1 = 6, 25
for r in range(N0, N1 + 1):
    s = sample[r - N0] if r - N0 < len(sample) else (None,) * 8
    band = (r - N0) % 2 == 1
    for j, (col, fmt) in enumerate(zip("BCDEFGHI", [None, None, CUR, CUR, "0", "0", PCT, CUR])):
        cell(de, f"{col}{r}", s[j], fmt, inp=True, band=band, align={0: "left", 1: "center"}.get(j, "right"))
    has = f"AND($B{r}<>\"\",$E{r}>0)"
    apr = f'IF(NOT({has}),"",IF(ISNUMBER($H{r}),$H{r},IF(AND($D{r}>0,$F{r}>0),IFERROR(RATE($F{r},-$E{r},$D{r})*12,""),"")))'
    f = {"J": f"={apr}",
         "K": f'=IF(NOT({has}),"",IF($F{r}>0,MAX(0,$F{r}-N($G{r})),IF(AND(ISNUMBER($I{r}),ISNUMBER($J{r})),IF($J{r}=0,ROUNDUP($I{r}/$E{r},0),IFERROR(ROUNDUP(NPER($J{r}/12,-$E{r},$I{r}),0),"Never")),"")))',
         "L": f'=IF(NOT({has}),"",IF(ISNUMBER($I{r}),$I{r},IF(AND(ISNUMBER($K{r}),ISNUMBER($J{r})),IF($J{r}=0,$E{r}*$K{r},PV($J{r}/12,$K{r},-$E{r})),"")))',
         "M": f'=IF(ISNUMBER($K{r}),$E{r}*$K{r},"")',
         "N": f'=IF(AND(ISNUMBER($M{r}),ISNUMBER($L{r})),MAX(0,$M{r}-$L{r}),"")',
         "O": f'=IF(ISNUMBER($K{r}),EDATE({TODAY},$K{r}),"")',
         "P": f'=IF(ISNUMBER($J{r}),COUNTIF($J${N0}:$J${N1},">"&$J{r})+1,"")',
         "Q": f'=IF(ISNUMBER($L{r}),COUNTIF($L${N0}:$L${N1},"<"&$L{r})+1,"")',
         "R": f'=IF(NOT(ISNUMBER($J{r})),"",IF($J{r}>={RED_APR},"HIGH",IF($J{r}>={AMB_APR},"CHECK","OK")))'}
    for col, fx in f.items():
        fmt = {"J": PCT, "K": "0", "L": CUR, "M": CUR, "N": CUR, "O": DATE, "P": "0", "Q": "0"}.get(col)
        cell(de, f"{col}{r}", fx, fmt, band=band, align="center" if col in "KPQR" else "right")
    de[f"S{r}"] = f'=IF(ISNUMBER($J{r}),$J{r}+ROW()/10000000,"")'               # sort key for the dashboard
    de.row_dimensions[r].height = 22
de["S5"] = "key"; de.column_dimensions["S"].hidden = True
dr = lambda c: f"'Debts & Installments'!${c}${N0}:${c}${N1}"
de["B3"] = (f'=COUNT({dr("J")})&" debts   ·   owed now "&TEXT(SUM({dr("L")}),"$#,##0")&"   ·   paying "&TEXT(SUM({dr("E")}),"$#,##0")'
            f'&" a month   ·   interest still to pay "&TEXT(SUM({dr("N")}),"$#,##0")&"   ·   debt-free "&IF(COUNT({dr("O")})=0,"-",TEXT(MAX({dr("O")}),"mmm yyyy"))')
de["B3"].font = F(TXT, True, 10)
de["J5"].comment = Comment("Stated APR if you entered one. Otherwise worked out with RATE() from original amount, monthly payment and number of payments. An estimate: fees charged separately are not included. Your contract is the final word.", "CheckMaybe")
listdv(de, DEBT_TYPES, f"C{N0}:C{N1}")
chips(de, f"C{N0}:C{N1}", {"Credit card": "red", "Loan": "blue", "Installment": "amber", "BNPL": "pink", "Family / friend": "teal", "Other": "grey"})
chips(de, f"R{N0}:R{N1}", {"HIGH": "red", "CHECK": "amber", "OK": "green"})
de.conditional_formatting.add(f"J{N0}:J{N1}", FormulaRule(formula=[f'AND(ISNUMBER($J{N0}),$J{N0}>={RED_APR})'], font=FD(RED, True)))
de.conditional_formatting.add(f"P{N0}:P{N1}", CellIsRule(operator="equal", formula=["1"], fill=fill(CHIP["orange"][1]), font=FD(ORANGE, True)))
de.auto_filter.ref = f"B5:R{N1}"

# ---------------- Subscriptions ----------------
su = sheet("Subscriptions", {"A": 3, "B": 22, "C": 13, "D": 11, "E": 12, "F": 13, "G": 13, "H": 11, "I": 10, "J": 10,
                             "K": 9, "L": 12, "M": 12, "N": 14, "O": 11, "P": 14, "Q": 10, "R": 14, "S": 4, "T": 4, "U": 4}, rows=37, cols=22)
title(su, "Subscriptions & Free Trials")
su["M2"] = "BLUE headers: you fill in   ·   ORANGE headers: calculated for you"; su["M2"].font = F(MUTED, False, 8, True)
su.row_dimensions[4].height = 40
scol = ["Name", "Category", "Price", "Billing", "Start date", "Paid with", "Auto-renew?", "Cancel it?", "Free trial?", "Trial days",
        "Monthly cost", "Yearly cost", "Next charge", "Days to charge", "Trial: cancel by", "Trial days left", "Alert"]
header(su, 5, 2, scol[:10], BLUE); header(su, 5, 12, scol[10:], ORANGE)
d = lambda y, m, dd: dt.date(y, m, dd)
Y, N = "Yes", "No"
ssample = [("Netflix", "Streaming", 15.49, "Monthly", d(2025, 3, 5), "Credit card", Y, N, N, None),
           ("Spotify", "Streaming", 11.99, "Monthly", d(2024, 11, 20), "PayPal", Y, N, N, None),
           ("Disney+", "Streaming", 13.99, "Monthly", d(2025, 8, 12), "Credit card", Y, Y, N, None),
           ("YouTube Premium", "Streaming", 13.99, "Monthly", d(2025, 5, 28), "Google Pay", Y, N, N, None),
           ("Sports streaming", "Streaming", 9.99, "Monthly", d(2026, 9, 24), "Credit card", Y, N, Y, 7),
           ("Gym membership", "Fitness", 45, "Monthly", d(2025, 1, 10), "Debit card", Y, Y, N, None),
           ("Yoga app", "Fitness", 69.99, "Yearly", d(2026, 1, 15), "Apple Pay", Y, N, N, None),
           ("Photo editing app", "Software", 22.99, "Monthly", d(2026, 2, 14), "Credit card", Y, N, N, None),
           ("AI assistant", "Software", 20, "Monthly", d(2025, 9, 3), "Credit card", Y, N, N, None),
           ("Password manager", "Software", 35.88, "Yearly", d(2025, 12, 1), "Credit card", Y, N, N, None),
           ("VPN", "Software", 59.88, "Yearly", d(2026, 2, 20), "PayPal", Y, N, N, None),
           ("Online shopping club", "Shopping", 139, "Yearly", d(2025, 10, 2), "Credit card", Y, N, N, None),
           ("Beauty box", "Shopping", 28, "Monthly", d(2025, 7, 18), "Debit card", Y, Y, N, None),
           ("Cloud storage", "Cloud", 2.99, "Monthly", d(2025, 6, 1), "Apple Pay", Y, N, N, None),
           ("Meal kit", "Food", 59.99, "Weekly", d(2026, 9, 20), "Credit card", Y, N, Y, 14),
           ("Coffee subscription", "Food", 18, "Monthly", d(2026, 4, 9), "PayPal", Y, N, N, None),
           ("News site", "News", 4.99, "Monthly", d(2026, 9, 15), "PayPal", Y, Y, Y, 30),
           ("Language app", "Education", 12.99, "Monthly", d(2026, 9, 25), "Credit card", Y, N, Y, 7),
           ("Online course platform", "Education", 59, "Quarterly", d(2026, 3, 3), "Credit card", N, N, N, None)]
S0, S1 = 6, 35
for r in range(S0, S1 + 1):
    s = ssample[r - S0] if r - S0 < len(ssample) else (None,) * 10
    band = (r - S0) % 2 == 1
    for j, (col, fmt) in enumerate(zip("BCDEFGHIJK", [None, None, CUR, None, DATE, None, None, None, None, "0"])):
        cell(su, f"{col}{r}", s[j], fmt, inp=True, band=band, align="left" if col in "BG" else "right" if col in "DFK" else "center")
    live = f'AND($B{r}<>"",$D{r}>0)'
    step = f'IF($E{r}="Monthly",1,IF($E{r}="Quarterly",3,IF($E{r}="Yearly",12,0)))'
    first = f'IF($J{r}="Yes",$F{r}+N($K{r}),$F{r})'                                  # first paid charge
    kk = f'IF({first}>={TODAY},0,CEILING(DATEDIF({first},{TODAY},"M")/{step},1))'
    mnext = f'IF(EDATE({first},{step}*({kk}))>={TODAY},EDATE({first},{step}*({kk})),EDATE({first},{step}*({kk}+1)))'
    wnext = f'IF({first}>={TODAY},{first},{first}+7*CEILING(({TODAY}-{first})/7,1))'
    f = {"L": f'=IF(NOT({live}),"",IF($E{r}="Weekly",$D{r}*52/12,IF($E{r}="Quarterly",$D{r}/3,IF($E{r}="Yearly",$D{r}/12,$D{r}))))',
         "M": f'=IF(ISNUMBER($L{r}),$L{r}*12,"")',
         "N": f'=IF(OR(NOT({live}),$F{r}=""),"",IF($E{r}="Weekly",{wnext},{mnext}))',
         "O": f'=IF(ISNUMBER($N{r}),$N{r}-{TODAY},"")',
         "P": f'=IF(AND({live},$J{r}="Yes",ISNUMBER($K{r})),$F{r}+$K{r}-1,"")',
         "Q": f'=IF(ISNUMBER($P{r}),$P{r}-{TODAY},"")',
         "R": f'=IF(NOT({live}),"",IF(AND(ISNUMBER($Q{r}),$Q{r}<0,$I{r}<>"Yes"),"Trial ended",IF(AND(ISNUMBER($Q{r}),$Q{r}<={WARN}),"Cancel soon?",IF($I{r}="Yes","To cancel",IF(AND(ISNUMBER($O{r}),$O{r}<={WARN}),"Charge soon","OK")))))'}
    for col, fx in f.items():
        fmt = {"L": CUR, "M": CUR, "N": DATE, "O": DAYS, "P": DATE, "Q": DAYS}.get(col)
        cell(su, f"{col}{r}", fx, fmt, band=band, align="center" if col in "OQR" else "right")
    su[f"S{r}"] = f'=IF(ISNUMBER($O{r}),$O{r}+ROW()/1000,"")'                            # next charge order
    su[f"T{r}"] = f'=IF(ISNUMBER($M{r}),$M{r}+ROW()/100000,"")'                          # yearly cost order
    su[f"U{r}"] = f'=IF(AND(ISNUMBER($Q{r}),N($Q{r})>=0,$I{r}<>"Yes"),$Q{r}+ROW()/1000,"")'  # open trials order
    su.row_dimensions[r].height = 22
for c in "STU": su[f"{c}5"] = "key"; su.column_dimensions[c].hidden = True
sr = lambda c: f"Subscriptions!${c}${S0}:${c}${S1}"
su["B3"] = (f'=COUNT({sr("L")})&" subscriptions   ·   "&TEXT(SUM({sr("L")}),"$#,##0.00")&" a month   ·   "&TEXT(SUM({sr("M")}),"$#,##0")'
            f'&" a year   ·   cancel the ticked ones and save "&TEXT(SUMIFS({sr("M")},{sr("I")},"Yes"),"$#,##0")&" a year"')
su["B3"].font = F(TXT, True, 10)
su["I5"].comment = Comment("Tick (Yes) anything you plan to cancel. The Dashboard shows what you'd save in a year.", "CheckMaybe")
listdv(su, CATS, f"C{S0}:C{S1}"); listdv(su, BILLING, f"E{S0}:E{S1}"); listdv(su, PAID, f"G{S0}:G{S1}")
listdv(su, '"Yes,No"', f"H{S0}:J{S1}")
chips(su, f"C{S0}:C{S1}", {"Streaming": "pink", "Software": "blue", "Fitness": "green", "Shopping": "orange", "News": "grey",
                           "Cloud": "teal", "Food": "amber", "Education": "purple", "Other": "grey"})
chips(su, f"E{S0}:E{S1}", {"Weekly": "pink", "Monthly": "purple", "Quarterly": "teal", "Yearly": "amber"})
chips(su, f"H{S0}:H{S1}", {"Yes": "green", "No": "grey"})
chips(su, f"I{S0}:I{S1}", {"Yes": "red", "No": "grey"})
chips(su, f"J{S0}:J{S1}", {"Yes": "amber", "No": "grey"})
chips(su, f"R{S0}:R{S1}", {"Cancel soon?": "red", "Trial ended": "red", "Charge soon": "amber", "To cancel": "grey", "OK": "green"})
su.conditional_formatting.add(f"Q{S0}:Q{S1}", FormulaRule(formula=[f'AND(ISNUMBER($Q{S0}),$Q{S0}>=0,$Q{S0}<=3)'], fill=fill(CHIP["red"][1]), font=FD(RED, True)))
su.conditional_formatting.add(f"O{S0}:O{S1}", FormulaRule(formula=[f'AND(ISNUMBER($O{S0}),$O{S0}<={WARN})'], font=FD(AMBER, True)))
su.conditional_formatting.add(f"B{S0}:G{S1}", FormulaRule(formula=[f'$R{S0}="Cancel soon?"'], fill=fill("3A1C24")))
su.conditional_formatting.add(f"B{S0}:Q{S1}", FormulaRule(formula=[f'$I{S0}="Yes"'], fill=fill(INPUT), font=FD("6E6C80", False, 10, True, True)))
su.auto_filter.ref = f"B5:R{S1}"

# ---------------- Chart Data (feeds the dashboard charts) ----------------
cd = sheet("Chart Data", {"A": 3, "B": 24, "C": 14, "D": 14, "E": 14, "F": 14}, rows=34, cols=7)
title(cd, "Chart Data", "Feeds the Dashboard charts and lists. Nothing to edit here.")
DB = "Dashboard"
VIEW = f"{DB}!$I$27"
header(cd, 4, 2, ["Where each month's income goes", "Per month"], MUTED)
for i, (lab, src) in enumerate([("Loans & cards", "C41"), ("Installments & BNPL", "C42"), ("Subscriptions", "C43"), ("Left over", "C45")]):
    cell(cd, f"B{5 + i}", lab); cell(cd, f"C{5 + i}", f"=MAX(0,{DB}!{src})", CUR, align="right")
header(cd, 11, 2, ["Spend vs savings", "Yearly spend", "Could save"], MUTED)
for i in range(1, 10):
    r = 11 + i; cat = f"Settings!$D${12 + i}"
    m = f'MATCH(LARGE({sr("T")},{i}),{sr("T")},0)'
    cell(cd, f"B{r}", f'=IF({VIEW}="By subscription",IFERROR(INDEX({sr("B")},{m}),""),{cat})')
    cell(cd, f"C{r}", f'=IF({VIEW}="By subscription",IFERROR(INDEX({sr("M")},{m}),0),SUMIFS({sr("M")},{sr("C")},{cat}))', CUR, align="right")
    cell(cd, f"D{r}", f'=IF({VIEW}="By subscription",IFERROR(IF(INDEX({sr("I")},{m})="Yes",C{r},0),0),SUMIFS({sr("M")},{sr("C")},{cat},{sr("I")},"Yes"))', CUR, align="right")
header(cd, 23, 2, ["Debt (highest APR first)", "Real APR", "Flag", "Interest left", "Type"], MUTED)
for i in range(1, 9):
    r = 23 + i
    m = f'MATCH(LARGE({dr("S")},{i}),{dr("S")},0)'
    for col, src, fmt in (("B", "B", None), ("C", "J", PCT), ("D", "R", None), ("E", "N", CUR), ("F", "C", None)):
        cell(cd, f"{col}{r}", f'=IFERROR(INDEX({dr(src)},{m}),"")', fmt, align="left" if col in "BF" else "right")

# ---------------- Dashboard ----------------
db = sheet("Dashboard", {"A": 2, "B": 24, "C": 14, "D": 14, "E": 14, "F": 16, "G": 16, "H": 16, "I": 18, "J": 2},
           first=True, rows=64, cols=11)
wb.move_sheet("Dashboard", -(len(wb.sheetnames) - 1))
db["B2"] = "HIDDEN COST TRACKER"; db["B2"].font = F(ORANGE, True, 22); db.row_dimensions[2].height = 34
db["B3"] = "What your debts, installments and subscriptions really cost you."; db["B3"].font = F(MUTED, False, 10, True)
gap = Side(style="thick", color=BG)

def panel(r1, r2, c1, c2):
    """Card look: panel fill with a thick background-coloured edge so neighbouring cards read as separate."""
    for r in range(r1, r2 + 1):
        for c in range(c1, c2 + 1):
            x = db.cell(r, c); x.fill = fill(PANEL)
            x.border = Border(left=gap if c == c1 else None, right=gap if c == c2 else None,
                              top=gap if r == r1 else None, bottom=gap if r == r2 else None)

panel(2, 3, 8, 9)
db.merge_cells("H2:I2"); db.merge_cells("H3:I3")
db["H2"] = "TODAY"; db["H2"].font = F(MUTED, True, 8); db["H2"].alignment = Alignment(horizontal="center", vertical="bottom")
db["H3"] = f"={TODAY}"; db["H3"].number_format = "dddd, mmm d, yyyy"; db["H3"].font = F(TXT, True, 11)
db["H3"].alignment = Alignment(horizontal="center", vertical="top")

def kpi(r, c, label, fx, fmt, color, caption):
    panel(r, r + 2, c, c + 1)
    for k in range(3): db.merge_cells(start_row=r + k, start_column=c, end_row=r + k, end_column=c + 1)
    a, b, cap = db.cell(r, c), db.cell(r + 1, c), db.cell(r + 2, c)
    a.value = label; a.font = F(MUTED, True, 8); a.alignment = Alignment(indent=1, vertical="bottom")
    b.value = fx; b.font = F(color, True, 20); b.number_format = fmt; b.alignment = Alignment(horizontal="left", indent=1, vertical="center")
    cap.value = caption; cap.font = F(MUTED, False, 8, True); cap.alignment = Alignment(indent=1, vertical="top")
    db.row_dimensions[r].height = 20; db.row_dimensions[r + 1].height = 32; db.row_dimensions[r + 2].height = 20

INC, DEBTM, SUBM, COMM, LEFT = "$C$40", "($C$41+$C$42)", "$C$43", "$C$44", "$C$45"
kpi(5, 2, "MONTHLY INCOME", f"={INC}", CUR, TXT, "take-home · change it in Settings")
kpi(5, 4, "COMMITTED EACH MONTH", f"={COMM}", CUR, ORANGE, f'=TEXT({DEBTM},"$#,##0")&" debts + "&TEXT({SUBM},"$#,##0")&" subscriptions"')
kpi(5, 6, "SHARE OF INCOME COMMITTED", f"=IF({INC}>0,{COMM}/{INC},0)", PCT, ORANGE,
    f'="of every $1 you earn, "&TEXT(IF({INC}>0,{COMM}/{INC},0)*100,"0")&"¢ is already spoken for"')
kpi(5, 8, "LEFT OVER EACH MONTH", f"={LEFT}", CUR, GREEN, "after debts & subscriptions")
kpi(9, 2, "HIGHEST REAL APR", f'=IF(COUNT({dr("J")})=0,"",MAX({dr("J")}))', PCT, RED,
    f'=IF(COUNT({dr("J")})=0,"add a debt to see it",\'Chart Data\'!$B$24&"  ·  "&COUNTIF({dr("R")},"HIGH")&" flagged HIGH")')
kpi(9, 4, "INTEREST STILL TO PAY", f'=SUM({dr("N")})', CUR, RED,
    f'=COUNT({dr("J")})&" debts  ·  debt-free "&IF(COUNT({dr("O")})=0,"-",TEXT(MAX({dr("O")}),"mmm yyyy"))')
kpi(9, 6, "FREE TRIALS ENDING SOON", f'=COUNTIF({sr("R")},"Cancel soon?")', "0", AMBER,
    f'=IF(COUNT({sr("U")})=0,"no open free trials","first cancel-by: "&TEXT({TODAY}+INT(SMALL({sr("U")},1)),"mmm d"))')
kpi(9, 8, "YEARLY SAVINGS IF YOU CANCEL", f'=SUMIFS({sr("M")},{sr("I")},"Yes")', CUR, GREEN,
    f'=COUNTIF({sr("I")},"Yes")&" subscriptions ticked Cancel it?"')

def section(ref, text, color=TEAL):
    db[ref] = text; db[ref].font = F(color, True, 9); db[ref].alignment = Alignment(vertical="bottom")

def table(r0, labels, n, rowfx, fmts, aligns, color=TEAL):
    header(db, r0, 2, labels, color); db.row_dimensions[r0].height = 24
    for k in range(1, n + 1):
        r = r0 + k
        for j, (fx, fmt, al) in enumerate(zip(rowfx(k), fmts, aligns)):
            cell(db, db.cell(r, 2 + j).coordinate, fx, fmt, align=al, band=k % 2 == 0)
        db.row_dimensions[r].height = 21

pick = lambda key, k, col: f'IFERROR(INDEX({sr(col)},MATCH(SMALL({sr(key)},{k}),{sr(key)},0)),"")'
section("B13", "COMING UP  ·  NEXT CHARGES")
table(14, ["Subscription", "Amount", "Date", "Due in"], 6,
      lambda k: [f"={pick('S', k, 'B')}", f"={pick('S', k, 'D')}", f"={pick('S', k, 'N')}", f"={pick('S', k, 'O')}"],
      [None, CUR, "mmm d", DAYS], ["left", "right", "center", "center"])
db.conditional_formatting.add("E15:E20", FormulaRule(formula=[f'AND(ISNUMBER(E15),E15<={WARN})'], fill=fill(CHIP["amber"][1]), font=FD(AMBER, True)))

section("B22", "FREE TRIALS  ·  CANCEL BEFORE YOU'RE CHARGED", AMBER)
table(23, ["Free trial", "Then costs", "Cancel by", "Days left"], 4,
      lambda k: [f"={pick('U', k, 'B')}", f"={pick('U', k, 'D')}", f"={pick('U', k, 'P')}", f"={pick('U', k, 'Q')}"],
      [None, CUR, "mmm d", DAYS], ["left", "right", "center", "center"], AMBER)
db.conditional_formatting.add("E24:E27", FormulaRule(formula=["AND(ISNUMBER(E24),E24<=3)"], fill=fill(CHIP["red"][1]), font=FD(RED, True)))
db.conditional_formatting.add("E24:E27", FormulaRule(formula=[f"AND(ISNUMBER(E24),E24<={WARN})"], fill=fill(CHIP["amber"][1]), font=FD(AMBER, True)))

section("B29", "DEBTS  ·  PAY EXTRA ON #1 FIRST (HIGHEST REAL APR)", RED)
table(30, ["Debt", "Real APR", "Flag", "Interest left"], 6,
      lambda k: [f"='Chart Data'!B{23 + k}", f"='Chart Data'!C{23 + k}", f"='Chart Data'!D{23 + k}", f"='Chart Data'!E{23 + k}"],
      [None, PCT, None, CUR], ["left", "right", "center", "right"], RED)
chips(db, "D31:D36", {"HIGH": "red", "CHECK": "amber", "OK": "green"})

section("B38", "MONTHLY MONEY MAP", ORANGE)
header(db, 39, 2, ["Where the money goes", "Per month", "Share"], ORANGE); db.row_dimensions[39].height = 24
money = [("Take-home income", f"={INCOME}", TXT),
         ("Loans & cards", f'=SUM({dr("E")})-SUMIFS({dr("E")},{dr("C")},"Installment")-SUMIFS({dr("E")},{dr("C")},"BNPL")', TXT),
         ("Installments & BNPL", f'=SUMIFS({dr("E")},{dr("C")},"Installment")+SUMIFS({dr("E")},{dr("C")},"BNPL")', TXT),
         ("Subscriptions", f'=SUM({sr("L")})', TXT),
         ("Committed before you spend a cent", "=SUM(C41:C43)", ORANGE),
         ("Left for everything else", "=C40-C44", GREEN)]
for i, (lab, fx, col) in enumerate(money):
    r = 40 + i; bold = i in (0, 4, 5)
    cell(db, f"B{r}", lab, bold=bold, color=col, band=i % 2 == 1)
    cell(db, f"C{r}", fx, CUR, bold=bold, color=col, align="right", band=i % 2 == 1)
    cell(db, f"D{r}", "" if i == 0 else f"=IF($C$40>0,C{r}/$C$40,0)", '0%', color=MUTED if i in (1, 2, 3) else col, align="right", band=i % 2 == 1)
    db.row_dimensions[r].height = 21

section("B47", "WHAT THE FLAGS MEAN", MUTED)
flags = [("HIGH", "red", f'="Real APR at or above "&TEXT({RED_APR},"0%")&". Pay these down first."'),
         ("CHECK", "amber", f'="Real APR at or above "&TEXT({AMB_APR},"0%")&". Worth a look."'),
         ("OK", "green", '="Lower-cost debt. Keep paying on time."')]
for i, (lab, col, fx) in enumerate(flags):
    r = 48 + i; fg, bg = CHIP[col]
    c = db[f"B{r}"]; c.value = lab; c.font = F(fg, True, 9); c.fill = fill(bg); c.alignment = Alignment(horizontal="center", vertical="center")
    db[f"C{r}"] = fx; db[f"C{r}"].font = F(MUTED, False, 9); db[f"C{r}"].alignment = Alignment(indent=1, vertical="center")
    db.row_dimensions[r].height = 20
db["B52"] = ("Real APR is worked out from your payment schedule when a lender only shows a monthly price. "
             "0% offers stay 0% only if every payment is on time.")
db["B52"].font = F(MUTED, False, 8, True)

# right column: section titles + charts
section("F13", "WHERE EACH MONTH'S INCOME GOES", ORANGE)
section("F27", "SPEND VS SAVINGS (YEARLY)", PURPLE)
db["H27"] = "VIEW  ▸"; db["H27"].font = F(MUTED, True, 8); db["H27"].alignment = Alignment(horizontal="right", vertical="bottom")
cell(db, "I27", "By category", inp=True, bold=True, color=BLUE, align="center", size=9)
listdv(db, '"By category,By subscription"', "I27")
section("F44", "REAL APR BY DEBT", RED)

db["B60"] = ("Estimates only, not financial advice. Real APR is worked out from your payments and excludes fees charged "
             "separately; your contract is the final word. Example rows are made up.")
db["B60"].font = F(MUTED, False, 8, True)

def rich(color, sz=900, bold=False):
    cp = CharacterProperties(sz=sz, b=bold, solidFill=color)
    return RichText(p=[Paragraph(pPr=ParagraphProperties(defRPr=cp), endParaRPr=cp)])

def dark(ch, axes=True):
    ch.graphical_properties = GraphicalProperties(solidFill=PANEL, ln=LineProperties(noFill=True))
    ch.plot_area.graphicalProperties = GraphicalProperties(noFill=True, ln=LineProperties(noFill=True))
    if ch.legend is not None: ch.legend.txPr = rich(TXT)
    ch.visible_cells_only = False
    if axes:
        for ax in (ch.x_axis, ch.y_axis):
            ax.delete = False; ax.txPr = rich(MUTED, 800)
            ax.graphicalProperties = GraphicalProperties(ln=LineProperties(solidFill=LINE))
        ch.y_axis.majorGridlines.spPr = GraphicalProperties(ln=LineProperties(solidFill=LINE))

CDS = wb["Chart Data"]
don = DoughnutChart(holeSize=58)
don.add_data(Reference(CDS, min_col=3, min_row=4, max_row=8), titles_from_data=True)
don.set_categories(Reference(CDS, min_col=2, min_row=5, max_row=8))
for i, colr in enumerate([RED, AMBER, PURPLE, GREEN]):
    don.series[0].dPt.append(DataPoint(idx=i, spPr=GraphicalProperties(solidFill=colr, ln=LineProperties(solidFill=PANEL))))
don.dataLabels = DataLabelList(); don.dataLabels.showPercent = True; don.dataLabels.showVal = False
don.dataLabels.showCatName = False; don.dataLabels.showSerName = False; don.dataLabels.showLegendKey = False
don.dataLabels.txPr = rich(BG, 900, True)
don.legend.position = "r"; dark(don, axes=False)
don.width, don.height = 12.9, 6.6; db.add_chart(don, "F14")

col = BarChart(); col.type = "col"; col.gapWidth = 60; col.overlap = -10
col.add_data(Reference(CDS, min_col=3, max_col=4, min_row=11, max_row=20), titles_from_data=True)
col.set_categories(Reference(CDS, min_col=2, min_row=12, max_row=20))
for s, colr in zip(col.series, [PURPLE, GREEN]): s.graphicalProperties = GraphicalProperties(solidFill=colr, ln=LineProperties(noFill=True))
col.y_axis.number_format = '$#,##0'; col.legend.position = "t"; dark(col)
col.width, col.height = 12.9, 7.4; db.add_chart(col, "F28")

bar = BarChart(); bar.type = "bar"; bar.gapWidth = 50; bar.legend = None
bar.add_data(Reference(CDS, min_col=3, min_row=23, max_row=31), titles_from_data=True)
bar.set_categories(Reference(CDS, min_col=2, min_row=24, max_row=31))
bar.series[0].graphicalProperties = GraphicalProperties(solidFill=ORANGE, ln=LineProperties(noFill=True))
bar.y_axis.number_format = '0%'; bar.x_axis.scaling.orientation = "maxMin"; dark(bar)
bar.width, bar.height = 12.9, 7.4; db.add_chart(bar, "F45")

# ---------------- How to use ----------------
hw = sheet("How to Use", {"A": 3, "B": 110}, rows=26, cols=3)
title(hw, "How to use", "Five minutes to set up.")
steps = ["1. Settings: enter your monthly take-home income. Adjust the red/amber APR levels if you like (defaults 20% / 10%).",
         "2. Debts & Installments: one row per debt. BLUE-header columns are yours; ORANGE-header columns calculate themselves.",
         "   • Installment / BNPL / store financing: enter Original amount, Monthly payment, Total payments and Payments made. Leave Stated APR empty: the Real APR is worked out for you.",
         "   • Credit card / loan: enter Monthly payment, Stated APR and Balance now.",
         "   • Family loan with no interest: enter 0% as the Stated APR.",
         "3. Subscriptions: one row per subscription. Tick Cancel it? on anything you'd drop: the Dashboard shows the yearly saving.",
         "   • Free trial? Tick Free trial? and enter Trial days. You get a 'cancel by' date and a countdown.",
         "4. Dashboard: see what share of your income is committed before you spend anything, your highest-cost debt, and what's coming up.",
         "   • Switch the spending chart between By category and By subscription with the VIEW box above it.",
         "   • Use the filter buttons on each table's header row (or the filter bars above it in Google Sheets) to sort and filter.",
         "",
         "Avalanche order = pay extra on #1 first (highest APR, saves the most interest). Snowball order = smallest balance first (quick wins).",
         "The example rows are made up. Replace or delete them.",
         "",
         "Estimates only. Not financial advice. The Real APR is an estimate from your payment schedule and does not include fees charged separately."]
for i, s in enumerate(steps):
    hw[f"B{5 + i}"] = s; hw[f"B{5 + i}"].font = F(TXT if s[:1].isdigit() else MUTED, s[:1].isdigit(), 10)
    hw[f"B{5 + i}"].alignment = Alignment(wrap_text=True, vertical="top")
wb.move_sheet("How to Use", -(len(wb.sheetnames) - 2))
wb.move_sheet("Chart Data", len(wb.sheetnames) - 1 - wb.sheetnames.index("Chart Data"))
for ws in wb.worksheets: ws.sheet_properties.tabColor = {"Dashboard": ORANGE, "How to Use": TEAL, "Chart Data": "2A2D3A"}.get(ws.title, "3A3F58")
wb.save("Hidden-Cost-Tracker.xlsx"); import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "build")); import excel_compat; excel_compat.fix("Hidden-Cost-Tracker.xlsx"); print("saved", wb.sheetnames)
