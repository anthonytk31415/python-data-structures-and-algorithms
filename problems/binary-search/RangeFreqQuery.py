from collections import defaultdict
from bisect import bisect

# https://leetcode.com/problems/range-frequency-queries/description/
# 2080. Range Frequency Queries

# Trick: keep a hash map of the number as the key and a list of the indexes as the values
# When you search, binary search the left - 1 and the right. take the difference of the two. 

#O(qlogn) for q queries taking logn for n length of list
#Space: O(n)


class RangeFreqQuery:

    def __init__(self, arr: list[int]):
        self.count = defaultdict(list)         
        for i, num in enumerate(arr): 
            self.count[num].append(i)
        # print(self.count)

    def query(self, left: int, right: int, value: int) -> int:
        i = bisect(self.count[value], left - 1)        
        j = bisect(self.count[value], right)        
        return j - i
    
arr = [12, 33, 4, 56, 22, 2, 34, 33, 22, 12, 34, 56]
# arr = [5,7,2,8,5,7]
r = RangeFreqQuery(arr)

print(r.query(1,2,4))
print(r.query(1,2,2))
print(r.query(1,2,12))