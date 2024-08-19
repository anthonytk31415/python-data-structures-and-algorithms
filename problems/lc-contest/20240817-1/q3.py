
# return matrix where i, j is the max from i j to up and left
def maxUpperLeft(grid): 
    dp = [[x for x in row] for row in grid]
    for i in range(len(grid)):
        for j in range(len(grid[0])):            
            if i == 0: 
                if j == 0: continue
                else: dp[i][j] = max(dp[i][j], dp[i][j-1])
            else: 
                if j == 0: 
                    dp[i][j] = max(dp[i][j], dp[i-1][j])
                else: 
                    dp[i][j] = max(dp[i][j], dp[i-1][j], dp[i][j-1])
    return dp

def maxUpperRight(grid): 
    dp = [[x for x in row] for row in grid]
    for i in range(len(grid)):
        for j in range(len(grid[0])-1, -1, -1):            
            if i == 0: 
                if j == len(grid[0])-1: continue
                else: dp[i][j] = max(dp[i][j], dp[i][j+1])
            else: 
                if j == len(grid[0])-1: 
                    dp[i][j] = max(dp[i][j], dp[i-1][j])
                else: 
                    dp[i][j] = max(dp[i][j], dp[i-1][j], dp[i][j+1])
    return dp

def maxLowerRight(grid): 
    dp = [[x for x in row] for row in grid]
    for i in range(len(grid)-1, -1, -1):
        for j in range(len(grid[0])-1, -1, -1):            
            if i == len(grid)-1: 
                if j == len(grid[0])-1: continue
                else: dp[i][j] = max(dp[i][j], dp[i][j+1])
            else: 
                if j == len(grid[0])-1: 
                    dp[i][j] = max(dp[i][j], dp[i+1][j])
                else: 
                    dp[i][j] = max(dp[i][j], dp[i+1][j], dp[i][j+1])
    return dp

def maxLowerLeft(grid): 
    dp = [[x for x in row] for row in grid]
    for i in range(len(grid)-1, -1, -1):
        for j in range(len(grid[0])):            
            if i == len(grid)-1: 
                if j == 0: continue
                else: dp[i][j] = max(dp[i][j], dp[i][j-1])
            else: 
                if j == 0: 
                    dp[i][j] = max(dp[i][j], dp[i+1][j])
                else: 
                    dp[i][j] = max(dp[i][j], dp[i+1][j], dp[i][j-1])
    return dp



board = [[1,2,3],[4,5,6],[7,8,9]]
board = [[-3,1,1,1],[-3,1,-3,1],[-3,2,1,1]]
# print(maxUpperLeft(board))
# print(maxUpperRight(board))
print(maxLowerRight(board))
print(maxLowerLeft(board))

from math import inf 
def maximumValueSum(board):
    upperLeft = maxUpperLeft(board)
    upperRight = maxUpperRight(board)
    lowerRight = maxLowerRight(board)
    lowerLeft = maxLowerLeft(board)

    maxValue = -inf
    for i1 in range(len(board)):
        for i2 in range(i1+1, len(board)):
            for j1 in range(len(board[0])):
                for j2 in range(j1+1, len(board[0])): 
                    candidates = []
                    if i1 > 0: 
                        candidates.append()
