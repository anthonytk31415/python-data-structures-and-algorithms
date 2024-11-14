# https://leetcode.com/problems/min-cost-to-connect-all-points/description/
# 1584. Min Cost to Connect All Points

from heapq import heappush, heappop

def mDist(u, v): 
    x1, y1 = u
    x2, y2 = v
    return abs(x1 - x2) + abs(y1 - y2)

def buildHeap(points): 
    minHeap = []
    for i in range(len(points)): 
        for j in range(i + 1, len(points)): 
            dist = mDist(points[i], points[j])
            edge = [dist, i, j]         # i, j are the indexes within points; hence their vertex number
            heappush(minHeap, edge)
    return minHeap

def find(u, parent):
    if u != parent[u]: 
        parent[u] = find(parent[u], parent)
    return parent[u] 
    
def union(pu, pv, parent, rank):
    if rank[pv] > rank[pu]: 
        pu, pv = pv, pu
    parent[pv] = pu
    rank[pu] += rank[pv]
     

class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        n = len(points)
        parent = [i for i in range(n)]
        rank = [1 for _ in range(n)]
        numEdgesChosen = minCost = 0
        minHeap = buildHeap(points)
        while minHeap and numEdgesChosen < n - 1: 
            cost, u, v = heappop(minHeap)
            pu, pv = find(u, parent), find(v, parent)
            if pu != pv: 
                minCost += cost
                union(pu, pv, parent, rank)
                numEdgesChosen += 1              
        return minCost