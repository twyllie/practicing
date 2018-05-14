def sumOfSquares(arrayOfNumbers):
    sum = arrayOfNumbers[0]
    for i in range(1, len(arrayOfNumbers)):
        sum += arrayOfNumbers[i]**2
    return sum;

def squareOfSums(arrayOfNumbers):
    sum = arrayOfNumbers[0]
    for i in range(1, len(arrayOfNumbers)):
        sum += arrayOfNumbers[i]
    return sum**2;

def doTheThing():
    numbersToTest = range(1, 101)
    answer = squareOfSums(numbersToTest) - sumOfSquares(numbersToTest)
    return answer;

print (doTheThing())
