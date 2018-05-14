def produceChainFromNumber(number):
    chain = []
    while number > 1:
        chain.append(number)
        if number % 2 == 0:
            number = number // 2
        else:
            number = (3*number)+1
    return chain;

def findLongestChainUnder(limit):
    currentNumber = limit
    longestChain = 0
    longestChainNumber = 0
    while currentNumber > 0:
        currentChain = produceChainFromNumber(currentNumber)
        print(len(currentChain))
        if len(currentChain) > longestChain:
            longestChain = len(currentChain)
            longestChainNumber = currentNumber
        currentNumber -= 1
    return (longestChain, longestChainNumber)

limit = 1000000
answer = findLongestChainUnder(limit)
print('Length: ' + str(answer[0]) + ', value: ' + str(answer[1]))
