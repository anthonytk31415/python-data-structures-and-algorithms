# https://leetcode.com/problems/making-a-large-island/

# build islands: all cells and perimeter
# build adjacency list
# for each island:

from collections import deque

DIRS = [0,1,0,-1,0]

def find_island(start, grid, m, n): 
    land = set([start])
    queue = deque([start])
    while queue: 
        x, y = queue.popleft()
        for z in range(4): 
            u, v = x + DIRS[z], y + DIRS[z+1]
            if 0 <= u < m and 0 <= v < n and (u, v) not in land and grid[u][v] == 1: 
                land.add((u,v))
                queue.append((u,v))    
    return land

def find_islands(grid, m, n): 
    island = 0
    island_size = []            
    beach_lookup = {}          # beach[cell] = island i    
    for i in range(m): 
        for j in range(n): 
            if (i, j) not in beach_lookup and grid[i][j] == 1: 
                land = find_island((i,j), grid, m, n)
                island_size.append(len(land))
                for x in land: 
                    beach_lookup[x] = island     
                island += 1                    
    return island_size, beach_lookup
                
def get_island_connections(cell, beach_lookup, island_size, m, n): 
    x, y = cell
    island_connections = set()
    for z in range(4): 
        u, v = x + DIRS[z], y + DIRS[z+1]
        if 0 <= u < m and 0 <= v < n and (u, v) in beach_lookup: 
            island_connections.add(beach_lookup[(u,v)])
    return sum([island_size[x] for x in island_connections])

def find_max_count(grid): 
    m, n = len(grid), len(grid[0])
    island_size, beach_lookup = find_islands(grid, m, n)
    max_count = 1
    if island_size: 
        max_count = max(max_count, max(island_size))
    for i in range(m): 
        for j in range(n): 
            if grid[i][j] == 0: 
                max_count = max(max_count, 1 + get_island_connections((i,j), beach_lookup, island_size, m, n))
    return max_count
                       
class Solution:
    def largestIsland(self, grid: list[list[int]]) -> int:
        return find_max_count(grid) 
      
grid = [[0,0,0,0,0,0,0],
        [0,1,1,1,1,0,0],
        [0,1,0,0,1,0,0],
        [1,0,1,0,1,0,0],
        [0,1,0,0,1,0,0],
        [0,1,0,0,1,0,0],
        [0,1,1,1,1,0,0]]
# grid = [[1,0],[0,1]]
# # grid = [[1,1],[1,0]]
# # grid = [[1,1],[1,1]]
print(find_max_count(grid))
