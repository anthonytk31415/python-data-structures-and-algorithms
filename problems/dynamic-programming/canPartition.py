# https://leetcode.com/problems/partition-equal-subset-sum/description/
# 416. Partition Equal Subset Sum

# You need to create all possible sumsof each number with each other. 
# Iterate across nums. Store each possible sum. Check after sum construction if target is in the set. 

# Time: O(n*targetSum), Space: O(targetSum)

def canPartition(nums):
    s = sum(nums)
    if s % 2 == 1: return False
    prevSums = set()
    target = int(s/2)
    for num in nums: 

        curSums = set()
        for x in prevSums: 
            curSums.add(x + num)
            curSums.add(x)
        curSums.add(num)
        if target in curSums: return True
        prevSums = curSums
    return False


nums = [1,5,11,5]
nums = [1,2,7,2]
# nums = [14,9,8,4,3,2]
# nums = [1,2,5,7,3,6,4]
print(canPartition(nums))