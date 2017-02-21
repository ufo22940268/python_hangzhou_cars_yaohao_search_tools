
#coding=utf-8

import requests
import re
from bs4 import BeautifulSoup



def gen_url_indexs():
    url_index_main = "http://xkctk.hzcb.gov.cn/gbl/index.html"
    url_pre ="http://xkctk.hzcb.gov.cn/gbl/index_"
    url_suf =".html"
    url_num = range(2,13)
    url_indexs=list(map(lambda x:url_pre+str(x)+url_suf, url_num))
    url_indexs.append(url_index_main)
    return url_indexs

def get_link_urls(indexs):
    link_urls=[]
    responses = list(map(lambda x:requests.get(x).content.decode('ISO-8859-1').encode('utf-8'), indexs))
    soups = list(map(lambda x:BeautifulSoup(x,'html.parser'),responses))
    for soup in soups:
        patterm = re.compile("\d{4}年\d{1,2}月杭州市小客车增量指标摇号结果公告")
        #print soup.find_all('a', class_='text')
        tags = soup.find_all('a', class_='text',string=patterm)
        [link_urls.append(i) for i in map(lambda x:x.get('href'), tags)]
    return link_urls


def get_pdf_urls(link_urls):
    pdf_urls = []
    responses = list(map(lambda x:requests.get(x).content.decode('ISO-8859-1').encode('utf-8'), link_urls))
    soups = list(map(lambda x:BeautifulSoup(x,'html.parser'),responses))
    for soup in soups:
        patterm = re.compile("\s*个人摇号指标配置结果")
        tags = soup.find_all('a',string=patterm)
        [pdf_urls.append(i) for i in map(lambda x:x.get('href'), tags)]
    print pdf_urls
    return pdf_urls



def download_pdf(pdf_urls):
    for url in pdf_urls:
        pdf_name = re.search("\d{13}.pdf", url).group(0)
        response = requests.get(url,stream=True).content
        with open('./pdf/%s' %pdf_name, 'wb') as fd:
            fd.write(response)

