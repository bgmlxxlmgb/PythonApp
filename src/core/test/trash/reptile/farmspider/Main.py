# -*- coding: utf-8 -*-
import urllib2
from bs4 import BeautifulSoup
import random
class Main():
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
        }
        self.ipAddressListUrl='http://www.xicidaili.com/'

    def downloadSinglePage(self,url,headers,proxies=None):
        print "开始下载："+url
        request = urllib2.Request(url, headers=headers)
        response = urllib2.urlopen(request)
        pageContent = response.read()
        return pageContent
    def initProxiesPropert(self,main):
        proxies={}
        ipListPage = main.downloadSinglePage(main.ipAddressListUrl, headers=main.headers, proxies=None)
        soup = BeautifulSoup(ipListPage, 'lxml')
        trs = soup.find_all('tr')
        ipList = []
        if len(trs) > 0:
            for i in range(1, len(trs)):
                info = trs[i]
                ip = info.find_all('td')
                if len(ip) > 3:
                    ipList.append('http://'+str(ip[1].text) + ":" + str(ip[2].text))
        if len(ipList)>0:
            proxy_ip = None
            while proxy_ip is None or proxy_ip=='':
                proxy_ip = random.choice(ipList)
            proxies = {'http': proxy_ip}
        return proxies
if __name__=="__main__":
    main=Main()
    #proxies=main.initProxiesPropert(main)
    #print '当前代理信息：'+str(proxies)
    pear_page_url='http://www.zgncpw.com/sell/list/64/1/'
    pear_page_content=main.downloadSinglePage(pear_page_url,headers=main.headers)
    soup=BeautifulSoup(pear_page_content,'lxml')
    prod_lis=soup.find_all('li')
    for i in range(1,len(prod_lis)):
        if len(prod_lis[i].find_all('a'))>1:
            prod_a_tag_url=prod_lis[i].find_all('a')[1].get('href')
            if prod_a_tag_url.find('/sell/show/')!=-1:
                print prod_a_tag_url