from collections import deque

# https://leetcode.com/problems/merge-intervals/description/
# 56	Merge Intervals

def merge( intervals: list[list[int]]) -> list[list[int]]:
    def isOverlap(a, b): 
        return a[0] <= b[1] and b[0] <= a[1]

    def mergeInterval(a, b): 
        return [min(a[0], b[0]), max(a[1], b[1])]

    intervals.sort(key = lambda x: (x[0], x[1]))
    res = []
    intervals = deque(intervals)
    while intervals:
        curInterval = intervals.popleft()
        while intervals and isOverlap(curInterval, intervals[0]): 
            curInterval = mergeInterval(curInterval, intervals[0])
            intervals.popleft()
        res.append(curInterval)

    return res


intervals = [[1,3],[2,6],[8,10],[15,18]]

print(merge(intervals))