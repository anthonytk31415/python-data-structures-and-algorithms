from collections import defaultdict

# https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/description/
# 947. Most Stones Removed with Same Row or Column

# Union Find version


def removeStones(stones: list[list[int]]) -> int: 

    def find(u, parent): 
        if parent[u] != u: 
            parent[u] = find(parent[u], parent)
        return parent[u]
        
    def union(pu, pv, parent, rank):
        if rank[pu] < rank[pv]: 
            pv, pu = pu, pv
        parent[pv] = pu
        rank[pu] += rank[pv]

    stones = [tuple(x) for x in stones]
    parent, rank = {x: x for x in stones}, {x: 1 for x in stones}
    rows, cols = defaultdict(set), defaultdict(set)
    for stone in stones: 
        row, col = stone
        rows[row].add(stone)
        cols[col].add(stone)

    def unionOnPaths(rows): 
        for row in rows:         
            baseChild = None
            for rowChild in rows[row]:
                if baseChild == None: 
                    baseChild = rowChild
                    continue
                pu, pv = find(baseChild, parent), find(rowChild, parent)
                if pu != pv: 
                    union(pu, pv, parent, rank)

    unionOnPaths(rows)
    unionOnPaths(cols)
    res = 0
    for stone in stones: 
        if parent[stone] == stone: 
            res += rank[stone] - 1
    return res

# stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
# stones = [[0, 0], [1,0], [1, 2], [2, 2], [2,1], [3, 3]]
print(removeStones(stones))