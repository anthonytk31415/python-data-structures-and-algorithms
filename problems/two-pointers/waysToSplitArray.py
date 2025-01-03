# 2270. Number of Ways to Split Array
# https://leetcode.com/problems/number-of-ways-to-split-array/description/

# right = sum numbers
# traverse the nums list once again up to index n - 2
# add to left, substract from right. 
# check condition and add to a counter

# Time: O(n); Space O(1)

class Solution:
    def waysToSplitArray(self, nums: list[int]) -> int:
        right = sum(nums)
        left = 0
        counter = 0
        for i in range(len(nums) - 1): 
            left += nums[i]
            right -= nums[i]
            if left >= right: counter += 1
        return counter