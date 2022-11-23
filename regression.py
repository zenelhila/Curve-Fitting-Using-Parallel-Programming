import matplotlib.pyplot as plt
import numpy as np
from utilityFunctions import *
import sys

class Regression:
    def __init__(self,data,xDim,yDim):
        self.data = data
        self.xDim = xDim
        self.yDim = yDim

        self.m = 0
        self.b = 0
        self.error = 0

    def fitCurve(self):
        self.findMAndB()
        self.calculateError()

    def maxDimension(self,dimension,asc):
        currentVal = self.data[0][dimension]

        for i in self.data:
            if not (asc ^ (currentVal<i[dimension])):
                currentVal = i[dimension]
        return currentVal

    def calculateError(self):
        self.error = 0

        for i in self.data:
            try:
                self.error += (self.function(i[self.xDim]) - i[self.yDim]) ** 2
            except Exception as e:
                self.error = sys.maxsize
                break


    def visualize(self,title):
        plt.scatter([i[self.xDim] for i in self.data],[i[self.yDim] for i in self.data],s=5,c='b',zorder=1)

        minX = self.maxDimension(self.xDim,False)-10
        minY =self.maxDimension(self.yDim,False)-10
        maxX = self.maxDimension(self.xDim,True)+10
        maxY = self.maxDimension(self.yDim,True)+10

        yFunc = np.vectorize(self.function)
        x = np.linspace(minX,maxX,1000)
        y = yFunc(x)

        plt.plot(x,y,c='g',zorder=0)

        plt.xlabel(self.xDim)
        plt.ylabel(self.yDim)

        # plt.xlim(minX,maxX)
        #
        # plt.ylim(minY,maxY)

        plt.title(title)

        plt.show()

    def function(self, x):
        return 0

    def findMAndB(self):
        pass


class LinearRegression(Regression):
    def functionString(self):
        return str(round(self.m,3))+"x + "+str(round(self.b,3))

    def findMAndB(self):
        acX = AverageCalculator(self.data,self.xDim,linear)
        acY = AverageCalculator(self.data,self.yDim,linear)

        diffDom = 0
        diffXSq = 0

        for i in self.data:
            diffDom += (i[self.xDim] - acX.result)*(i[self.yDim] - acY.result)
            diffXSq += (i[self.xDim] - acX.result)**2

        self.m = diffDom/diffXSq
        self.b = acY.result - self.m*acX.result

    def function(self,x):
        return x*self.m + self.b

class PolynomialRegression(Regression):
    def functionString(self):
        return str(round(self.b,3))+"X^"+str(round(self.m, 3))

    def findMAndB(self):
        acX = AverageCalculator(self.data, self.xDim, logarithmic)
        acY = AverageCalculator(self.data, self.yDim, logarithmic)

        diffDom = 0
        diffXSq = 0

        for i in self.data:
            diffDom += (logarithmic(i[self.xDim]) - acX.result) * (logarithmic(i[self.yDim]) - acY.result)
            diffXSq += (logarithmic(i[self.xDim]) - acX.result) ** 2

        self.m = diffDom / diffXSq

        self.b = acY.result - self.m * acX.result
        self.b = math.e ** self.b

    def function(self,x):
        try:
            return self.b * (math.pow(x,self.m))
        except Exception:
            return sys.maxsize

class ExponentialRegression(Regression):
    def functionString(self):
        return str(round(self.b,3))+"e^"+str(round(self.b,3))

    def findMAndB(self):
        acX = AverageCalculator(self.data, self.xDim, linear)
        acY = AverageCalculator(self.data, self.yDim, logarithmic)

        diffDom = 0
        diffXSq = 0

        for i in self.data:
            diffDom += (i[self.xDim] - acX.result) * (logarithmic(i[self.yDim]) - acY.result)
            diffXSq += (i[self.xDim] - acX.result) ** 2

        self.m = diffDom / diffXSq

        self.b = acY.result - self.m * acX.result
        self.b = math.e ** self.b

    def function(self,x):
        try:
            return self.b * (math.e ** x)
        except Exception:
            return sys.maxsize

class ReciprocalRegression(Regression):
    def functionString(self):
        return "1/("+str(round(self.m,3))+"x + "+str(round(self.b,3))+")"

    def findMAndB(self):
        acX = AverageCalculator(self.data, self.xDim, linear)
        acY = AverageCalculator(self.data, self.yDim, reciprocal)

        diffDom = 0
        diffXSq = 0

        for i in self.data:
            diffDom += (i[self.xDim] - acX.result) * (reciprocal(i[self.yDim]) - acY.result)
            diffXSq += (i[self.xDim] - acX.result) ** 2

        self.m = diffDom / diffXSq
        self.b = acY.result - self.m * acX.result

    def function(self,x):
        return 1/(self.b + x*self.m)

class LogarithmicRegression(Regression):
    def functionString(self):
        return str(round(self.m,3))+"ln(x) + "+str(round(self.b,3))

    def findMAndB(self):
        acX = AverageCalculator(self.data, self.xDim, logarithmic)
        acY = AverageCalculator(self.data, self.yDim, linear)

        diffDom = 0
        diffXSq = 0

        for i in self.data:
            diffDom += (i[self.xDim] - acX.result) * (reciprocal(i[self.yDim]) - acY.result)
            diffXSq += (i[self.xDim] - acX.result) ** 2

        self.m = diffDom / diffXSq
        self.b = acY.result - self.m * acX.result

    def function(self,x):
        return self.m * math.log(x) + self.b