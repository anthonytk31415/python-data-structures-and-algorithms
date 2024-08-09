# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/?envType=study-plan-v2&envId=top-interview-150
# 3. Longest Substring Without Repeating Characters

# Sliding window implementation
# O(n) time and space. 
from collections import Counter
def lengthOfLongestSubstring(s):

    res = 0
    left = 0
    counter = Counter()
    for right in range(len(s)):
        counter[s[right]] += 1
        while counter[s[right]] > 1: 
            counter[s[left]] -= 1
            left += 1
        res = max(res, right - left + 1)
    return res 


s = "baabacabbaadd"
s = "abcabcbb"
print(lengthOfLongestSubstring(s))