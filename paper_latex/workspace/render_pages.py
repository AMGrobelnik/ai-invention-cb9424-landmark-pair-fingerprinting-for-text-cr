import fitz
doc = fitz.open("paper.pdf")
for i, page in enumerate(doc):
    mat = fitz.Matrix(150/72, 150/72)
    pix = page.get_pixmap(matrix=mat)
    pix.save(f"page_{i+1:02d}.png")
print(f"Rendered {len(doc)} pages")
