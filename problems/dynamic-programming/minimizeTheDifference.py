# https://leetcode.com/problems/minimize-the-difference-between-target-and-chosen-elements/description/
# 1981. Minimize the Difference Between Target and Chosen Elements


# Similar to Partition Subararray Sum. For each row element, add to the previous sum. 
# Keep track of all possible sums in a set (to avoid duplication). 
# Time: O(mn*len(totalSum)); Space: O(len(totalSum))

from math import inf

def minimizeTheDifference(mat, target):
    res = inf
    prevSums = set(mat[0])

    for i in range(1, len(mat)):
        curSums = set()
        for j in range(len(mat[0])):
            for x in prevSums: 
                curSums.add(x + mat[i][j])
        prevSums = curSums

    for x in prevSums: 
        res = min(res, abs(x - target))
    return res

mat = [[1,2,3],[4,5,6],[7,8,9]]
target = 13
mat = [[1],[2],[3]]
target = 100

print(minimizeTheDifference(mat, target))