# https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/
# 1353. Maximum Number of Events That Can Be Attended

from collections import deque 
from heapq import heappush, heappop

def maxEvents(events: list[list[int]]) -> int:
    minStart = min([event[0] for event in events])
    maxEnd = max([event[1] for event in events])
    starts = deque(sorted(events))
    active = []
    count = 0
    for i in range(minStart, maxEnd + 1):
        while starts and starts[0][0] == i: 
            cur = starts.popleft()
            heappush(active, cur[1])
        if active: 
            count += 1
            heappop(active)
        while active and active[0] == i: 
            heappop(active)
    return count




events = [[1,2],[2,3],[3,4]]
# events= [[1,2],[2,3],[3,4],[1,2]]
print(maxEvents(events))