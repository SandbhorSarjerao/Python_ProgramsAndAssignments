import PyPDF4

with open('dummy.pdf','rb') as file:
    reader = PyPDF4.PdfFileReader(file)
    print(reader)
    page = reader.getPage(0)
    print(page)


