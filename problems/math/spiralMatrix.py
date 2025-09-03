





def spiralOrder(matrix): 
    DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    m, n = len(matrix), len(matrix[0])
    visited = set()
    res = []
    i, j = 0, 0
    idx = 0
    while len(res) < m*n:         
        # do move. if next move within, update
        res.append(matrix[i][j])
        visited.add((i, j))
        u, v = i + DIRS[idx][0], j + DIRS[idx][1]
        if not (0 <= u < m and 0 <=  v < n) or ((u, v) in visited): 
            idx = (idx + 1)% 4
        i, j = i + DIRS[idx][0], j + DIRS[idx][1]
    return res

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(spiralOrder(matrix))