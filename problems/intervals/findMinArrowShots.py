# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/description/
# 452	Minimum Number of Arrows to Burst Balloons


# intervals problem. n log n for sort. space = O(1)

def findMinArrowShots(points: list[list[int]]) -> int:

    def isOverlap(a, b): 
        return a[0] <= b[1] and b[0] <= b[1]

    points.sort(key = lambda x: (x[0], x[1]))
    count = 1
    curIntersection = points[0]
    for i in range(1, len(points)):
        if isOverlap(points[i], curIntersection): continue            
        else: 
            curIntersection = points[i]
            count += 1
    return count

# points = [[10,16],[2,8],[1,6],[7,12]]
# points = [[1,2],[3,4],[5,6],[7,8]]
points = [[1,2],[2,3],[3,4],[4,5]]
print(findMinArrowShots(points))