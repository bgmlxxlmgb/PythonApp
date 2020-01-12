# -*- coding: utf-8 -*
import urllib
import urllib2
import requests
class DownloadFile:
    def __init__(self):
        self.downloadPath="F:\\Development\\DownloadsTest\\20171119"

    def downloadOneFileWithUrlLib(self,url,fileName):
        urllib.urlretrieve(url, self.downloadPath + fileName)

    def downloadOneFileWithRequest(self,url,fileName):
        r = requests.get(url)
        with open( self.downloadPath + fileName, "wb") as code:
            code.write(r.content)

    def downloadOneFileWithUrlLib2(self,url,fileName):
        f = urllib2.urlopen(url)
        data = f.read()
        with open( self.downloadPath + fileName, "wb") as code:
            code.write(data)

if __name__ == "__main__":
    downloadFile = DownloadFile()
    url="http://c.siimg.com/u/20171119/222152291.jpg"
    path="222152291.jpg"
    downloadFile.downloadOneFileWithRequest(url,path)