# airbnb
# https://leetcode.com/problems/sort-integers-by-the-power-value/?envType=company&envId=airbnb&favoriteSlug=airbnb-more-than-six-months
# 1387. Sort Integers by The Power Value

# dp with memoization

def numSteps(x, memo):
    if x in memo: 
        return memo[x]
    if x == 1: return 0
    if x % 2 == 0: 
        res = 1 + numSteps(x//2, memo)
    else: 
        res = 1 + numSteps(3*x + 1, memo)
    memo[x] = res
    return res

class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        memo = {}
        nums = [(numSteps(x, memo), x) for x in range(lo, hi + 1)]
        nums.sort(key = lambda x: (x[0], x[1]))
        return nums[k-1][1]