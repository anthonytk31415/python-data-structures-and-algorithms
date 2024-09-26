
# O(n^4) implementation; can we do better? i think we can with DP
from collections import Counter


# This is a dp O(n^3) solution. When you find a pair, see if you found a pair earlier. Then keep track of the pairs. 
class Solution:
    def countCornerRectangles(self, grid: list[list[int]]) -> int:
        pairs = Counter()
        res = 0
        for i in range(len(grid)): 
            curOnes = []
            for j in range(len(grid[i])): 
                if grid[i][j] == 1: 
                    curOnes.append(j)
            for u in range(len(curOnes)):
                for v in range(u + 1, len(curOnes)): 
                    pair = (curOnes[u], curOnes[v])
                    if pair in pairs: 
                        res += pairs[pair]
                    pairs[pair] += 1
        return res

class Solution1:
    def countCornerRectangles1(self, grid: list[list[int]]) -> int:
        if len(grid) <= 1: return 0
        rowList, rowSet = [], []

        for i in range(len(grid)):
            curList = []
            curSet = set()
            for j in range(len(grid[0])):
                if grid[i][j] == 1: 
                    curList.append(j)
                    curSet.add(j)
            if len(curList) >= 1: 
                rowList.append(curList)
                rowSet.append(curSet)

        res = 0
        for i in range(len(rowList)):
            for u in range(len(rowList[i])):
                uIdx = rowList[i][u]
                for v in range(u + 1, len(rowList[i])):
                    vIdx = rowList[i][v]
                    for k in range(i + 1, len(rowList)):
                        if uIdx in rowSet[k] and vIdx in rowSet[k]: 
                            res += 1
        return res
    
grid = [[1,0,0,1,0],[0,0,1,0,1],[0,0,0,1,0],[1,0,1,0,1]] # 1
grid = [[1,0,0,1,0],
        [0,0,1,0,1],
        [1,0,1,1,0],
        [1,0,1,1,1]]

# a = [1,2,3,4]
# a.pop(2)
# print(a)

s = Solution()
print(s.countCornerRectangles(grid))