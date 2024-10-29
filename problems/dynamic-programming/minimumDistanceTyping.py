# 1320. Minimum Distance to Type a Word Using Two Fingers
# https://leetcode.com/problems/minimum-distance-to-type-a-word-using-two-fingers/description/

# 2d DP. Trust your instincts with DFS and memoization. 


def getCoordinateMap(): 
    coordinateMap = {}
    row = col = 0
    for x in "ABCDEFGHIJKLMNOPQRSTUVWXYZ": 
        coordinateMap[x] = (row, col) 
        col += 1
        if col == 6: 
            row += 1
            col = 0    
    return coordinateMap

def getDist(x, y, coordinateMap): 
    if x == None: return 0
    a, b = coordinateMap[x]
    c, d = coordinateMap[y]
    return abs(a - c) + abs(b - d)

def dfs(i, left, right, memo, word, coordinateMap): 
    if (i, left, right) in memo: return memo[(i, left, right)]
    if i >= len(word): 
        res = 0
    else: 
        char = word[i]
        res = min(
            dfs(i+1, char, right, memo, word, coordinateMap) + getDist(left, char, coordinateMap), 
            dfs(i+1, left, char, memo, word, coordinateMap) + getDist(right, char, coordinateMap))
    memo[(i, left, right)] = res
    return res

class Solution:
    def minimumDistance(self, word: str) -> int:
        coordinateMap = getCoordinateMap()
        memo = {}
        return dfs(0, None, None, memo, word, coordinateMap)