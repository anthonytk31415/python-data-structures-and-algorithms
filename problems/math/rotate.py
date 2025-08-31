# https://leetcode.com/problems/rotate-image/description/

# transpose, then reverse the matrix

def reverse(matrix): 
    for i in range(len(matrix)): 
        matrix[i] = matrix[i][::-1]

def transpose(matrix): 
    for i in range(len(matrix)): 
        for j in range(i + 1, len(matrix[0])): 
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]



def rotate(matrix): 
    transpose(matrix)
    reverse(matrix)
    