# https://leetcode.com/problems/making-a-large-island/

# build islands: all cells and perimeter
# build adjacency list
# for each island:

from collections import deque

DIRS = [[1,0], [-1, 0], [0, 1], [0, -1]]

def within_bounds(u, v, rows, cols): 
    return 0 <= u < rows and 0 <= v < cols

def is_land(cell, grid, rows, cols): 
    x, y = cell
    for dx, dy in DIRS:
        u, v = x + dx, y + dy
        if within_bounds(u, v, rows, cols) and grid[u][v] == 0: 
            return False
    return True

def find_island(start, grid, rows, cols): 
    beach, land = set(), set()
    queue = deque()
    if is_land(start, grid, rows, cols): 
        land.add(start)
    else: 
        beach.add(start)
    queue.append(start)
    while queue: 
        x, y = queue.popleft()
        for dx, dy in DIRS:
            u, v = x + dx, y + dy
            if within_bounds(u, v, rows, cols) and (u, v) not in beach and (u, v) not in land and grid[u][v] == 1: 
                if is_land((u,v), grid, rows, cols): 
                    land.add((u,v))
                else: 
                    beach.add((u,v))
                queue.append((u,v))    
    return beach, land

def find_islands(grid, rows, cols): 
    island = 0
    island_size = []            
    beach_lookup = {}          #beach[cell] = island i    
    visited = set()
    for i in range(rows): 
        for j in range(cols): 
            if (i, j) in visited: 
                continue  
            if grid[i][j] == 1: 
                beach, land = find_island((i,j), grid, rows, cols)
                cur_island_size = len(beach) + len(land)
                island_size.append(cur_island_size)
                for x in beach: 
                    visited.add(x) 
                    beach_lookup[x] = island
                for x in land: 
                    visited.add(x)                   
                island += 1                    
            else: 
                visited.add((i,j))
    return island_size, beach_lookup
                
def get_island_connections(cell, beach_lookup, island_size, rows, cols): 
    x, y = cell
    island_connections = set()
    for dx, dy in DIRS:
        u, v = x + dx, y + dy
        if within_bounds(u, v, rows, cols) and (u, v) in beach_lookup: 
            island_connections.add(beach_lookup[(u,v)])
    return sum([island_size[x] for x in island_connections])

def find_max_count(grid): 
    rows, cols = len(grid), len(grid[0])
    island_size, beach_lookup = find_islands(grid, rows, cols)
    max_count = 1
    if island_size: 
        max_count = max(max_count, max(island_size))
    for i in range(rows): 
        for j in range(cols): 
            if grid[i][j] == 0: 
                max_count = max(max_count, 1 + get_island_connections((i,j), beach_lookup, island_size, rows, cols))
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


