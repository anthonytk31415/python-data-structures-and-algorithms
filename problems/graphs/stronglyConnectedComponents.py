from collections import defaultdict
from math import inf

# first we're going to dfs and get their start and exit times
def stronglyConnectedComponents(n, edges):
    visited = set()
    start, end, parent = [None]*n, [None]*n, [None]*n
    graph, graphT = defaultdict(list), defaultdict(list)        # build adj adn adj transpose
    time = [0]
    for u, v in edges: 
        graph[u].append(v)
        graphT[v].append(u)

    def dfs(u):
        time[0] += 1
        visited.add(u)
        start[u] = time[0]
        for v in graph[u]:
            if v not in visited: 
                parent[v] = u
                dfs(v)
        time[0] += 1
        end[u] = time[0]

    # traverse, find start and end times for each node. 
    for i in range(n):
        if i not in visited: dfs(i)

    # Sort by end time descending to find the process order for second dfs
    orderEnds = [(node, endTime) for node, endTime in enumerate(end)]
    orderEnds.sort(key = lambda x: -x[1])

    # each connected dfs from graph Transpose will give you the connected set
    def findComponents(u):
        visitedF.add(u)
        curComponents.add(u)
        for v in graphT[u]: 
            if v not in visitedF:
                findComponents(v) 

    visitedF = set()
    condensationGraph = []
    for node, _ in orderEnds: 
        if node not in visitedF: 
            curComponents = set()
            findComponents(node)
            condensationGraph.append(curComponents)

    startCG, endCG,  =[None]*len(condensationGraph), [None]*len(condensationGraph)
    nodeToCG = [None]*n

    # build the node to CG 
    for i, scc in enumerate(condensationGraph): 
        for u in scc: 
            nodeToCG[u] = i


    # For CG: build start and ends, and adj list
    graphCG = defaultdict(set)
    for i, scc in enumerate(condensationGraph): 
        startTime = inf
        endTime =  -inf
        for u in scc: 
            startTime = min(startTime, start[u])
            endTime = max(endTime, end[u])
            for v in graph[u]: 
                if v not in scc: graphCG[i].add(nodeToCG[v])
        startCG[i] = startTime
        endCG[i] = endTime

    return condensationGraph

    # print("order ends: ", orderEnds)
    # print("start:  ", start)
    # print("end:    ", end)
    # print("parent: ", parent)
    # print("condensation graph: ", condensationGraph)
    # print("graphCG: ", graphCG)
    # print("startCG: ", startCG)
    # print("endCG:   ", endCG)

edges = [[0, 7], [7, 0], [0, 1], [7, 6], [1, 1], [1, 2], [2, 1], [2, 5], [5, 3], [3, 2], [3, 4], [4, 9], [9, 4], [5, 9], [5, 6], [6, 2], [7, 8], [8, 9], [8, 6]]
n = 10

print("strongly connected components: ", stronglyConnectedComponents(n, edges))