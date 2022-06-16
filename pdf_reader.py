import PyPDF2
pdfFileObj = open('listicle-of-covid-startups.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
print(pdfReader.numPages)
for i in range(10,pdfReader.numPages-1):
    pageObj = pdfReader.getPage(i)
    print(pageObj.extractText())
pdfFileObj.close()