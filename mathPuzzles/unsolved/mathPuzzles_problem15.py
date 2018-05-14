import time
startTime = time.time()

def squareGridBuilder(gridsize):
    # Make the grid by using nested lists as x,y coordinates
    coords = []
    for x in range(0, gridsize):
        coords.append([])
        for y in range(0, gridsize):
            coords[x].append('.')
    return coords

def gridPrinter(grid):
    endPoint = len(grid)
    for y in range(0, endPoint):
        for x in range(0, endPoint):
            prntStr = str(grid[x][y])
            if(x != endPoint-1):
                print(prntStr, end='  ')
            else:
                print(prntStr);

# def findRoutesInGrid(grid):


grid = squareGridBuilder(3)
gridPrinter(grid)
# print(findRoutesInGrid(grid))

endTime = time.time()
print('script ran in ' + '{:.5f}'.format(endTime - startTime) + ' seconds')
