# https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/   
# 2962. Count Subarrays Where Max Element Appears at Least K Times

# O(n) Time
# O(1) Space 

# Sliding window solution. 
# start L = 0 and with R, iterate across nums. 
# Find the smallest window between L and R such that
# you have k max's. Then increment the result by the 
# length between 0 and L, which is L + 1

class Solution:
    def countSubarrays(self, nums: list[int], k: int) -> int:
        maxNums = max(nums)
        countMax = 0
        left = 0
        countSubarrays = 0
        for right in nums: 
            if right == maxNums: 
                countMax += 1
            while countMax >= k: 
                if countMax == k and nums[left] == maxNums: break
                if nums[left] == maxNums: countMax -= 1
                left += 1
            if countMax == k: 
                countSubarrays += left + 1
        return countSubarrays