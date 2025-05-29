# https://leetcode.com/problems/flip-game-ii/description  
# 294. Flip Game II

# Must do a top down dp approach and run through all the states of the currentState 
# to see if you can do amove. Basically you dfs every possible move you can make. 
# If you can do a move and the dfs(new_move) is False, then you win. 
# So each round try all moves to see if you can force your opponent can lose. 
# dfs(state) returns basically if you can win at that state. 

# Time: O(2**n) for going through each state
# Space: O(2**n) for storing the possible states.

# pretty fun dp prob..
def canWin(currentState): 
    memo = {}    
    
    def do_move(state, i): 
        return state[:i] + "--" + state[i+2:]
    
    def dfs(state): 
        if state in memo: return memo[state]
        res = False

        for i in range(len(state) - 1): 
            if state[i:i+2] == "++": 
                if dfs(do_move(state, i)) == False: 
                    res = True
                    break         
        memo[state] = res
        return res
    
    return dfs(currentState)