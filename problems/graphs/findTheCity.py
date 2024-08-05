# https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/description/
# 1334. Find the City With the Smallest Number of Neighbors at a Threshold Distance

from math import inf 
from heapq import heappush, heappop
from collections import defaultdict

# One way is to dfs each node. if you reach a visited node with a lower cost, you must lower the cost
# and update. N^3 time implementation, O(V^2) space. 

# Another is to floyd warshall dp to find the min cost to traverse from i to j. then for each (i,j), 
# if it's within threshold, count it. Also N^3 time, O(V^2) space. 

# can you do an n^2 log n with a priority queue? Yes. You can run Djikstras n times. 
# O(nlogn) Time, O(V+E) Space. 
# Tiny note - you don't need a visited. You only visit somethign when you have min dist to get there. 
# the priority queue takes care of it. 

# floyd warshall implementation
def findTheCity1(n, edges, distanceThreshold):
    dp = [[inf]*n for _ in range(n)]
    for u, v, w in edges: 
        dp[u][v] = w
        dp[v][u] = w
    for i in range(n):
        dp[i][i] = 0
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
    vertex = n-1
    numConnections = inf 

    for i in range(n):
        curConnections = 0
        for j in range(n): 
            if j == i: continue
            if dp[i][j] <= distanceThreshold: curConnections += 1
        if curConnections <= numConnections:
            vertex = i
            numConnections = curConnections 
    return vertex

# bfs priority queue
# basically a djikstras done n times. 
def findTheCity(n, edges, distanceThreshold):
    graph = defaultdict(list)
    for u, v, w in edges: 
        graph[u].append((v, w))
        graph[v].append((u, w))

    # return an array from 0 to n -1 of the min distances
    def bfs(start): 
        res = [inf]*n
        pq = [(0, start)]
        while pq: 
            curDist, curNode = heappop(pq)
            if curDist < res[curNode]: 
                res[curNode] = curDist
                for childNode, childWeight in graph[curNode]:
                    if curDist + childWeight < res[childNode]:
                        heappush(pq, (curDist + childWeight, childNode))
        return res
    
    resNode = n-1
    minConns = inf
    for i in range(n):
        curRes = bfs(i)
        curConns = sum([1 for j, dist in enumerate(curRes) if j != i and dist <= distanceThreshold])
        if curConns <= minConns: 
            minConns = curConns
            resNode = i
    return resNode

n = 4
edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]]
distanceThreshold = 4

n = 5
edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]]
distanceThreshold = 2

print(findTheCity(n, edges, distanceThreshold))