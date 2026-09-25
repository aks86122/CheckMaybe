#!/bin/bash
# usage: build.sh name   (reads name.json → name.html, name.pdf, name-report.json, png/name-pNN.png, name-sheet.png)
set -e; B=$(dirname "$0"); cd "$B"; n=$1
python3 render.py $n.json style.css $PWD/$n.html
node print.mjs $PWD/$n.html $PWD/$n.pdf $PWD/$n-report.json
mkdir -p png; rm -f png/$n-p*.png
python3 - $n <<'PY'
import pymupdf,sys
n=sys.argv[1]; d=pymupdf.open(n+'.pdf')
for i,p in enumerate(d): p.get_pixmap(dpi=110).save(f'png/{n}-p{i+1:02d}.png')
w,h=int(595*0.5),int(842*0.5); cols=6; rows=(d.page_count+cols-1)//cols
s=pymupdf.open(); pg=s.new_page(width=cols*w,height=rows*h)
for i in range(d.page_count): pg.show_pdf_page(pymupdf.Rect((i%cols)*w,(i//cols)*h,(i%cols+1)*w,(i//cols+1)*h),d,i)
pg.get_pixmap(dpi=100).save(n+'-sheet.png'); print('pages',d.page_count)
PY
