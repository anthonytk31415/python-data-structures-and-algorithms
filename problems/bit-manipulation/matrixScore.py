# https://leetcode.com/problems/score-after-flipping-matrix/?envType=problem-list-v2&envId=bit-manipulation
# 861. Score After Flipping Matrix

def getBin(row):
    strInt = "".join([str(int(x)) for x in row])
    return int(strInt, base=2)

class Solution:

    def matrixScore(self, grid: list[list[int]]) -> int:
        rowState = [None]*(len(grid))
        colState = [None]*len(grid[0])
        res = [0]

        # each transformation 
        def dfs(bitGrid): 
            m, n = len(bitGrid), len(bitGrid[0])
            binSum = sum(getBin(row) for row in bitGrid)
            res[0] = max(res[0], binSum)
            for i in range(m): 
                if rowState[i] == None: 
                    flipped = [not(x) for x in bitGrid[i]]
                    if getBin(flipped) > getBin(bitGrid[i]): 
                        bitGrid[i] = flipped
                        rowState[i] = 1
                        dfs(bitGrid)
            for j in range(n): 
                if colState[j] == None: 
                    delta = 1 if m % 2 == 1 else 0
                    numBitsInCol = sum(bitGrid[i][j] for i in range(m))
                    if (numBitsInCol < m//2 + delta) : 
                        for i in range(m): 
                            bitGrid[i][j] = not(bitGrid[i][j])
                        colState[j] = 1
                        dfs(bitGrid)
        dfs(grid)
        return res[0]

grid = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
# grid = [[0,1],[1,1]]
# grid =[[1,1],[0,1],[0,0],[1,0],[1,1],[1,1]]
grid = [[0,0,0],[0,0,0],[1,0,1],[0,1,0],[0,1,0],[0,0,1],[1,1,1]]
s = Solution()
print(s.matrixScore(grid))




# print (int(not(0)))

# 1100
# 1010
# 0101

# 1101
# 1011
# 0100

# 1101
# 1011
# 1011

# 1001
# 1111
# 1111
# terminal