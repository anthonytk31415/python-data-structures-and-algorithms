# https://leetcode.com/problems/jump-game-vii/description/?envType=problem-list-v2&envId=sliding-window
# 1871. Jump Game VII

# DP/Sliding window
# If you're a candidate, add 1 to the sum. if you are out of the window and you were a true, remove 1 from sum.
# dp[i] = if windowSum > 0
# O(n) for the window Space; O(n) Time one pass. 

class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:        
        n = len(s)
        dp = [0]*len(s)
        dp[n-1] = True
        windowSum = 0
        for i in range(n-2, -1, -1): 
            if i + maxJump + 1 < n and s[i + maxJump + 1 ] == "0" and dp[i + maxJump + 1]: windowSum -= 1
            if i + minJump < n and s[i + minJump] == "0" and dp[i + minJump]: windowSum += 1             
            dp[i] = windowSum > 0
        return dp[0]

s = "011010"
minJump = 2
maxJump = 3


# s = "01101110"
# minJump = 2
# maxJump = 3

sol = Solution()
print(sol.canReach(s, minJump, maxJump))