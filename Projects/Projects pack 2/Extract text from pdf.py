# extract text from pdf 

import PyPDF2
# rb: read binary mode 
Pdf_File = open("file_name.pdf", "rb")
# object to read the pdf file
PDF_Reader = PyPDF2.PdfFileReader(Pdf_File)
# get page and extract
Text = PDF_Reader.getPage(0).extractText()
print(Text)


