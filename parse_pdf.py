#coding=utf-8

import scratch_pdf

from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFResourceManager,PDFPageInterpreter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from cStringIO import StringIO



def parse_pdf_to_txt(pdfs):
    fp = file(pdfs, 'rb')
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()

    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    # Create a PDF interpreter object.
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    # Process each page contained in the document.
    for page in PDFPage.get_pages(fp):
        interpreter.process_page(page)
        data =  retstr.getvalue()
    print data


def parse_pdf():
    pass



parse_pdf_to_txt("./pdf/1443426333748.pdf")

# download_pdf(get_pdf_urls(get_link_urls(gen_url_indexs())))

