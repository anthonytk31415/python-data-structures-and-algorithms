from collections import Counter

def subarraysWithKDistinct(nums: list[int], k: int) -> int:

    midCounter, leftCounter =  Counter(), Counter()
    left = mid = 0
    count = 0
    for right, num in enumerate(nums): 
        midCounter[num] += 1
        leftCounter[num] += 1
        
        # 

        while len(leftCounter) > k and left <= right: 
            leftCounter[nums[left]] -= 1
            if leftCounter[nums[left]] == 0: del leftCounter[nums[left]]
            left += 1

        while len(midCounter) > k and mid <= right: 
            midCounter[nums[mid]] -= 1
            if midCounter[nums[mid]] == 0: del midCounter[nums[mid]]
            mid += 1

        while len(midCounter) == k and mid <= right and midCounter[nums[mid]] > 1: 
            midCounter[nums[mid]] -= 1
            if midCounter[nums[mid]] == 0: del midCounter[nums[mid]]
            mid += 1
        
        if len(midCounter) == k: 
            count += mid - left + 1
    return count

nums = [1,2,1,2,3]
k = 2
nums = [1,2,1,3,4]
k = 3

print(subarraysWithKDistinct(nums, k))
