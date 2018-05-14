import time
startTime = time.time()

data = '75 95 64 17 47 82 18 35 87 10 20 4 82 47 65 19 1 23 75 3 34 88 2 77 73 7 63 67 99 65 4 28 6 16 70 92 41 41 26 56 83 40 80 70 33 41 48 72 33 47 32 37 16 94 29 53 71 44 65 25 43 91 52 97 51 14 70 11 33 28 77 73 17 78 39 68 17 57 91 71 52 38 17 14 91 43 58 50 27 29 48 63 66 4 68 89 53 67 30 73 16 69 87 40 31 4 62 98 27 23 9 70 98 73 93 38 53 60 4 23'

def gridPrinter(grid):
    endPoint = len(grid)
    for y in range(0, endPoint):
        for x in range(0, endPoint):
            prntStr = grid[x][y]
            if(prntStr.isalnum()):
                if(int(grid[x][y]) < 10):
                    prntStr = '0' + grid[x][y]
            if(x != endPoint-1):
                print(prntStr, end=' ')
            else:
                print(prntStr)

def dataTriangleBuider(data, gridsize):
    dataIndex = 0
    data = data.split()
    dataTriangle = []
    dataIndex = 0
    for num in range(0, gridsize):
        dataTriangle.append([])
        for otherNum in range(0, gridsize):
            dataTriangle[num].append('*')
    for y in range(0, gridsize):
        for x in range(0, gridsize):
            offset = y+2
            if(x > gridsize-offset):
                dataTriangle[x][y] = data[dataIndex]
                dataIndex += 1
    return dataTriangle

# def findGreatestAdjacent()

# def findGreatestPochinki(pochinkiBoard):
#     greatestPochinki = 0

dataTriangle = dataTriangleBuider(data, 15)
gridPrinter(dataTriangle)

endTime = time.time()
print('script ran in ' + '{:.5f}'.format(endTime - startTime) + ' seconds')
