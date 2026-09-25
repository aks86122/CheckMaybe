import pymupdf,sys
d=pymupdf.open(sys.argv[1]); idx=[int(x)-1 for x in sys.argv[3:]]; w,h=595,842
s=pymupdf.open(); pg=s.new_page(width=len(idx)*w,height=h)
for j,i in enumerate(idx): pg.show_pdf_page(pymupdf.Rect(j*w,0,(j+1)*w,h),d,i)
pg.get_pixmap(dpi=80).save(sys.argv[2])
