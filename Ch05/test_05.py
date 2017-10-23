# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 20:43:44 2017

@author: hh
"""
import logRegres
from numpy import *

"""测试梯度上升"""
def testGradAscent():
    dataArr,labelMat = logRegres.loadDataSet()
    weights=logRegres.gradAscent(dataArr,labelMat)
    print(weights)
    
"""测试绘制拟合的直线""" 
def testPlotBestFit():
    dataArr,labelMat = logRegres.loadDataSet()
    weights =logRegres.gradAscent(dataArr,labelMat)
    logRegres.plotBestFit(weights.getA())    # getA() : matrix --> array 

"""测试随机梯度上升0"""
def teststocGradAscent0():
    dataArr,labelMat = logRegres.loadDataSet()
    weights =logRegres.stocGradAscent0(array(dataArr),labelMat)
    logRegres.plotBestFit(weights) 
    
"""测试随机梯度上升1"""
def teststocGradAscent1():
    dataArr,labelMat = logRegres.loadDataSet()
    weights =logRegres.stocGradAscent1(array(dataArr),labelMat)
    logRegres.plotBestFit(weights)    
    
    
"""预测病马死亡率"""    
def multiTest():
    numTests = 10; errorSum=0.0
    for k in range(numTests):
        errorSum += logRegres.colicTest()
    print ("after %d iterations the average error rate is: %f" % (numTests, errorSum/float(numTests)))
"""--------------------------------"""
#testGradAscent()
#testPlotBestFit()
#teststocGradAscent0()
#teststocGradAscent1()
multiTest()
