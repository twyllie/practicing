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
    for n in range(3, math.ceil(math.sqrt(number))):
        if n % 2 != 0 and number % n == 0:
            return False
    return True;

def findTheNthPrime(primeLimit):
    primeList = []
    primesFound = 0
    numberToCheck = 1
    currentPrime = 2
    while primesFound < primeLimit:
        isPrime = primalityOfNumber(numberToCheck)
        stringEnding = 'No'
        if isPrime:
            primeList.append(numberToCheck)
            primesFound += 1
            currentPrime = numberToCheck
            stringEnding = 'Yes! \n        found ' + str(primesFound) + ' primes so far...'
        print('\n is ' + str(numberToCheck) + ' prime? ' + stringEnding)
        numberToCheck += 1

findTheNthPrime(10001)
