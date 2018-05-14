import time
startTime = time.time()

def parseNumberIntoNaturalLanguage(number):
    

def stringCountBuilder(limit):
    bigNumberString = ''
    for number in range(1, limit+1):
        littleNumberString = parseNumberIntoNaturalLanguage(number)
        bigNumberString += littleNumberString
    return bigNumberString;

def alphaCharacterCounter(s):
    counter = 0
    for c in s:
        if c.isAlpha():
            counter += 1
    return counter;

def doTheThing(limit):
    stringToCount = stringCountBuilder(limit)
    return alphaCharacterCounter(stringToCount);

limit = 1000
print(doTheThing(limit))

endTime = time.time()
print('script ran in ' + '{:.5f}'.format(endTime - startTime) + ' seconds')
