# -*- coding: utf-8 -*
import urllib2
from bs4 import BeautifulSoup
class Splider:
    def __init__(self):
        self.downloadUtils = DownloadUtils()
        self.ParseHtml = ParseHtml()

class DownloadUtils:
    def downloadSingleHtmlFile(self,targetURL):
        if targetURL is None:
            print "error target url"
            return None
        else:
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
                "Cookie": "__jdv=122270672|direct|-|none|-|1507347400071; areaId=19; ipLoc-djd=19-1601-3633-0; __jda=122270672.373567638.1506248973.1506248973.1507347400.1; __jdc=122270672; 3AB9D23F7A4B3C9B=TT2AIXEUZJ4QXIBDNNLJ3D7PYV36R4GLVI3TXLCADUAV6WL466YYNSBX6HGZLETVYTV2AG5EPRXQ3DSDYNARLUMBTY; aud=4562e504e09e2038b694d8632be254c0; aud_ver=1; avt=1; asn=13; __jdu=373567638",
                "Accept": "text/html,application/xhtml+xml,application/xml,image/webp,image/apng,image/*;q=0.9,*/*;q=0.8"
            }
            content = ""
            try:
                request = urllib2.Request(targetURL, headers=headers)
                response = urllib2.urlopen(request)
                content = response.read()
            except urllib2.URLError, e:
                if hasattr(e, "reason") and hasattr(e, "code"):
                    print e.code
                    print e.reason
                else:
                    print "请求下载页面失败"
            return content

class ParseHtml:
    def parseSingleHtml(self,content):
        soup = BeautifulSoup(content,"html.parser")
        # print soup.prettify()
        # print soup.li
        for child in soup.find_all("a"):
            print child


if __name__ =="__main__":
    targetURL="https://list.jd.com/list.html?cat=9987,653,655&page=4&sort=sort_rank_asc&trans=1&JL=6_0_0#J_main"
    splider = Splider()

    downloadUtil = DownloadUtils()
    content = downloadUtil.downloadSingleHtmlFile(targetURL)

    parseHtml = ParseHtml()
    parseHtml.parseSingleHtml(content)



