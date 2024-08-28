# https://leetcode.com/problems/count-sub-islands/
# 1905. Count Sub Islands

# for g1, get the subislands. use a hash map 
# iterating through g2, if all cells in an island are contained in the same island in g1, increment. 

# Time: O(mn), Space: O(mn)

def countSubIslands1(grid1: list[list[int]], grid2: list[list[int]]) -> int:

    visited1, curIslandNum= {}, 1
    curIslandNum = 1
    def dfs1(i, j, grid, curIslandNum): 
        visited1[(i, j)] = curIslandNum        
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            u, v = i + dx, j + dy
            if 0 <= u < len(grid) and 0 <= v < len(grid[0]) and (u, v) not in visited1 and grid[u][v] == 1: 
                dfs1(u, v, grid, curIslandNum)

    for i in range(len(grid1)):
        for j in range(len(grid1[0])):
            if (i, j) not in visited1 and grid1[i][j] == 1: 
                dfs1(i, j, grid1, curIslandNum)            
                curIslandNum += 1

    visited2, res = {}, 0
    # dfs 2 all i, j if i, j == 1. check if that cell is a subisland. all child islands in that subisland must match that . 
    # so dfs all child and do that check ot make srue all cells are associated with the same subisland 
    # return whether it's a subisland, checking the condition recursively

    def dfs2(i, j, grid, curIslandNum, isSubIsland): 
        visited2[(i, j)] = True
        if (i, j) not in visited1 or visited1[(i, j)] != curIslandNum: 
            isSubIsland = False        
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            u, v = i + dx, j + dy
            if 0 <= u < len(grid) and 0 <= v < len(grid[0]) and (u, v) not in visited2 and grid[u][v] == 1: 
                isChildSubIsland = dfs2(u, v, grid, curIslandNum, isSubIsland)
                isSubIsland = isSubIsland and isChildSubIsland
        return isSubIsland

    for i in range(len(grid2)):
        for j in range(len(grid2[0])):
            if (i, j) not in visited2 and grid2[i][j] == 1: 
                curIslandNum = -1
                if (i, j) in visited1: curIslandNum = visited1[(i, j)]
                isSubIsland = dfs2(i, j, grid2, curIslandNum, True)            
                if isSubIsland: 
                    res += 1
    return res


# combined the same dfs. Used a ones matrix to compare with grid1. then used visited1 to compare with grid2 to biuld visited2. 
# key condition: when you dfs, you must be associated with the same island in your comparison.

def countSubIslands(grid1: list[list[int]], grid2: list[list[int]]) -> int:
    
        def dfs(i, j, grid, curIslandNum, isSubIsland, compareGrid, visited, comparisonNum): 
            visited[i][j] = curIslandNum
            if comparisonNum == 0 or compareGrid[i][j] != comparisonNum: 
                isSubIsland = False        
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                u, v = i + dx, j + dy
                if 0 <= u < len(grid) and 0 <= v < len(grid[0]) and visited[u][v] == None: 
                    if grid[u][v] == 0: visited[u][v] = 0
                    else:  
                        isChildSubIsland = dfs(u, v, grid, curIslandNum, isSubIsland, compareGrid, visited, comparisonNum)
                        isSubIsland = isSubIsland and isChildSubIsland
            return isSubIsland
        
        ones = [[1 for _ in grid1[0]] for _ in grid1]
        visited1, visited2 = [[None for _ in grid1[0]] for _ in grid1], [[None for _ in grid2[0]] for _ in grid2]
        curIslandNum, res = 1, 0
        for i in range(len(grid1)):
            for j in range(len(grid1[0])):
                if visited1[i][j] == None: 
                    if grid1[i][j] == 1: 
                        dfs(i, j, grid1, curIslandNum, True, ones, visited1, 1)            
                        curIslandNum += 1
                    else: visited1[i][j] = 0

        for i in range(len(grid2)):
            for j in range(len(grid2[0])):
                if visited2[i][j] == None: 
                    if grid2[i][j] == 1: 
                        curIslandNum = visited1[i][j]                    
                        isSubIsland = dfs(i, j, grid2, curIslandNum, True, visited1, visited2, curIslandNum)            
                        if isSubIsland: res += 1
                    else: visited2[i][j] = 0
        return res



# grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]]
# grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]

grid1 = [[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]]
grid2 = [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]

# print(0 == False)
print(countSubIslands(grid1, grid2))