# matrix operations


def transpose(mat): 
    n, m = len(mat), len(mat[0])
    res = [[None for _ in range(n)] for _ in range(m)]
    for i in range(n):
        for j in range(m): 
            res[j][i] = mat[i][j]
    return res

mat = [[1,2,3], [4,5,6]]
matT = transpose(mat)
print(matT)