# https://leetcode.com/problems/adding-spaces-to-a-string/
# 2109. Adding Spaces to a String

# in my solution, I added sentinel values on spaces so you always take i, i+1
# use sentinel values on spaces for convenience. 

# Time and space: O(n)

class Solution:
    def addSpaces(self, s: str, spaces: list[int]) -> str:
        spaces = [0] + spaces + [len(s)]
        res = []
        for i in range(len(spaces)-1): 
            start, end = spaces[i], spaces[i+1]
            res.append(s[start:end])
        return " ".join(res)
