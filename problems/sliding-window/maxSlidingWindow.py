# https://leetcode.com/problems/sliding-window-maximum/description/
# 239. Sliding Window Maximum

from collections import deque 

# Implement monotonic deque. front is max element. 
# pop elements from top if top is smaller than current. 
# popleft element if index is out of range of window. 
# At each iteration, append the current max element. 


#O(n) TIme and space

def maxSlidingWindow(nums: list[int], k: int) -> list[int]:

    res = []
    q = deque()
    for i, num in enumerate(nums):
        while q and q[0] < i - k + 1: 
            q.popleft()
        while q and nums[q[-1]] < num: 
            q.pop()
        q.append(i)
        if i >= k - 1: 
            res.append(nums[q[0]])
    return res

nums = [1,3,-1,-3,5,3,6,7]
k = 3

print(maxSlidingWindow(nums, k))