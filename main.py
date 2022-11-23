import json
from regression import *
from utilityFunctions import *
import multiprocessing

if __name__ == '__main__':
    dataPath = "datasets/" + input("Enter the name of the dataset(json only): ")

    file = open(dataPath)
    data = json.load(file)

    xDim = input("Enter the X dimension from the dataset: ")
    yDim = input("Enter the Y dimension from the dataset: ")

    regressionAlgorithms = [LinearRegression(data,xDim,yDim),ExponentialRegression(data,xDim,yDim),
                            ReciprocalRegression(data,xDim,yDim),PolynomialRegression(data,xDim,yDim),
                            LogarithmicRegression(data,xDim,yDim)]

    processes = [multiprocessing.Process(target=processFitting(x)) for x in regressionAlgorithms]

    for process in processes:
        process.start()

    for process in processes:
        process.join()

    leastCostingProcess = getLeastErrorAlgorithm(regressionAlgorithms)

    leastCostingProcess.visualize("Function with best fitting: "+leastCostingProcess.functionString()
                                  +"\nMean squared error: "+str(round(leastCostingProcess.error,4)))