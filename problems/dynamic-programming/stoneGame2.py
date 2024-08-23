from functools import lru_cache

# dp with tabulation. Start from the back 
# use lru_cache so you dont make multiple calls. 

def stoneGameII(piles):

    @lru_cache(None)
    def helper(i, m):
        if i + 2*m >= len(piles): 
            res = (sum(piles[i:]), 0)
            return res

        candidates = []
        for x in range(1, 2*m+1): 
            if i + x > len(piles): break 
            curSum = sum(piles[i:(i+x)])
            opp, your = helper(i+x, max(m, x))
            candidates.append((your + curSum, opp))
        candidates.sort()
        return candidates[-1]

    for m in range(1, len(piles)): 
        for i in range(len(piles)-1, 0, -1):
            helper(i, m)

    res = helper(0, 1)
    return res[0]

piles = [2,7,9,4,4]
piles = [1,2,3,4,5,100]
print(stoneGameII(piles))