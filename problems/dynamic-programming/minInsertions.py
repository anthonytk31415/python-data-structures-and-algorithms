from functools import cache

def minInsertions(s: str) -> int:

    @cache
    def helper(s):
        if len(s) <= 1: return 0
        if len(s) == 2: 
            if s[0] != s[-1]: return 1
            else: return 0

        if s[0] == s[-1]: return helper(s[1:-1])
        return 1 + min(helper(s[1:]), helper(s[:-1]))

    return helper(s)

s = "mbadm"
s = "anthony"
# s= "leetcode"

print(s[-(len(s))])



# print(minInsertions(s))
# print(s[1:-1])