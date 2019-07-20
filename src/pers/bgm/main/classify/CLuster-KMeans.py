# -*- coding:utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import numpy as np
#from numpy import *

#计算欧式距离
def distEcloud(vecA,vecB):
    return np.sqrt(np.sum(np.power(vecA-vecB,2)))

#随机设置K个中心点
def randCenter(dataSet,k):
    raw_number=np.shape(dataSet)[1]
    zeroMatrix=np.mat(np.zeros([k,raw_number]))
    for i in range(raw_number):
        mini=np.min(dataSet[:,i])
        rangei=float(np.max(dataSet[:,i])-mini)
        zeroMatrix[:,i]=np.mat(mini+rangei*np.random.rand(k,1))
    return zeroMatrix


def KMeans(dataSet, k, distMeans=distEcloud, createCent=randCenter):
    m = np.shape(dataSet)[0]  # 得到行数，即为样本数
    clusterAssement = np.mat(np.zeros([m, 2]))  # 创建 m 行 2 列的矩阵
    centroids = createCent(dataSet, k)  # 初始化 k 个中心点
    clusterChanged = True
    while clusterChanged:
        clusterChanged = False
        for i in range(m):
            minDist = np.inf  # 初始设置值为无穷大
            minIndex = -1
            for j in range(k):
                #  j循环，先计算 k个中心点到1 个样本的距离，在进行i循环，计算得到k个中心点到全部样本点的距离
                distJ = distMeans(centroids[j, :], dataSet[i, :])
                if distJ < minDist:
                    minDist = distJ  # 更新 最小的距离
                    minIndex = j
            if clusterAssement[i, 0] != minIndex:  # 如果中心点不变化的时候， 则终止循环
                clusterChanged = True
            clusterAssement[i, :] = minIndex, minDist ** 2  # 将 index，k值中心点 和  最小距离存入到数组中
        print(centroids)

        # 更换中心点的位置
        for cent in range(k):
            ptsInClust = dataSet[np.nonzero(clusterAssement[:, 0].A == cent)[0]]  # 分别找到属于k类的数据
            centroids[cent, :] = np.mean(ptsInClust, axis=0)  # 得到更新后的中心点
    return centroids, clusterAssement

def KMeans1(dataset,k,distMeans=distEcloud):
    line_number=np.shape(dataset)[0]
    row_number = np.shape(dataset)[1]
    clusterMat=np.mat(np.zeros([line_number,row_number]))
    center_point=randCenter(dataset,k)
    clusterChanged=True
    while clusterChanged:
        clusterChanged=False
        for i in range(line_number):
            minDist=np.inf
            minIndex=-1
            for j in range(k):
                distJ=distEcloud(center_point[j,:],dataset[i,:])
                if distJ < minDist:
                    minDist=distJ
                    minIndex=j
            if clusterMat[i,0] !=minIndex:
                clusterChanged=True
            clusterMat[i,:]=[minIndex,minDist**2]

        for cent in range(k):
            ptsInClust=dataset[np.nonzero(clusterMat[:,0].A==cent)[0]]
            center_point[cent,:]=np.mean(ptsInClust,axis=0)
        print ptsInClust
    return center_point,clusterMat

dataSetMatrix=np.mat([
        [0.90796996, 5.05836784]
        , [-2.88425582, 0.01687006]
        , [-3.3447423, -1.01730512]
        , [-0.32810867, 0.48063528]
        , [1.90508653, 3.530091]
        , [-3.00984169, 2.66771831]
        , [-3.38237045, -2.9473363]
        , [2.22463036, -1.37361589]
        , [2.54391447, 3.21299611]
        , [-2.46154315, 2.78737555]
        , [-3.38237045, -2.9473363]
        , [2.8692781, -2.54779119]
        , [2.6265299, 3.10868015]
        , [-2.46154315, 2.78737555]
        , [-3.38237045, -2.9473363]
        , [2.80293085, -2.7315146]
    ]
)

#distEcloud计算点与点之间的距离-测试
#vecA=np.array([1,0])
#vecB=np.array([4,4])
#print distEcloud(vecA,vecB)
#201907201715 update
center,cluster=KMeans1(dataSetMatrix,5)
print center
print cluster
