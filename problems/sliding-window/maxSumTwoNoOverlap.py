# https://leetcode.com/problems/maximum-sum-of-two-non-overlapping-subarrays/
# 1031. Maximum Sum of Two Non-Overlapping Subarrays

from math import inf

# Do Kadane for first going left, second going right. Then second going left, first going right. 
# Find max max of each i. 

def maxSumTwoNoOverlap(nums: list[int], firstLen: int, secondLen: int) -> int:

    # returns max left of subArray Sum at i of length k 
    def dp(nums, k):
        dp = [-inf]*len(nums)
        cSum = sum(nums[:(k-1)])
        for i in range(k-1, len(nums)):
            cSum += nums[i]
            if i == k-1: 
                dp[i] = max(dp[i], cSum)
            else: 
                dp[i] = max(dp[i-1], cSum)        
            cSum -= nums[i-k+1]
        return dp

    dp1L = dp(nums, firstLen)
    dp2L = dp(nums, secondLen)
    dp1R = dp(nums[::-1], firstLen)[::-1]
    dp2R = dp(nums[::-1], secondLen)[::-1]

    res = -inf
    for i in range(len(nums)-1):
        res = max(res, dp1L[i] + dp2R[i+1], dp2L[i] + dp1R[i+1])
        
    return res 

nums = [0,6,5,2,2,5,1,9,4]
firstLen = 1
secondLen = 2

nums = [3,8,1,3,2,1,8,9,0]
firstLen = 3
secondLen = 2
print(maxSumTwoNoOverlap(nums, firstLen, secondLen))