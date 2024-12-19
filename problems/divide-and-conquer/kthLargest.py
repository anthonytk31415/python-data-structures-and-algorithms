print("Hi Richard")

from bisect import insort_left  
from heapq import heappush, heappop 

# Implementation using binary insertion
# class KLargest:
#     def __init__(self, k):
#         self.nums = [] # this will always be sorted
#         self.k = k

#     # O(N) Time for pushing elements from the insertion index     
#     def insert(self, num): 
#         insort_left(self.nums, num)
 
#     # O(1) Time for array lookup given an index
#     def getKth(self):
#         if len(self.nums) < self.k: return -1 
#         idx = len(self.nums) - self.k
#         return self.nums[idx] 
    
class KLargest:

    def __init__(self, k):
        self.nums = [] # minheap
        self.k = k

    # O(logn) Time for pushing elements from the insertion index     
    def insert(self, num): 
        if len(self.nums) == self.k: 
            if num < self.nums[0]: return 
            else: 
                heappush(self.nums, num)
                heappop(self.nums)
        else: 
            heappush(self.nums, num)
        
    # O(1) Time for array lookup given an index
    def getKth(self):
        if len(self.nums) < self.k: return -1
        return self.nums[0]


# nums > 0
kLargest = KLargest(3)
# for x in [1,5,2,7,3,10, 11, 3]: 
for x in [1,5]: 
    kLargest.insert(x)

# 3rd largest = 7
print(kLargest.getKth())

