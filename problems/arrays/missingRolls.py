# https://leetcode.com/problems/find-missing-observations/
# 2028. Find Missing Observations

from math import floor

def missingRolls(rolls: list[int], mean: int, n: int) -> list[int]:
    m = len(rolls)
    r = sum(rolls)
    x = mean*(m + n) - r

    a = floor(x/n)
    res = [a]*n
    delta = x - a*n
    for i in range(len(res)): 
        curDelta = min(6 - res[i], delta) 
        res[i] += curDelta 
        delta -= curDelta 
        if delta == 0: break 

    return res


rolls = [3,2,4,3]
mean = 4
n = 2


rolls = [1,5,6]
mean = 3
n = 4

print(missingRolls(rolls, mean, n))