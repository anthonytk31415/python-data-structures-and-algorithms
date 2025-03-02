# here's the classic template

def f(nums, i, target): 
    return target <= nums[i] 

def binarySearch(nums, f, target): 
    left = -1
    right = len(nums)
    while right - left > 1: 
        mid = (left + right) // 2
        if f(nums, mid, target): 
            right = mid
        else: 
            left = mid        
    return right 

nums = [1,3, 6,7,10,14]
target = 11
print(binarySearch(nums, f, target))