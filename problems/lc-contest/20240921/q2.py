from bisect import bisect_left
# https://leetcode.com/problems/minimum-number-of-seconds-to-make-mountain-height-zero/description/
# 3296. Minimum Number of Seconds to Make Mountain Height Zero

# binary search twice. 

# returns whether mid is sufficinet time 

# Find the largest height you can take given the max time you can take

def firstNTerms(n): 
    return n*(n+1)// 2

# def findMaxHeight(workerTime, maxTime, mountainHeight):
#     left = 0
#     right = mountainHeight
#     while left <= right:        # terminal: [3, 2] 
#         mid = (left + right) // 2
#         arithSum = firstNTerms(mid)
#         if arithSum * workerTime == maxTime: 
#             return mid
#         if arithSum* workerTime < maxTime: 
#             left = mid + 1
#         else: 
#             right = mid - 1
#     return right

# equivalent
# def findMaxHeight(workerTime, maxTime, mountainHeight):
#     left = -1
#     right = mountainHeight + 1
#     while right - left > 1:        # terminal: [3, 2] 
#         mid = (left + right) // 2
#         arithSum = firstNTerms(mid)
#         if arithSum* workerTime <= maxTime: 
#             left = mid
#         else: 
#             right = mid
#     return left


def findMaxHeight(workerTime, maxTime, mountainHeight):
    left = -1
    right = mountainHeight + 1
    while right - left > 1:        # terminal: [3, 2] 
        mid = (left + right) // 2
        arithSum = firstNTerms(mid)
        if arithSum* workerTime > maxTime: 
            right = mid
        else: 
            left = mid
    return left

print("findMaxHeight: ", findMaxHeight(2, 2, 3))        # 1
# print("findMaxHeight: ", findMaxHeight(1, 1, 4))      # should return 1
print("findMaxHeight: ", findMaxHeight(1, 5, 5))        # max height is 2, i.e. you can take 2 terms; with 5 seconds you cant do more than 2: 1*(1 + 2) = 3; 1*(1 + 2+ 3) = 6 which is > 5
# print("findMaxHeight: ", findMaxHeight(3, 17, 5))        # 2
# print("findMaxHeight: ", findMaxHeight(3, 18, 5))        # 3
# with time = 2, max height is 3
# mid = 1, low = 0, high = 3 
# 0, 0, 1


def cond(time, nums, mountainHeight): 
    height = 0
    # for each num in arr, whats the largest height you can take?
    for workerTime in nums: 
        height += findMaxHeight(workerTime, time, mountainHeight)
    # print("time: {}, ht: {}, mtnHt: {}".format(time, height, mountainHeight))
    return height >= mountainHeight

def minNumberOfSeconds(mountainHeight: int, workerTimes: list[int]) -> int:
    # workerTimes.sort()
    left = -1
    right = max(workerTimes)*firstNTerms(mountainHeight) + 1      # review this condition
    while right - left > 1: # terminal condition: [3, 2]
        mid = (left + right) // 2
        condit = cond(mid, workerTimes, mountainHeight)
        # print(left, mid, right, condit)
        if condit: 
            right = mid 
        else: 
            left = mid 
    return right

# r - l > 1
# - l > 1 - r
# l < -1 + r
# l + 1 < r
mountainHeight = 4
workerTimes = [2,1,1] # 
# 3

mountainHeight = 10
workerTimes = [3,2,2,4]
# 12

# 1, 2, 2, 1 with 11 seconds
# 2, 3, 3, 2 --> 12 secondsx

# print("result: ", minNumberOfSeconds(mountainHeight, workerTimes))