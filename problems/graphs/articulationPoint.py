# Finding articulation points 

from collections import defaultdict

def findArticulationPoint(edges, n):
    graph = defaultdict(list)
    for u, v in edges: 
        graph[u].append(v)

    parent = defaultdict(set)
    visited = [0] * n # 0 not visited, 1 visiting, 2 visited
    tIn = [None] * n
    low = [None] * n
    articulationPoints = set()


    def dfs(u):
        visited[u] = 1
        tIn[u] = time[0] 
        low[u] = time[0]
        time[0] += 1 
        children = 0
        for v in graph[u] : 
            parent[v].add(u)
            if visited[v] in set([1, 2]): 
                low[u] = min(low[u], tIn[v])                                
            else:  
                dfs(v)
                low[u] = min(low[u], low[v])
                if low[v] >= tIn[u] and len(parent[u]) != 0: 
                    print("adding u: ", u, v, "parent: ", parent, low, tIn)
                    articulationPoints.add(u)        
                children += 1
        visited[u] = 2
        if len(parent[u]) == 0 and children > 1:
            articulationPoints.add(u)  

    time = [0]
    for u in range(n): 
        if visited[u] == 0: 
            dfs(u)

    print(parent)
    print("tIn: ", tIn)
    print("low: ", low)

    return articulationPoints


edges = []
n = 1



edges = [[0,1], [1,2], [2,0], [2, 3], [3,4 ], [4,5 ], [5,3]]
n = 6

print(findArticulationPoint(edges, n))
