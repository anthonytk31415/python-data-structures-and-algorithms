# https://leetcode.com/problems/next-greater-element-ii/description/
# 503. Next Greater Element II

# Keep a monotonic decreasing stack where the top is smallest. For each num in nums, 
# if stack[-1] is smaller than the num, that's the earliest next greater element. 
# You might have "unseen" elements so you do the loop again with the same stack. 
# But this time, you do not enqueue new elements into the stack. There should be one element
# left that is still -1, and that is the max.  


# O(n) time for running through nums twice and O(n) space for the stack

def nextGreaterElements(nums): 
    res = [-1] * len(nums)
    stack = []
    for i, num in enumerate(nums): 
        while stack and nums[stack[-1]] < nums[i]: 
            res[stack[-1]] = num
            stack.pop()         
        stack.append(i)

    for i, num in enumerate(nums): 
        while stack and nums[stack[-1]] < nums[i]: 
            res[stack[-1]] = num
            stack.pop()     
        
    return res


nums = [1,2,1]

nums = [5,8,6,1,3,2]

print(nextGreaterElements(nums))