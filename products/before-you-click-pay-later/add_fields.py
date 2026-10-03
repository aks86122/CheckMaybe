"""Add fillable text fields (page 10) to base.pdf using the cell positions in fields.json.

CSS px (96 per inch) -> PDF points (72 per inch): multiply by 0.75. Writes Before-You-Click-Pay-Later.pdf.
"""
import json, os
import pymupdf

K = 0.75
doc = pymupdf.open("base.pdf")
for f in json.load(open("fields.json")):
    page = doc[f["page"]]
    x, y, w, h = f["x"] * K, f["y"] * K, f["w"] * K, f["h"] * K
    wd = pymupdf.Widget()
    wd.field_type = pymupdf.PDF_WIDGET_TYPE_TEXT
    wd.field_name = f["name"]
    wd.rect = pymupdf.Rect(x + 2, y + 2, x + w - 2, y + h - 2)
    wd.text_font = "Helv"
    wd.text_fontsize = 10
    wd.text_color = (0.93, 0.92, 0.96)
    wd.fill_color = None
    wd.border_width = 0
    page.add_widget(wd)
doc.set_metadata({"title": 'Before You Click "Pay Later"', "author": "CheckMaybe",
                  "subject": "Five checks before you choose a pay-later plan. Estimates only, not financial advice."})
doc.save("Before-You-Click-Pay-Later.pdf", garbage=3, deflate=True)
os.remove("base.pdf"); os.remove("fields.json")
print("saved Before-You-Click-Pay-Later.pdf")
