# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 08:54:06 2017

@author: hh
"""

import bayes
from numpy import *

"""测试获取词汇表"""
def testCreateVocabList():
    listOposts,listClass = bayes.loadDataSet()
    myVocabList = bayes.createVocabList(listOposts)
    print(myVocabList)

"""测试获取文档向量""" 
def testSetOfWords2Vec():
    listOposts,listClass = bayes.loadDataSet()
    myVocabList = bayes.createVocabList(listOposts)
    myVec = bayes.setOfWords2Vec(myVocabList,listOposts[0])
    print(myVec)
    
""" 测试训练函数"""
def testTrainNB0():
    listOposts,listClass = bayes.loadDataSet()
    myVocabList = bayes.createVocabList(listOposts)
    trainMat = []
    for postinDoc in listOposts:
        trainMat.append(bayes.setOfWords2Vec(myVocabList,postinDoc))
    p0V,p1V,pAb = bayes.trainNB0(trainMat,listClass)
    print(p0V)
    print("--------------------------------------------------")
    print(p1V)
    print("--------------------------------------------------")
    print(pAb)
    
""" 测试分类函数 """
def testingNB():
    listOposts,listClass = bayes.loadDataSet()
    myVocabList = bayes.createVocabList(listOposts)
    trainMat = []
    for postinDoc in listOposts:
        trainMat.append(bayes.setOfWords2Vec(myVocabList,postinDoc))
    p0V,p1V,pAb = bayes.trainNB0(trainMat,listClass)
    testEntry = ['love', 'my', 'dalmation']
    thisDoc = array(bayes.setOfWords2Vec(myVocabList, testEntry))
    print (testEntry,'classified as: ',bayes.classifyNB(thisDoc,p0V,p1V,pAb))
    testEntry = ['stupid', 'garbage']
    thisDoc = array(bayes.setOfWords2Vec(myVocabList, testEntry))
    print (testEntry,'classified as: ',bayes.classifyNB(thisDoc,p0V,p1V,pAb))   
    
    

    
    
    
    
    
    
    
    
"""-------------------------------------------"""
# testCreateVocabList()
# testSetOfWords2Vec()
testingNB()
# testTrainNB0()