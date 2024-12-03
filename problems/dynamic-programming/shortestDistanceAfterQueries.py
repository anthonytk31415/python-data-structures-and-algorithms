from math import inf
class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: list[list[int]]) -> list[int]:
        dist = [[inf for _ in range(n)] for _ in range(n)]
        for u in range(n):
            for v in range(u, n): 
                dist[u][v] = v - u
        res = [inf]*len(queries)
        for k in range(len(queries)): 
            u, v = queries[k]
            for i in range(u+1): 
                for j in range(v, n):                     
                    dist[i][j] = min(dist[i][j], dist[i][u] + 1 + dist[v][j])
            res[k] = dist[0][n-1]
        return res
        
s = Solution()

# n = 5
# queries = [[2,4],[0,2],[0,4]]

n = 14
queries = [[0,6],[4,12]]
print(s.shortestDistanceAfterQueries(n, queries))
        