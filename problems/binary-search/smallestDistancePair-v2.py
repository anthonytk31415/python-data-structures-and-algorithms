# https://leetcode.com/problems/find-k-th-smallest-pair-distance/?envType=daily-question&envId=2024-08-16
# 719. Find K-th Smallest Pair Distance

# binary search to find the smallest distance that has at least k pairs 
# use two pointers to find whether condition works

# O(nlogn) Time, O(1) space

def smallestDistancePair(nums, k):
    def checkCondition(nums, k, dist):
        count = 0
        left = 0
        for right in range(1, len(nums)):
            while left < right and abs(nums[right] - nums[left]) > dist: 
                left += 1
            if left < right: 
                count += right - left 
        return count >= k

    nums.sort()
    lower = 0
    upper = abs(nums[-1] - nums[0])
    while lower < upper:
        mid = (upper + lower) // 2
        if not checkCondition(nums, k, mid):
            lower = mid + 1
        else: 
            upper = mid
    return lower


nums = [1,3,1]
k = 1

# nums = [1,6,1]
# k = 3

# nums = [1,1,1]
# k = 2

nums = [1,10,100,1000]
k = 2

print(smallestDistancePair(nums, k))