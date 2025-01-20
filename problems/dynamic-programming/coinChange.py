# https://leetcode.com/problems/coin-change/description/?envType=study-plan-v2&envId=top-interview-150
# 322. Coin Change

# Classic DP knapsack problem. Time O(mn), Space; O(n) optimized for prev and current iteration. 

from math import inf 
def coinChange(coins: list[int], amount: int) -> int:
    prev, cur = [inf]*(amount + 1), [0]*(amount + 1)
    for i in range(len(coins)):
        for j in range(1, amount + 1):
            cur[j] = prev[j]
            if j - coins[i] >= 0: 
                cur[j] = min(cur[j], 1 + cur[j - coins[i]])
        prev, cur = cur, [0]*(amount + 1)
    if prev[-1] == inf: return -1
    return prev[-1]

coins = [1,2,5]
amount = 11

print(coinChange(coins, amount))