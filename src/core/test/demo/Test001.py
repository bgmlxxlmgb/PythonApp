# -*- coding: utf-8 -*
# import re
# from bs4 import BeautifulSoup
# import json
# import threading
# from requests import Session
import urllib2
class Splider:
    def __init__(self):
        self.downloader = Download()

    def craw_search_word(self, root_url):
        content=self.downloader.download(root_url)
        print content


class Download(object):
    def download(self, url):
        if url is None:
            return None
        headers = {
                   "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:52.0) Gecko/20100101 Firefox/52.0",
                   "Cookie" : "Hm_lvt_0c0e9d9b1e7d617b3e6842e85b9fb068=1466075280; __utma=194070582.826403744.1466075281.1466075281.1466075281.1; __utmv=194070582.|2=User%20Type=Visitor=1; signin_redirect=http%3A%2F%2Fwww.jianshu.com%2Fsearch%3Fq%3D%25E7%2594%259F%25E6%25B4%25BB%26page%3D1%26type%3Dnote; _session_id=ajBLb3h5SDArK05NdDY2V0xyUTNpQ1ZCZjNOdEhvNUNicmY0b0NtMnVuUUdkRno2emEyaFNTT3pKWTVkb3ZKT1dvbTU2c3c0VGlGS0wvUExrVW1wbkg1cDZSUTFMVVprbTJ2aXhTcTdHN2lEdnhMRUNkM1FuaW1vdFpNTDFsQXgwQlNjUnVRczhPd2FQM2sveGJCbDVpQUVWN1ZPYW1paUpVakhDbFVPbEVNRWZzUXh5R1d0LzE2RkRnc0lJSHJEOWtnaVM1ZE1yMkt5VC90K2tkeGJQMlVOQnB1Rmx2TFpxamtDQnlSakxrS1lxS0hONXZnZEx0bDR5c2w4Mm5lMitESTBidWE4NTBGNldiZXVQSjhjTGNCeGFOUlpESk9lMlJUTDVibjNBUHdDeVEzMGNaRGlwYkg5bHhNeUxJUVF2N3hYb3p5QzVNTDB4dU4zODljdExnPT0tLU81TTZybUc3MC9BZkltRDBiTEsvU2c9PQ%3D%3D--096a8e4707e00b06b996e8722a58e25aa5117ee9; CNZZDATA1258679142=1544596149-1486533130-https%253A%252F%252Fwww.baidu.com%252F%7C1486561790; _ga=GA1.2.826403744.1466075281; _gat=1",
                   "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
                   }
        content = ""
        try:
            request = urllib2.Request(url, headers = headers)
            response = urllib2.urlopen(request)
            content = response.read()
        except urllib2.URLError, e:
            if hasattr(e, "reason") and hasattr(e, "code"):
                print e.code
                print e.reason
            else:
                print "请求失败"
        return content

if __name__ == "__main__":
    root_url = "https://list.jd.com/list.html?cat=9987,653,655&page=4&sort=sort_rank_asc&trans=1&JL=6_0_0#J_main"
    splider = Splider()
    splider.craw_search_word(root_url)