# https://leetcode.com/problems/find-median-from-data-stream/

from heapq import heappush, heappop

# Keep min heap for top, max_heap for bot
# insert accordingly; balance after insertions

class MedianFinder:

    def __init__(self):
        self.bot = []       # max heap 
        self.top = []       # min heap

    def rebalance(self): 
        while abs(len(self.bot) - len(self.top)) > 1: 
            if len(self.bot) > len(self.top): 
                heappush(self.top, (-heappop(self.bot)))
            else: 
                heappush(self.bot, -heappop(self.top))          
            
    def addNum(self, num):
        if self.top and num >= self.top[0]: 
            heappush(self.top, num)
        else: 
            heappush(self.bot, -num)
        self.rebalance()

    def findMedian(self):
        if len(self.bot) > len(self.top): 
            return -self.bot[0]
        elif len(self.top) > len(self.bot): 
            return self.top[0]
        else: 
            return (self.top[0] -self.bot[0]) / 2