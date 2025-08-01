# write wtr.pdf over all pages on super.pdf
# from PyPDF2 import PdfFileReader, PdfFileWriter
# import sys

# doc_to_mark = sys.argv[1]
# print(doc_to_mark)

# def watermark():
#     reader = PdfFileReader(doc_to_mark)
#     num_pgs = len(reader.pages)
#     print(f"the doc has {num_pgs} pages")

#     writer = PdfFileWriter
#     for pg in num_pgs:
#         content_pg = reader.pages[pg]
#         print(content_pg)

# watermark()
import PyPDF2

template = PyPDF2.PdfFileReader(open('super.pdf', 'rb'))
watermark = PyPDF2.PdfFileReader(open('resources/wtr.pdf', 'rb'))
output = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()): #this shows how many pages we have and creates a range
    page = template.getPage(i)
    page.mergePage(watermark.getPage(0)) # watermark pdf only has the one page therefore index 0
    output.addPage(page)

    with open('watermarked_output.pdf', 'wb') as file:
        output.write(file)