# https://leetcode.com/problems/describe-the-painting/?envType=problem-list-v2&envId=mzw3cyy6
# 1943. Describe the Painting

from collections import Counter

# Sweep Line. Time O(nlogn) for sorting. O(n) for counts

def splitPainting(segments: list[list[int]]) -> list[list[int]]:
    starts, ends = Counter(), Counter()
    intervals = set()
    for st, end, val in segments: 
        starts[st] += val  
        ends[end] += val
        intervals.add(st)
        intervals.add(end)
    intervals = sorted(list(intervals))
    # print(intervals)
    res = []
    count = starts[intervals[0]]

    for i in range(1, len(intervals)):
        if count > 0 : 
            res.append([intervals[i-1],intervals[i], count])
        count += starts[intervals[i]]
        count -= ends[intervals[i]]

    return res
    
segments = [[1,7,9],[6,8,15],[8,10,7]]
# [[1,6,9],[6,7,24],[7,8,15],[8,10,7]]


segments = [[1,4,5],[1,4,7],[4,7,1],[4,7,11]]
segments =[[4,16,12],[9,10,15],[18,19,13],[3,13,20],[12,16,3],[2,10,10],[3,11,4],[13,16,6]]
print(splitPainting(segments))


a = Counter()

print("nonexistant value in a: ", a[1])