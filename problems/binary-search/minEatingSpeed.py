# 875. Koko Eating Bananas
# https://leetcode.com/problems/koko-eating-bananas/description/

from math import ceil 

# Time: O(nlogn) for doing binary search on the entire pile of n elements logn times
# Space: O(1) for keeping track of bananas per hour

# Key: binary search the bananas per hour

def canFinishPiles(piles, bananasPerHour, h): 
    totalHours = sum([ceil(pile/bananasPerHour) for pile in piles])
    return totalHours <= h


class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        left = 0
        right = max(piles)
        while right - left > 1: 
            mid = (right + left) // 2
            if canFinishPiles(piles, mid, h): 
                right = mid
            else: 
                left = mid             
        return right