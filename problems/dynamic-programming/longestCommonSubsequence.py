# 1143. Longest Common Subsequence
# O(MN), space: O(M)
# classic DP. dp[i][j] = longest commonn subsequence at i for text1 and j for text 2; 
# if equal dp[i][j] = 1 + dp[i+1][j+1]
# else: dp[i][j] = max(dp[i+1][j], dp[i][j+1])
# can do a space optimization so you have O(n) space instead of O(MN) since you only care about the prevoius iteration


from functools import lru_cache
def longestCommonSubsequence1(text1: str, text2: str) -> int:

    @lru_cache(None)
    def helper(i, j):
        if i >= len(text1) or j >= len(text2): 
            return 0
        if text1[i] == text2[j]: 
            return 1 + helper(i+1, j+1)
        return max(helper(i, j+1), helper(i+1, j))
    return helper(0,0)


def longestCommonSubsequence(text1: str, text2: str) -> int:

    m, n = len(text1), len(text2)
    dpPrev, dpCur = [0]*n, [0]*n

    for i in range(m-1, -1, -1): 
        dpPrev, dpCur = dpCur, [0]*n
        for j in range(n - 1, -1, -1):
            if j == n - 1: 
                if text1[i] == text2[j]: dpCur[j] = 1
                else: dpCur[j] = dpPrev[j]            
            else: 
                if text1[i] == text2[j]: dpCur[j] = 1 + dpPrev[j+1]
                else: 
                    dpCur[j] = max(dpCur[j+1], dpPrev[j])         
    return dpCur[0]

text1 = "abcde"
text2 = "ace" 

text1 = "abc"
text2 = "def"

text1 = "aaaaaabbbbb"
text2 = "aaabbb"

text1 = "abcba"
text2 = "abcbcba"

print(longestCommonSubsequence(text1, text2))