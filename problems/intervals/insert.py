from bisect import bisect_right

# https://leetcode.com/problems/insert-interval/description/
# 57	Insert Interval

def insert(intervals, newInterval): 
    def isOverlap(a, b ): 
        return a[0] <= b[1] and b[0] <= a[1]

    def mergeIntervals(a, b): 
        return [min(a[0], b[0]), max(a[1], b[1])]

    idx = bisect_right(intervals, newInterval[0], key = lambda x: x[0])
    left = intervals[:idx]
    right = intervals[idx:][::-1]
    while left and isOverlap(newInterval, left[-1]): 
        newInterval = mergeIntervals(newInterval, left[-1])
        left.pop()
    while right and isOverlap(newInterval, right[-1]): 
        newInterval = mergeIntervals(newInterval, right[-1])
        right.pop()
    return left + [newInterval] + right[::-1]

intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]

# idx = bisect_right(intervals, newInterval[0], key = lambda x: x[0])

print(insert(intervals, newInterval))