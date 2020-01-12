# -*- coding: utf-8 -*-
import urllib2
import urllib
import requests
import os
from requests.adapters import HTTPAdapter
import sys

headers = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'zh-CN,zh;q=0.9',
    'Cache-Control':'max-age=0',
    'Connection':'keep-alive',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
}

def saveImage( imgUrl,savePath,imgName ="default.jpg"):
    print "准备下载："+imgUrl
    try:
        DstDir = savePath
        if os.path.exists(DstDir + imgName):
            return ""

        #request = urllib2.Request(imgUrl, headers=headers)
        #response = urllib2.urlopen(request)
        #image = response.read()
        s = requests.Session()
        s.mount('http://', HTTPAdapter(max_retries=3))
        image = s.get(imgUrl, timeout=1)
        print("saveFile " + unicode(DstDir + imgName) + "\n")
        deleteTag=0
        with open(DstDir+imgName ,"wb") as jpg:
            if (sys.getsizeof(image.content)/1024) > 10 :
                jpg.write( image.content)
                jpg.close
            else:
                deleteTag=1
        if deleteTag==1 :
            print "删除空文件："+(DstDir + imgName)
            os.remove(DstDir + imgName)
    except:
        print "下载图片"+imgUrl+"进入异常，图片不存在！"
        return ""

if __name__ =="__main__":
    savedPath='F:/Development/DownloadsTest/20171209v1/'
    prefix='http://img.easi88.com:89/91pc/mt/'
    for i in range(1,41,1):
        for j in range(1,20,1):
            fileName=str(i)+'-'+str(j)+'.jpg'
            suffix=str(i)+'/'+fileName
            imgUrl=prefix+suffix
            saveImage(imgUrl,savedPath,fileName)