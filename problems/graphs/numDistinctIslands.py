# https://leetcode.com/problems/number-of-distinct-islands/?envType=company&envId=amazon&favoriteSlug=amazon-six-months
# 694. Number of Distinct Islands

# Time O((mn)**2) since for each island, you then compare to each other island
# Space: O(mn)

class Solution:
    def numDistinctIslands(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])

        # dfs to get an array of the islands
        def getIslands(grid): 
            visited = set()
            
            def dfs(i, j):
                visited.add((i, j))
                dfsVisit.add((i, j))
                for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    u, v = i + di, j + dj
                    if (0 <= u < m and 0 <= v < n and 
                            grid[u][v] == 1 and 
                            (u, v) not in dfsVisit and 
                            (u, v) not in visited ): 
                        dfs(u, v)
                return 

            res = []
            for i in range(m): 
                for j in range(n):
                    if (i, j) not in visited and grid[i][j] == 1:
                        dfsVisit = set()
                        dfs(i, j)
                        res.append(dfsVisit)
            return res
        
        def calcDelta(u, v): 
            x = v[0] - u[0]
            y = v[1] - u[1]
            return (x, y)
        
        # are islands equal after translation? 
        def compareIsland(i1, i2): 
            if len(i1) != len(i2): return False
            prev1, prev2 = i1[0], i2[0]    
            
            for i in range(1, len(i1)):
                cur1, cur2 = i1[i], i2[i]
                delta = calcDelta(prev1, cur1)
                if (prev2[0] + delta[0], prev2[1] + delta[1]) != cur2: return False
                prev1, prev2 = cur1, cur2
            return True   

        islands = getIslands(grid)
        # sort islands to compare
        islands = [sorted(list(x), key = lambda x: (x[0], x[1])) for x in islands]
        
        copy = set()
        res = 0
        # iterate through the islands and compare if equal by translation
        for i in range(len(islands)): 
            if i in copy: continue
            for j in range(i + 1, len(islands)):
                curRes = compareIsland(islands[i], islands[j])
                if curRes: 
                    copy.add(j)                    
            res += 1
        return res
    
grid = [[1,1,0,1,1],[1,0,0,0,0],[0,0,0,0,1],[1,1,0,1,1]]
s = Solution()
print(s.numDistinctIslands(grid))