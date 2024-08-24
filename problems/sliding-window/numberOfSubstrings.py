# https://leetcode.com/problems/count-the-number-of-substrings-with-dominant-ones/
# 3234. Count the Number of Substrings With Dominant Ones

import math

def numberOfSubstrings(s):

    # zeroes = 0
    ones = 0
    left = 0
    count = 0
    for right in range(len(s)):
        if s[right] == "1": ones += 1
        # else: zeroes += 1
        while left < right and s[left] != "1":            
            left += 1
        
        while ones < (right - left + 1 - ones)**2 and left <= right:
            if s[left] == "1": ones -= 1
            left += 1 

        if ones > 0:
            numZeroes = right - left + 1 - ones
            canSupport = int(math.sqrt(ones)) - numZeroes
            print("numZeroes: {}, canSupport: {}, right: {}, left: {}".format(numZeroes, canSupport, right, left))
            addition = (right - left + 1) + min(left, canSupport)
            print("addition: ", addition)
            count += addition

    return count

s = "00011"
s = "101101"
# s = "1"


print(numberOfSubstrings(s))