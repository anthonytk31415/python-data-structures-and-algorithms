# https://leetcode.com/problems/spiral-matrix-iii/description/?envType=daily-question&envId=2024-08-08
# 885. Spiral Matrix III

# Move 1, 1, 2, 2, 3, 3, 4, 4 ...  n steps where each n step is done at the 0th dir, 1th dir... etc.

def spiralMatrixIII(rows: int, cols: int, rStart: int, cStart: int): 
    res = [[rStart, cStart]]
    steps = 1
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    curDir = 0
    i, j = rStart, cStart
    while len(res) < rows*cols: 
        for _ in range(2):
            for _ in range(steps):
                i, j = i + dirs[curDir][0], j + dirs[curDir][1]
                if 0 <= i < rows and 0 <= j < cols: 
                    res.append([i, j])                    
            curDir = (curDir + 1) % 4
        steps += 1
    return res


rows = 5
cols = 6
rStart = 1
cStart = 4

print(spiralMatrixIII(rows, cols, rStart, cStart))