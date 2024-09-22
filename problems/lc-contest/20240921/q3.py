# https://leetcode.com/problems/count-substrings-that-can-be-rearranged-to-contain-a-string-i/description/
# 3297. Count Substrings That Can Be Rearranged to Contain a String I

from collections import Counter

def checkWindow(window, word2): 
    for x in word2:
        if x in window and word2[x] <= window[x]: continue
        else: return False
    return True 


# window = Counter("aa")
# word2 = Counter("abc")
# print(checkWindow(window, word2))

def validSubstringCount(word1: str, word2: str) -> int:
    window = Counter()
    word2 = Counter(word2)
    j = 0       # keep the 
    res = 0
    for i, char in enumerate(word1):
        # add element to window
        # print("initiating: ", window, char, i)
        window[char] += 1
        # print(window)
        # if valid window, get smallest window that's valid
        if checkWindow(window, word2): 
            # print("valid window: ", window, word2)
            
            while window[word1[j]] > word2[word1[j]]: 
                window[word1[j]] -= 1
                j += 1
            # then add length of result
            res += j- 0 + 1
    return res

word1 = "bcca"
word2 = "abc"

word1 = "abcabc"
word2 = "abc"


word1 = "abcabc"
word2 = "aaabc"

word1 = "dabc"
word2 = "abc"

print(validSubstringCount(word1, word2))