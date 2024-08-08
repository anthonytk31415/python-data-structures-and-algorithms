# https://leetcode.com/problems/word-break/description/?envType=study-plan-v2&envId=top-interview-150
# 139. Word Break

from functools import lru_cache

# Backtrack. Use a memoization/cache to ensure if you traverse that path again, you dont go through
# the whole DFS. Create a words set to check for membership in constant time. 

# Time: O(n**3), Space: O(n + m)

def wordBreak(s, wordDict): 
    words = set(wordDict)

    @lru_cache(None)
    def dfs(s):
        if len(s) == 0: return True

        for i in range(len(s)):
            candidate = s[:(i+1)]
            if candidate in words and dfs(s[(i+1):]):
                return True
        return False

    return dfs(s)


s = "leetcode"
wordDict = ["leet","code"]

s = "applepenapple"
wordDict = ["apple","pen"]

s = "catsandog"
wordDict = ["cats","dog","sand","and","cat"]

print(wordBreak(s, wordDict))