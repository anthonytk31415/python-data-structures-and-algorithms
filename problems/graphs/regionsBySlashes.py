# https://leetcode.com/problems/regions-cut-by-slashes/description/?envType=company&envId=amazon&favoriteSlug=amazon-six-months
# 959. Regions Cut By Slashes

# DFS islands problem. 


class Solution:
    def regionsBySlashes(self, grid: list[str]) -> int:        
        n = len(grid) # k = 0 -> top and 1 -> bottom
        # for u, v start and end, find v's k. u = (i, j, k); v = destination (i_v, j_v ) with k left out        
        def getK(u, v): 
            compDir = grid[u[0]][u[1]]
            # special logic for blanks
            if grid[u[0]][u[1]] == " ":
                if (u[2] and u[1] < v[1]) or (not u[2] and v[1] < u[1]): compDir = "/" 
                else: compDir = "\\"        

            # same slashes: go to opposite top/bot of start; else go to same
            if compDir == grid[v[0]][v[1]]: return 1 - u[2]
            return u[2]

        # given your (i, j, k), find your neighbors for traversal
        def getDestinations(i,j,k):
            res = []
            if grid[i][j] == " ": res.append((i, j, 1 - k)) # blanks always traverse to the top/bot
            # get left or right traversals. 
            if k == 0: 
                if 0 <= i-1: res.append((i-1, j, 1))    # if top, go up, bottom 
                if grid[i][j] in set(["/", " "]):       # / and " " go to left
                    x, y = i, j - 1
                    if 0 <= x < len(grid) and 0 <= y < len(grid[0]): 
                        ks = getK((i, j, k), (x, y))
                        res.append((x, y, ks))
                if grid[i][j] in set(["\\", " "]):
                    x, y = i, j +1
                    if 0 <= x < len(grid) and 0 <= y < len(grid[0]): 
                        ks = getK((i, j, k), (x, y))
                        res.append((x, y, ks))
            if k == 1: 
                if i +1 < len(grid): res.append((i+1, j, 0))    # if bottom, go down, top
                if grid[i][j] in set(["/", " "]):               # \ and " " go to right
                    x, y = i, j + 1
                    if 0 <= x < len(grid) and 0 <= y < len(grid[0]): 
                        ks = getK((i, j, k), (x, y))
                        res.append((x, y, ks))
                if grid[i][j] in set(["\\", " "]):
                    x, y = i, j -1
                    if 0 <= x < len(grid) and 0 <= y < len(grid[0]): 
                        ks = getK((i, j, k), (x, y))
                        res.append((x, y, ks))
            return res

        # dfs your neighbors recursively
        def dfs(i, j, k):
            visited.add((i, j, k))
            destinations = getDestinations(i, j, k)
            for u, v, w in destinations: 
                if (u, v, w) not in visited:
                    dfs(u, v, w)

        # dfs and find the islands
        res = 0
        visited = set()
        for i in range(n):
            for j in range(n):
                for k in range(2): 
                    if (i, j, k) not in visited: 
                        dfs(i, j, k)
                        res += 1
        return res

grid = ["/\\", "\\/"] # 5
# grid = [" /","/ "] # 2
# grid = [" /","  "] # 1

# grid = ["\\/","/\\"] # 4
s = Solution()
print(s.regionsBySlashes(grid))