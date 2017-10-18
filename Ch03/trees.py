# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 16:07:39 2017

@author: hh
"""

from math import log
import operator
import pickle

"""创建测试数据集合"""
def createDataSet():
    dataSet = [[1, 1, 'yes'],
               [1, 1, 'yes'],
               [1, 0, 'no'],
               [0, 1, 'no'],
               [0, 1, 'no'],]
    labels = ['no surfacing','flippers']
    return dataSet, labels

"""计算熵值"""
def calcShannonEnt(dataSet):
    numEntries = len(dataSet)
    labelCounts = {}                            # 用于储存分类标签的种类和个数
    for featVec in dataSet: 
        currentLabel = featVec[-1]              # 当前数据点的分类标签
        if currentLabel not in labelCounts.keys(): 
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1
    shannonEnt = 0.0
    for key in labelCounts:
        prob = float(labelCounts[key])/numEntries
        shannonEnt -= prob * log(prob,2)        #以2为底求对数
    return shannonEnt



"""划分数据集"""
'''
dataSet:带划分数据集
axis:划分数据集的特征（第axis个，从零开始计数）
value:需要返回的特征的值

'''
def splitDataSet(dataSet, axis, value):
    retDataSet = []             
    for featVec in dataSet:
        if featVec[axis] == value:
            reducedFeatVec = featVec[:axis]    
            reducedFeatVec.extend(featVec[axis+1:])
            retDataSet.append(reducedFeatVec)          # 当前数据点 除去当前特征后保存
    return retDataSet




"""寻找最好的划分方式"""

def chooseBestFeatureToSplit(dataSet):
    numFeatures = len(dataSet[0]) - 1         # 获得特征个数    
    baseEntropy = calcShannonEnt(dataSet)     # 原始的熵值
    bestInfoGain = 0.0
    bestFeature = -1
    for i in range(numFeatures):             # 对于每一个特征都进行迭代
        featList = [example[i] for example in dataSet]   # 提取当前特征在每个数据点中的值
        uniqueVals = set(featList)           #转换为一个set集合（没有重复元素）
        newEntropy = 0.0
        for value in uniqueVals:
            # 针对数据集合，对第i个特征进行分类，返回值是特征值为value的
            subDataSet = splitDataSet(dataSet, i, value)  
            prob = len(subDataSet)/float(len(dataSet))
            newEntropy += prob * calcShannonEnt(subDataSet)     
        infoGain = baseEntropy - newEntropy     
        if (infoGain > bestInfoGain):       # 比较每次分类信息增益
            bestInfoGain = infoGain         # 如果大，就替换当前的值
            bestFeature = i
    return bestFeature  

    
"""返回出现次数最多的分类名称"""
def majorityCnt(classList):
    classCount={}
    for vote in classList:
        if vote not in classCount.keys(): classCount[vote] = 0
        classCount[vote] += 1
    sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]

"""创建树"""
def createTree(dataSet,labels):
    classList = [example[-1] for example in dataSet]    # 分类标签的值
    if classList.count(classList[0]) == len(classList): 
        return classList[0]      # 所有的标签的类都相同 返回这个类标签
    if len(dataSet[0]) == 1:     # 如果所有的特征都用完了，则停止
        return majorityCnt(classList)
    bestFeat = chooseBestFeatureToSplit(dataSet)  # 获得信息增益最大的分类特征
    bestFeatLabel = labels[bestFeat]              # 获得当前特征的具体含义
    myTree = {bestFeatLabel:{}}
    del(labels[bestFeat])   # 删除已分类的特征
    featValues = [example[bestFeat] for example in dataSet]   # 当前特征下的数据点特征值
    uniqueVals = set(featValues)     # 转换为list类型
    for value in uniqueVals:
        subLabels = labels[:]       # 拷贝标签 
        myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet, bestFeat, value),subLabels)
    return myTree 





"""利用决策树判断新数据点"""
def classify(inputTree,featLabels,testVec):
    firstSides = list(inputTree.keys())   # 第一个分类特征
    firstStr = firstSides[0]        #找到输入的第一个元素
    secondDict = inputTree[firstStr]      # 二级字典 
    featIndex = featLabels.index(firstStr)   # 当前特征值在数据集的位置,返回时索引
    key = testVec[featIndex]             # 拿到新数据点的当前特征的特征值
    valueOfFeat = secondDict[key]        # 根据特征值 划分数据点
    if isinstance(valueOfFeat, dict):  # 如果不是叶节点，迭代；
        classLabel = classify(valueOfFeat, featLabels, testVec)
    else: classLabel = valueOfFeat     # 如果是叶节点，返回标签类
    return classLabel

"""序列化并写入磁盘"""
def storeTree(inputTree,filename):
    fw = open(filename,'wb+')   # 要以二进制格式打开文件
    pickle.dump(inputTree,fw)
    fw.close()

"""读取磁盘并反序列化"""   
def grabTree(filename):
    fr = open(filename,'rb')    # 要以二进制格式打开文件
    return pickle.load(fr)





"""------------------------------------------------"""

def classify_lenses():
    fr = open('lenses.txt')
    lenses = [inst.strip().split('\t') for inst in fr.readlines()]
    lensesLabels = ['age','prescript','astigmatic','teraRate']
    lensesTree = createTree(lenses,lensesLabels)
    treePlotter.createPlot(lensesTree)
    
# classify_lenses()