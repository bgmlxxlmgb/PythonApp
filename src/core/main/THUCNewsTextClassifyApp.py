# -*- coding: UTF-8 -*-

import os
import jieba
import pymysql

trainDataDir = "/home/guimingbao/Data/model/train/"
stopWordsFilePath = "/home/guimingbao/Data/model/stopwords.txt"
stopwords = {}
wordPacketPath = "/home/guimingbao/Data/packet/vocaPacket.dat"
trainMatFile="/home/guimingbao/Data/trainMat.dat"
trainCatFile="/home/guimingbao/Data/trainCat.dat"

def init():
    print("----------------------------------------SUMMARY------------------------------------------\n"
          "- This is a sinple app to classify identify text by some classify algorithmic\n"
          "- you may change or input some other core classify choice if exists or you  \n"
          "- may extend it by your self.\n"
          "- Say Hurry Up to You!\n"
          "-----------------------------------------------------------------------------------------\n")

def readSingleFile(singlefilepath):

    fileExists = os.path.isfile(singlefilepath)
    singlefile = None
    fileContent = ""
    if bool(1-fileExists):
        print("The file path <"+singlefilepath+"> is not a file path or not exists , please check! Now ready to breakdown...")
        return -1
    try:
        singlefile = open(singlefilepath,'r')
        for line in singlefile.readlines():
            fileContent += line.replace("　　","").replace("\n"," ")
    except Exception as e:
        print(e.with_traceback())
    finally:
        singlefile.close()

    return fileContent

def combineSmallFile(combineFilePath,content):
    writeMode = "a"
    combineFile = open(combineFilePath,writeMode)
    combineFile.write(content+"\n")
    combineFile.flush()
    combineFile.close()

def combineSmallFileUnderDir(rootDir):

    dirExists = os.path.isdir(rootDir)

    if bool(1-dirExists):
        print("The directory <" + rootDir + "> is not a directory or not exists , please check! Now ready to breakdown...")
        return -1

    childFileNames = os.listdir(rootDir)

    for childFileName in childFileNames:

        childFileFullPath = rootDir + "" + childFileName
        childPathIsDir = os.path.isfile(childFileFullPath)

        if childPathIsDir:

            classify = childFileFullPath.split("/")[-2]
            fileContent = readSingleFile(childFileFullPath)
            trainDatachildDir = trainDataDir + "" + classify + ".dat"
            print(childFileFullPath)
            combineSmallFile(trainDatachildDir,fileContent)

        else:

            nextRootDir = childFileFullPath+"/"
            combineSmallFileUnderDir(nextRootDir)

def cutContentLine(lineContent):
    wordCut = jieba.cut(lineContent,cut_all=True)
    wordSet = set("|".join(wordCut).split("|")) - stopwords
    return wordSet

def genVocabPack(path):
    vocabPack = set({})
    filesName = os.listdir(path)
    conn = pymysql.connect(user='dev', password='dev', database='dev', charset='utf8mb4')
    #ccursor = conn.cursor()

    for singleFile in filesName:
        markedFilePath = path+""+singleFile
        print(markedFilePath)
        markedFile = open(markedFilePath,'r')
        ccursor = conn.cursor()
        for line in markedFile:
            wordList = cutContentLine(line)
            for s_word in wordList:

                query_sql = ("insert into train_model_word_top(word,tag) values(%s,%s);")

                ccursor.execute(query_sql,(s_word,singleFile.split('.')[0]))
            conn.commit()
            vocabPack.update(wordList)
        ccursor.close()
    conn.close()
    return vocabPack

def word2vect(path):
    filesName = os.listdir(path)
    packet = [line.strip() for line in open(wordPacketPath,"r").readlines()]
    vecDim = len(packet)
    trainMat = []
    trainCat = []
    for singleFile in filesName:
        markedFilePath = path+""+singleFile
        print(markedFilePath)
        markedFile = open(markedFilePath,'r')
        for line in markedFile:
            trainCat.append(singleFile)
            wordList = cutContentLine(line)
            lineVect = [0] * vecDim
            for word in wordList:
                if word in packet:
                    lineVect[packet.index(word)] = 1
            trainMat.append(lineVect)
    return trainMat,trainCat

if __name__ == "__main__":
    init()
    workingDir = "/home/guimingbao/Data/"
    trainSourceDataDir = workingDir + "upload/THUCNews/"
    trainCombinedDataDir = workingDir + "model/train/"
    stopwords = {line.strip() for line in open(stopWordsFilePath, 'r').readlines()}
    #packet = genVocabPack(path=trainCombinedDataDir)
    #print(len(packet))
    #open(workingDir+"packet/vocaPacket.dat",'a').write('\n'.join(packet))
    #print(stopwords)
    #combineSmallFileUnderDir(trainSourceDataDir)
    trainMat,trainCat=word2vect(trainCombinedDataDir)
    open(trainMatFile, "a").write(trainMat)
    open(trainCatFile, "a").write(trainCat)
