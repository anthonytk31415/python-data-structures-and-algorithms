
# Using prefix sum: if prefix[j] - prefix[i] is between [lower, upper] then you have a valid range. 
# We work backwards: for each prefix[j], iterate over target = range(lower, upper+1). Check if 
# prefix - target = otherPrefix is in cSums. 

from collections import Counter


# this is too slow because we have to iterate across all targets.  
def countRangeSum(nums: list[int], lower: int, upper: int) -> int:
    count = 0
    prefixs = [0] + [x for x in nums]   
    cSums = Counter()
    for i in range(1, len(prefixs)):
        prefixs[i] = prefixs[i] + prefixs[i-1]
    for prefix in prefixs: 
        for target in range(lower, upper + 1): 
            if prefix - target in cSums: 
                count += cSums[prefix - target]
        cSums[prefix] += 1
    return count 

nums = [1,2,3,4,5,6,7,8]
lower = 2 
upper = 4

nums = [-2,5,-1]
lower = -2
upper = 2

# nums = [0,0]
# lower = 0
# upper = 0

print(countRangeSum(nums, lower, upper))