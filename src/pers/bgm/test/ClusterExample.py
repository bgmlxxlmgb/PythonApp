from numpy import *
from PyKMeans import *
## step 1: load data
print "step 1: load data..."
dataSet = []
fileIn = open('F:/Development/Docu/PyResource/cluster-data.txt')
for line in fileIn.readlines():
    lineArr = line.strip().split('\t')
    dataSet.append([float(lineArr[0]), float(lineArr[1])])

## step 2: clustering...
print "step 2: clustering..."
dataSet_01 = mat(dataSet)
print dataSet_01
k = 4
centroids, clusterAssment = kmeans(dataSet_01, k)

## step 3: show the result
print "step 3: show the result..."
showCluster(dataSet_01, k, centroids, clusterAssment)