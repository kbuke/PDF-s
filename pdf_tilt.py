import PyPDF2

with open('./resources/dummy.pdf', 'rb') as file: # rb represents read-binary converts file obj to binary
    # use PyPDF to read file
    reader = PyPDF2.PdfFileReader(file)
    print(reader.numPages)
    print(reader.getPage(0)) # if this went to 1 you would get error as it doesnt exist
    
    page = reader.getPage(0)
    page.rotateCounterClockwise(90)
    writer = PyPDF2.PdfFileWriter() # allows us to wrute obj in memory
    writer.addPage(page)
    with open("tilt.pdf", 'wb') as new_file: #wb means write-binary
        writer.write(new_file)
    