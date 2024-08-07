# https://leetcode.com/problems/minimum-number-of-coins-for-fruits/description/
# 2944. Minimum Number of Coins for Fruits

from math import inf 

# DP implementation. DP = min total prices to get all fruit from i onward. Then 
# start from back of prices up to index = 0. 
# If ever your "window" gets all of the rest of i fruit, you dont need to take a min
# since you get it for free. 
# Time: O(n**2) Space: O(n); the N**2 is really for the min operation done N times. 

def minimumCoins(prices):
    dp = [inf] * len(prices)
    for i in range(len(dp) - 1, -1, -1):
        candidates = dp[(i+1): (i + i + 1 + 2)]
        if i + i + 1 >= len(dp)-1: 
            dp[i] = prices[i]
        else: 
            dp[i] = prices[i] + min(candidates) 
        # print(i, dp, slice)
    return dp[0]


# prices = [3,1,2]
prices = [26,18,6,12,49,7,45,45]
prices = [1,37,19,38,11,42,18,33,6,37,15,48,23,12,41,18,27,32] # 37: 1 + 19 + 11 + 6


print(minimumCoins(prices))


# now, how do you implement this as a deque? a la Lee. 