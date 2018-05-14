import math

# A function to check the primality of a given number
# return True if prime, False if
def primalityOfNumber(number):
    if number < 2 or type(number) != int: # Fast fail if the first number is a problem number
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    for n in range(3, int(math.sqrt(number))+1): # Needs the +1 or else, 9 short circuits it and returns true
        if n % 2 != 0 and number % n == 0:
            return False
    return True;

# A function to check if a number is prime and a multiple of another number
def isPrimeFactorOf(number, anotherNumber):
    return anotherNumber % number == 0 and primalityOfNumber(number);

# Keeps going until it finds a prime factor
def findLowestPrimeFactor(number):
    counter = 1
    notFound = True
    while notFound:
        if isPrimeFactorOf(counter, number) or counter == number:
            notFound = False
        else:
            counter += 1
    return counter;

# A function that returns a list of all of the prime factors of a number
def primeFactorization(number):
    primeFactors = []
    if number < 2 or type(number) != int: # Fast return if the first number is a problem number
        return primeFactors
    if primalityOfNumber(number): # Fast return if the number passed is prime.
        primeFactors.append(number)
        return primeFactors
    remainder = number
    notDone = True
    while notDone:
        factor = findLowestPrimeFactor(remainder)
        remainder = remainder // factor
        primeFactors.append(factor)
        if primalityOfNumber(remainder):
            primeFactors.append(remainder)
            notDone = False
    primeFactors.sort()
    return primeFactors;

def listMerger(fromList, toList):
    print(fromList, toList)
    for factor in fromList:
        if fromList.count(factor) > toList.count(factor):
            while fromList.count(factor) > toList.count(factor):
                toList.append(factor)
    toList.sort()
    print(fromList, toList);

def divisionChecker(number, limit):
    for n in range(1, limit):
        if number % n != 0:
            return False
    return True

def doTheThing1(limit):
    listOfPrimeFactors = []
    for n in range(1, limit):
        newFactors = primeFactorization(n)
        listMerger(newFactors, listOfPrimeFactors)
    product = 1
    for factor in listOfPrimeFactors:
        product = product * factor
    return product

limit = 20
returnVal = doTheThing1(limit)
print(returnVal)
print(divisionChecker(returnVal, limit))
