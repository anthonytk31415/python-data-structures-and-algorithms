# https://leetcode.com/problems/maximum-number-of-points-with-cost/description/
# 1937. Maximum Number of Points with Cost

# similar: 
# https://leetcode.com/problems/best-sightseeing-pair/description/
# https://leetcode.com/problems/minimum-falling-path-sum/description/


# you can program this easily using O(mnn) Time. But how do you go to O(mn)?
# leftDp[j] = max move on the left of j inclusive = max(leftDp[j-1] - 1, dp[j])
# rightDp[j] = max move on the right of j = max(rightDp[j+1] - 1, dp[j])
# note how we incorporate the "-1" for the positional penalty
# then dp[j] = max move picking j = points[i][j] + max(rightDp[j], leftDp[j]) 

# Time: O(mn), Space: O(n)

def maxPoints(points: list[list[int]]) -> int:
    n = len(points[0])
    dp = points[0]
    leftDp, rightDp = [0]*n, [0]*n

    for i in range(1, len(points)):
        for j in range(len(points[0])):
            if j == 0: 
                leftDp[j] = dp[j]
            else: 
                leftDp[j] = max(leftDp[j-1] -1, dp[j])

        for j in range(len(points[0])-1, -1, -1):
            if j == len(points[0])-1: 
                rightDp[j] = dp[j]
            else: 
                rightDp[j] = max(rightDp[j+1] -1, dp[j])

        for j in range(len(points[0])):
            dp[j] = points[i][j] + max(rightDp[j], leftDp[j])

    return max(dp)

points = [[1,2,3],[1,5,1],[3,1,1]]
points = [[1,5],[2,3],[4,2]]

print(len(points[0]), len(points))
print(maxPoints(points))