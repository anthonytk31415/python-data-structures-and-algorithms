# https://leetcode.com/problems/the-skyline-problem/submissions/1469588644/
# 218. The Skyline Problem

# skyline using mergesort-like divide and conquer

def isIntersect(left, right):         
    return left[1] >= right[0] and left[0] <= right[1]

# the trickiest part of the code. So mamny cases you need to walk through
def updateIntersection(i, j, left, right, skyline): 
    ls, le, lh = left[i]
    rs, re, rh = right[j]
    if lh == rh:                                    # equal ht; combine
        right[j] = [ls, max(re, le), lh]
        return i+1, j    
    elif rh > lh:                                   # right has higher ht        
        if ls < rs: skyline.append([ls, rs, lh])    # there's a left piece of left (lower ht) --> append the left piece        
        if le > re:                                 # there's a right piece of left (lower ht)
            left[i] = [re, le, lh]            
            skyline.append(right[j])    
            return i, j + 1
        else:                               
            return i + 1, j
    else:                                           # left has higher ht
        if re > le:                                 # there's a right end of right
            skyline.append(left[i])
            right[j] = [le, re, rh]
            return i + 1, j
        else: 
            return i, j+1

def updateNonInsersection(i, j, left, right, skyline):
    if left[i][0] < right[j][0]: 
        skyline.append(left[i])
        return i + 1, j
    else: 
        skyline.append(right[j])
        return i, j+1

def mergesort(buildings): 
    n = len(buildings)
    if n == 1: return buildings
    mid = n//2
    left = mergesort(buildings[:mid])
    right = mergesort(buildings[mid:]) 
    res = merge(left, right)
    return res

def merge(left, right): 
    skyline = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if isIntersect(left[i], right[j]): 
            i, j = updateIntersection(i, j, left, right, skyline)
        else: 
            i, j = updateNonInsersection(i, j, left, right, skyline)        
    # at end, put rest in skyline
    if i < len(left): 
        skyline += left[i:]    
    if j < len(right): 
        skyline += right[j:]    
    return skyline        
        
def getSkyline(skyline): 
    return [[x[0], x[2]] for x in skyline]

class Solution:
    def getSkyline(self, buildings: list[list[int]]) -> list[list[int]]:        
        maxEnd = max([x[1] for x in buildings])
        sentinel = [buildings[0][0], maxEnd + 1, 0]
        buildings.append(sentinel)
        buildings.sort(key = lambda x: (x[0], x[1]))
        skyline = mergesort(buildings)
        return getSkyline(skyline)
        
        
s = Solution()
# b = [[1, 11, 5], [2, 6, 7], [3, 13, 9], [12, 7, 16], [14, 3, 25], [19, 18, 22], [23, 13, 29], [24, 4, 28]]
b = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
b = [[0,2,3],[2,4,3],[4,6,3]]
print(s.getSkyline(b))

# Skyline for given buildings is
#  (1, 11), (3, 13), (9, 0), (12, 7), (16, 3), (19, 18), (22, 3), (23, 13), (29, 0),