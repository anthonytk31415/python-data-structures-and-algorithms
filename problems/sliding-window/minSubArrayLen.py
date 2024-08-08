# https://leetcode.com/problems/minimum-size-subarray-sum/submissions/1104668131/?envType=study-plan-v2&envId=top-interview-150
# 209. Minimum Size Subarray Sum

# Sliding window. Time: O(n); Space: O(n)

from math import inf 

def minSubArrayLen(target, nums):

    res = inf
    left = 0
    curSum = 0
    for right in range(len(nums)):
        curSum += nums[right]
        while curSum - nums[left] >= target: 
            curSum -= nums[left]
            left += 1
        if curSum >= target: 
            res = min(res, right - left + 1)
    if res == inf: return 0
    return res


target = 7
nums = [2,3,1,2,4,3]

print(minSubArrayLen(target, nums))