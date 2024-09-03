from bisect import bisect_left

# // https://leetcode.com/problems/find-the-distance-value-between-two-arrays/description/
# // 1385. Find the Distance Value Between Two Arrays

def findTheDistanceValue(arr1: list[int], arr2: list[int], d: int) -> int:

    arr1.sort()
    arr2.sort()
    res = 0
    for n1 in arr1: 
        isValidNum = True
        for x in [n1 - d, n1 + d]: 
            idx = bisect_left(arr2, x)
            for i in [idx-1, idx]: 
                if i >= 0 and abs(arr2[i] - n1) <= d: 
                    isValidNum = False
                    break
        if isValidNum: 
            res += 1
    return res