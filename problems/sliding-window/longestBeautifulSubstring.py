# https://leetcode.com/problems/longest-substring-of-all-vowels-in-order/description/?envType=problem-list-v2&envId=sliding-window
# 1839. Longest Substring Of All Vowels in Order


# Decently tricky sliding window.
# Keep track of where you are in the aeiou vowels.  
# Push forward only if you are at the current vowel, or you can progress. Reset if not. 
# Keep track of count; update maxCount when you are at "u"
# Reset when you aren't at the current vowel

# O(n) time, O(1) Space

class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        vowels = " aeiou"
        v = 0
        count = 0
        maxCount = 0
        i = 0
        while i < len(word): 
            if v + 1 < len(vowels) and word[i] == vowels[v+1]: 
                v += 1
            if word[i] == vowels[v]: 
                count += 1
                i += 1
                if vowels[v] == "u": 
                    maxCount = max(maxCount, count) 
            else: 
                v = 0
                count = 0
                while i < len(word) and word[i] != "a": 
                    i += 1
        return maxCount