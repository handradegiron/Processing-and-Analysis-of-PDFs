#Crear anotaciones transparentes en archivos PDFs
#create transparent annotations on PDFs files

#pip install PyMuPDF

import fitz 

# some colors
blue = (0, 0, 1)
green = (0, 1, 0)
red = (1, 0, 0)
gold = (1, 1, 0)

# a new PDF with 1 page
doc = fitz.open()
page = doc.new_page()

# start with this rectangle
r = fitz.Rect(100, 100, 200, 150)

# the text, Latin alphabet
t = "¡El documento requiere su revisión!"
fonts = ("Helv", "TiRo", "Cour")
# add 3 annots, modify the last one somewhat
for font in fonts:
    annot = page.add_freetext_annot(r, t, fontname=font, text_color=red, fill_color=gold)
    annot.set_border({"width": 1, "dashes": (2, 2)})
    annot.set_opacity(0.3)  # transparency 50%
    annot.update(border_color=blue)
    r += (0, 75, 0, 75)

# save the PDF
doc.save("a-result.pdf")
