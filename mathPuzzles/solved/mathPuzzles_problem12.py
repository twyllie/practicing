import math
import time
startTime = time.time()

def factorNumber(numberToFactor):
    factorList = []
    counter = 1
    while counter <= int(math.sqrt(numberToFactor))+1:
        if numberToFactor % counter == 0:
            factorList.append(counter)
            factorList.append(numberToFactor//counter)
        counter += 1
    factorList.sort()
    return factorList;

def calculateTriangular(num):
    return (num * (num + 1)) // 2;

def findFirstTriangularWithNFactors(soughtNumOfFactors):
    nthTriNum = 1
    triangularNumberValue = 0
    greatestLengthSoFar = 0
    notFound = True
    while notFound:
        triangularNumberValue = calculateTriangular(nthTriNum)
        listOfFactors = factorNumber(triangularNumberValue)
        numOfFactors = len(listOfFactors)
        if numOfFactors > greatestLengthSoFar:
            greatestLengthSoFar = numOfFactors
            print('Triangular # ' + str(nthTriNum) + ', with value: ' + str(triangularNumberValue) + ' has ' + str(numOfFactors) + ' factors')
        nthTriNum += 1
        if numOfFactors  > soughtNumOfFactors:
            notFound = False
    return triangularNumberValue;

print(findFirstTriangularWithNFactors(500))
endTime = time.time()
print('script ran in ' + '{:.5f}'.format(endTime - startTime) + ' seconds')
