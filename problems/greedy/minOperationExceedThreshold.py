# 3066. Minimum Operations to Exceed Threshold Value II
# https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-ii/description/?envType=daily-question&envId=2025-02-15

# Use a heap
# Time: O(nlogn) implementation
# Space: O(1) since we use the existing nums again. 

from heapq import heapify, heappop, heappush

def doOperation(nums): 
    a, b = heappop(nums), heappop(nums)
    x = 2*a + b
    heappush(nums, x)


class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        heapify(nums)
        counter = 0
        while nums[0] < k: 
            doOperation(nums)
            counter += 1
        return counter