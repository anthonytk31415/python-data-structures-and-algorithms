# https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/
# 1283. Find the Smallest Divisor Given a Threshold
from math import ceil

def smallestDivisor(nums: list[int], threshold: int) -> int:

    def condition(mid, nums, threshold): 
        curThreshold = sum([ceil(x/mid) for x in nums])             
        return curThreshold <= threshold
    
    low, high = 1, max(nums)
    while low < high: 
        mid = (low + high) // 2
        if not condition(mid, nums, threshold): 
            low = mid + 1
        else: 
            high = mid

    return low

nums = [1,2,5,9]
threshold = 6

nums = [44,22,33,11,1]
threshold = 5
print(smallestDivisor(nums, threshold))



# def generalBinarySearch(nums): 
#     low = minValueAllowed
#     high = maxValueAllowed
#     while low < high: 
#         mid = (high + low) // 2
#         if not condition(mid, nums): # condition is something that 
#                                      # satisfies the constraight of the problem
#             low = mid + 1 # require a larger value
#         else: 
#             high = mid # we found the largest allowable value to then cut in half
#     return low # low surpassed or is equal to high; return high 