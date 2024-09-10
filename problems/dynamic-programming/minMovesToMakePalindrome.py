from functools import cache
from math import inf

# https://leetcode.com/problems/minimum-number-of-moves-to-make-palindrome/description/
# 2193. Minimum Number of Moves to Make Palindrome

# Greedy approach. Each iteration, you want to take off the last element and bring the first element you find that 
# equals the last element to the front. 
# Why does this work? Work it out on paper. Either way you choose, whether its the last elemtn with the first, the first 
# with the last, the last with the 2nd to earliest element that's equal, you'll end up with the same palindrome. 
# So just take the earliest one. 
# if you have a solo element, your length is odd and you bring that end element to the middle: so += i//2. 
# So you can greedily swap.

# O(n**2) Time for the swaps, pop from the front or where is for each function called n times iteratively.
# O(n) space for the list. 

def minMovesToMakePalindrome(s):
    s = list(s)
    count = 0
    while s: 
        i = s.index(s[-1])
        if i == len(s) - 1: 
            count += i//2
        else: 
            count += i
            s.pop(i)
        s.pop()
    return count


# this is too slow; O(n^3) time complexity
def minMovesToMakePalindrome1(s):
    # print(s)
    @cache
    def helper(s):
        n = len(s)
        if len(s) <= 1: 
            return 0
        if s[0] == s[-1]: return helper(s[1:-1])

        # swap from front
        res = inf
        for i in range(1, n - 1): 
            if s[i] == s[-1]: 
                count = i
                newStr = s[:i]+s[i+1:-1]
                res = min(res, count + helper(newStr))

        for i in range(n - 2, 0, -1): 
            if s[i] == s[0]: 
                count = n - 1 - i 
                newStr = s[1:i] + s[(i+1):]
                res = min(res, count + helper(newStr))
        return res

    return helper(s)    

s = "letelt"

i = s.index("t")
print(i)

# s = "twytxtflgxpltsfywpgs"
# s = "aabb"
# s = "aa"
# print(len(s[1:-1]))

print(minMovesToMakePalindrome(s))