"""Post-save fix so desktop Excel shows the same styling as Google Sheets / LibreOffice.

openpyxl writes cell styles without applyFill / applyNumberFormat / applyFont / applyBorder flags, and some Excel builds
then ignore the fill and number format (white cells, raw date serials, 0.2565 instead of 25.7%). This adds the flags.
"""
import re, shutil, tempfile, zipfile

def _flag(xf: str) -> str:
    for attr, apply in (("numFmtId", "applyNumberFormat"), ("fontId", "applyFont"), ("fillId", "applyFill"), ("borderId", "applyBorder")):
        m = re.search(rf'{attr}="(\d+)"', xf)
        if m and m.group(1) != "0" and apply not in xf:
            xf = xf.replace("<xf ", f'<xf {apply}="1" ', 1)
    return xf

def fix(path: str) -> None:
    src = zipfile.ZipFile(path)
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".xlsx").name
    with zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as out:
        for item in src.infolist():
            data = src.read(item.filename)
            if item.filename == "xl/styles.xml":
                s = data.decode("utf-8")
                s = re.sub(r"<cellXfs.*?</cellXfs>", lambda m: re.sub(r"<xf [^>]*?/?>", lambda x: _flag(x.group(0)), m.group(0)), s, flags=re.S)
                # dxf (conditional formatting) fonts: Excel only takes colour/bold/italic, not name or size
                s = re.sub(r"<dxfs.*?</dxfs>", lambda m: re.sub(r"<(name|sz) val=\"[^\"]*\" ?/>", "", m.group(0)), s, flags=re.S)
                data = s.encode("utf-8")
            out.writestr(item, data)
    src.close(); shutil.move(tmp, path)
