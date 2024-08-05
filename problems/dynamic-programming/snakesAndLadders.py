from math import inf 

from functools import lru_cache

def snakesAndLadders(board):
    n = len(board)
    def get(i):
        idx = i - 1
        row = (n - 1) - (idx//n)
        col = idx % n
        if ((n % 2 == 1 and row % 2 == 1) or 
            (n % 2 == 0 and row % 2 == 0)): 
            col = (n - 1) - (idx % n)
        print("i: {}, row: {}, col: {}, board: {}".format(i, row, col, board[row][col]))
        return board[row][col]

    @lru_cache()
    def helper(i):     
        
        if i >= n**2: 
            print( "terminal state: i = ", i)
            return 0
        res = []
        for roll in range(1, 7):
            newCell = roll + i        
            if newCell >= n**2: return 1
            specialMove = get(newCell)
            print("i: {}, specialmove: {}".format(i, specialMove))
            if specialMove != -1: newCell = specialMove
            if newCell <= i: continue
            else: 
                res.append(1 + helper(newCell))
        if not res: return -1
        print("i: ", i, "res: ", res)
        return min(res)

    print(get(7))
    return helper(1)

        
# board = [[1,1,-1],[1,1,1],[-1,1,1]]


# board = [[-1,-1,-1,9,-1,-1],[-1,-1,10,7,-1,-1],[-1,-1,-1,-1,-1,20],[-1,14,-1,-1,15,20],[31,29,-1,-1,7,36],[-1,-1,-1,13,18,5]] # 1

board = [[-1,-1,-1,-1,48,5,-1],[12,29,13,9,-1,2,32],[-1,-1,21,7,-1,12,49],[42,37,21,40,-1,22,12],[42,-1,2,-1,-1,-1,6],[39,-1,35,-1,-1,39,-1],[-1,36,-1,-1,-1,-1,5]]

# board  = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]
print(snakesAndLadders(board))