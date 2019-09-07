from math import sqrt
from csv import reader

noOfRows = 34
noOfColumns = 18


def calculateCorrelation(x, y):
    n = len(x)
    sumX = 0
    sumY = 0
    sumXY = 0
    sumXX = 0
    sumYY = 0
    for i in range(n):
        sumX += x[i]
        sumY += y[i]
        sumXY += x[i]*y[i]
        sumXX += x[i]*x[i]
        sumYY += y[i]*y[i]
    numerator = n*sumXY - sumX*sumY
    denominatorSquare = (n*sumXX - sumX*sumX) * (n*sumYY - sumY*sumY)
    denominator = sqrt(denominatorSquare)
    return (numerator/denominator)

csvHeaders = []
allData = [[0 for i in range(noOfRows-1)] for j in range (noOfColumns)]

def readFile():
    with open('data.csv') as dataFile:
        allRows = reader(dataFile, delimiter=',')
        lineNumber = 1
        for row in allRows:
            if lineNumber == 1:
                csvHeaders = row
            else:
                for i in range(len(row)):
                    allData[i][lineNumber-2] = row[i]
            lineNumber += 1
    print allData

