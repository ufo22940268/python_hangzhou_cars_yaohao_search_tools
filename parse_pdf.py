#coding=utf-8

import scratch_pdf

from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFResourceManager,PDFPageInterpreter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from cStringIO import StringIO
import StringIO as SIO
import json
import re 



class ParsePdf:
    def __init__(self,pdf):
        self.pdf = pdf
        self.parse_pfd()
    
    def parse_pfd(self):
        fp = file(self.pdf, 'rb')
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
            data = retstr.getvalue()      
        return data
    
    def parse_data(self):
        data = self.parse_pfd()
        lines = data.split("\n")
        lottery_items = []
        for item in lines:
            lottery_dict = {}
            id = re.search("\s{6}\d{1,5}\s", item)
            user_number = re.search("\d{13}", item)
            user_name = re.search("\d{13}\s+(\S+)", item)
            if not id:
                continue
            if id is not None:
                lottery_dict['id'] = id.group(0)
            if user_number is not None:
                lottery_dict['user_number'] = user_number.group(0)
            if user_name is not None:
                lottery_dict['user_name'] = user_name.group(1)
                print lottery_dict['user_name']
            lottery_items.append(lottery_dict)
        return lottery_items
    
    def pdf_to_txt(self):
        # a = parse_data()
        # with open('./pdf/%s' %pdf_name, 'wb') as fd:
        #     fd.write(response)
        pass
    
    
    def pdf_to_json(self):
        pass

    

if __name__ == "__main__":
    ParsePdf('./pdf/1409037121186.pdf').parse_data()
