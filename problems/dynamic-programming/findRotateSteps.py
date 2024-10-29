from math import inf

# https://leetcode.com/problems/freedom-trail/description/
# 514. Freedom Trail


# DP. For each iteration, try all possible clockwise/counter-clockwise rotations and take the best one plus the 
# dfs at that ring position and the key position. 

# space: O(mn); time: O(mn)
def doRotation(i, j, ring, key, memo):
    res = inf
    for k in range(len(ring)): 
        new_j = int((j - k) % len(ring))
        if key[i] == ring[new_j]: 
            res = min(res, k + 1 + dfs(i+1, new_j, ring, key, memo)) 

        new_j = int((j + k) % len(ring))
        if key[i] == ring[new_j]: 
            res = min(res, k + 1 + dfs(i+1, new_j, ring, key, memo)) 
    return res

def dfs(i, j, ring, key, memo): 
    if (i, j) in memo: return memo[(i, j)] 
    if i >= len(key): return 0
    res = doRotation(i, j, ring, key, memo)
    memo[(i, j)] = res
    return res

class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        memo = {}
        return dfs(0, 0, ring, key , memo)