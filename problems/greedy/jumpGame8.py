# https://leetcode.com/problems/jump-game-viii/description/
# 2297. Jump Game VIII

# Use a montonic stack to find the next greater element and the next lesser element
# Why? Say x is in the stack. if x <= num that means num is x's next greater element. Process the score and store it. 
# Then pop it. Since you found the next greater element, x cannot jump to an element after num since the old num 
# would violate the jump criteria.   
# Similar logic for the smaller element. 
# Use a dp array to keep track of the smallest score at the ith index. 

# O(n) time and space for single traversal, stack, and dp array

from math import inf
def minCost(nums, costs): 

    dp = [inf]*len(nums)
    dp[0] = 0
    greater = []
    lesser = []

    for i in range(len(nums)): 
        
        while greater and nums[greater[-1]] <= nums[i]: 
            dp[i] = min(dp[i], dp[greater.pop()] + costs[i])
        
        while lesser and nums[lesser[-1]] > nums[i]: 
            dp[i] = min(dp[i], dp[lesser.pop()] + costs[i])

        greater.append(i)
        lesser.append(i)

    return dp[-1]

nums = [3,2,4,4,1]
costs = [3,7,6,4,2]


# nums = [0,1,2]
# costs = [1,1,1]


# #                  6     9 1,2,3 --> 21
# nums =  [5,4,3,0,1,5,6,7,4,5,6,7]
# # #                  ^     ^
# costs = [1,2,3,4,5,6,7,8,9,1,2,3]
# #       

# nums = [4,3,5,1,2]
# costs = [2,1,5,2,3]

print(minCost(nums, costs))



    # cost, i, j= 0, 0, 0
    # while i < len(nums)-1: 
    #     j = i + 1
    #     # cumeCost = 0
    #     if nums[i] > nums[j]: 
    #         while j+1 < len(nums) and nums[i] > nums[j+1]: 
    #             # cumeCost += costs[j]
    #             j += 1
    #         if j + 1 < len(nums) and nums[i] <= nums[j+1]: 
    #             j += 1
    #         else:  
    #             j = i + 1
    #     else: 
    #         while j + 1 < len(nums) and nums[i] <= nums[j+1]: 
    #             # cumeCost += costs[j]
    #             j += 1
    #         if j + 1 < len(nums) and nums[i] > nums[j+1]: 
    #             j += 1
    #         else:  
    #             j = i + 1

    #     cost += costs[j]
    #     i = j
    # return cost