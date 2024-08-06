# https://leetcode.com/problems/minimum-path-sum/
# 64. Minimum Path Sum

# Time: O(mn)
# Space: O(1) - we mutate the grid
def minPathSum(grid):
    for i in range(len(grid)-1, -1, -1):
        for j in range(len(grid[0])-1, -1, -1):
            if i == len(grid)-1 and j == len(grid[0])-1: continue
            candidates = []
            if i < len(grid)-1: candidates.append(grid[i+1][j])            
            if j < len(grid[0]) - 1: candidates.append(grid[i][j+1])
            grid[i][j] = min(candidates) + grid[i][j]
    return grid[0][0]