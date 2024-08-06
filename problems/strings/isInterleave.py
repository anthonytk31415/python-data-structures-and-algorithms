# https://leetcode.com/problems/interleaving-string/description/?envType=study-plan-v2&envId=top-interview-150
# 97. Interleaving String

from itertools import groupby
from functools import lru_cache

# Check all prefixes in s3 and see if they're in s1. if so, dfs with that prefix removed,
# checking prefixes on s2 now in the next call. 
# if s1, s2, and s3 are empty, we return True. 

# Time: O(mn) calls to helper
# Space: O(mn) for the memoization

def isInterleave(s1, s2, s3):
    memo = {}
    def dfs(s1, s2, s3):         
        if (s1, s2, s3) in memo: return memo[(s1, s2, s3)]
        res = False
        if len(s1) + len(s2) != len(s3): res = False
        elif s1 == s2 == s3 == "": res = True
        else: 
            for k in range(len(s3)):
                if k < len(s1) and s3[:(k+1)] == s1[:(k+1)]:
                    if dfs(s2, s1[k+1:], s3[k+1:]): 
                        res =  True
                        break                             
                else: res = False        
        memo[(s1, s2, s3)] = res
        return res
    return dfs(s1, s2, s3) or dfs(s2, s1, s3)

# same as above but uses LRU Cache. Use "None" to store all results. 
def isInterleave1(s1, s2, s3):
    @lru_cache(None)
    def dfs(s1, s2, s3): 
        if s1 == s2 == s3 == "": return True
        for k in range(len(s3)):
            if k < len(s1) and s3[:(k+1)] == s1[:(k+1)]:
                if dfs(s2, s1[k+1:], s3[k+1:]): return True                             
            else: break 
        return False

    return dfs(s1, s2, s3) or dfs(s2, s1, s3)




# s1 = "aaabbbbccccddddaabb"


s3 = "a"
print(s3[:99])

# # return array where arr[i] = [(char, count)]
# def countConsecutives(str): 
#     return [(char, len(list(group))) for char, group in groupby(str)]


s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"

s1 = "aabcc"
s2 = "dbbca" 
s3 = "aadbbbaccc"

s1 = "aaaaaaaaaaaaaaaaaaaaaaaaaaa"
s2 = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
s3 = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"

s1 = "abababababababababababababababababababababababababababababababababababababababababababababababababbb"
s2 = "babababababababababababababababababababababababababababababababababababababababababababababababaaaba"
s3 = "abababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababbb"


print(isInterleave(s1, s2, s3))









# # completely wrong interpretation lol
# def isInterleave(s1, s2, s3):
#     a1, a2= countConsecutives(s1), countConsecutives(s2)
    
#     inter = []
#     i, j = 0, 0
#     while i < len(a1) and j < len(a2):
#         inter.append(a1[i])
#         inter.append(a2[j])
#         i += 1
#         j += 1
    
#     while i < len(a1):
#         inter.append(a1[i])
#         i += 1
#     while j < len(a2):
#         inter.append(a2[j])
#         j += 1

#     interString = ""
#     for x, n in inter:
#         interString += x*n

#     print(interString)
#     for k in range(len(s3)):
#         if k < len(interString) and interString[k] == s3[k]: continue
#         else: return False
#     return True
