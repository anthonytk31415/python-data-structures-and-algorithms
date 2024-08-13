def rotate1(matrix: list[list[int]]) -> None:
    m = matrix
    n = len(matrix)
    for i in range(0, n//2):
        for j in range(0, n//2):
            m[i][j], m[j][n-1-i], m[n-1-i][n-j-1], m[n-1-j][i] = m[n-1-j][i], m[i][j], m[j][n-1-i], m[n-1-i][n-j-1]

    
    if n % 2 == 1: 
        i = n // 2
        for j in range(0, n // 2):
            m[i][j], m[j][i], m[i][n-1-j], m[n-1-j][i] = m[n-1-j][i], m[i][j], m[j][i], m[i][n-1-j]



def rotate(matrix: list[list[int]]) -> None:
    
    matrix[:] = matrix[::-1]

    # row-symmetry
    # for i in range(len(matrix)//2):
    #     matrix[i], matrix[len(matrix) -1 - i] = matrix[len(matrix) - 1 - i], matrix[i]

    # reflect across downsloping diagonal symmetry
    for i in range(len(matrix)):
        for j in range (i + 1, len(matrix[0])):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # --> net effect: rotation 90' clockwise    

    
# matrix = [[1,2,3],[4,5,6],[7,8,9]]
matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
rotate(matrix)
print(matrix)