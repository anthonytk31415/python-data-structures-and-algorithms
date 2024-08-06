# https://leetcode.com/problems/unique-paths-ii/description/?envType=study-plan-v2&envId=top-interview-150
# 63. Unique Paths II

def uniquePathsWithObstacles(obstacleGrid):
    dp = obstacleGrid
    if dp[-1][-1] == 1: return 0
    for i in range(len(obstacleGrid) - 1, -1, -1):
        for j in range(len(obstacleGrid[0]) -1, -1, -1):
            if i == len(obstacleGrid) - 1 and j == len(obstacleGrid[0]) - 1: dp[i][j] =  1 
            elif dp[i][j] == 1: dp[i][j] = 0
            else: 
                numPaths = 0
                if i+1 < len(obstacleGrid): numPaths += dp[i+1][j]
                if j+1 < len(obstacleGrid[0]): numPaths += dp[i][j+1]
                dp[i][j] = numPaths         
    return dp[0][0]

obstacleGrid = [[0,1],[0,0]]
obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
print(uniquePathsWithObstacles(obstacleGrid))