
# constant space using two pointers; O(n log n) time 
def twoSum(nums, target): 
    nums.sort()
    left, right = 0, len(nums) - 1
    while left < right: 
        if nums[left] + nums[right] == target: return nums[left], nums[right]
        if nums[left] + nums[right] > target: right -= 1
        else: left += 1        
    return -1, -1

nums = [5,1,3,4,2,9, 8, 17]

print(twoSum(nums, 99))



