from math import inf 

# https://leetcode.com/problems/dungeon-game/solutions/2303535/c-challenge-most-simple-intuitive/

# this problem is all about your base cases. 

# given the string matrix, return the val: int(val) or the string command
def getVal(i, j, matrix): 
    char = matrix[i][j]
    if char == "P" or char ==  "D": return char
    return int(char)

# given the cell (i, j) and the state of buffs (p, d), 
# return the value, newP, newD adjusted for buffs
def evalulateVal(i, j, p, d, matrix): 
    val = getVal(i, j, matrix)
    if val == "P": 
        return 0, 1, d
    elif val == "D": 
        return 0, p, 1
    elif val < 0: 
        if p == 1: 
            return 0, 0, d
        else: 
            return val, p, d
    elif val > 0 : 
        if d == 1: 
            return 2*val, p, 0
        else: 
            return val, p, d 
    
def dfs(i, j, p, d, matrix, dp):
    n, m = len(matrix), len(matrix[0])
    if i < 0 or i >= n or j < 0 or j >= m: return -inf

    val, newP, newD = evalulateVal(i, j, p, d, matrix) 
    # base case: 
    if i == n - 1 and j == m - 1:
        dp[i][j][p][d] = val
        return val 
    if dp[i][j][p][d] != -inf: 
        return dp[i][j][p][d]
    
    # now evaluate from your choices
    cand0 = val 
    cand1 = val + max(dfs(i+1, j, newP, newD, matrix, dp), dfs(i, j+1, newP, newD, matrix, dp))
    res = min(cand0, cand1) 
    dp[i][j][p][d] = res
    return res

def dungeon(matrix): 
    # p = 0, 1; d = 0 , 1
    n, m = len(matrix), len(matrix[0])
    dp = [[[ [-inf for _ in range(2)]for _ in range(2)]for _ in range(m+1)] for _ in range(n+1)] 
    res = dfs(0, 0, 0, 0, matrix, dp)
    # adjust neagive damage to appropriate health
    if res >= 0:        #
        return 1
    else: 
        res = -1 * res
        res += 1
        return res
# 8
matrix = [["-3", "D", "2"], 
          ["-2", "P", "-4"], 
          ["D", "-2", "-4"]
          ]

# 11
matrix = [["-4", "P", "-3", "D"], 
          ["D", "-1000", "-1000", "6"], 
          ["-4", "10", "-20", "-18"]
          ]


print(dungeon(matrix))




# path with min hp required is the path that maximizes heals 
# path with least damage required / highest hp recovery from (i, j) to (n-1, n-1)
def dfs(i, j, matrix, dp): 
    n, m = len(matrix), len(matrix[0])
    if i < 0 or i >= n or j < 0 or j >= m: return -inf          # if out of bounds return max dmg
    if i == n-1 and j == m-1: return matrix[i][j]               # base case
    if dp[i][j] != -inf: return dp[i][j]                        # recursive re-call
    cand0 = matrix[i][j]
    cand1 = matrix[i][j] + max(dfs(i+1, j, matrix, dp), dfs(i, j+1, matrix, dp))            # take the path with the least damage/highest hp recovery
    # Retain the smallest value the highest damage sustained; we keep track of most negative value, which will be our -health + 1 we need to maintain to keep hp at least 1; 
    # Heals in the recursive call will be carried back in the "past" to recover damage
    res = min(cand0, cand1)     # ensure you take the most negative one. 
    if res >= 0: res = 0        # cap delta at 0. can't overheal. 
    dp[i][j] = res
    return res

def dungeon_no_buffs(matrix): 
    print(matrix)
    n, m = len(matrix), len(matrix[0])
    dp = [[-inf for _ in range(m+1)] for _ in range(n+1)]
    res = dfs(0, 0, matrix, dp)
    if res >= 0:        #
        return 1
    else: 
        res = -1 * res
        res += 1
        return res



# matrix1 = [[-3, 4, 2], 
#           [-2, -3, -4], 
#           [1, -2, -4]
#           ]


# matrix = [["-3", "D", "2"], 
#           ["-2", "P", "-4"], 
#           ["D", "-2", "-4"]
#           ]

# print(dungeon(matrix))




