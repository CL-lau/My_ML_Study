# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 08:32:35 2017

@author: hh
"""
from numpy import *

"""创建一个数据集"""
def loadDataSet():
    postingList=[['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
                 ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
                 ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
                 ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                 ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
                 ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    classVec = [0,1,0,1,0,1]                    #1 表示侮辱类词汇, 0 表示正常词汇
    return postingList,classVec

"""获得词汇表"""
def createVocabList(dataSet):
    vocabSet = set([])              #创建一个空的set集合
    for document in dataSet:
        vocabSet = vocabSet | set(document)   #合并两个Set集合（求并集）
    return list(vocabSet)

"""获取文档向量"""
def setOfWords2Vec(vocabList, inputSet):
    returnVec = [0]*len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] = 1
        else: print ("the word: %s is not in my Vocabulary!" % word)
    return returnVec


"""从词向量计算概率"""
def trainNB0(trainMatrix,trainCategory):
    numTrainDocs = len(trainMatrix)    # 文本个数
    numWords = len(trainMatrix[0])     # 词表长度
    pAbusive = sum(trainCategory)/float(numTrainDocs)   # 所有训练文本中，是侮辱性质的所占比例。
    p0Num = ones(numWords); p1Num = ones(numWords)      #生成与词表长度一致的单位向量 （防止出现0）
    p0Denom = 2.0; p1Denom = 2.0                        
    for i in range(numTrainDocs):
        if trainCategory[i] == 1:
            p1Num += trainMatrix[i]
            p1Denom += sum(trainMatrix[i])
        else:
            p0Num += trainMatrix[i]
            p0Denom += sum(trainMatrix[i])
    p1Vect = log(p1Num/p1Denom)         # 防止最后的乘积过小，溢出
    p0Vect = log(p0Num/p0Denom)         
    return p0Vect,p1Vect,pAbusive

"""朴素贝叶斯分类函数"""
def classifyNB(vec2Classify, p0Vec, p1Vec, pClass1):
    p1 = sum(vec2Classify * p1Vec) + log(pClass1)    #element-wise mult
    p0 = sum(vec2Classify * p0Vec) + log(1.0 - pClass1)
    if p1 > p0:
        return 1
    else: 
        return 0
    

""" 词袋模型"""
def bagOfWords2VecMN(vocabList, inputSet):
    returnVec = [0]*len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] += 1
    return returnVec
  
""" 切分文本"""
def textParse(bigString):    
    import re
    listOfTokens = re.split(r'\W*', bigString)
    return [tok.lower() for tok in listOfTokens if len(tok) > 2]    


"""垃圾邮件处理"""
def spamTest():
    docList=[]; classList = []; fullText =[]
    for i in range(1,26):
        wordList = textParse(open('email/spam/%d.txt' % i).read())
        docList.append(wordList)
        fullText.extend(wordList)
        classList.append(1)
        wordList = textParse(open('email/ham/%d.txt' % i).read())
        docList.append(wordList)
        fullText.extend(wordList)
        classList.append(0)
    vocabList = createVocabList(docList)                # 获得一个词表
    trainingSet = list(range(50)); testSet=[]           
    for i in range(10):            # 随机划分训练集和测试集合 (40/10)
        randIndex = int(random.uniform(0,len(trainingSet))) # 随机生成0到50的一个整数
        testSet.append(trainingSet[randIndex])
        del(trainingSet[randIndex])  
    trainMat=[]; trainClasses = []
    for docIndex in trainingSet:        # 获得训练数据集合（通过词表转换为向量） 以及对应的分类标签
        trainMat.append(bagOfWords2VecMN(vocabList, docList[docIndex]))
        trainClasses.append(classList[docIndex])
    p0V,p1V,pSpam = trainNB0(array(trainMat),array(trainClasses))
    errorCount = 0
    for docIndex in testSet:        
        wordVector = bagOfWords2VecMN(vocabList, docList[docIndex])
        if classifyNB(array(wordVector),p0V,p1V,pSpam) != classList[docIndex]:
            errorCount += 1
            print ("classification error",docList[docIndex])
    print ('the error rate is: ',float(errorCount)/len(testSet))
    #return vocabList,fullText
    
spamTest()