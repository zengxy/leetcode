import math
import numpy as np

def calErrorRate(alpha, f_DecisionTree, features, featureSelected, Y_label):
    instanceNum = Y_label.__len__()
    caculatedLabels = []
    ErrorNum = 0
    for i in range(instanceNum):
        if Y_label[i] == caculateLabel(alpha, f_DecisionTree, features[:][i]):
            caculatedLabels.append(-1)
            ErrorNum = ErrorNum + 1
        else:
            caculatedLabels.append(1)

    return ErrorNum/instanceNum, caculatedLabels

def caculateLabel(alpha,f_DecisionTree,features,featureChooesd):
    f = 0
    for i in range(alpha.__len__()):
        f = f + alpha[i] * f_DecisionTree[i][features[featureChooesd]]
    if f > 0:
        return 1
    else:
        return -1



def calWeight():
    pass


def chooseBestTree(features, Y_label, D_weight):
    featureNum = features.__len__()
    Loss = Y_label.__len__()
    featureChoosed = None
    G_decisionTree = None

    for i in range(featureNum):
        candidateLoss,candidateDecisionTree = decisionTreeBy(features[i],Y_label)
        if candidateLoss < Loss:
            Loss=candidateLoss
            featureChoosed=i
            G_decisionTree = candidateDecisionTree

    return featureChoosed, G_decisionTree

def decisionTreeBy(feature,D_weight,groundtruth):
    featureSet = set(feature)
    labelCountDic = {}
    for i in feature.__len__():
        pass



    return 1,1



def train(features, Y_label):
    instanceNum = Y_label.__len__()
    D_weight =  np.array([0.1]).repeat(instanceNum)

    alpha = []
    f_DecisionTree = []
    featureChoosed = []

    ErrorRate = 1.0

    while(ErrorRate > 0):
        ft, G = chooseBestTree(features, Y_label, D_weight)
        featureChoosed.append(ft)
        f_DecisionTree.append(G)



    print(D_weight)


if __name__ == '__main__':
    #train([11, 1, 1, ], [1, 2, 3, 4, 5])
    a = np.array([0.1]).repeat(10)
    a = np.hstack([a, np.array([0.2]).repeat(2)])
    print(a)