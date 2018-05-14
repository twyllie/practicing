import time
startTime = time.time()

def sumTheDigits(number):
    rollingSum = 0
    for digit in str(number):
        rollingSum += int(digit)
    return rollingSum;

print(sumTheDigits(2**1000))

endTime = time.time()
print('script ran in ' + '{:.5f}'.format(endTime - startTime) + ' seconds')
