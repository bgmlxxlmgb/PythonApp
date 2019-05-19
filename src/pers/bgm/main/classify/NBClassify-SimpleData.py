# -*- coding:utf-8 -*-

from numpy import *

# 创建样例数据
def loadDataSet():
    d_set = [['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
             ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
             ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
             ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
             ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
             ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']
            ]
    c_set = [0, 1, 0, 1, 0, 1]  # 1代表脏话
    return d_set, c_set


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
        else:
            print ("The word %s is not in Common Vocabulary Set!" %word)
    return r_vec

#训练模型
def trainNB0(trainMat,trainCat):
    numTrainDocs = len(trainMat)
    numWords = len(trainMat[0])
    pAbusive = sum(trainCat)/float(numTrainDocs)
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
    return p0Vect,p1Vect,pAbusive

#分类器
def classifyNB(vec2Classify,p0Vec,p1Vec,pClass1):
    p1 = sum(vec2Classify*p1Vec) + log(pClass1)
    p0 = sum(vec2Classify*p0Vec) + log(1-pClass1)
    print p1
    print p0

# 测试案例
def testNB():
    d_set,c_set = loadDataSet()
    cv_set = createVocabList(d_set)
    trainMatrix = []
    for postinDoc in d_set:
        trainMatrix.append(setOfWords2Vec(cv_set,postinDoc))
    p0V,p1V,pAbusive = trainNB0(array(trainMatrix),array(c_set))
    print p0V
    print p1V
    print pAbusive
    testEntry = ['stupid','my','dog','quit']
    testDoc = array(setOfWords2Vec(cv_set,testEntry))
    print testDoc
    classifyNB(testDoc,p0V,p1V,pAbusive)

# 测试启动入口
if __name__ == '__main__':
    testNB()