import nltk
# from nltk.book import *
#
# x = text1.concordance_list("monstrous")
#
# print(type(x))


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
data = ["Total shareholders' equity, ending balances"]

reader = PyPDF2.PdfFileReader(
    'test.pdf')

print(reader.documentInfo)

num_of_pages = reader.numPages
print('Number of pages: ' + str(num_of_pages))

writer = PyPDF2.PdfFileWriter()


writer.addPage(reader.getPage(36))

output_filename = 'output.txt'

with open(output_filename, 'wb') as output:
    writer.write(output)

text = convert_pdf_to_string(
    'output.pdf')




from nltk.tokenize import MWETokenizer, word_tokenize, TweetTokenizer


# tokenizer = TweetTokenizer()
# print(tokenizer.tokenize(text))

tokenizer = MWETokenizer()
tokenizer.add_mwe(('Total', 'shareholders', "’", "equity"))
#print(f'Multi-word expression tokenization = {tokenizer.tokenize((word_tokenize(text)))}')
mwe = tokenizer.tokenize((word_tokenize(text)))

sentence = nltk.Text(mwe)

print(sentence[10:20])


# Replaces newline characters with spaces
#
# processed_string = list((map(lambda s: s.replace("\n", " "), text)))
#
# output = ""
# for letter in processed_string:
#     output += letter






#print(text)
#text.common_contexts(["Total", "shareholders"])
#print(text.concordance_list("equity"))
#text.collocations()


#sentence.concordance("Total_shareholders_'_equity")

# Importing package and summarizer
# import gensim
# from gensim.summarization import summarize
#
# short_summary = gensim.summarize(sentence)
# print(short_summary)

