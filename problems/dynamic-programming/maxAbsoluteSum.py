# https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/
# 1749. Maximum Absolute Sum of Any Subarray

# Another Kadane solution. 
# Time: O(n), Space: O(1)



def longestPos(nums): 
    maxPos = 0
    curPos = 0
    for num in nums: 
        curPos = max([0, curPos + num, num])
        maxPos = max(maxPos, curPos)
    return maxPos

def longestNeg(nums): 
    minNeg = 0
    curNeg = 0
    for num in nums: 
        curNeg = min([0, curNeg + num, num])
        minNeg = min(minNeg, curNeg)
    return minNeg

class Solution:
    def maxAbsoluteSum(self, nums: list[int]) -> int:
        return max(abs(longestNeg(nums)), abs(longestPos(nums)))


nums = [1,8,-7,20, -20,-26,2]
s = Solution()

print(longestPos(nums))
print(longestNeg(nums))
print(s.maxAbsoluteSum(nums))