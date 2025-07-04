# https://leetcode.com/problems/zero-array-transformation-i/?envType=company&envId=google&favoriteSlug=google-thirty-days
# 3355. Zero Array Transformation I

# a google problem

# use a diff array to update your diff_array in O(1) time. 
# make sure you do update on j + 1 -= 1. Think about why. 
# (you do this because it's after the fact that the diff drops)

# O(n) Time.
# O(n) Space.

from typing import List 


def get_diff_array(n, queries): 
    diff = [0]*n
    for i, j in queries: 
        diff[i] += 1
        if j + 1 < n: 
            diff[j+1] -= 1
    return diff

def is_valid(nums, diff): 
    tracker = 0
    for i in range(len(nums)): 
        tracker += diff[i]
        if nums[i] > tracker: 
            return False
    return True

class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        diff = get_diff_array(n, queries)
        return is_valid(nums, diff)