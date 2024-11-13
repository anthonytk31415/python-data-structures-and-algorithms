# kruskals 
from heapq import heappush, heappop

def union(pu, pv, parent, rank): 
    if rank[pu] < rank[pv]: 
        pu, pv = pv, pu
    parent[pv] = pu
    rank[pu] += rank[pv]    

def find(u, parent): 
    if u != parent[u]: 
        parent[u] = find(parent[u], parent)
    return parent[u]

def kruskals(edges, numVertices):
    parent = [i for i in range(numVertices)]
    rank = [1 for _ in range(numVertices)]
    numEdgesChosen = minCost = 0
    heap = []
    for u, v, w in edges: 
        heappush(heap, [w, u, v])
    while numEdgesChosen < numVertices - 1 and heap: 
        w, u, v = heappop(heap)
        pu, pv = find(u, parent), find(v, parent)
        if pu != pv: 
            union(pu, pv, parent, rank)            
            numEdgesChosen += 1
            minCost += w
    return minCost


edges = [(0, 1, 10),(0, 2, 6),(0, 3, 5),(1, 3, 15),(2, 3, 4)]
v = 4
res = kruskals(edges, v)
print("result: ", res)