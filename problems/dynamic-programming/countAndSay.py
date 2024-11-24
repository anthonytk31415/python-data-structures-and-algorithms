# https://leetcode.com/problems/count-and-say/description/
# 38. Count and Say



# You can solve this iteratively using a bottoms-up DP. Start with the base case. Then for each 
# base case, apply compress, which we do for n-1 times to build the nth case. 
# To build compress, we can iterate across out input string recursively, at O(n) time. 
# Namely, we find consecutives and the counts, and then attach to our result the number
# of consecutives and the count. When we get to a new char in the s, we start our count over 
# and append our result. At the end, if there's a count, we ensure we append it. 


# Time: O(2**n) for n calls of compress. Since the string doubles in the worst, case we have 2**n. 
# Space: O(n) for the string

def compress(s, i, res, curCheck, curCount):     
    # base case
    if i >= len(s): 
        if curCount > 0: 
            return res + str(curCount) + str(curCheck) 
        else: 
            return res
    # start anew
    elif curCheck == None: 
        return compress(s, i + 1, res, s[i], 1)
    elif s[i] == curCheck: 
        return compress(s, i+1, res, curCheck, curCount + 1)
    # new char; reset inputs and update res
    else:
        return compress(s, i, res + str(curCount) + str(curCheck) , None, 0)

class Solution:
    def countAndSay(self, n: int) -> str:
        res = "1"
        for _ in range(2, n+1):
            res = compress(res, 0, "", None, 0)
        return res
    
z = Solution()
n = 4
# 1211

n = 6
# 111221

n = 2
# 11

n = 6
# 312211
print(z.countAndSay(n))

