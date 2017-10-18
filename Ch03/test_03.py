# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 14:22:22 2017

@author: hh
"""

import treePlotter
import trees

"""测试熵值计算"""
def testShannonEnt():
    myDat,labels = trees.createDataSet()
    print (trees.calcShannonEnt(myDat))

"""测试划分数据集"""
def testSplitData():
    myDat,labels = trees.createDataSet()
    print(trees.splitDataSet(myDat,0,1))
    print(trees.splitDataSet(myDat,0,0))

"""测试最好的划分方式"""
def testChooseBestFeatureToSplit():
    myDat,labels = trees.createDataSet()
    print(trees.chooseBestFeatureToSplit(myDat))

"""测试创建树"""
def testCreateTree():
    myDat,labels = trees.createDataSet()
    myTree = trees.createTree(myDat,labels)
    print(myTree)
    
"""测试决策树判断新数据点"""
def testClassify():
    myDat,labels = trees.createDataSet()
    myTree = trees.createTree(myDat,labels)
    myDat,labels = trees.createDataSet()
    print(trees.classify(myTree,labels,[1,0]))
    print(trees.classify(myTree,labels,[1,1]))
    
"""测试决策树保存"""   
def testStoreAndGrabTree():
    myDat,labels = trees.createDataSet()
    myTree = trees.createTree(myDat,labels)
    trees.storeTree(myTree,'trees.txt')
    reloadMyTree = trees.grabTree('trees.txt')
    print(reloadMyTree)    
"""---------------------------------------"""



# testShannonEnt()
# testSplitData()
# testChooseBestFeatureToSplit()
# testCreateTree()
# testClassify()
# testStoreAndGrabTree()

testCreateTree()