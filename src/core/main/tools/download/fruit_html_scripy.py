# -*- coding:utf8 -*-
import requests
from bs4 import BeautifulSoup
from lxml import etree
import time
import sys
reload(sys)
sys.setdefaultencoding('utf8')
j=55
def downloadHtml(url):
    time.sleep(1)
    content_html = requests.get(url).content
    return content_html
downloadPath = "F:\\Development\\DataTrain\\shuiguo\\"

for i in range(55,277):
    index_page = 'http://www.zgncpw.com/nongyezixun/list/134153/%s/' %i
    if i == 1 :
        index_page='http://www.zgncpw.com/nongyezixun/list/134153/'
    content_html=downloadHtml(index_page)
    soup = BeautifulSoup(content_html, "html.parser")
    a_list=soup.findAll('a',{'class':'l-img pos-abs'})
    for c_a_list in a_list:
        j+=1
        c_path=c_a_list['href']
        print str(j) + ":" +c_path
        c_html=downloadHtml(c_path)
        c_soup=BeautifulSoup(c_html,'html.parser')
        detail_content = c_soup.find('div',{'id':'article','class':'content'})
        file_content=detail_content.get_text().replace('	', '').replace(' ', '').replace('\n',',').strip()
        with open(downloadPath + str(j) + '.txt', "wb") as code:
            if file_content == '':
                file_content = c_soup.get_text().replace('	', '').replace(' ', '').replace('\n',',').strip()
            code.write(file_content)