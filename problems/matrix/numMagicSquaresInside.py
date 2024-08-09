# https://leetcode.com/problems/magic-squares-in-grid/
# 840. Magic Squares In Grid


def numMagicSquaresInside(grid: list[list[int]]) -> int:
    def sumRow(row):
        return sum(row)
    
    #return 1x3 row
    def getColumn(grid, startR, endR, col):
        res = []
        for row in range(startR, endR + 1):
            res.append(grid[row][col])
        return res

    def downRightDiag(grid, upperLeftRow, upperLeftCol):
        return [grid[upperLeftRow][upperLeftCol], grid[upperLeftRow + 1][upperLeftCol + 1], grid[upperLeftRow + 2][upperLeftCol + 2]]

    def downLeftDiag(grid, upperRightRow, upperRightCol):
        return  [grid[upperRightRow][upperRightCol], grid[upperRightRow + 1][upperRightCol - 1], grid[upperRightRow + 2][upperRightCol - 2]]
    
    def getSquare(grid, row, col):
        res = []
        for i in range(row, row + 3):
            rowRes = grid[i][col:(col + 3)]
            res.append(rowRes)
        return res

    def check3square(square):
        sqSum = sumRow(square[0])
        for i in range(1, 3):
            if sumRow(square[i]) != sqSum: 
                print('row:', square[i])
                return False
        
        for j in range(0, 3):
            row = getColumn(square, 0, 2, j)
            if sumRow(row) != sqSum: 
                print('col:', row)
                return False
        
        diag1, diag2 = downRightDiag(square, 0, 0), downLeftDiag(square, 0, 2)
        for row in [diag1, diag2]: 
            if sumRow(row) != sqSum: 
                print('diag', row)
                return False
        return True
    
    def verifyElements(square):
        nums = set()
        for i in range(len(square)):
            for j in range(len(square[0])):
                nums.add(square[i][j])
        for i in range(1, 10):
            if i not in nums: 
                # print("invalid square")
                return False
        return True


    res = 0
    for i in range(len(grid)):
        if i + 2 >= len(grid): break         
        for j in range(len(grid[0])):
            if j + 2 >= len(grid[0]): break 
            square = getSquare(grid, i, j)
            print("grid at i: {}, j: {}, square: {}".format(i, j, square))
            if verifyElements(square) and check3square(square): 
                res += 1             
    return res


grid = [[4,3,8,4],[9,5,1,9],[2,7,6,2]]



grid = [[3,2,9,2,7],[6,1,8,4,2],[7,5,3,2,7],[2,9,4,9,6],[4,3,8,2,5]]

print(numMagicSquaresInside(grid))




# print(getSquare(grid, 0, 1))
