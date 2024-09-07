# https://leetcode.com/problems/the-skyline-problem/submissions/1382488204/
# 218. The Skyline Problem

from heapq import heappush, heappop
# from collections import deque

# Process the times in order. Keep track of the tallest building at each time with maxHeap.
# Add height/endtime to heap. Evict when time == the top. After eviction, evict anything on top < time. 
# At each interval, you record when maxHeight changes. Keep track of the prior curMax. 
# So hard!
# Time: O(nlogn) for minheap and sort; Space: O(n) for the nodes. 

def getSkyline(buildings: list[list[int]]) -> list[list[int]]:

    buildings.sort(key = lambda x: (x[0], x[1]))    # buildings[i] = [start, end, height]
    q, times, h = [], [], []
    for start, end, _ in buildings: 
        times += [start, end]
    times.sort()
    curMax, i = 0, 0
    for t in times: 
        # add all start times
        while i < len(buildings) and buildings[i][0] == t:           
            heappush(q, [-buildings[i][2], buildings[i][1]])
            i += 1      
        # remove all things less than or equal to t
        while q and q[0][1] <= t: 
            heappop(q)        
        # record newHeight or 0 if curMax changed to res. Then update curMax.
        if not q and curMax > 0:
            h.append([t, 0])
            curMax = 0
        elif q and -q[0][0] != curMax:  
            h.append([t, -q[0][0]])
            curMax = -q[0][0]
    return h



x = set([3,1,2])
print(sorted(x))

buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
print(getSkyline(buildings))