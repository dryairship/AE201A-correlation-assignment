from math import sqrt
from csv import reader

dataFileName = 'data.csv'
noOfRows = 34
noOfColumns = 18
restrictedColumns = [0, 1, 2, 8]

csvHeaders = []
allData = [[0 for i in range(noOfRows-1)] for j in range (noOfColumns)]

def calculateCorrelation(X, Y):
    n = len(X)
    sumX = 0
    sumY = 0
    sumXY = 0
    sumXX = 0
    sumYY = 0
    for i in range(n):
        sumX += X[i]
        sumY += Y[i]
        sumXY += X[i]*Y[i]
        sumXX += X[i]*X[i]
        sumYY += Y[i]*Y[i]
    numerator = n*sumXY - sumX*sumY
    denominatorSquare = (n*sumXX - sumX*sumX) * (n*sumYY - sumY*sumY)
    denominator = sqrt(denominatorSquare)
    return (numerator/denominator)

def readFile():
    global csvHeaders
    with open(dataFileName) as dataFile:
        allRows = reader(dataFile, delimiter=',')
        lineNumber = 1
        for row in allRows:
            if lineNumber == 1:
                csvHeaders = row
            else:
                for i in range(len(row)):
                    allData[i][lineNumber-2] = row[i]
            lineNumber += 1

def getArrayPairForColumns(x, y):
    X = []
    Y = []
    for i in range(noOfRows-1):
        if allData[x][i] and allData[y][i]:
            X.append(float(allData[x][i]))
            Y.append(float(allData[y][i]))
    return X, Y


if __name__ == '__main__':
    readFile()
    for i in range(noOfColumns):
        if i in restrictedColumns:
            continue
        for j in range(i+1, noOfColumns):
            if j in restrictedColumns:
                continue
            X, Y = getArrayPairForColumns(i,j)
            correlation = calculateCorrelation(X, Y)
            print(f'Correlation between "{csvHeaders[i]}" ({i}) and "{csvHeaders[j]}" ({j}) = {correlation}')
