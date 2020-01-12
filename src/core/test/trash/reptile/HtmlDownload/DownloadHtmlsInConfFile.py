# -*- coding: utf-8 -*
# import sys
# sys.path.append('F:/Development/Project/PythonApp/src/pers/bgm/main/reptile/FilesOperate/FileOperate.py')
# from Spider import *
from FilesOperate import FileOperate

class DownloadHtmlsInConfFile:
    def __init__(self):
        print "hello"
        self.fileOperate = FileOperate()

    def download(self,parentPath,confFileName,dataFileName):
        for url in self.fileOperate.readByLines():
            print url
if __name__ == "__main__":
    downloadHtmlsInConfFile = DownloadHtmlsInConfFile()
    parentPath = "F:\\Development\\Project\\PythonApp\\src\\pers\\bgm\\main\\reptile\\resources"
    confFileName = "UrlsConf.txt"
    dataFileName = "htmlsDataFile.txt"
    downloadHtmlsInConfFile.download(parentPath,confFileName,dataFileName)

