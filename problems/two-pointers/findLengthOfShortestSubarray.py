# https://leetcode.com/problems/shortest-subarray-to-be-removed-to-make-array-sorted/
# 1574. Shortest Subarray to be Removed to Make Array Sorted



# Approach: 
# - Invariant: your left and right ALWAYS makes a valid output. 
# - An optimization: we put smallest value, largest value on front, back of array, respective, 
#   as sentinel values so no matter what, your pointers will always point to something instead
#   of out of bounds

# - Push left pointer as far as you can to the right while the stuff prior to left is in order. 
#   Update your answer as if you deleted everything to the right of left. 
# - Then in a while loop, start at n - 1. If your right pointer is "valid" with left, 
#   update your solution as if you deleted all stuff between left and right.  
# - Then, see if you can do better. If you can push right to one right, and still maintain
#   sorted order on both left and right sides, then do it. 
#   Otherwise your curreft left cannot improve your answer. So move left - 1. 
# - Finally, return the min answer at each iteration

from math import inf

class Solution:
    def findLengthOfShortestSubarray(self, arr: list[int]) -> int:
        arr = [-inf] + arr + [inf]
        n = len(arr)
        left = 0
        right = n - 1
        
        # go farthest left
        while left + 1 < len(arr):
            if arr[left] <= arr[left+1]: left += 1
            else: break        
        if left == n - 1: return 0
        minRemovals = n - 1

        # for each left, try to move right towards left
        # invariant; your left and right is always valid 
        while left >= 0:         
            minRemovals = min(right - left - 1, minRemovals)    
            if arr[right - 1] <= arr[right] and arr[left] <= arr[right - 1]: right -= 1
            else: left -= 1
        return minRemovals



# 0 1 2  3  4 5 6 7 
# 1,2,3, 4, 5,x,x,x
# 1,2,3,10,11,4,5,6
# x,x,x, x, x,3,2,1

# at 3, get the smallest
# 1,2,3, 4,x,x,x,x
# 1,2,3,10,4,2,3,5
# x,x,x, x,x,3,2,1

# Time: O(n)
# Space: O(1)

# Test Cases: 
# arr = [1,2,3,10,11,4,5,6]
# ans = 2
# remove [10,11]

# arr = [1,2,3,3,3,3,3,3,3]
# ans = 0
# remove []


# arr = [10,2,3,3,3,3,3,3,3]
# ans = 1
# remove [10]

# arr = [1,2,10,3,4,3,3,3,3]
# ans = 3
# remove [10,3,4]