# https://leetcode.com/problems/reverse-pairs/description/
# 493. Reverse Pairs

from typing import List 
from bisect import bisect_left, insort


def condition(current_num, num): 
    return 2*num < current_num

def find_condition(ordered_nums, num): 
    left = -1
    right = len(ordered_nums)
    while right - left > 1: 
        mid = (left + right) // 2
        if condition(ordered_nums[mid], num): 
            right = mid
        else: 
            left = mid    
    return right

def reversePairs(nums): 
    count = 0
    ordered_nums = []
    for num in nums: 
        if not ordered_nums: 
            ordered_nums.append(num)
        else:
            idx = find_condition(ordered_nums, num)
            count += len(ordered_nums) - idx
            insort(ordered_nums, num)            
    return count

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        return reversePairs(nums)