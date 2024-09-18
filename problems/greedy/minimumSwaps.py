
# https://leetcode.com/problems/minimum-adjacent-swaps-to-make-a-valid-array/description/?envType=company&envId=amazon&favoriteSlug=amazon-six-months
# 2340. Minimum Adjacent Swaps to Make a Valid Array

# Do a greedy swap. Take the smallest index that contains the min. Then swap. 
# Then take the largest index that contains the max. 
# Then swap. Doing one first vs the other makes no difference. 

from math import inf

def swap(nums, start, end): 
    if start == end: return nums
    delta = 1
    if start > end: delta = -1
    i = start
    while i != end: 
        j = i + delta
        nums[i], nums[j] = nums[j], nums[i]
        i += delta
    return nums


class Solution:
    def minimumSwaps(self, nums: list[int]) -> int:
        smallestIdx = 0
        minVal = inf
        for i, num in enumerate(nums):
            if num < minVal: 
                smallestIdx = i
                minVal = num
        res = smallestIdx    
        nums = swap(nums, smallestIdx, 0)
        largestIdx = 0
        maxVal = -inf
        for i, num in enumerate(nums):
            if num >= maxVal: 
                largestIdx = i
                maxVal = num        
        res += (len(nums) - 1 - largestIdx)
        return res
    
nums = [3,4,5,5,3,1]
# print(swap(nums, 5, 1))
s = Solution()
print(s.minimumSwaps(nums))

