# https://leetcode.com/problems/shortest-bridge/description/
# 934. Shortest Bridge

'''given square binary matrix
1 = land
0 = water

island = connected 1's 
2 group of 1's, not connected
return smallest number of 0's that will connect the 2 groups

Example:
[[0,1],
 [1,0]]
 
 [[0,1,0],
  [0,0,0],
  [0,0,1]]

  [[1,1,1,1,1],
  [1,0,0,0,1],
  [1,0,1,0,1],
  [1,0,0,0,1],
  [1,1,1,1,1]]  
'''

# DFS to find the two islands,
# BFS to find the shortest path

from collections import deque 

def shortestBridge(grid: list[list[int]]) -> int:
    q = deque()
    def dfs(i,j): 
        grid[i][j] = 2
        q.append([(i, j), 0])
        for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]: 
            u, v = i + di, j + dj
            if 0 <= u < len(grid) and 0 <= v < len(grid[0]) and grid[u][v] == 1: 
                dfs(u, v)
        return 

    # find the 1st occurance of the itself    
    for i in range(len(grid)): 
        isFound = False
        for j in range(len(grid[0])):
            if grid[i][j] != 0: 
                dfs(i, j) # label the island 2
                isFound = True
                break 
        if isFound: 
            break

    # bfs to find the shortest path to other island
    while q: 
        node, dist = q.popleft()
        i, j = node
        for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]: 
            u, v = i + di, j + dj
            if 0 <= u < len(grid) and 0 <= v < len(grid[0]) and not grid[u][v] == 2 : 
                if grid[u][v] == 1: return dist
                grid[u][v] = 2        
                q.append([(u, v), dist + 1])               
    return False

# grid =  [[0,1,0],
#   [0,0,0],
#   [0,0,1]]

# grid = [[0,1],
#  [1,0]]
grid =   [[1,1,1,1,1],
  [1,0,0,0,1],
  [1,0,1,0,1],
  [1,0,0,0,1],
  [1,1,1,1,1]]

print(shortestBridge(grid))

# q = [,  [(1, 1), 1], [(1, 0), 2]]

# [(0, 1), 0]

# [(0, 0), 1]
# [(0, 2), 1],