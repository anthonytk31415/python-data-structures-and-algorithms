

# https://leetcode.com/problems/number-of-longest-increasing-subsequence/description/
# 673. Number of Longest Increasing Subsequence

from bisect import bisect_left
from collections import defaultdict



# Use the binary search technique to fill in path (as in pathLIS), but this time, each position in path is a list, which keeps track of possible elements in 
# a LIS. When you insert in the path, keep track of its number of predecessors. The length of the path is your length of LIS, and at each path[i], you have candidates for predessors. 
# If the parent candidate is smaller than the current num (since when you traverse the nums, if you found a number smaller than the older one, you place it above so its possible you have parent
# candidates that are larger than the current), add the parent's paths to your current num, which gives you numpaths for that node. 
# At the end, for each element in paths[-1], the sum of these paths is your answer. 


def findNumberOfLIS(nums: list[int]) -> int:
    path, numPaths = [], defaultdict(list)
    for i, num in enumerate(nums): 
        if not path or num > nums[path[-1][-1]]:
            if not path: 
                numPaths[i] = 1
            else: 
                numPaths[i] = sum([numPaths[j] for j in path[-1] if nums[j] < num])
            path.append([i])
        else: 
            idx = bisect_left(path, num, key = lambda x: nums[x[-1]])
            if idx > 0: numPaths[i] = sum([numPaths[j] for j in path[idx - 1] if nums[j] < num])
            else: numPaths[i] = 1
            path[idx].append(i)
    res = 0
    for node in path[-1]:
        res += numPaths[node]
    return res


# x = []
# print(len(x), not x )

# nums = [1,3,2,7,6,10,5,11]
# nums = [1]

nums = [1,2,4,3,5,4,7,2] # 3

print(findNumberOfLIS(nums))



# You could use a variation of this to actually find and trace the many paths. Here we keep track of its actual parents. 
def findNumberOfLIS1(nums: list[int]) -> int:
    path = []
    parent = defaultdict(list)
    for i, num in enumerate(nums): 
        # print(num, path)
        if not path or num > nums[path[-1][-1]]:
            if not path: 
                parent[i] = []
            else: 
                parent[i] = [x for x in path[-1]]
            path.append([i])
        else: 
            idx = bisect_left(path, num, key = lambda x: nums[x[-1]])
            if idx > 0: 
                parent[i] = [x for x in path[idx - 1]]
            else: 
                parent[i] = []
            path[idx].append(i)

    # print(path, parent)
    memo = {}
    def dfs(node): 
        if node in memo: return memo[node]
        if not parent[node]: return 1 
        res = 0
        for child in parent[node]:
            if nums[child] < nums[node]:
                res += dfs(child)
        memo[node] = res
        return res

    res = 0
    for node in path[-1]:
        res += dfs(node)
    return res
