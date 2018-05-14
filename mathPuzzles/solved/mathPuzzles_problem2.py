
def findSumOfEvenFib(limit):
    currentNum = 1
    nextNum = 2
    sum = nextNum

    while nextNum < limit:
        tempNum = currentNum + nextNum
        currentNum = nextNum
        nextNum = tempNum
        if tempNum % 2 == 0:
            sum += tempNum

    print(str(sum));

findSumOfEvenFib(4000000)
