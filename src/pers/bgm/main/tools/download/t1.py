# -*- coding:utf8 -*-
import requests
from bs4 import BeautifulSoup
from lxml import etree
import sys
reload(sys)
sys.setdefaultencoding('utf8')

j=0
def downloadHtml(url):
    content_html = requests.get(url).content
    return content_html
downloadPath = "F:\\Development\\DataTrain\\xingai\\"
f_c_path='http://baike.xmeise.com/xya/nvxa/4244.html'
detail_page=downloadHtml(f_c_path)
print str(j)+":"+f_c_path
c_html=etree.HTML(detail_page)
c_html_div = c_html.xpath('/html/body/div/div/div/text()')
c_html_p = c_html.xpath('/html/body/div/div/p/text()')
c_html_p_span2 = c_html.xpath('/html/body/div/div/p/span/span/text()')
detail_page_content=''.join(c_html_div)
detail_page_content_p = ''.join(c_html_p)
detail_page_content_p_span2 = ''.join(c_html_p_span2)
file_content = detail_page_content.replace('	', '').replace(' ', '').strip()
file_content_p = detail_page_content_p.replace('	', '').replace(' ', '').strip()
file_content_p_span2 = detail_page_content_p_span2.replace('	', '').replace(' ', '').strip()
print BeautifulSoup(detail_page,'html.parser').get_text()
exit(0)
with open(downloadPath + str(j) + '.txt', "wb") as code:
    if file_content == '':
        file_content = file_content_p
        if file_content == '':
            file_content=file_content_p_span2
    code.write(file_content)