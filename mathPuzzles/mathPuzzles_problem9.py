import math

# Function to the find the Pythogoreon Triplet
# whose a + b + c = givenSum
def findThePythagoreonTriplet(givenSum):
    for numA in range(1, givenSum):
        for numB in range (1, givenSum):
            numC = math.sqrt((numA**2) + (numB**2))
            if numC.is_integer():
                print(numA,numB,numC)
                if numA + numB + numC == givenSum:
                    return (numA, numB, numC);

def doTheThing():
    tup = findThePythagoreonTriplet(1000)
    print('The answer is: ' + str(tup[0] * tup[1] * tup[2]));

doTheThing()
