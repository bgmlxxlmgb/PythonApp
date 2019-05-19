# -*- coding:utf-8 -*-

# To re set python golbal character
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# Inport word cut tools about jieba lib
import jieba
import random
import time
import pickle
from numpy import *

DOC_NUM=4000
CLASS_SEX = 1
CLASS_NOT_SEX=0

def loadstopword():
    stopwords = []
    lines = open('F://Development//DataTrain//stopwords.txt').readlines()
    for line in lines:
        stopwords.append(line.strip().decode('utf-8'))
    return stopwords

# 创建词库，这里把所有词去重后，当作词库
def createVocabList(dataSet):
    vocabSet = set([])
    for document in dataSet:
        vocabSet = vocabSet | set(document) #求两个集合的并集
    return list(vocabSet)

#创建文本词向量，词库中每个词当作一个特征，文本中有这个词，则该词特征值就是1，否则为0
def setOfWords2Vec(comnvocanlist,dataset_line):
    r_vec = [0] * len(comnvocanlist)
    for word in dataset_line:
        if word in comnvocanlist:
            r_vec[comnvocanlist.index(word)] = 1
        #else:
         #   print ("The word %s is not in Common Vocabulary Set!" %word)
    return r_vec


# 训练模型
def trainNB0(trainMat, trainCat):
    numTrainDocs = len(trainMat)
    numWords = len(trainMat[0])
    pAbusive = sum(trainCat) / float(numTrainDocs)
    p0Num = ones(numWords)
    p1Num = ones(numWords)
    p0Denom = 2
    p1Denom = 2
    for i in range(numTrainDocs):
        if trainCat[i] == 1:
            p1Num += trainMat[i]
            p1Denom += sum(trainMat[i])
        else:
            p0Num += trainMat[i]
            p0Denom += sum(trainMat[i])

    p1Vect = log(p1Num / p1Denom)
    p0Vect = log(p0Num / p0Denom)
    return p0Vect, p1Vect, pAbusive

def textpreparser(stopwordlist,textcontent):
    cutedtext = jieba.cut(textcontent,cut_all=False)
    listofword = []
    for word in cutedtext:
        if word not in stopwordlist:
            if word !='\n':
                listofword.append(word)
    return listofword


# 分类方法(这边只做二类处理)
def classifyNaiveBayes(vec2Classify, pADVec, pNotADVec, pClass1):
    pIsAD = sum(vec2Classify * pADVec) + log(pClass1)  # element-wise mult
    pIsNotAD = sum(vec2Classify * pNotADVec) + log(1.0 - pClass1)

    if pIsAD > pIsNotAD:
        return CLASS_SEX
    else:
        return CLASS_NOT_SEX

def trainModel(stopwordlist):
    listAllDoc = []
    listClasses = []
    for i in range(1,DOC_NUM):
        wordslist = textpreparser(stopwordlist,open('F://Development//DataTrain//xingai/%d.txt'%i).read())
        listAllDoc.append(wordslist)
        listClasses.append(CLASS_SEX)
        print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))+":正在处理第%d个正文本"%i
    for i in range(1,DOC_NUM):
        wordslist = textpreparser(stopwordlist,open('F://Development//DataTrain//shuiguo/%d.txt'%i).read())
        listAllDoc.append(wordslist)
        listClasses.append(CLASS_NOT_SEX)
        print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))+":正在处理第%d个负文本" % i
    cv_set = createVocabList(listAllDoc)

    docNum = len(listAllDoc)
    print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))+":累计文档数:%d"%docNum
    testSetNum = int(docNum*0.1)
    print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))+":测试文档数:%d" % docNum
    trainingIndexSet = range(docNum)

    testSet = []
    for i in range(testSetNum):
        a=random.uniform(0,len(trainingIndexSet))
        rangeIndex = int(a)
        testSet.append(trainingIndexSet[rangeIndex])
        del(trainingIndexSet[rangeIndex])

    trainMatrix = []
    trainClasses = []

    for docIndex in trainingIndexSet:
        trainMatrix.append(setOfWords2Vec(cv_set,listAllDoc[docIndex]))
        trainClasses.append(listClasses[docIndex])

    p0,p1,pa=trainNB0(trainMatrix,trainClasses)
    errorCount = 0
    for docIndex in testSet:
        vecWord = setOfWords2Vec(cv_set, listAllDoc[docIndex])
        if classifyNaiveBayes(array(vecWord), p1, p0, pa) != listClasses[docIndex]:
            errorCount += 1
            doc = ' '.join(listAllDoc[docIndex])
    print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))+':错误率: ', float(errorCount) / len(testSet)

    #保存训练的模型
    args = dict()
    args['p0'] = p0
    args['p1'] = p1
    args['pa'] = pa

    fw = open("F://Development//DataTrain//classifyModel.dat", "wb")
    pickle.dump(args,fw,2)
    fw.close()
    print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))+":模型已经保存"

    fw = open("F://Development//DataTrain//classifyWordList.dat", "wb")
    pickle.dump(cv_set, fw, 2)
    fw.close()
    print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))+":词袋子已经保存"

if __name__ == "__main__":
    stopwordlist = loadstopword()
    #trainModel(stopwordlist)

    f=open("F://Development//DataTrain//classifyWordList.dat",'rb')
    word_bag=pickle.load(f)
    f.close()
    f=open("F://Development//DataTrain//classifyModel.dat",'rb')
    args=pickle.load(f)
    p0=args['p0']
    p1=args['p1']
    pa=args['pa']
    f.close()

    print classifyNaiveBayes(setOfWords2Vec(word_bag, textpreparser(stopwordlist, open( 'F://Development//DataTrain//xingai/4067.txt').read())), p1, p0, pa)



