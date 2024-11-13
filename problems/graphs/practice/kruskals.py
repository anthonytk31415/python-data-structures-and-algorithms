## kruskals 
from heapq import heappop, heappush
 
def union(pu, pv, parent, rank): 
    if rank[pu] < rank[pv]: 
        pv, pu = pu, pv
    parent[pv] = pu
    rank[pu] += rank[pv]

def find(u, parent): 
    if u != parent[u]: 
        parent[u] = find(parent[u], parent)
    return parent[u]

def kruskals(edges, numVertices): 
    parent = [i for i in range(numVertices)]
    rank = [1 for _ in range(numVertices)]
    numEdges = minCost = 0
    queue = []
    for u, v, w in edges: 
        heappush(queue, [w, u, v])
    while numEdges < numVertices - 1 and queue: 
        w, u, v = heappop(queue)
        pu, pv = find(u, parent), find(v, parent)
        if pu != pv: 
            numEdges += 1
            minCost += w
            union(pu, pv, parent, rank)     
    return minCost

# edges = [[0, 1, 1],[0, 2, 1],[1, 2, 10],[1, 3, 10],[2, 3, 1],[3, 4, 1],[4, 5, 1], [5, 6, 1]]
# v = 7


edges = [(0, 1, 10),(0, 2, 6),(0, 3, 5),(1, 3, 15),(2, 3, 4)]
v = 4
res = kruskals(edges, v)
print("result: ", res)