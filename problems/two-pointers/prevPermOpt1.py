# https://leetcode.com/problems/previous-permutation-with-one-swap/
# 1053. Previous Permutation With One Swap

# Two pointers
# Time: O(n); space: O(1)

# Find first index of arr from right to left it is not in descending order.
def find_break(arr): 
    for i in range(len(arr)-2, -1, -1): 
        if arr[i] > arr[i+1]: return i
    return -1

# Find the index of the largest number smaller than the break_index. 
# Ensure this index is the also the largest from left to right if 
# adjacent indices are equal. 
def find_largest(arr, break_idx): 
    res_idx = break_idx + 1
    for i in range(break_idx + 2, len(arr)): 
        if arr[i] > arr[res_idx] and arr[i] < arr[break_idx]: res_idx = i
    return res_idx

class Solution:
    def prevPermOpt1(self, arr: list[int]) -> list[int]:        
        break_idx = find_break(arr)
        if break_idx == -1: return arr
        largest_idx = find_largest(arr, break_idx)
        arr[break_idx], arr[largest_idx] = arr[largest_idx], arr[break_idx]
        return arr
        