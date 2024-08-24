# https://leetcode.com/problems/count-the-number-of-complete-components/
# 2685. Count the Number of Complete Components

from collections import defaultdict, deque

# dfs to get the size of the connected component 
# keep track of nodes visited for each connected component
# then for each parent of connected component, check if the children have that same size as the parent. 
# Time: O(mn), Space: O(n)


def countCompleteComponents(n: int, edges: list[list[int]]) -> int:
    adj = defaultdict(list)
    for u, v in edges: 
        adj[u].append(v)
        adj[v].append(u)

    def dfs(u): 
        visited.add(u)
        for v in adj[u]:
            if v not in visited:
                dfs(v)

    allVisited = set()
    groups = {}
    for i in range(n):
        visited = set()
        if i not in allVisited: 
            dfs(i)
            for x in visited: allVisited.add(x)
            groups[i] = visited
    res = 0
    for u in groups: 
        connected = True
        for v in groups[u]: 
            if len(adj[v]) != len(groups[u]) - 1: 
                connected = False
                break 
        if connected: res += 1
    return res



n = 6
edges = [[0,1],[0,2],[1,2],[3,4]]

# n = 6
# edges = [[0,1],[0,2],[1,2],[3,4],[3,5]]


edges = [[1,0],[2,1],[3,0],[3,1],[3,2]]
n = 4
print(countCompleteComponents(n, edges))


# something a bit more convoluted
def countCompleteComponents1(n: int, edges: list[list[int]]) -> int:
    adj = defaultdict(list)
    for u, v in edges: 
        adj[u].append(v)
        adj[v].append(u)

    def dfs(u):
        visited.add(u)
        for v in adj[u]: 
            if v not in visited: 
                dfs(v)

    allVisited = set()
    groups = {}
    for i in range(n):
        visited = set()
        if i not in allVisited: 
            dfs(i)
            for x in visited: allVisited.add(x)
            groups[i] = visited

    def checkConected(u, parent): 
        for v in adj[u]: 
            if v not in groups[parent]: return False
        for v in groups[parent]: 
            if v != u and v not in adj[u]: return False
        return True

    # Now for each group, test for each element in the group, that its connected to each other     
    count = 0
    for parent in groups: 
        connected = True
        for u in groups[parent]: 
            if not checkConected(u, parent): 
                connected = False
                break             
        if connected: 
            count += 1
    return count

        
