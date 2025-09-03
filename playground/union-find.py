


# union find 
from collections import defaultdict



def build_adj_list(edges):     
    adj_list = defaultdict(list)
    for u, v, w in edges:  
        adj_list[u].append((v, w))
    return adj_list

def find_parent(u, parent): 
    if parent[u] != u: 
        parent[u] = find_parent(parent[u], parent)
    return parent[u]


def union(pu, pv, parent, rank): 
    if rank[pv] > rank[pu]: 
        pu, pv = pv, pu
    parent[pv] = pu
    rank[pu] += rank[pv]


def min_spanning_tree(n, edges): 
    edges.sort(key = lambda x: x[2])
    parent = [-1]*n
    rank = [1]*n
    
     
    
    
    
    return 



for vertex in vertices: 
    for edge in adjacencylist[vertex]: 
        parent u, parent v
        if parents are not equal: union(parent_u, parent v)
        
        else: 
            cycle
            
            
from collections import deque

DIRS = [0,1,0,-1,0]
m, n = len(grid), len(grid[0])
for z in range(4): 
    u, v = x + DIRS[z], y + DIRS[z+1]
    if 0 <= u < m and 0 <= v < n and ... 
