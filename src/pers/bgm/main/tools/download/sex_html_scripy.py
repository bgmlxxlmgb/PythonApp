# -*- coding:utf8 -*-
import requests
from bs4 import BeautifulSoup
from lxml import etree
import time
import sys
reload(sys)
sys.setdefaultencoding('utf8')

#j=0
#j=121
j=3762
def downloadHtml(url):
    time.sleep(1)
    content_html = requests.get(url).content
    return content_html
downloadPath = "F:\\Development\\DataTrain\\xingai\\"

for i in range(1,118):
    index_page = 'http://baike.xmeise.com/xsl/list_%s.html' %i
    content_html=downloadHtml(index_page)
    soup = BeautifulSoup(content_html, "html.parser")
    div_list=soup.findAll('div',{'class':'name'})
    for c_div in div_list:
        j+=1
        c_path=c_div.a['href']
        f_c_path="http://baike.xmeise.com%s" %c_path
        if c_path[:3].isdigit():
            f_c_path = "http://baike.xmeise.com/xsl/%s" % c_path
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
        with open(downloadPath + str(j) + '.txt', "wb") as code:
            if file_content == '':
                file_content = file_content_p_span2
                if file_content == '':
                    file_content=file_content_p
            code.write(file_content)