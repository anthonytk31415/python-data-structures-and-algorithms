# Q1
from collections import deque

# def resultsArray(nums, k):
#     n = len(nums)
#     res = []

#     for i in range(n - k + 1):
#         curArr = nums[i:(i+k)]
#         toSort = [x for x in curArr]
#         toSort.sort()
#         fail = False
#         print(curArr, toSort)
#         for j in range(len(curArr)):
#             if curArr[j] != toSort[j]: 
#                 fail = True
#                 break
#             elif j > 0 and curArr[j] != curArr[j-1] + 1: 
#                 fail = True
#                 break        
#         # print(fail, j)
#         if fail: 
#             res.append(-1)
#         else: 
#             res.append(max(curArr))

#     return res

# https://leetcode.com/contest/biweekly-contest-137/problems/find-the-power-of-k-size-subarrays-ii/submissions/1359119792/
# Find the Power of K-Size Subarrays II



def resultsArray(nums, k):
    def isLastKSorted(nums, k):
        res = []
        d = deque()
        for i, num in enumerate(nums):
            while d and d[0] < i - k + 1: 
                d.popleft()        
            while d and nums[d[-1]] > num: 
                d.pop()
            d.append(i)
            if i >= k - 1:
                if len(d) == k:  
                    res.append(True)
                else: 
                    res.append(False)
        return res

    def getMaxLastK(nums, k):
        maxLastK = []
        d = deque()
        for i, num in enumerate(nums):
            while d and d[0] < i - k + 1: 
                d.popleft()        
            while d and nums[d[-1]] < num: 
                d.pop()
            d.append(i)
            if i >= k - 1: 
                maxLastK.append(nums[d[0]])
        return maxLastK

    def isLastKConsecutive(nums, k):
        res = []
        d = deque()
        for i, num in enumerate(nums):
            while d and d[0] < i - k + 1: 
                d.popleft()        
            if d and num != nums[d[-1]] + 1: 
                d = deque()            
            d.append(i)
            if i >= k - 1:
                if len(d) == k: 
                    res.append(True)
                else: 
                    res.append(False)
        return res

    maxK = getMaxLastK(nums, k)
    consec = isLastKConsecutive(nums, k)
    ksorted = isLastKSorted(nums, k)

    res = []
    for i in range(len(maxK)):
        curRes = -1
        if consec[i] and ksorted[i]: curRes = maxK[i] 
        res.append(curRes)
    return res


nums = [1,2,3,4,3,2,5]
k = 3

# nums = [2,2,2,2,2]
# k = 4
# nums = [3,2,3,2,3,2]
# k = 2


# print("get last k: ", getMaxLastK(nums, k))
# print("last k consec:", isLastKConsecutive(nums, k))
# print("is last k sorted:", isLastKSorted(nums, k))

print(resultsArray(nums, k))

