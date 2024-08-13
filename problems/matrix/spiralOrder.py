def spiralOrder(matrix: list[list[int]]) -> list[int]:
    i, j = 0, 0
    dirs = [(0,1), (1,0), (0, -1), (-1, 0)]    
    curDir = 0
    res = [matrix[i][j]]
    visited = set()
    visited.add((0,0))
    while len(visited) < len(matrix) * len(matrix[0]):
        di, dj = dirs[curDir]
        u, v  = i + di, j + dj
        if 0 <= u < len(matrix) and 0 <= v < len(matrix[0]) and (u, v) not in visited:
            visited.add((u, v))            
            res.append(matrix[u][v])
            i, j = u, v
        else: curDir = (curDir + 1) % 4    
        
    return res

matrix = [[1,2,3],[4,5,6],[7,8,9]]
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(spiralOrder(matrix))