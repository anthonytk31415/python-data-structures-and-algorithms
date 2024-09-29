# https://leetcode.com/problems/count-unique-characters-of-all-substrings-of-a-given-string/submissions/1405491041/
# 828. Count Unique Characters of All Substrings of a Given String

# This problem is the same as solving this question: 
# For each character char in s, count all of the substrings that contain 1 occurance of char. 
# Then sum these across all char in s. 

# Rationale (*): 
# Say at j we have the index of the occurance of char. And at i, we have the index of the occurance 
# of char on the left, and similarly, we have k for the index of the char occurance on the right. 
# Then the number of substrings that contain s = (j - i)  * (k - j)
# For example, suppose s = ABCDADIIID       
#                          0123456789
#                             ^ ^   ^

# for d at j = 5, i = 3, k = 9: (5-3) * (9-5) = 2*4 = 8 substrings, and they are: 
# AD, ADI, ADII, ADIII
# D, DI, DII, DIII

# For the first and last occurance of char in s:
#   - the left width is the length from -1 to j
#   - the right width is the length from j to n (n = length of s)

# For example, suppose s =  ABCDADIIID       
#                         -10123456789
#                          ^  ^ ^
# for d at j = 2: (3- -1) * (5-3) = 4*2 = 8 substrings, and they are: 
# ABCD, BCD, CD, D
# ABCDA, BCDA, CDA, DA

# So we do the following: 
# - Go through s to find the index of char. Put it in a hash map (call it "index") with the key = char, value = list.
#   At the front of the list is -1 and at the back is an n index for the left and right most based calculations.  
# - Then for each char in the index, do a for loop from 1 to m - 1, calculate the # substrings with char of 1 occurrance
#   using the formula (*) we discussed in the rationale. Add that to the result. 

# Time: O(n) time for effectively 2 traversals through s. 
# Space: O(n) for the organization of the indices in index. 


def buildIndex(s): 
    index = defaultdict(list)
    for i, char in enumerate(s):
        if char not in index: 
            index[char].append(-1)          
        index[char].append(i)
    for char in index: 
        index[char].append(len(s))
    return index

from collections import defaultdict
class Solution:
    def uniqueLetterString(self, s: str) -> int:
        index = buildIndex(s)
        res = 0
        for char in index: 
            charIndex = index[char]
            m = len(charIndex)
            for x in range(1, m-1): 
                i, j, k = charIndex[x-1], charIndex[x], charIndex[x+1]
                subStringsOnLeft, subStringsOnRight = (j - i), (k - j)
                res += subStringsOnLeft * subStringsOnRight
        return res % (10**9 + 7)

sol = Solution()
s = "LEETCODE"
s = "ABC"
s = "ABA"
s = ""
# s = "AAAAABBBBB" # 20
print(sol.uniqueLetterString(s))

# x = defaultdict(list)
# x["a"] += 1
# print(x["a"])