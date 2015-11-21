import math
import numpy as np


class decisionTree:
    def __init__(self, features, weight, labels):
        '''
        @:param features: feature vector, numpy array
        @:param weight: weight of instances
        @:param labels: groundtruth
        '''
        self.features = features
        self.labels = labels
        self.weight = weight
        self.featureChoosed = -1
        self.decisionTreeDict = {}
        self.loss = 0
        self.labelCaculated = None

    def train(self):
        self.chooseBestSplitAttribute()
        return self.loss, self.labelCaculated

    def chooseBestSplitAttribute(self):
        m, n = self.features.shape
        self.loss = n
        for i in range(m):
            lossTemp, decisionDictTemp = self.caculateleastLossBy(self.features[i])
            print(lossTemp)
            if lossTemp < self.loss:
                self.loss = lossTemp
                self.decisionTreeDict = decisionDictTemp
                self.featureChoosed = i
        self.labelCaculated = self.caculateLabel()

    def caculateleastLossBy(self, feature):
        featureValueSet = set(feature)
        weightDic= {}
        for featureValue in featureValueSet:
            weightDic[featureValue]={-1:0,1:0}

        for i in range(feature.size):
            weightDic[feature[i]][self.labels[i]] = weightDic[feature[i]][self.labels[i]]+self.weight[i]

        totalLoss = 0
        decisionDic = {}
        for featureValue in featureValueSet:
            if weightDic[featureValue][-1] > weightDic[featureValue][1]:
                decisionDic[featureValue] = -1
                totalLoss += weightDic[featureValue][1]
            else:
                decisionDic[featureValue] = 1
                totalLoss += weightDic[featureValue][-1]
        return totalLoss,decisionDic



    def caculateLabel(self):
        labelCaculated=[]
        feature = self.features[self.featureChoosed]
        for i in range(self.labels.size):
            labelCaculated.append(self.decisionTreeDict[feature[i]])

        return np.array(labelCaculated)

    def caculateErrorRate(self):
        pass


class adaBoost:
    MIN_ERROR_RATE = 0.01
    def __init__(self):
        self.features = np.array([[0, 0, 1, 1, 1, 0, 1, 1, 1, 0],
                                  [1, 3, 2, 1, 2, 1, 1, 1, 3, 2],
                                  [3, 1, 2, 3, 3, 2, 2, 1, 1, 1]])
        self.labels = np.array([-1, -1, -1, -1, -1, -1, 1, 1, -1, -1])
        m, n = self.features.shape
        self.weight = np.array([0.1]).repeat(n)
        self.alphas = []
        self.weakClassifier = []
        self.overallErrorRate = 1

    def train(self):
        while True:
            newWeakClassifier =  decisionTree(self.features,self.weight,self.labels)
            loss, labelCaculated = newWeakClassifier.train()
            alpha = math.log((1-loss)/loss,math.e)/2

            self.weakClassifier.append(newWeakClassifier)
            self.alphas.append(alpha)

            self.overallErrorRate = self.calculateOverallErrorRate()
            print("alpha:",alpha,
                  "featureChoosed:",newWeakClassifier.featureChoosed,
                  "DecisionTree",newWeakClassifier.decisionTreeDict,
                  "Loss",newWeakClassifier.loss,
                  "ErrorRate:",self.overallErrorRate)
            if self.overallErrorRate < self.MIN_ERROR_RATE:
                return

            self.updateWeight(alpha,labelCaculated)


    def updateWeight(self,alpha,labelCaculated):
        Z = self.weight*np.exp(-alpha*self.labels*labelCaculated)
        self.weight = Z/Z.sum()



    def calculateOverallErrorRate(self):
        n = self.labels.size
        calWeiht=np.array([0])*n
        for i in range(self.alphas.__len__()):
            calWeiht = calWeiht + self.alphas[i]*self.weakClassifier[i].labelCaculated
        overAllLabel = np.sign(calWeiht)
        return(n - (overAllLabel*self.labels).sum()) / (2*n)



if __name__ == '__main__':
    a = adaBoost()
    a.train()