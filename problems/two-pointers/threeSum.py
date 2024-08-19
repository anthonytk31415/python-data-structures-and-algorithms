# https://leetcode.com/problems/3sum/description/?envType=study-plan-v2&envId=top-interview-150
# 15. 3Sum


# Time: O(n^2)
# Space: O(1)
# Sort. For each num, do two pointers just like 2Sum. 
# For optimization, if num == prev num, skip. 


def threeSum(nums):
    nums.sort()
    n = len(nums)
    res = set()
    for k in range(len(nums)):
        if k > 0 and nums[k] == nums[k-1]: continue            
        if k == 0: 
            left, right  = 1, n - 1
        elif k == n - 1: 
            left, right = 0, n - 2 
        else: 
            left, right = 0, n - 1 

        while left < right: 
            curSum = nums[left] + nums[right] + nums[k]
            if curSum == 0:
                curRes = [nums[k], nums[left], nums[right]]
                curRes.sort() 
                res.add(tuple(curRes)) 
            if curSum <= 0: 
                left += 1
                if left == k: left += 1
            else: 
                right -= 1
                if right == k: right -= 1
    return res

nums = [-1,0,1,2,-1,-4]
print(threeSum(nums))