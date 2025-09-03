# https://leetcode.com/problems/set-matrix-zeroes/description/

def setZeroes(matrix): 
    m, n = len(matrix), len(matrix[0])    
    row0 = False

    # fill in first row/col with 0 but if it's the top row, just designate row0
    for i in range(m): 
        for j in range(n): 
            if matrix[i][j] == 0: 
                if i > 0: 
                    matrix[0][j] = 0
                    matrix[i][0] = 0
                if i == 0: 
                    row0 = True

    # fill in non-anchors
    for i in range(1, m): 
        for j in range(1, n): 
            if matrix[i][0] == 0 or matrix[0][j] == 0: 
                matrix[i][j] = 0

    # fill in anchors: Col
    if matrix[0][0] == 0: 
        for i in range(m): 
            matrix[i][0] = 0    
    
    # now fill in row
    if row0: 
        for j in range(n): 
            matrix[0][j] = 0 
