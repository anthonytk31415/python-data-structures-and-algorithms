from heapq import heappush, heappop

class Solution:
    def minGroups(self, intervals: list[list[int]]) -> int:
        
        maxCount = 1
        count = 0
        endIntervals = []
        intervals.sort(key = lambda x: (x[0], x[1]))

        for i in range(len(intervals)): 
            start, end = intervals[i]
            # insert the end interval   
            # print(start, end)
            heappush(endIntervals, end)
            count += 1
            maxCount = max(maxCount, count)
            # evict the 
            if i < len(intervals) - 1: 
                while endIntervals and endIntervals[0] < intervals[i+1][0]:
                    heappop(endIntervals)
                    count -= 1

        return maxCount
    

intervals = [[5,10],[6,8],[1,5],[2,3],[1,10]]
sol = Solution()
print(sol.minGroups(intervals))