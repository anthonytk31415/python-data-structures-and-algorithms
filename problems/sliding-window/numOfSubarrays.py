# https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/
# 1343. Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold

def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
    cSum = sum(arr[:(k-1)])
    res = 0
    for i in range(k-1, len(arr)):
        cSum += arr[i]
        if cSum / k >= threshold: 
            res += 1
        cSum -= arr[i - k + 1]
    return res