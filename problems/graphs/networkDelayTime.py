from math import inf 
from heapq import heappush, heappop
from collections import defaultdict

# floyd warshall implementation
def networkDelayTime1(times: list[list[int]], n: int, k: int) -> int:
    graph = [[inf for _ in range(n)] for _ in range(n)]
    for i in range(n): 
        graph[i][i] = 0
    for u, v, w in times: 
        graph[u-1][v-1] = w
    for z in range(n): 
        for i in range(n):
            for j in range(n):
                graph[i][j] = min(graph[i][j], graph[i][z] + graph[z][j])
    res = max(graph[k-1])
    if res == inf: return -1
    return res

#  djikstra's implementation
def networkDelayTime(times: list[list[int]], n: int, k: int) -> int:
    dist = [inf] * n
    graph = defaultdict(list)
    for u, v, w in times: 
        graph[u-1].append([v-1, w])
    q = [[k-1, 0]]
    while q: 
        u, uWeight = heappop(q)
        if dist[u] > uWeight: 
            dist[u] = uWeight
            for v, vWeight in graph[u]: 
                if dist[v] > uWeight + vWeight: 
                    heappush(q, [v, uWeight + vWeight])
    res = max(dist)
    if res == inf: return -1
    return res


# times = [[2,1,1],[2,3,1],[3,4,1]]
# n = 4
# k = 2

times = [[1,2,1]]
n = 2
k = 1

print(networkDelayTime(times, n, k))