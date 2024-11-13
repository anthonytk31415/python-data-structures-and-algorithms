
# kruskals 
from heapq import heappush, heappop

def union(pu, pv, parent, rank):
    if rank[pv] > rank[pu]: 
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
    minCost = numEdgesChosen = 0
    queue = []
    for u, v, w in edges: 
        heappush(queue, [w, u, v])
    while queue and numEdgesChosen < numVertices - 1:
        w, u, v = heappop(queue)
        pu, pv = find(u, parent), find(v, parent)
        if pu != pv: 
            union(pu, pv, parent, rank)
            minCost += w
            numEdgesChosen += 1
    return minCost

edges = [(0, 1, 10),(0, 2, 6),(0, 3, 5),(1, 3, 15),(2, 3, 4)]
v = 4
res = kruskals(edges, v)
print("result: ", res)