
# https://leetcode.com/problems/minimum-window-substring/description/?envType=study-plan-v2&envId=top-interview-150
# 76. Minimum Window Substring

# Iterate right across the string. put chars in a hash map (counter) for comparison with a hash map of t. If you have a valid window, 
# try to shrink the window by removing s[left]. If it's not valid, add it back in. If it's still valid, update res. 

from collections import Counter

def minWindow(s: str, t: str) -> str:

    def check(sCounter, tCounter):
        for y in tCounter: 
            if y not in sCounter or sCounter[y] < tCounter[y]: return False
        return True

    sCounter, tCounter = Counter(), Counter(t)
    left, res = 0, ""
    for right in range(len(s)):
        sCounter[s[right]] += 1
        # if counters are valid try to reduce the window to see if it's still valid
        if check(sCounter, tCounter): 
            while left < right: 
                # start with removing, if it's valid then continue, if not, then add it back in
                sCounter[s[left]] -= 1
                if sCounter[s[left]] == 0 : del sCounter[s[left]]
                if not check(sCounter, tCounter): 
                    sCounter[s[left]] += 1
                    break 
                else: 
                    left += 1
        # if it's valid, update res              
            if res == "" or (right - left + 1) < len(res): 
                res = s[left:(right + 1)]
    return res


s = "ADOBECODEBANC"
t = "ABC"

s = "a"
t = "aa"

s = "a"
t = "a"


s = "aaabaaaaaa"
t = "aaaaa"

s = "ab"
t = "a"

# print(s[0:0+1])

print(minWindow(s, t))

