# https://leetcode.com/problems/minimum-moves-to-make-array-complementary/?envType=problem-list-v2&envId=mzw3cyy6
# 1674. Minimum Moves to Make Array Complementary

from math import inf
from collections import Counter

# a very complex Line Sweep problem. O(n) time and space. 

# For a target t, 
# min moves to hit t = n - {(1) pairs that require only 1 change} - {(2) pairs that require zero changes} 
# n = you change everything: maximum moves

# Notes: 
# - for pair x, y: 
# - If your pair is a "zero" (i.e. you require zero chanegs), you are in the (1) bucket as well
# Here are the possible conditions for a given t: 
# - if min(x, y) + 1 > target, you need to make 2 changes. Why? the LHS is the smallest possible value after 1 change and is too big to hit target. So you need to make 2 changes. 
# - if max(x, y) + limit < target, you need to make 2 changes. Why: the LHS is the largest possible value after 1 change and is too small. 
# - anything else is a 1-change (you're in the (1) bucket) 

# Iterate across all possible values of t that are attainable. 


def minMoves(nums: list[int], limit: int) -> int:
    n = len(nums)
    start, end, zeroes = Counter(), Counter(), Counter()

    for i in range(n//2):
        x, y = nums[i], nums[n - 1 - i]
        zeroes[x+y] += 1
        start[min(x, y) + 1] += 1
        end[max(x, y) + limit] += 1        
    minMoves = inf 
    intervals = 0
    for t in range(2, 2*limit + 1):
        intervals += start[t]
        curCost = n - intervals - zeroes[t]
        intervals -= end[t]
        minMoves = min(minMoves, curCost)
    return minMoves

nums = [1,2,2,1]
limit = 2

nums = [1,2,1,2]
limit = 2

nums = [100, 100, 100, 100]
limit = 100

print(minMoves(nums, limit))


