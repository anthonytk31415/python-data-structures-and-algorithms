from collections import Counter
from math import inf 


# y = Counter(x)
# print(y)

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
        # print("cond check: ", countWindow, countLargestChar, "res: ", res)
        return res

    window = Counter()      # this represents a valid window that includes right
    res = -inf
    left = 0
    curSum = 0
    for right in range(len(s)):
        window[s[right]] += 1
        curSum += 1
        # print(right, curSum)
        while not isWindowValid(window, k) and left < right: 
            window[s[left]] -= 1
            curSum -= 1
            left += 1   

        # print(window, curSum)
        if isWindowValid(window, k):
            # print("an answer: ", left, right, curSum)
            res = max(res, curSum)
    return res


s = "AABABBA"

k = 1

print(charReplacement(s, k))