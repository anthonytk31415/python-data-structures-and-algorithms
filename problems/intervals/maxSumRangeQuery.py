# https://leetcode.com/problems/maximum-sum-obtained-of-any-permutation/?envType=problem-list-v2&envId=mzw3cyy6
# 1589. Maximum Sum Obtained of Any Permutation

from collections import Counter

# Sweep Line 
# O(nLogn) for sorting, O(n) Space for count frequency storing 

def maxSumRangeQuery(nums: list[int], requests: list[list[int]]) -> int:
    starts, ends = Counter(), Counter()
    for s, e in requests: 
        starts[s] += 1
        ends[e] += 1
    countIndex = [0]*len(nums)
    count = 0 
    for i in range(len(nums)):
        count += starts[i]
        countIndex[i] = count 
        count -= ends[i]
    countIndex.sort()
    nums.sort()
    res = 0
    for i in range(len(countIndex)):
        res += nums[i] * countIndex[i]
    return res

nums = [1,2,3,4,5]
requests = [[1,3],[0,1]]

nums = [1,2,3,4,5,6]
requests = [[0,1]]
print(maxSumRangeQuery(nums, requests))
