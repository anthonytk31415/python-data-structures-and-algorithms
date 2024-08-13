# https://leetcode.com/problems/valid-sudoku/description/?envType=study-plan-v2&envId=top-interview-150
# 36. Valid Sudoku

from collections import defaultdict, Counter

# super straightforward, broken up in pieces. 
def isValidSudoku1(board: list[list[str]]) -> bool:
    def checkRow(row):
        rowNums = Counter(row)
        # print(rowNums)
        for i in range(1, 10):
            num = str(i)
            if num not in rowNums or rowNums[num] == 1: continue
            else: 
                return False
        return True

    def getColumn(board, col):
        res = []
        for row in range(0, len(board)):
            res.append(board[row][col])

        return res

    def getBox(board, row, col):
        res = []
        for i in range(row, row + 3):
            for j in range(col, col + 3):
                res.append(board[i][j])
        return res
    for row in board:
        if not checkRow(row): return False
    for col in range(len(board[0])):
        if not checkRow(getColumn(board, col)): return False
    for row in range(0, len(board), 3):
        for col in range(0, len(board[0]), 3):
            if not checkRow(getBox(board, row, col)): return False            
    return True



def isValidSudoku(board: list[list[str]]) -> bool:
    rows, cols, box = defaultdict(Counter), defaultdict(Counter), defaultdict(Counter)

    for i in range(len(board)):
        for j in range(len(board[0])):
            num = board[i][j]
            if num == ".": continue
            if num in rows[i]: return False
            if num in cols[j]: return False
            if num in box[(i//3, j//3)]: return False
            rows[i][num] += 1
            cols[j][num] += 1
            box[(i//3, j//3)][num] += 1
    return True


# board = [["5","3",".",".","7",".",".",".","."]
#         ,["6",".",".","1","9","5",".",".","."]
#         ,[".","9","8",".",".",".",".","6","."]
#         ,["8",".",".",".","6",".",".",".","3"]
#         ,["4",".",".","8",".","3",".",".","1"]
#         ,["7",".",".",".","2",".",".",".","6"]
#         ,[".","6",".",".",".",".","2","8","."]
#         ,[".",".",".","4","1","9",".",".","5"]
#         ,[".",".",".",".","8",".",".","7","9"]]

board = [["8","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]


print(isValidSudoku(board))