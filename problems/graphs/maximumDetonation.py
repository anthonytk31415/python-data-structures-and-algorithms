from math import sqrt
from collections import defaultdict

# https://leetcode.com/problems/detonate-the-maximum-bombs/description/
# 2101. Detonate the Maximum Bombs

# Time O(n**2), Space: O(n)
# DFS, and you want to visit total nodes recursively and then count visits at the end. 


# def find(u, parent):
#     if parent[u] != u: 
#         parent[u] = find(parent[u], parent)
#     return parent[u]



# def union(pu, pv, parent, rank):
#     if rank[pu] < rank[pv]: 
#         pv, pu = pu, pv
#     parent[pv] = pu
#     rank[pu] += rank[pv]



def withinDist(u, v, threshold): 
    return sqrt((u[0] - v[0])**2 + (u[1] - v[1])**2) <= threshold




def maximumDetonation(bombs: list[list[int]]) -> int:
    n = len(bombs)
    graph = defaultdict(set)
    for i, bomb1 in enumerate(bombs): 
        x, y, r = bomb1
        for j, bomb2 in enumerate(bombs): 
            a, b, c = bomb2
            if i == j: continue
            if withinDist([x, y], [a, b], r): 
                graph[i].add(j)
            if withinDist([x, y], [a, b], c):
                graph[j].add(i) 

    def dfs(u): 
        visited.add(u)
        for v in graph[u]: 
            if v not in visited: dfs(v)

    visited = set()
    res = 0
    for i in range(n): 
        visited = set()
        dfs(i)
        res = max(len(visited), res)

    return res

bombs = [[1,2,3],[2,3,1],[3,4,2],[4,5,3],[5,6,4]]
bombs = [[2,1,3],[6,1,4]]
print(maximumDetonation(bombs))