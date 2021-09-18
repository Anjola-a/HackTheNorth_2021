# import nltk
# from nltk.book import *
#
# x = text1.concordance_list("monstrous")
#
# print(type(x))

# import PyPDF2
#
# reader = PyPDF2.PdfFileReader('Ben_Sun_Resume.pdf')

from io import StringIO

from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser


def convert_pdf_to_string(file_path):
    output_string = StringIO()
    with open(file_path, 'rb') as in_file:
        parser = PDFParser(in_file)
        doc = PDFDocument(parser)
        rsrcmgr = PDFResourceManager()
        device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        for page in PDFPage.create_pages(doc):
            interpreter.process_page(page)

    return (output_string.getvalue())


def convert_title_to_filename(title):
    filename = title.lower()
    filename = filename.replace(' ', '_')
    return filename


def split_to_title_and_pagenum(table_of_contents_entry):
    title_and_pagenum = table_of_contents_entry.strip()

    title = None
    pagenum = None

    if len(title_and_pagenum) > 0:
        if title_and_pagenum[-1].isdigit():
            i = -2
            while title_and_pagenum[i].isdigit():
                i -= 1

            title = title_and_pagenum[:i].strip()
            pagenum = int(title_and_pagenum[i:].strip())

    return title, pagenum


import PyPDF2
import csv

reader = PyPDF2.PdfFileReader(
    'test.pdf')

print(reader.documentInfo)

num_of_pages = reader.numPages
print('Number of pages: ' + str(num_of_pages))

writer = PyPDF2.PdfFileWriter()


writer.addPage(reader.getPage(36))

output_filename = 'output.pdf'

with open(output_filename, 'wb') as output:
    writer.write(output)

text = convert_pdf_to_string(
    'output.pdf')

print(type(text))
