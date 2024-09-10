# https://leetcode.com/problems/jump-game-iii/
# 1306. Jump Game III

from functools import lru_cache

# dfs a node. don't revisit if you got there

def canReach(arr, start): 
    visited = [None] * len(arr)

    def dfs(i): 
        # print(i)
        if visited[i] != None: return visited[i]
        visited[i] = False
        res = False
        if arr[i] == 0: res = True
        else: 
            for j in [i - arr[i], i + arr[i]]: 
                if 0 <= j < len(arr) and visited[j] == None: 
                    res = res or dfs(j)    
        visited[i] = res
        return res 
    return dfs(start)


arr = [4,2,3,0,3,1,2]
start = 5

arr = [4,2,3,0,3,1,2]
start = 0


arr = [3,0,2,1,2]
start = 2

print(canReach(arr, start))