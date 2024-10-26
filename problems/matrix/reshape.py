# https://leetcode.com/problems/reshape-the-matrix/
# 566. Reshape the Matrix

def getNext(u, v, r, c): 
    # get rows
    newU, newV = [None, None]
    if v+1 < c: 
        newV = v + 1
        newU = u
    else: 
        newV = 0
        if u + 1 < r: newU = u + 1
        else: newU = 0
    return [newU, newV]
    # get cols


class Solution:
    def matrixReshape(self, mat: list[list[int]], r: int, c: int) -> list[list[int]]:
        rows, cols = len(mat), len(mat[0])
        if rows*cols != r*c: return mat
        newMat = [[None for _ in range(c)] for _ in range(r)]
        u, v = 0, 0
        for i in range(rows):
            for j in range(cols): 
                newMat[u][v] = mat[i][j]
                u, v = getNext(u, v, r, c)

        return newMat