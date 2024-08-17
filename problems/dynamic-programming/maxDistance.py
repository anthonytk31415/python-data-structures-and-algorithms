# 624. Maximum Distance in Arrays
# https://leetcode.com/problems/maximum-distance-in-arrays/description/?envType=daily-question&envId=2024-08-16

from math import inf 


# Can solve this in O(n) Time and Space with maxLeft and maxRight tricks and DP. 
# What's a greedy approach? 2 Pointers? 

def maxDistance(arrays):
    mini = [x[0] for x in arrays]
    maxi = [x[-1] for x in arrays]
    minLeft, minRight = [x for x in mini], [x for x in mini]
    maxLeft, maxRight = [x for x in maxi], [x for x in maxi]

    for i in range(1, len(arrays)):
        minLeft[i] = min(minLeft[i], minLeft[i-1])
        maxLeft[i] = max(maxLeft[i], maxLeft[i-1])

    for i in range(len(arrays)-2, -1, -1):
        minRight[i] = min(minRight[i], minRight[i+1])
        maxRight[i] = max(maxRight[i], maxRight[i+1])    
    
    maxDist = -inf 
    for i in range(len(arrays)):
        if i == 0: 
            distWithMini = abs(mini[i] - maxRight[i+1])
            distWithMaxi = abs(maxi[i] - minRight[i+1])
        elif i == len(arrays) - 1: 
            distWithMini = abs(mini[i] - maxLeft[i-1])
            distWithMaxi = abs(maxi[i] - minLeft[i-1])
        else: 
            distWithMini = abs(mini[i] - max(maxLeft[i-1], maxRight[i+1]))
            distWithMaxi = abs(maxi[i] - min(minRight[i+1], minLeft[i-1]))
        maxDist = max(maxDist, distWithMini, distWithMaxi)       

    return maxDist
    # print(mini, maxi)
    # print(minLeft, minRight)
    # print(maxLeft, maxRight)

arrays = [[1,2,3],[4,5],[1,2,3]]
# arrays = [[1],[1]]
arrays = [[1,4],[0,5]]
arrays = [[-1,1],[-3,1,4],[-2,-1,0,2]]
print(maxDistance(arrays))
