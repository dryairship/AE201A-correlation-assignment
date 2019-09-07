from math import sqrt

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
