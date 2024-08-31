# https://leetcode.com/problems/path-with-maximum-probability/
# 1514. Path with Maximum Probability

from collections import defaultdict
from heapq import heappush, heappop 

def maxProbability(n: int, edges: list[list[int]], succProb: list[float], start_node: int, end_node: int) -> float:
    prob = [0]*n
    graph = defaultdict(list)
    for i, edge in enumerate(edges): 
        u, v = edge 
        w = succProb[i]
        graph[u].append([v, w])
        graph[v].append([u, w])
    visited = set() 
    q = [[-1, start_node]]
    while q: 
        curProb, u = heappop(q)
        curProb = -curProb
        prob[u] = curProb
        visited.add(u)
        if u == end_node: return curProb
        for v, w in graph[u]: 
            if v not in visited and curProb*w > prob[v]: 
                heappush(q, [-curProb*w, v])
    return 0

n = 3
edges = [[0,1],[1,2],[0,2]]
succProb = [0.5,0.5,0.2]
start = 0
end = 2

n = 3
edges = [[0,1],[1,2],[0,2]]
succProb = [0.5,0.5,0.3]
start = 0
end = 2

n = 3
edges = [[0,1]]
succProb = [0.5]
start = 0
end = 2

print(maxProbability(n, edges, succProb, start, end))