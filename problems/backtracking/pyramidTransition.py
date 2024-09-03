from collections import defaultdict

# https://leetcode.com/problems/pyramid-transition-matrix/description/?envType=problem-list-v2&envId=bit-manipulation
# 756. Pyramid Transition Matrix

# I solved this using backtracking. Kind of build a adj list.
# Time: O(allowed**bottom); Space: O(bottom**2)

# can you design this with bit manipulation? 

def pyramidTransition(bottom, allowed):

    lookup = defaultdict(list)
    for a in allowed: 
        lookup[a[0:2]].append(a[2])

    p = []
    for i in range(len(bottom)): 
        curBucket = [None]*(i + 1)
        p.append(curBucket)
    for i, x in enumerate(bottom): 
        p[len(bottom) - 1][i] = x

    def dfs(i, j): 
        if i == 0: return True
        cur = p[i][j] + p[i][j+1]
        if cur in lookup: 
            for x in lookup[cur]: 
                p[i-1][j] = x
                if j + 2 < len(p[i]): 
                    if dfs(i, j + 1): 
                        return True
                else: 
                    if dfs(i - 1, 0): 
                        return True
                p[i-1][j] = None    
        return False

    return dfs(len(bottom) - 1, 0)


# bottom = "BCD"
# allowed = ["BCC","CDE","CEA","FFF"]


bottom = "AAAA"
allowed = ["AAB","AAC","BCD","BBE","DEF"]

print(pyramidTransition(bottom, allowed))