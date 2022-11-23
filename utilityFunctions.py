import math
import sys

class AverageCalculator:
    def __init__(self,data,dimension,operation):
        self.data = data
        self.dimension = dimension
        self.operation = operation
        self.result = self.getResult()

    def getResult(self):
        result = 0

        for i in self.data:
            result+=self.operation(i[self.dimension])

        return result/len(self.data)

def printAll(regressionAlgorithms):
    for alg in regressionAlgorithms:
        alg.visualize("Function with best fitting: "+alg.functionString()+"\nMean squared error: "+str(round(alg.error,4)))

def getLeastErrorAlgorithm(algorithms):
    leastCostingProcess = algorithms[0]

    for alg in algorithms:
        print(alg.__class__.__name__,alg.error)
        if alg.error < leastCostingProcess.error:
            leastCostingProcess = alg

    return leastCostingProcess

def processFitting(regression):
    regression.fitCurve()

def linear(x):
    return x

def logarithmic(x):
    if x>0:
        return math.log(x)
    return -sys.maxsize

def reciprocal(x):
    if x!=0:
        return 1/x
    return 0
