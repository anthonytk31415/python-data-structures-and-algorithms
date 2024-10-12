# https://leetcode.com/problems/reorganize-string/description/
# 767. Reorganize String




def reorganizeString(s):
    countChars = {}
    
    for char in s: 
        if char not in countChars: 
            countChars[char] = 0
        countChars[char] += 1
    


    return s