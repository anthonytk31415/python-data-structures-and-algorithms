from collections import defaultdict
from bisect import bisect_left

# This is an O(n^3) Algorithm, with O(n) space. 
# Put the indices of common starting letters in a hash map. 
# then for each index, we effectively "dfs" all subsequent indices. 

def longestRepeatingSubstring(s): 
    def checkLongest(i, j, s):
        counter = 0
        while j < len(s) and s[i] == s[j]:
            i += 1
            j += 1
            counter += 1
        return counter

    starting = defaultdict(list)
    for i, char in enumerate(s):
        starting[char].append(i) 
    
    res = 0

    for char in starting: 
        curChar = starting[char]
        for i in range(len(curChar)):
            for j in range(i + 1, len(curChar)): 
                res = max(res, checkLongest(curChar[i], curChar[j], s))

    return res

s = "aabcaabdaab"
# s = "aaaaa"
print(longestRepeatingSubstring(s))