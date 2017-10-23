# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 20:14:00 2017

@author: hh
"""

from numpy import *

""" 加载数据集 """
def loadDataSet():
    dataMat = []; labelMat = []
    fr = open('testSet.txt')
    for line in fr.readlines():
        lineArr = line.strip().split()
        dataMat.append([1.0, float(lineArr[0]), float(lineArr[1])])
        labelMat.append(int(lineArr[2]))
    return dataMat,labelMat

""" sigmoid函数 """
def sigmoid(inX):
    return 1.0/(1+exp(-inX))

""" 梯度上升 """
def gradAscent(dataMatIn, classLabels):
    dataMatrix = mat(dataMatIn)             #转换为 NumPy 矩阵
    labelMat = mat(classLabels).transpose() #转换为 NumPy 矩阵，求转置 （行向量-->列向量）
    m,n = shape(dataMatrix)                 #获取矩阵的大小 
    alpha = 0.001                           #步长
    maxCycles = 500                         #迭代代数
    weights = ones((n,1))                   #权重向量
    for k in range(maxCycles):              
        h = sigmoid(dataMatrix*weights)
        error = (labelMat - h)              # 惩罚度
        weights = weights + alpha * dataMatrix.transpose()* error 
    return weights

""" 绘制拟合后的直线 """
def plotBestFit(weights):
    import matplotlib.pyplot as plt
    dataMat,labelMat=loadDataSet()
    dataArr = array(dataMat)
    n = shape(dataArr)[0]      #  数据点的个数 
    xcord1 = []; ycord1 = []
    xcord2 = []; ycord2 = []
    for i in range(n):         #  根据数据点的类型进行分类
        if int(labelMat[i])== 1:
            xcord1.append(dataArr[i,1]); ycord1.append(dataArr[i,2])
        else:
            xcord2.append(dataArr[i,1]); ycord2.append(dataArr[i,2])
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(xcord1, ycord1, s=30, c='red', marker='s')
    ax.scatter(xcord2, ycord2, s=30, c='green')
    x = arange(-3.0, 3.0, 0.1)
    y = (-weights[0]-weights[1]*x)/weights[2]
    ax.plot(x, y)
    plt.xlabel('X1'); plt.ylabel('X2');
    plt.show()
    
    
    
""" 随机梯度上升0"""
def stocGradAscent0(dataMatrix, classLabels):
    m,n = shape(dataMatrix)
    alpha = 0.01
    weights = ones(n)   
    for i in range(m):
        h = sigmoid(sum(dataMatrix[i]*weights)) # 每次只选取一个特征点进行训练
        error = classLabels[i] - h
        weights = weights + alpha * error * dataMatrix[i]
    return weights
    

""" 随机梯度上升1 """
def stocGradAscent1(dataMatrix, classLabels, numIter=150):
    m,n = shape(dataMatrix)
    weights = ones(n)   
    for j in range(numIter):
        dataIndex = list(range(m))    # rang 对象无法迭代
        for i in range(m):
            alpha = 4/(1.0+j+i)+0.0001    # 步长会随着迭代进行而减少，但不会为0。防止波动和停止不前
            randIndex = int(random.uniform(0,len(dataIndex)))  # 随机选取迭代值，防止周期波动
            h = sigmoid(sum(dataMatrix[randIndex]*weights))
            error = classLabels[randIndex] - h
            weights = weights + alpha * error * dataMatrix[randIndex]
            del(dataIndex[randIndex])
    return weights

"""-----------------------------------------------------------"""

""" 利用回归系数和特征量计算类别"""
def classifyVector(inX, weights):
    prob = sigmoid(sum(inX*weights))
    if prob > 0.5: return 1.0
    else: return 0.0

""" 加载数据 训练 测试"""
def colicTest():
    # 训练回归系数
    frTrain = open('horseColicTraining.txt'); frTest = open('horseColicTest.txt')
    trainingSet = []; trainingLabels = []
    for line in frTrain.readlines():
        currLine = line.strip().split('\t')
        lineArr =[]
        for i in range(21):
            lineArr.append(float(currLine[i]))
        trainingSet.append(lineArr)
        trainingLabels.append(float(currLine[21]))
    trainWeights = stocGradAscent1(array(trainingSet), trainingLabels, 500)
    # 测试分类效果
    errorCount = 0; numTestVec = 0.0
    for line in frTest.readlines():
        numTestVec += 1.0
        currLine = line.strip().split('\t')
        lineArr =[]
        for i in range(21):
            lineArr.append(float(currLine[i]))
        if int(classifyVector(array(lineArr), trainWeights))!= int(currLine[21]):
            errorCount += 1
    errorRate = (float(errorCount)/numTestVec)
    print ("the error rate of this test is: %f" % errorRate)
    return errorRate


    
    
