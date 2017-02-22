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
import os



class ParsePdf:
    def __init__(self,pdf):
        self.pdf = pdf
    
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
            lottery_items.append(lottery_dict)
        return lottery_items
    
    def pdf_to_txt(self):
        
        # a = parse_data()
        # with open('./pdf/%s' %pdf_name, 'wb') as fd:
        #     fd.write(response)
        pass
        
    def pdf_to_json(self, name):
        data = self.parse_data()
        with open('./json/%s' %name, 'wb') as f:
            json.dump(data,f)
        


    

if __name__ == "__main__":
    pdfs = filter( lambda f: not f.startswith('.'), os.listdir('./pdf'))
    for i in pdfs:
        pdf_path = './pdf/'+i
        print pdf_path
        json_name = i.replace('.pdf', '.json')    
        ParsePdf(pdf_path).pdf_to_json(json_name)
