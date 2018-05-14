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
    for n in range(3, int(math.sqrt(number))+1, 2): # Needs the +1 or else, 9 short circuits it and returns true
        if n % 2 != 0 and number % n == 0:
            return False
    return True;

def findTheSumOfPrimesUpTo(endPoint):
    sum = 0
    for n in range(1, endPoint):
        if primalityOfNumber(n):
            print(str(n), end='')
            sum += n
    print(': sum='+str(sum))
    return sum;

limit = 2000000
print(findTheSumOfPrimesUpTo(limit))
