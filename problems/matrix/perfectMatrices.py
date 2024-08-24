# Perfect Cross: 
# Codesignal 


# given i, j, return whether all elements are equal except for the jth entry
def rowCheck(i, j, row):
    for y in range(1, len(row)): 
        if row[y] != row[y-1]: return False
    return row[0]

def getRow(i, j, mat): 
    row = mat[i][:j] + mat[i][j+1:] 
    # print(i, j, row)
    return row

def getCol(i, j, mat): 
    col = []
    for u in range(len(mat)): 
        if u == i: continue
        col.append(mat[u][j])
    return col

def buildRowsCheck(mat): 
    n, m = len(mat), len(mat[0])
    res = [[None for _ in range(m)] for _ in range(n)]
    for i in range(n): 
        for j in range(m):
            row = getRow(i, j, mat)
            res[i][j] = rowCheck(i, j, row)
    return res

def buildColsCheck(mat): 
    n, m = len(mat), len(mat[0])
    res = [[None for _ in range(m)] for _ in range(n)]
    for i in range(n): 
        for j in range(m):
            col = getCol(i, j, mat)
            res[i][j] = rowCheck(i, j, col)
    return res

def getNumPerfectCross(mat): 
    rowCheck = buildRowsCheck(mat)
    colCheck = buildColsCheck(mat)
    n, m = len(mat), len(mat[0])
    count = 0
    for i in range(n): 
        for j in range(m):
            rc, cc = rowCheck[i][j], colCheck[i][j]
            if rc != False and cc != False and rc == cc: 
                count += 1
    return count


mat = [[1,1,1,1], 
[2,1,1,1],
[1,1,1,0], 
[1,0,1,1]
]

for x in mat: 
    print(x)


print(getNumPerfectCross(mat))