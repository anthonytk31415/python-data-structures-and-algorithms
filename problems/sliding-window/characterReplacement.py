from collections import Counter
from math import inf 

# https://leetcode.com/problems/longest-repeating-character-replacement/
# 424. Longest Repeating Character Replacement

def charReplacement1(s, k):
    def isWindowValid(window, k): 
        largestChar = None
        countLargestChar = 0
        countWindow = 0
        for char, v in window.items(): 
            countWindow += v
            if not largestChar or countLargestChar < v:
                countLargestChar = v
                largestChar = char
        res = countWindow - countLargestChar <= k
        return res
    window = Counter()      # this represents a valid window that includes right
    res = -inf
    left = 0
    curSum = 0
    for right in range(len(s)):
        window[s[right]] += 1
        curSum += 1
        while not isWindowValid(window, k) and left < right: 
            window[s[left]] -= 1
            curSum -= 1
            left += 1   
        if isWindowValid(window, k):
            res = max(res, curSum)
    return res


def charReplacement(s, k):
    def isWindowValid(window, k): 
        largestChar = None
        countLargestChar = 0
        countWindow = 0
        for char, v in window.items(): 
            countWindow += v
            if not largestChar or countLargestChar < v:
                countLargestChar = v
                largestChar = char
        res = countWindow - countLargestChar <= k
        return res
    window = Counter()      # this represents a valid window that includes right
    left = 0
    curSum = 0
    for right in range(len(s)):
        window[s[right]] += 1
        curSum += 1
        if not isWindowValid(window, k) and left < right: 
            window[s[left]] -= 1
            curSum -= 1
            left += 1   

    return right - left + 1


s = "AABABBA"
s = "ABCCCCCCCCCCCCCCCBAAAAAAAAAAA"
k = 3

print(charReplacement(s, k))