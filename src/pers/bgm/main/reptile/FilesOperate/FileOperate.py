# -*- coding: utf-8 -*
import os
class FileOperate:
    def __init__(self, parentPath, confFileName):
        # self.readOnce(parentPath,confFileName)
        self.readByLines(parentPath, confFileName)

    def readOnce(self, parentPath, confFileName):
        print "in readOnce fun"
        os.chdir(parentPath)
        urlsConfFile = open(confFileName)
        try:
            content = urlsConfFile.read()
            print content
        finally:
            urlsConfFile.close()

    def readByLines(self, parentPath, confFileName):
        print "in readByLines fun"
        os.chdir(parentPath)
        urlsConfFile = open(confFileName)
        try:
            for line in urlsConfFile:
                print line
        finally:
            urlsConfFile.close()

    def writeByContent(self, parentPath, dataFileName, content):
        os.chdir(parentPath)
        htmlsDataFile = open(dataFileName, "w+")
        htmlsDataFile.write(content)
        htmlsDataFile.close()


if __name__ == "__main__":
    parentPath = "F:\\Development\\Project\\PythonApp\\src\\pers\\bgm\\main\\reptile\\resources"
    confFileName = "UrlsConf.txt"
    dataFileName = "htmlsDataFile.txt"
    FileOperate = FileOperate(parentPath, confFileName)
