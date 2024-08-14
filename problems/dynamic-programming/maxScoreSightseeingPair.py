# https://leetcode.com/problems/best-sightseeing-pair/
# 1014. Best Sightseeing Pair

# build a rightDp array: rightDp[i] = largest value on the right 

def maxScoreSightseeingPair(values: list[int]) -> int:
    n = len(values)
    dp, rightDp = [0]*n, [0]*n

    for j in range(n-1, -1, -1):
        if j == n-1: rightDp[j] = values[j]
        else: rightDp[j] = max(rightDp[j+1]-1, values[j])

    for j in range(0, n-1):
        dp[j] = rightDp[j+1]-1 + values[j]

    return max(dp)

values = [8,1,5,2,6]
print(maxScoreSightseeingPair(values))