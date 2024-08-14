# https://leetcode.com/problems/smallest-range-ii/description/
# 910. Smallest Range II

# Cause there are two segments (A[0]+K, A[1]+K, ..., A[i]+K, A[i+1]-K, ..., A[n]-K), 
# the first one is on the left of the current point (A[i] + K is the last element of 
# the first segment), the second one is on the right of the current point (A[i + 1] - K 
# is the first element of the second segment). For the first segment, the smallest element 
# is left, the largest is A[i] + K; For the second segment, A[i + 1] - K is the smallest 
# element, the largest is right. Thus, for each point, the largest element should be either 
# A[i] + K or right, the smallest element should be either left or A[i + 1] - K


from math import inf 
def smallestRangeII1(nums, k):

    

    dpp, dpm = [[0,0] for _ in range(len(nums))], [[0,0] for _ in range(len(nums))]# dp[i] = [max, min]
    # print(dpp, dpm)
    dpp[0], dpm[0] = [nums[0] + k, nums[0] + k], [nums[0] - k, nums[0] - k]


    # x = nums[i] + k, or nums[i] - k
    def defineDp(x, i, dpp, dpm):
        if abs(max(x, dpp[i-1][0]) - min(x, dpp[i-1][1])) < abs(max(x, dpm[i-1][0]) - min(x, dpm[i-1][1])): 
            return [max(x, dpp[i-1][0]), min(x, dpp[i-1][1])]
        else: 
            return [max(x, dpm[i-1][0]), min(x, dpm[i-1][1])]


    for i in range(1, len(nums)): 
        dpp[i] = defineDp(nums[i] + k, i, dpp, dpm)
        dpm[i] = defineDp(nums[i] - k, i, dpp, dpm)


    x, y = dpp[-1]
    u, v = dpm[-1]
    print(dpp, dpm)

    return min(abs(x - y), abs(u - v))



def smallestRangeII(nums, k):
    nums.sort()
    res = nums[-1] - nums[0]
    for i in range(1, len(nums)-1):
        big = max(nums[-1], nums[i] + 2*k)
        small = min(nums[i+1], nums[0] + 2*k)
        res = min(res, big - small)
    return res

# nums = [1,3,6]
# k = 3

nums = [0,10]
k = 2
nums = [1]
k = 0


nums = [1,5,7,4,12]
k = 3

nums = [9,10,5,9]
k = 5

print(smallestRangeII(nums, k))