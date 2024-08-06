 
# https://leetcode.com/problems/maximize-area-of-square-hole-in-grid/description/
# 2943. Maximize Area of Square Hole in Grid


# Time: O(nlogn) for the sort, O(n) for iterating across each list
# Space: O(1) using prev and cur optimization

# DP using a kadane-like solution. Sort lists and find longestConsecutiveLength for each list. 
# Ans = min(lcl's ) **2

def maximizeSquareHoleArea(n: int, m: int, hBars: list[int], vBars: list[int]) -> int:
    hBars.sort()
    vBars.sort()
    def longestConsecutiveLength(arr):
        res = 1
        longestPrev, longestCur = 0, 1
        for i in range(1, len(arr)):
            longestPrev, longestCur = longestCur, 1
            if arr[i] == arr[i-1] + 1: 
                longestCur = longestPrev + 1
                res = max(longestCur, res)
        return res
    
    longestH, longestV = longestConsecutiveLength(hBars) + 1, longestConsecutiveLength(vBars) + 1
    return min(longestH, longestV)**2

n = 2
m = 1
hBars = [2,3]
vBars = [2]
# 4

n = 1
m = 1
hBars = [2]
vBars = [2]

n = 2
m = 3
hBars = [2,3]
vBars = [2,4]

print(maximizeSquareHoleArea(n, m, hBars, vBars))