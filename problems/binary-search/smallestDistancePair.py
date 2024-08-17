
# https://leetcode.com/problems/find-k-th-smallest-pair-distance/?envType=daily-question&envId=2024-08-16
# 719. Find K-th Smallest Pair Distance

k = 3
arr = [1,5,2,7,3,8,10, 9, 12, 14, 15, 0, 3]
arr.sort()

def getPairsWithinK(arr, k):
    
    # 
    right = len(arr) - 1    # largest index where [i, right] <= k
    left = 1        # smallest index for with [i, left] <= k; dist = left - i
    for i in range(len(arr)):
        left = min(left, i+1)
        while left - i < k: left += 1
        right = max(right, left + 1)
        