# https://leetcode.com/problems/maximum-number-of-fish-in-a-grid/description/
# 2658. Maximum Number of Fish in a Grid

# Time: O(MN), Space: O(MN) 

# 2d union find; can also do prob a bfs or a dfs

def findMaxFish(grid: list[list[int]]) -> int:
    parent, rank = {}, {}
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            parent[(i,j)] = (i, j)
            rank[(i, j)] = grid[i][j]

    def find(u, parent):
        if u != parent[u]: 
            parent[u] = find(parent[u], parent)
        return parent[u]

    def union(pu, pv, parent, rank):
        if rank[pu] < rank[pv]:
            pu, pv = pv, pu
        parent[pv] = pu
        rank[pu] += rank[pv]
        return rank[pu]

    maxFish = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0: continue 
            for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                u, v = i + di, j + dj
                if 0 <= u < len(grid) and 0 <= v < len(grid[0]) and grid[u][v] != 0: 
                    pa, pb = find((i, j), parent), find((u, v), parent)
                    if pa != pb: 
                        union(pa, pb, parent, rank)
            maxFish = max(maxFish, rank[find(parent[(i, j)], parent)])

    return maxFish 

grid = [[0,2,1,0],[4,0,0,3],[1,0,0,4],[0,3,2,0]]
# grid = [[1,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,1]]
print(findMaxFish(grid))