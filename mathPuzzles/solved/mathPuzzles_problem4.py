def reverseString(string):
    newString = ''
    for i in range(len(string)-1, -1, -1):
        newString += string[i]
    return newString;

def isPalindrome(thing):
    reverseThing = reverseString(str(thing))
    if str(thing) == reverseThing:
        return True
    else:
        return False;

def doTheThing():
    answer = 0
    for x in range(100, 1000):
        for y in range(100, 1000):
            if isPalindrome(x * y):
                if (x*y) > answer:
                    answer = (x * y)
                    print(answer)
    return answer;

doTheThing()
