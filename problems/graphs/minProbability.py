from heapq import heappush, heappop
from collections import defaultdict

class Solution:
    def maxProbability(self, n: int, edges: list[list[int]], succProb: list[float], start_node: int, end_node: int) -> float:
        visited = set()
        graph = defaultdict(list)
        prob = [0]*n
        prob[start_node] = 1
        for i in range(len(edges)): 
            u, v = edges[i]
            w = succProb[i]
            graph[u].append([w, v])
            graph[u].append([w, u])        
        maxHeap = [[-1, start_node]]       ## implement max heap: take the path with highest prob        
        while maxHeap:             
            # dequeue
            u_weight, u = heappop(maxHeap)
            u_weight = -u_weight                         # transform to positive
            if u not in visited: 
                visited.add(u)
                if u == end_node: return u_weight
                for v_weight, v in graph[u]: 
                    if v not in visited and prob[v] < u_weight*v_weight: 
                        prob[v] = u_weight*v_weight
                        heappush(maxHeap, [-u_weight*v_weight, v])                                
        return 0