# https://leetcode.com/problems/minimum-time-difference/description/
# 539. Minimum Time Difference

# O(1) space, time O(nlogn) for sort

def convertStringToMinutes(time): 
    hrs = int(time[:2])
    minutes = int(time[3:])
    totalTime = hrs*60 + minutes
    return totalTime


def deltaTime(time1, time2): 
    return min((24*60 - time1) + time2, abs(time2 - time1), (24*60 - time2) + time1)

class Solution:
    def findMinDifference(self, timePoints: list[str]) -> int:
        n = len(timePoints)
        timePoints = [convertStringToMinutes(time) for time in timePoints]
        res = 24*60
        for i in range(1, n): 
            delta = deltaTime(timePoints[i], timePoints[i-1])
            res = min(res, delta)
        res = min(res, deltaTime(timePoints[n-1], timePoints[0]))
        return res
