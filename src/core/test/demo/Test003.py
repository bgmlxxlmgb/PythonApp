# -*- coding: utf-8 -*-
import urllib2
import re
import time
import urllib
import requests
import os
headers = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'zh-CN,zh;q=0.9',
    'Cache-Control':'max-age=0',
    'Connection':'keep-alive',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
}
request = urllib2.Request("http://c.siimg.com/u/20171119/222152291.jpg")
response = urllib2.urlopen(request)
image = response.read()
print(image)