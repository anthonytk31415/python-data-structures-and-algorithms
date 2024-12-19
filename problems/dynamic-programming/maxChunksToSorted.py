from math import inf

# 769. Max Chunks To Make Sorted
# https://leetcode.com/problems/max-chunks-to-make-sorted

def isEqual(start, end, arr, sorted_arr): 
    return sorted(arr[start:end]) == sorted_arr[start:end]

def dp(start, end, memo, arr, sorted_arr):
    key = (start, end)
    if key in memo: return memo[key]
    res = -inf
    if isEqual(start, end, arr, sorted_arr): res = 1
    for mid in range(start+1, end): 
        curRes = dp(start, mid, memo, arr, sorted_arr) + dp(mid, end, memo, arr, sorted_arr)
        res = max(res, curRes)
    memo[key] = res    
    return res

class Solution:
    def maxChunksToSorted(self, arr: list[int]) -> int:
        n = len(arr)
        sorted_arr = sorted(arr)
        memo = {}
        res = dp(0, n, memo, arr, sorted_arr)
        return res