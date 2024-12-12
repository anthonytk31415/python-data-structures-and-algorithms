# https://leetcode.com/problems/take-gifts-from-the-richest-pile/description/?envType=daily-question&envId=2024-12-12
# 2558. Take Gifts From the Richest Pile

from heapq import heappush, heappop
from math import floor, sqrt

class Solution:
    def pickGifts(self, gifts: list[int], k: int) -> int:        
        pq = []
        for x in gifts: 
            heappush(pq, -x)
        res = 0
        for _ in range(k):
            curAmt = -heappop(pq)
            toLeave = floor(sqrt(curAmt))
            toTake = curAmt - toLeave
            res += toTake
            heappush(pq, -toLeave)
        return sum(gifts) - res