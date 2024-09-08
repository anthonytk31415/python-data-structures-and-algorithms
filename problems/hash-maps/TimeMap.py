from collections import defaultdict
from bisect import bisect_right

# https://leetcode.com/problems/time-based-key-value-store/description/?envType=company&envId=amazon&favoriteSlug=amazon-thirty-days
# 981. Time Based Key-Value Store

# Space: O(n) for each value stored

class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)        

    # O(1) operation
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append([timestamp, value])        

    # O(logn) operation for binary search each call
    def get(self, key: str, timestamp: int) -> str:
        i = bisect_right(self.store[key], timestamp, key = lambda x: x[0])
        if i -1 < 0: return ""
        return self.store[key][i-1][1]
    
t = TimeMap()
t.set("foo", "bar", 1)
print(t.get("foo", 1))
print(t.get("foo", 3))
t.set("foo", "bar2", 4)
print(t.get("foo", 4))
print(t.get("foo", 5))
print(t.get("foo", 2))