# -*- coding: utf-8 -*-
import urllib2
import re
import time
import urllib
import requests
import os
from requests.adapters import HTTPAdapter

headers = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'zh-CN,zh;q=0.9',
    'Cache-Control':'max-age=0',
    'Connection':'keep-alive',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
}
def saveImage( imgUrl,savePath,imgName ="default.jpg",dTimes=0 ):
    print "准备下载："+imgUrl
    #request = urllib2.Request(imgUrl, headers=headers)
    #response = urllib2.urlopen(request)
    #image = response.read()
    try:
        DstDir = savePath
        if os.path.exists(DstDir + imgName):
            return ""
        time.sleep(1)
        s = requests.Session()
        s.mount('http://', HTTPAdapter(max_retries=3))
        image = s.get(imgUrl, timeout=10)
        print("saveFile " + unicode(DstDir + imgName) + "\n")
        with open(DstDir+imgName ,"wb") as jpg:
            jpg.write( image.content)
            jpg.close
    except:
        print "下载图片进入异常"
        return ""
        #if dTimes<3:
        #    print "尝试下载"+imgUrl+"第"+str(dTimes)+"次"
        #    saveImage(imgUrl,imgName,dTimes+1)
        #    jpg.close

def downloadSingleHtmlFile(targetURL,dTime=0):
    if targetURL is None:
        print "error target url"
        return ""
    else:
        content = ""
        try:
            request = urllib2.Request(targetURL, headers=headers)
            response = urllib2.urlopen(request)
            content = response.read()
        except:
            print "下载网页进入异常"
            return ""
            #if dTime<3:
            #    print "尝试下载" + targetURL + "第" + str(dTime) + "次"
            #    content=downloadSingleHtmlFile(targetURL,dTime+1)
            #    return content
            #else:
            #    return ""
        return content

def downloadPicsInOnePage(main_url,savePath):
    print "开始下载"+main_url+"中的图片。"
    content = downloadSingleHtmlFile(main_url)
    if content!="":
        reg = r'<a href="(.+?\.jpg)" target="_blank">'
        imgre = re.compile(reg)
        imglist = re.findall(imgre, content)
        for imgurl in imglist:
            imgurl = imgurl.replace("i/?i=", '')
            pic_name = imgurl.split("/")[len(imgurl.split("/")) - 1]
            saveImage(imgurl,savePath,pic_name,0)

def queryAllPage(mode_urls,total):
    for i in range(1, total):
        page_urls = mode_urls + str(i)
        content = downloadSingleHtmlFile(page_urls)
        if content!="":
            reg = r'<a href="htm_data/(.+?\.html)"'
            pagere = re.compile(reg)
            pagelist = re.findall(pagere, content)
            for pageurl in pagelist:
                reg = r'<a href="htm_data/' + pageurl + '" id="a_ajax_(.+?)">'
                idre = re.compile(reg)
                idlist = re.findall(idre, content)
                pageid = ""
                for id in idlist:
                    pageid = id
                reg = r'<a href="htm_data/' + pageurl + '" id="a_ajax_' + pageid + '">(.+?)</a>'
                titlere = re.compile(reg)
                titlelist = re.findall(titlere, content)
                pagetitle = ""
                for title in titlelist:
                    pagetitle = title
                pagefullurl = "http://w3.afulyu.rocks/pw/htm_data/" + pageurl
                path="F:/Development/DownloadsTest/20171119/pics/"
                pagetitle = unicode(pagetitle.replace(" ", ""),"utf-8")
                path+=pagetitle+"/"
                if not os.path.exists(path):
                    os.makedirs(path)
                print path
                print pagefullurl
                downloadPicsInOnePage(pagefullurl,path)
                print "\n"
    time.sleep(3)

#701
# Pages: ( 1/701 total )
def queryTotalPages(mode_urls):
    for i in range(1, 2):
        page_urls = mode_urls + str(i)
        content = downloadSingleHtmlFile(page_urls)
        reg = r'Pages: \( 1/(.+?) total \) '
        pagecntre = re.compile(reg)
        pagecntlist = re.findall(pagecntre, content)
        totalPageNum = 0
        for pagecnt in pagecntlist:
            totalPageNum = int(pagecnt)
        totalPageNum += 1
        return totalPageNum

mode_urls="http://w3.afulyu.rocks/pw/thread.php?fid=15&page="
cnt=queryTotalPages(mode_urls)
print cnt
queryAllPage(mode_urls,cnt)