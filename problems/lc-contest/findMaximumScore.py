# https://leetcode.com/contest/weekly-contest-414/problems/reach-end-of-array-with-max-score/

# O(n), O(1) problem


# dp version, O(n^2). TLE
def findMaximumScore1(nums: list[int]) -> int:
    dp = [0]*len(nums)
    for j in range(1, len(nums)):         
        res = 0
        for i in range(j): 
            curRes = dp[i] + (j-i)*nums[i]
            res = max(curRes, res)
        dp[j] = res
    return dp[-1]

from math import inf


# greedy - take the largest num
def findMaximumScore(nums: list[int]) -> int:
    maxNum = nums[0]
    score = 0
    for i in range(1, len(nums)): 
        score += maxNum
        maxNum = max(maxNum, nums[i])
    return score


nums = [1,3,1,5]
nums = [4,3,1,3,2]

print(findMaximumScore(nums))