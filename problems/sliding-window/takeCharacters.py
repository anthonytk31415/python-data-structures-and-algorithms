
# https://leetcode.com/problems/take-k-of-each-character-from-left-and-right/description/
# 2516. Take K of Each Character From Left and Right

from collections import Counter
from math import inf

# think of the window as going from i to 0 and then wrapping from front to back in a ring. 
# then as i grows, your end window j shrinks to the right most. 
# time: O(n), space: O(1)

def takeCharacters(s, k):
    n = len(s)
    counter = Counter(s)
    res = inf
    for char in "abc":
        if counter[char] < k: return -1
    i, j = -1, 0
    while i < len(s):
        while j < len(s) and counter[s[j]] > k: 
            counter[s[j]] -= 1
            j += 1
        res = min(res, i+1 + (n - 1 - (j) + 1))   
        i += 1
        if i < len(s) and i < j:
            counter[s[i]] += 1
        if i == j: 
            j += 1
    return res

s = "aabaaaacaabc"
k = 2

# s = "a"
# k = 0

# s = "acbcc"
# k = 1

print(takeCharacters(s, k))