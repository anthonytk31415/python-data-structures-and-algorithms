
# https://leetcode.com/contest/biweekly-contest-136/problems/minimum-number-of-flips-to-make-binary-grid-palindromic-ii/submissions/


# When considering 2d-palindromes, 



def minFlips(grid):

    def isEven(num): 
        return num %2 == 0

    # return (oneChanges, sumOnes)
    def checkPair(pair):
        pSum = sum(pair)
        if pSum == 1: return [1,0]
        elif pSum == 0: return [0,0]
        else: return [0,2]

    # return (sumChanges, sumOnes, numPairs)
    def checkPairsInRow(row):
        midLeft, midRight = len(row) // 2 - 1, len(row) // 2 + 1
        if isEven(len(row)):
            midLeft, midRight = len(row) // 2 - 1, len(row) // 2
        res = [0, 0, 0]
        for i in range(0, len(row) // 2 ): 
            pair = [row[midLeft - i], row[midRight + i]]
            oneChange, sumOne = checkPair(pair)
            res[0] += oneChange
            res[1] += sumOne
            res[2] += 1
        return res

    # return (sumChanges, sumOnes, numPairs)
    def doMiddleCross(grid):
        res = [0]*3
        if not isEven(len(grid)): 
            row = len(grid) // 2
            middle = grid[row]
            middleRes = checkPairsInRow(middle)
            for i in range(len(res)):
                res[i] += middleRes[i]
        if not isEven(len(grid[0])):  
            middle = []
            col = len(grid[0]) // 2
            for i in range(len(grid)):
                middle.append(grid[i][col])
            middleRes = checkPairsInRow(middle)
            for i in range(len(res)):
                res[i] += middleRes[i]
        return res

    # return Bool, sumOne
    def doCenter(grid): 
        if not isEven(len(grid)) and not isEven(len(grid[0])):
            return [True, grid[len(grid)//2][len(grid[0])//2]]
        return [False, 0]

    # return min changes 
    def checkQuad(points):
        qSum = sum(points)
        if qSum == 1 or qSum == 3: return 1
        return qSum % 4


    #  return sumOnes
    def doQuads(grid): 
        m, n = len(grid), len(grid[0])
        sumOnes = 0
        for i in range(0, m//2):
            for j in range(0, n//2):
                points = [grid[i][j], grid[m - 1 - i][j], grid[m-1-i][n-1-j], grid[i][n-1-j]]
                sumOnes += checkQuad(points)
        return sumOnes

    sumChanges, sumOnes = 0, 0
    sumChanges += doQuads(grid)
    middleRes = doMiddleCross(grid)
    [middleChanges, middleOnes, _] = middleRes
    sumChanges += middleChanges
    sumOnes += middleOnes
    _, centerOne = doCenter(grid)
    sumOnes += centerOne

    if sumOnes % 4 == 0: return sumChanges
    elif sumOnes % 4 == 2: 
        if middleChanges >= 1: return sumChanges
        else: return sumChanges + 2
    elif sumOnes % 4 == 3: 
        if middleChanges >= 1: return sumChanges + 1
        else: return sumChanges + 3
    elif sumOnes % 4 == 1: return sumChanges + 1









# grid = [[0,0,1], [1,0,1], [0,1,1], [1,0,0]] # [0, 1, 0], 0 # 4x3
# grid = [[1, 0, 1, 0], [0, 0, 1, 1], [1, 0, 0, 0]] # [0, 2, 0] 0 # 3x4
# grid = [[1, 0, 0, 0, 0], [1, 0, 1, 0, 0], [1, 1, 0, 0, 0], [1, 0, 0, 1, 1]] # 4x5
# print(doMiddleCross(grid))

# grid = [[0,1],[0,1],[0,0]] # [0, 2, 0], 0

# grid = [[1,0,0],[0,1,0],[0,0,1]]

grid = [[1],[1],[1],[0]]


# grid = [[1,0,0],[0,0,0],[0,0,1]] # [0, 0, 1] 0

# grid = [[1, 0, 1, 0], [0, 0, 1, 1], [1, 0, 0, 0]] # [0, 3, 1] 0
# grid = [[1, 0, 0, 0, 0], [1, 0, 1, 0, 0], [1, 1, 0, 0, 0], [1, 0, 0, 1, 1]] # 4x5
# grid = [[1],[0]]
# grid = [[1],[1]]

print("grid: ", grid)
print("answer: ", minFlips(grid))


# print("quads: ", doQuads(grid))

# print(minFlips(grid))