# https://leetcode.com/problems/meeting-rooms-ii/?envType=company&envId=amazon&favoriteSlug=amazon-all
# 253. Meeting Rooms II

from heapq import heappush, heappop

# Intervals using sweep line technique. When a meeting occurs, count += 1. When it ends, count -=1. Process by time. 
# Time: O(nlogn), Space: O(n) for the endQueue

def minMeetingRooms(intervals: list[list[int]]) -> int:
    count = 0
    maxCount = 0
    endQueue = []
    intervals.sort(key = lambda x: (x[0], x[1]))
    for start, end in intervals: 
        while endQueue and endQueue[0] <= start: 
            count -= 1
            heappop(endQueue)
        count += 1
        maxCount = max(maxCount, count)         # this is set so counts are measured before end time, i.e considers <=
        heappush(endQueue, end)
    return maxCount


intervals = [[0,30],[5,10],[15,20]]
print(minMeetingRooms(intervals))