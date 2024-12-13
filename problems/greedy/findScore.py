# 2593. Find Score of an Array After Marking All Elements
# https://leetcode.com/problems/find-score-of-an-array-after-marking-all-elements/

from heapq import heappush, heappop

# Greedy implementation. Create a new array of tuples with num and index pair. 
# Sort by num in ascending order.
# Also create a visited array. 
# Go through the array and if the num is not visited, add it to solution, mark the 
# num and its neighbors as visited. 

# O(nlogn) Time, Space O(n)

class Solution:
    def findScore(self, nums: list[int]) -> int:
        pq = [[num, i] for i, num in enumerate(nums)]
        pq.sort(key=lambda x: (x[0], x[1]))
        visited = [False for _ in range(len(nums))]
        res = 0
        for num, i in pq: 
            if visited[i] == False: 
                res += num
                visited[i] = True
                if i-1 >= 0: visited[i-1] = True
                if i+1 < len(nums): visited[i+1] = True
        return res