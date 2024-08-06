# https://leetcode.com/problems/triangle/description/?envType=study-plan-v2&envId=top-interview-150
# 120. Triangle

# Space: O(len triangle base)
# Time: O(mn)

def minimumTotal(triangle):
    dpPrev = [x for x in triangle[-1]]
    for i in range(len(triangle) - 2, -1, -1):
        dpCur = [0]*len(triangle[i])
        for j in range(len(dpCur)):
            dpCur[j] = triangle[i][j] + min(dpPrev[j], dpPrev[j+1])
        dpPrev = dpCur
    return dpPrev[0]


triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
print(minimumTotal(triangle))
