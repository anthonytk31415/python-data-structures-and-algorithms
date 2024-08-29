# https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/description/
# 947. Most Stones Removed with Same Row or Column

# Build adj list for row each row where for row i, you put in all points in that row. 
# Do same for cols. Recursively DFS to get num of nodes visited in that recursive trip. 
# O(mn) Time and space

from collections import defaultdict
def removeStones(stones: list[list[int]]) -> int:
    stones = [tuple(x) for x in stones]
    rows, cols = defaultdict(set), defaultdict(set)
    for stone in stones: 
        row, col = stone
        rows[row].add(stone)
        cols[col].add(stone)

    def dfs(stone): 
        row, col = stone
        visited.add(stone)
        res = 1
        for rowChild in rows[row]: 
            if rowChild not in visited:
                res += dfs(rowChild)
        for colChild in cols[col]:
            if colChild not in visited: 
                res += dfs(colChild) 
        return res

    visited = set()
    res = 0
    for stone in stones: 
        if stone not in visited: 
            res += dfs(stone) - 1
    return res

stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
print(removeStones(stones))

