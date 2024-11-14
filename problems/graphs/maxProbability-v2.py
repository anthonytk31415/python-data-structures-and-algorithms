from heapq import heappush, heappop
from collections import defaultdict

# https://leetcode.com/problems/path-with-maximum-probability/description/
# 1514. Path with Maximum Probability

# - Djikstras with max heap. 
# - Create an adjacency list with succProb[i] = weight i, and u, v edges[i]. 
# - Enqueue start with prob = 1. 
# - Create a visited set so you don't visit nodes twice. 
# - Create a prob array for each vertex to set the prob when you enqueue so 
#   if newly relaxed vertices come in, they don't make it in the queue unless
#   it gives you a better path. 
# - Return the answer if you arrive at the end_node. If you don't ever get there, 
#   the problem terminates and returns 0.  

# Time: O((V+E )log v)
# Space: O(V + E)


def createAdjList(edges, succProb): 
    adjList = defaultdict(list)
    for i in range(len(edges)): 
        u, v = edges[i]
        w = succProb[i]
        adjList[u].append([w, v])
        adjList[v].append([w, u])       
    return adjList

class Solution:
    def maxProbability(self, n: int, edges: list[list[int]], succProb: list[float], start_node: int, end_node: int) -> float:
        visited = set()        
        prob = [0]*n
        prob[start_node] = 1
        maxHeap = [[-1, start_node]]                    # implement max heap: take the path with highest prob      
        adjList = createAdjList(edges, succProb)
         
        while maxHeap:             
            u_weight, u = heappop(maxHeap)
            if u not in visited: 
                u_weight = -u_weight                         # transform to positive
                visited.add(u)
                if u == end_node: return u_weight
                for v_weight, v in adjList[u]: 
                    if v not in visited and prob[v] < u_weight*v_weight: 
                        prob[u] = u_weight*v_weight
                        heappush(maxHeap, [-u_weight*v_weight, v])             
        return 0
    
n = 5    
edges = [[1,4],[2,4],[0,4],[0,3],[0,2],[2,3]]
succProb = [0.9,0.17,0.6,0.23,0.39,0.04]
start_node = 1
end_node = 4
s = Solution()
res = s.maxProbability(n, edges, succProb, start_node, end_node)
print(res)