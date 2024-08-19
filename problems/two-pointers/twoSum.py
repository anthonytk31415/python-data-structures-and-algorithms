# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/?envType=study-plan-v2&envId=top-interview-150
# 167. Two Sum II - Input Array Is Sorted

def twoSum(numbers: list[int], target: int) -> list[int]:
    nums = numbers
    left, right = 0, len(nums) - 1

    while left < right: 
        curSum = nums[left] + nums[right]
        if curSum == target: return [left + 1, 1 + right]
        elif curSum > target: right -= 1
        else: left += 1
    
numbers = [2,7,11,15, 17, 23]
target = 22

print(twoSum(numbers, target))