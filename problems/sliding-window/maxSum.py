# 2841. Maximum Sum of Almost Unique Subarray
# https://leetcode.com/problems/maximum-sum-of-almost-unique-subarray/description/

# Sliding window. Insert from kth element, check condition, evict last in window. 
# Time O(n), Space (k)

from collections import Counter

def maxSum(nums, m, k):
    counter = Counter(nums[:(k-1)])
    cSum = sum(nums[:(k-1)])

    res = 0
    for i in range(k-1, len(nums)):
        counter[nums[i]] += 1
        cSum += nums[i]
        if len(counter) >= m: 
            res = max(res, cSum)        
        last = i - k + 1
        counter[nums[last]] -= 1
        if counter[nums[last]] == 0: del counter[nums[last]]
        cSum -= nums[last]
    return res

nums = [2,6,7,3,1,7]
m = 3
k = 4

nums = [5,9,9,2,4,5,4]
m = 1
k = 3

print(maxSum(nums, m, k))