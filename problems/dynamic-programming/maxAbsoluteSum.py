# https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/
# 1749. Maximum Absolute Sum of Any Subarray

# Another Kadane solution. 
# Time: O(n), Space: O(1)
# I used a cool trick to feed comparisons as inputs to helper functions

def longestStreak(nums, comparison): 
    overallLargest = 0
    curLargest = 0
    for num in nums: 
        curLargest = comparison([0, curLargest + num, num])
        overallLargest = comparison(overallLargest, curLargest)
    return overallLargest

class Solution:
    def maxAbsoluteSum(self, nums: list[int]) -> int:
        return max(abs(longestStreak(nums, max)), abs(longestStreak(nums, min)))


nums = [1,8,-7,20, -20,-26,2]
s = Solution()

# print(longestPos(nums))
# print(longestNeg(nums))
print(s.maxAbsoluteSum(nums))