# https://leetcode.com/problems/subarray-sum-equals-k/description/
# 560. Subarray Sum Equals K

from collections import Counter

# O(n) time and space

# For the jth itereation, how do you check all of the prefix[i,j] 
# for all i <= j in constant time? Use a hashmap and take the 
# difference of current total Prefix. At end of check, add prefix to 
# hash map. 


def subarraySum(nums: list[int], k: int) -> int:
    prefix = Counter() # prefix, count
    prefix[0] += 1
    cSum = 0
    totalSum = 0
    for num in nums: 
        cSum += num
        if cSum - k in prefix: 
            totalSum += prefix[cSum - k]
        prefix[cSum] += 1
    return totalSum


nums = [1,1,1]
k = 2

# nums = [1,2,3]
# k = 3


# nums = [1,5,2,7,8]
# k = 7

# nums = [1]
# k = 0
print(subarraySum(nums, k))