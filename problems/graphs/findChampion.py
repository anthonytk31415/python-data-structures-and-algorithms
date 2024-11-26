# 2924. Find Champion II
# https://leetcode.com/problems/find-champion-ii/description/?envType=daily-question&envId=2024-11-26

from collections import defaultdict


def dfs(u, adj, visited): 
    for v in adj[u]: 
        if visited[v] == -1: 
            visited[v] = 1
            dfs(v, adj, visited)
        elif visited[v] == 0: 
            visited[v] = 1

class Solution:
    def findChampion(self, n: int, edges: list[list[int]]) -> int:
        visited = [-1]*n
        adj = defaultdict(list)        
        for u, v in edges: 
            adj[u].append(v)

        for u in range(n): 
            if visited[u] == -1: 
                dfs(u, adj, visited)        
        
        countWinners = 0
        winner = None
        for u, numVisited in enumerate(visited): 
            if numVisited == -1: 
                countWinners += 1 
                winner = u
        if countWinners > 1: return -1        
        return winner