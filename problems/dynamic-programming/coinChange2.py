# https://leetcode.com/problems/coin-change-ii/description/
# 518. Coin Change II

def coinChange2(coins, amt):
    
    # number of ways using coins up to i (inclusive)
    # you can build the kth amount
    cur = [1] + [0 for _ in range(amt)]
    for i in range(len(coins)):
        for k in range(1, len(cur)): 
            if k - coins[i-1] >= 0: cur[k] += cur[k-coins[i-1]]
    return cur[-1]


amt = 5
coins = [1,2,5]
print(coinChange2(coins, amt))

print("hi richard")