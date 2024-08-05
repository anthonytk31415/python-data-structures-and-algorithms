


def makeRowPalindromic(row):
    n = len(row)
    left = n//2 - 1
    right = n//2
    if n % 2 == 1: 
        left = n//2 - 1
        right = n//2 + 1

    res = 0
    for i in range(n//2):
        leftNum, rightNum = row[left - i], row[right + i]
        # print(i, leftNum, rightNum)
        if leftNum != rightNum: 
            res += 1
            # print("called", res)
    return res

# row = [1 , 0, 0]

row = [1, 1, 1, 1, 0, 1, 0, 0, 1]
row = [1, 1, 1, 1, 0, 1, 0, 0, 0, 1]

# print("ans: ", makeRowPalindromic(row))





def checkMinFlipsRows(grid):
    res = 0
    for row in grid: 
        res += makeRowPalindromic(row)
    return res

grid = [[1,0,0],[0,0,0],[0,0,1]]
# print(checkMinFlipsRows(grid) )

def checkMinFlipsCols(grid):
    res = 0
    for j in range(len(grid[0])):
        col = []
        for i in range(len(grid)):
            col.append(grid[i][j])
        res += makeRowPalindromic(col)
    return res

grid = [[1,0,0],[0,0,0],[0,0,1]]
# print(checkMinFlipsCols(grid))




def minFlips(grid):
    return min(checkMinFlipsCols(grid), checkMinFlipsRows(grid))


grid = [[0,1],[0,1],[0,0]]
grid = [[1,0,0],[0,0,0],[0,0,1]]
grid = [[1],[0]]


print(minFlips(grid))