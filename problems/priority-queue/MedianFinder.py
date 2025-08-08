from heapq import heappush, heappop


# implement two heaps. 

class MedianFinder:

    def __init__(self):
        self.smalls = []        # max heap
        self.bigs = []          # min heap

    # add to self.bigs first if both empty
    def addNum(self, num: int) -> None:
        if (not self.bigs and not self.smalls) or num >= self.bigs[0]: 
            heappush(self.bigs, num)
        else: 
            heappush(self.smalls, -num)
        self.balanceHeaps()


    def findMedian(self) -> float:
        res = 0
        if not self.smalls or len(self.bigs) > len(self.smalls): 
            res = self.bigs[0]
        elif len(self.smalls) > len(self.bigs):
            res = -self.smalls[0]
        else: 
            res = (-self.smalls[0] + self.bigs[0]) / 2
        return res
    
    def balanceHeaps(self): 
        while abs(len(self.smalls) - len(self.bigs)) > 1: 
            if len(self.smalls) > len(self.bigs):
                toAdd = -heappop(self.smalls)
                heappush(self.bigs, toAdd)
            else: 
                toAdd = heappop(self.bigs)
                heappush(self.smalls, -toAdd)



x = MedianFinder()
x.addNum(1)
x.addNum(2)
print(x.findMedian())
x.addNum(3)
print("median: ", x.smalls, x.bigs, x.findMedian())
# print(x.bigs[0], x.smalls[0])
# print(x.bigs, x.smalls)

x.addNum(4)
x.addNum(1)
x.addNum(2)
x.addNum(8)
print("median: ", x.smalls, x.bigs, x.findMedian())