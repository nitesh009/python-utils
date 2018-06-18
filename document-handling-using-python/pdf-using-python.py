# Reading & Editing PDFs
# pip install PyPDF2

import  PyPDF2
import os

os.chdir('/Users/Username/Downloads/')

pdfFile = open('python_practice/meetingminutes1.pdf', 'rb')

print(type(pdfFile))


reader = PyPDF2.PdfFileReader(pdfFile)

print(reader.numPages)

page = reader.getPage(0)

print(page.extractText())


# read all pages

for pageNum in range(reader.numPages):
    print(reader.getPage(pageNum).extractText())


# combining two pdf files into new one

pdfFile1 = open('python_practice/meetingminutes1.pdf', 'rb')

pdfFile2 = open('python_practice/meetingminutes2.pdf', 'rb')


reader1 = PyPDF2.PdfFileReader(pdfFile1)

reader2 = PyPDF2.PdfFileReader(pdfFile2)

# creating a new blank pdf
writer = PyPDF2.PdfFileWriter()


# writing first file
for pageNum in range(reader1.numPages):
    page = reader1.getPage(pageNum)
    writer.addPage(page)

# writing second file
for pageNum in range(reader2.numPages):
    page = reader2.getPage(pageNum)
    writer.addPage(page)

outputFile = open('combinedminutes.pdf','wb')
writer.write(outputFile)

outputFile.close()

pdfFile1.close()

pdfFile2.close()
