# https://leetcode.com/problems/longest-uploaded-prefix/?envType=problem-list-v2&envId=segment-tree
# 2424. Longest Uploaded Prefix

from heapq import heappush, heappop

# this heap implementation is super clean. Is there a Binary Indexed Tree implementation
# O(nlogn) for n queries, logn for each upload Time
# O(n) space
class LUPrefix1:

    def __init__(self, n: int):
        self.heap = []
        self.longestNum = 0
        self.n = n

    def upload(self, video: int) -> None:
        heappush(self.heap, video)
        while self.heap and self.heap[0] == self.longestNum + 1: 
            self.longestNum += 1
            heappop(self.heap)
        return 

    def longest(self):
        return self.longestNum
    

# a binary implmentation
class LUPrefix:

    def __init__(self, n: int):
        self.n = n
        self.x = 0

    def upload(self, video: int) -> None:
        toSet = 1<<(video - 1)
        self.x = self.x | toSet
        return 

    def longest(self):
        # get the rightmost cleared bit and return that minus 1
        rightmost = ~self.x & (self.x + 1)
        # rightmost = self.x | ~(self.x + 1)
        return rightmost.bit_length() - 1 
    

a = LUPrefix(4)
a.upload(3)
a.longest()
print(a.longest())
a.upload(1)
print(a.longest())
a.upload(2)
print(a.longest())





x = 0

# ~x & (x+1) returns the rightmost cleared bit
# then return the length minus 1 to get the n


