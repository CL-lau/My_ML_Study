# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 10:05:05 2017

@author: hh
"""

import matplotlib.pyplot as plt

""" 定义文本框和箭头格式 """
decisionNode = dict(boxstyle="sawtooth", fc="0.8")
leafNode = dict(boxstyle="round4", fc="0.8")
arrow_args = dict(arrowstyle="<-")

""" 绘制带箭头的注解 """
def plotNode(nodeTxt, centerPt, parentPt, nodeType):
    createPlot.ax1.annotate(nodeTxt, xy=parentPt,  xycoords='axes fraction',
             xytext=centerPt, textcoords='axes fraction',
             va="center", ha="center", bbox=nodeType, arrowprops=arrow_args )
    
def createPlot_test():
    fig = plt.figure(1, facecolor='white')
    fig.clf()
    createPlot.ax1 = plt.subplot(111, frameon=False)   
   
    plotNode('decisionNode',(0.5,0.1),(0.1,0.5),decisionNode)
    plotNode('leafNode',(0.8,0.1),(0.3,0.8),leafNode)
    plt.show()
    
""" 获取叶节点的数目 """
def getNumLeafs(myTree):
    numLeafs = 0
    firstSides = list(myTree.keys()) 
    firstStr = firstSides[0]        #树集合的第一个元素 
    secondDict = myTree[firstStr]
    for key in secondDict.keys():
        if type(secondDict[key]).__name__=='dict':#test to see if the nodes are dictonaires, if not they are leaf nodes
            numLeafs += getNumLeafs(secondDict[key])
        else:   numLeafs +=1
    return numLeafs


""" 获取树的层数 """
def getTreeDepth(myTree):
    maxDepth = 0
    firstSides = list(myTree.keys()) 
    firstStr = firstSides[0]        #找到输入的第一个元素
    secondDict = myTree[firstStr]
    for key in secondDict.keys():
        if type(secondDict[key]).__name__=='dict':#test to see if the nodes are dictonaires, if not they are leaf nodes
            thisDepth = 1 + getTreeDepth(secondDict[key])
        else:   thisDepth = 1
        if thisDepth > maxDepth: maxDepth = thisDepth
    return maxDepth


def retrieveTree(i):
    listOfTrees =[{'no surfacing': {0: 'no', 1: {'flippers': {0: 'no', 1: 'yes'}}}},
                  {'no surfacing': {0: 'no', 1: {'flippers': {0: {'head': {0: 'no', 1: 'yes'}}, 1: 'no'}}}}
                  ]
    return listOfTrees[i]


def testGitTreeInf():
    myTree = retrieveTree(1)
#    print(getNumLeafs(myTree))
    print(getTreeDepth(myTree))
    
  
def plotMidText(cntrPt, parentPt, txtString):
    xMid = (parentPt[0]-cntrPt[0])/2.0 + cntrPt[0]
    yMid = (parentPt[1]-cntrPt[1])/2.0 + cntrPt[1]
    createPlot.ax1.text(xMid, yMid, txtString, va="center", ha="center", rotation=30)

def plotTree(myTree, parentPt, nodeTxt):
    numLeafs = getNumLeafs(myTree)  # 叶的个数，也是整个图的 X 范围
    depth = getTreeDepth(myTree)    # 树的深度，也是整个图的 y 范围
    firstSides = list(myTree.keys())   # 第一个键，转换为list
    firstStr = firstSides[0]        #找到输入的第一个元素
    cntrPt = (plotTree.xOff + (1.0 + float(numLeafs))/2.0/plotTree.totalW, plotTree.yOff)
    plotMidText(cntrPt, parentPt, nodeTxt)
    plotNode(firstStr, cntrPt, parentPt, decisionNode)
    secondDict = myTree[firstStr]
    plotTree.yOff = plotTree.yOff - 1.0/plotTree.totalD
    for key in secondDict.keys():
        if type(secondDict[key]).__name__=='dict':
            plotTree(secondDict[key],cntrPt,str(key))        
        else:   
            plotTree.xOff = plotTree.xOff + 1.0/plotTree.totalW
            plotNode(secondDict[key], (plotTree.xOff, plotTree.yOff), cntrPt, leafNode)
            plotMidText((plotTree.xOff, plotTree.yOff), cntrPt, str(key))
    plotTree.yOff = plotTree.yOff + 1.0/plotTree.totalD


def createPlot(inTree):
    fig = plt.figure(1, facecolor='white')
    fig.clf()
    axprops = dict(xticks=[], yticks=[])              # 一个字典，存有x和y
  #  createPlot.ax1 = plt.subplot(111, frameon=False, **axprops)    # 没有间隔
    createPlot.ax1 = plt.subplot(111, frameon=False)  #有间隔
    plotTree.totalW = float(getNumLeafs(inTree))      # 获取叶的个数
    plotTree.totalD = float(getTreeDepth(inTree))     # 获取树的深度
    plotTree.xOff = -0.5/plotTree.totalW; plotTree.yOff = 1.0;
    plotTree(inTree, (0.5,1.0), '')
    plt.show()
    
 
def testCreatPlot():
    myTree = retrieveTree(1)
    createPlot(myTree)

#testGitTreeInf()
# createPlot_test()
#testCreatPlot()
