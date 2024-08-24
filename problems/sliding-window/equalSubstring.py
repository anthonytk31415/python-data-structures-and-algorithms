# https://leetcode.com/problems/get-equal-substrings-within-budget/description/
# 1208. Get Equal Substrings Within Budget


def equalSubstring(s: str, t: str, maxCost: int) -> int:

    def getCost(i): 
        return abs(ord(s[i]) - ord(t[i]))

    left, curCost, res = 0, 0, 0
    for right in range(len(s)):
        curCost += getCost(right)
        while curCost > maxCost and left < right: 
            curCost -= getCost(left)
            left += 1
        if curCost <= maxCost: 
            res = max(res, right - left + 1)
    return res

s = "abcd"
t = "bcdf"
maxCost = 3

s = "abcd"
t = "cdef"
maxCost = 3

print(equalSubstring(s, t, maxCost))


print(s.charAt(0))