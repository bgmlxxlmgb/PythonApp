# -*- coding:UTF-8 -*-

import urllib.request

local_headers={
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Cookie': 'Hm_lvt_91cf34f62b9bedb16460ca36cf192f4c=1587280623; Hm_lpvt_91cf34f62b9bedb16460ca36cf192f4c=1587284014',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0'
}

def downloadCore(url,r_times=0):
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
            html=html.decode('utf-8')
        except Exception as r:
            r_times+=1
            print(r)
    return html