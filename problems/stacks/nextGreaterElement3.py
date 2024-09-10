# https://leetcode.com/problems/next-greater-element-iii/description/
# 556. Next Greater Element III

from collections import deque 

# We use a Monotonic Deque and a Stack. 
# If all the digits are in descending order from left to right, then we cannot make the num smaller. 
# The goal is to increase the smallest digit whose digit value is smaller than its predecessor with the next
# larger number of our choices (or predecessors)

# Iterate from right to left of nums. Append elements to the deque when the ith element is larger than the top. 
# When we find the index of num that is smaller than the top: we change.  
# Keep a "smaller" stack that empties numbers from the deque's left until we find the smallest greater 
# than the ith number. That number is the new ith number. The next digits from i+1 onward are placed
# from the deque in ascending order. 

# O(n) for the num and stack traversal. Space and Time. 

def nextGreaterElement(n: int) -> int:
    nums = str(n)
    res = [x for x in nums]
    d, smaller = deque(), deque()
    for i in range(len(nums) - 1, -1, -1): 
        if not d or nums[d[-1]] <= nums[i]:             
            d.append(i)
        else: 
            # empty stack from the left and put in smaller until stack found an element that is larger
            while nums[d[0]] <= nums[i]: 
                smaller.append(d.popleft())
            res[i] = nums[d.popleft()]
            d.appendleft(i)
            # then pop from smaller, appendleft to the stack
            while smaller: 
                d.appendleft(smaller.pop())
            for k in range(i+1, len(res)): 
                res[k] = nums[d.popleft()]
            res = int("".join(res))
            if res > 2**31 - 1: return -1
            return res
    return -1

# n = 78876
n = 12345
# n = 54321
# n = 1111
# n = 99999
# n = 0
# n = 2147483486
#   2147483648
print(nextGreaterElement(n))