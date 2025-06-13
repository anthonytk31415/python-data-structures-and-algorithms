from collections import deque

# # from math import inf
# https://leetcode.com/problems/swim-in-rising-water/?envType=company&envId=google&favoriteSlug=google-thirty-days
# 778. Swim in Rising Water



def does_path_exist(grid, depth): 
    rows, cols = len(grid), len(grid[0])
    queue = deque()
    visited = set()
    if grid[0][0] <= depth: 
        queue.append((0,0))
        visited.add((0,0))
    while queue: 
        cur = queue.popleft()
        if cur == (rows-1, cols - 1): 
            return True
        x, y = cur
        for dx, dy in [[1,0], [-1, 0], [0, 1], [0, -1]]: 
            u, v = x + dx, y + dy
            if (u,v) not in visited and 0 <= u < rows and 0 <= v < cols and grid[u][v] <= depth: 
                queue.append((u, v))       
                visited.add((u,v))
    return False


def binary_search(grid): 
    left = -1
    right = max(max(x) for x in grid)
    while right - left > 1: 
        mid = (right + left) // 2
        if does_path_exist(grid, mid): 
            right = mid
        else: 
            left = mid 
    return right



# bottoms up dp does nto work

# class Solution:
#     def swimInWater(self, grid: List[List[int]]) -> int:
        
#         rows, cols = len(grid), len(grid[0])
#         prev, cur = [inf]*cols, [None]*cols
        
#         for i in range(rows): 
#             for j in range(cols): 
#                 if i == 0 and j == 0: 
#                     cur[j] = list[i][j]                    
#                 elif j == 0: 
#                     cur[j] = max(grid[i][j], prev[j]) 
#                 elif i == 0: 
#                     cur[j] = max(grid[i][j], cur[j-1])
#                 else: 

#                     cur[j] = min(max(grid[i][j], cur[j-1]), grid[i][j], prev[j])                        
#             prev, cur = cur, [None]*cols                
#         return prev[-1]