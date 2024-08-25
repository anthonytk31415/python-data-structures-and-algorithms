# https://leetcode.com/problems/k-closest-points-to-origin/description/
# 973. K Closest Points to Origin

from math import sqrt

def kClosest(points, k):

    def getDistance(a, b): 
        return sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)
    origin = [0,0]
    points.sort(key = lambda x: getDistance(x, origin))
    return points[:k]
