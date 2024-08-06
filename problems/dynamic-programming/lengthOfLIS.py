# https://leetcode.com/problems/longest-increasing-subsequence/?envType=study-plan-v2&envId=top-interview-150
# 300. Longest Increasing Subsequence

# A classic DP problem with the binary search modification. 
# Iterate across nums. If its the largest you've seen, append to path. 
# Otherwise, find the largest index in path where path[idx] < num. 
# Put that number there. This method keeps track of the longest 
# subsequence since you replace numbers in the sequence with smaller ones
# so it's easier to find a number larger than its predecessor. 


from bisect import bisect_left

def lengthOfLIS(nums: list[int]) -> int:
    path = []
    for num in nums: 
        if not path or num > path[-1]:
            path.append(num)
        else: 
            idx = bisect_left(path, num)
            path[idx] = num
        
    return len(path)

x = [1,2,3,5]
idx = bisect_left(x, 4)
print(idx)


nums = [10,9,2,5,3,7,101,18]
nums = [0,1,0,3,2,3]
nums = [7,7,7,7,7,7,7]
print(lengthOfLIS(nums))