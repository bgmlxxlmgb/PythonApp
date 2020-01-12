# -*- coding: utf-8 -*-
import urllib.request
import time
from bs4 import BeautifulSoup
import string
local_headers={
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    #'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Cookie': '__cfduid=d5dd5640ae0522e743b04d4742c67ad3d1571149712; UM_distinctid=16e276f5d41166-0b986bdcdd8987-386a410b-100200-16e276f5d422d9; CNZZDATA1261158850=1700658907-1572614581-null%7C1576507644; aafaf_threadlog=%2C25%2C18%2C3%2C111%2C83%2C; aafaf_lastpos=F83; aafaf_ol_offset=201760; aafaf_lastvisit=6247%091576512128%09%2Fpw%2Fthread.php%3Ffid%3D83%26page%3D1',
    #'Host': '7086bt.com',
    #'Referer': 'http://7086bt.com/pw/thread.php?fid=83',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
}


def core(url,r_times=0):
    b_tag = 1
    html = ''
    while r_times<=3 and b_tag==1:
        try:
            # url 作为Request()方法的参数，构造并返回一个Request对象
            request = urllib.request.Request(url, headers=local_headers,)
            # Request对象作为urlopen()方法的参数，发送给服务器并接收响应
            response = urllib.request.urlopen(request,timeout=10)
            html = response.read()
            b_tag = 0
            html=html.decode('gb2312')
        except:
            r_times+=1
    return html




list_arr = []
for i in range(213,1215): #1214
    try:
        url='http://www.fl5y.com/xiazai/yuju/'+str(i)+'.html'
        content = core(url)
        soup = BeautifulSoup(content, "html.parser")
        ll=str(i)+"-"+soup.find("p").text+"|"+soup.find("source").attrs['src']
        list_arr.append(ll)
        print(ll)
    except:
        print(str(i)+"|")

index_file='file_list.txt'
ff = open(index_file,'a+')
for i in list_arr:
    ff.write(i+"\n")
ff.flush()
ff.close()