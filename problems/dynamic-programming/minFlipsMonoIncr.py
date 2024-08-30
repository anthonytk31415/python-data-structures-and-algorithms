from math import inf
# https://leetcode.com/problems/flip-string-to-monotone-increasing/description/
# 926. Flip String to Monotone Increasing

# This is an O(n) time complexity implementation; maybe too lazy to amke the space O(1)

def minFlipsMonoIncr(s: str) -> int:

    # dp[i] = num changes needed to make "isone"
    def buildDP(s, isOne):
        check = "0"
        if isOne: check = "1"
        dp = [0]*len(s)
        for i, char in enumerate(s): 
            if char != check: dp[i] += 1
            if i > 0: dp[i] += dp[i-1]
        return dp
    
    dpLeft0, dpLeft1 = buildDP(s, False), buildDP(s, True)
    dpRight0, dpRight1 = buildDP(s[::-1], False)[::-1], buildDP(s[::-1], True)[::-1]
    res = inf
    for i in range(len(s)):
        change01 = dpLeft0[i]  
        change1 = dpLeft1[i]                     
        if i < len(s) - 1: 
            change01 += min(dpRight0[i+1], dpRight1[i+1]) 
            change1 += dpRight1[i+1]        
        res = min(res, min(change01, change1))
    return res


s = "00110"
# s = "00011000"
s = "010110"
print(minFlipsMonoIncr(s))