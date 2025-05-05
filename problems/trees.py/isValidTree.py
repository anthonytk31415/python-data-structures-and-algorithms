# edges = [edge]
# edge = [a, b]

# Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
# 0: 1,2,3
# 1: 0, 4
# 2: 0
# 3: 0


# write a function: is this a tree
# - can have multiple children 
# - only one parent 

# build an adjacency list 

# critique on time saving operations
# O(n) time - need to traverse entire tree in the worst case

from collections import defaultdict

def isValidTree(n, edges): 
    # time saving operations
    num_edges = len(edges)
    if num_edges != n-1: 
        return False
    
    def createAdjList(edges):
        adjList = defaultdict(list)
        for u, v in edges: 
            adjList[u].append(v)         
            adjList[v].append(u)         
        return adjList

    def dfs(start): 
        visited.add(start)
        for children in adjList[start]: 
            if children not in visited: 
                dfs(children, visited, adjList)
    
    adjList = createAdjList(edges)
    start = 0
    visited = set()
    dfs(start)
    return len(visited) == n 