def maximalSquare(matrix):
    left = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    up = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    square = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

    for i in range(len(matrix)): 
        for j in range(len(matrix[0])):
            if matrix[i][j] == "0": left[i][j] = 0
            else: 
                left[i][j] = 1
                if j - 1 >= 0: left[i][j] += left[i][j-1]

    for i in range(len(matrix)): 
        for j in range(len(matrix[0])):
            if matrix[i][j] == "0": up[i][j] = 0
            else: 
                up[i][j] = 1
                if i - 1 >= 0: up[i][j] += up[i - 1][j]
    
    res = 0
    for i in range(len(matrix)): 
        for j in range(len(matrix[0])):
            if matrix[i][j] == "0": square[i][j] = 0
            else: 
                square[i][j] = 1
                if i - 1 >= 0 and j - 1 >= 0: 
                    square[i][j] = min(square[i-1][j-1]+1, up[i][j], left[i][j])
                res = max(square[i][j], res)
    
    return res **2



matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
matrix = [["0","1"],["1","0"]]
matrix = [["0"]]
print(maximalSquare(matrix))