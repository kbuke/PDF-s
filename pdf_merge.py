import sys 
import PyPDF2

# in terminal run
    # python pdf_merge.py resources/dummy.pdf resources/twopage.pdf resources/wtr.pdf

inputs = sys.argv[1:] # this grabs all inputs except the first

def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger() # this creates a merger object with PyPDF
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)
    merger.write('super.pdf')

pdf_combiner(inputs)