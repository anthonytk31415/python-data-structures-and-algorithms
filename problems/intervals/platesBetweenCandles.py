from math import inf
from bisect import bisect_right, bisect_left

# a segment tree implementation. 
# https://leetcode.com/problems/plates-between-candles/description/?envType=company&envId=amazon&favoriteSlug=amazon-thirty-days
# 2055. Plates Between Candles

# Space: O(n) for the prefix and candles in both implementations, Time: O(klogn) for binary searching k times for k queries

#binary search the left and right candle
def platesBetweenCandles(s: str, queries: list[list[int]]) -> list[int]:
    candles = [i for i in range(len(s)) if s[i] == "|"]
    prefix = [0]* len(s)
    for i in range(len(prefix)): 
        if s[i] == "*": 
            prefix[i] = 1
        if i > 0: 
            prefix[i] += prefix[i-1] 
    res = []
    for left, right in queries: 
        iLeft, iRight = bisect_left(candles, left), bisect_right(candles, right) - 1
        curRes = 0
        if iLeft < iRight: 
            curRes = prefix[candles[iRight]] - prefix[candles[iLeft]]
        res.append(curRes)
    return res


# segment tree approach
def platesBetweenCandles1(s: str, queries: list[list[int]]) -> list[int]:
    n = len(s)
    # build the segment tree
    minCandles, maxCandles = [inf]*n*2, [-inf]*n*2
    for i in range(n): 
        k = i + n
        if s[i] == "|": 
            minCandles[k] = i
            maxCandles[k] = i
    for i in range(n-1, 0, -1): 
        minCandles[i] = min(minCandles[2*i], minCandles[2*i + 1])
        maxCandles[i] = max(maxCandles[2*i], maxCandles[2*i + 1])

    # build the query for segment tree
    def getMinMaxCandle(left, right): 
        minIdx = inf
        maxIdx = -inf
        left += n
        right += n
        while left <= right: 
            if left % 2 == 1: 
                minIdx = min(minIdx, minCandles[left])
                maxIdx = max(maxIdx, maxCandles[left])
                left += 1
            if right % 2 == 0: 
                minIdx = min(minIdx, minCandles[right])
                maxIdx = max(maxIdx, maxCandles[right])
                right -= 1
            left //= 2
            right //= 2
        return minIdx, maxIdx

    prefix = [0]* len(s)
    for i in range(len(prefix)): 
        if i == 0 and s[i] == "*": 
            prefix[i] = 1
        else: 
            increment = 1 if s[i] == "*" else 0
            prefix[i] = prefix[i-1] + increment

    res = []
    for left, right in queries: 
        cLeft, cRight = getMinMaxCandle(left, right)
        if cLeft > cRight: 
            numCandles = 0
        else: 
            numCandles = prefix[cRight] - prefix[cLeft]
        res.append(numCandles)
    return res

s = "**|**|***|"
queries = [[2,5],[5,9]]

s = "***|**|*****|**||**|*"
queries = [[1,17],[4,5],[14,17],[5,11],[15,16]]

# s = "||*"
# queries = [[2,2]]



print(len(s))
print(platesBetweenCandles(s, queries))