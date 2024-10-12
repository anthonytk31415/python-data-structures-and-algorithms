# https://leetcode.com/problems/longest-palindromic-substring/
# 5. Longest Palindromic Substring

# increment: 0 for odd, 1 for even
def getLongestOdd(s, i): 
    res = s[i]
    for delta in range(1, len(s) - i): 
        if i - delta < 0 or s[i - delta] != s[i + delta]: 
            break 
        res = s[i - delta] + res + s[i + delta]
    return res

def getLongestEven(s, i): 
    res = ""
    for j in range(len(s) - (i+1)): 
        if i-j < 0 or s[i-j] != s[i+1+j]: 
            break
        res = s[i-j] + res + s[i+1+j]
    return res

def longestPalindrome(s):
    res = ""    
    for i in range(len(s)): 
        curRes = getLongestOdd(s, i)
        if len(curRes) > len(res): 
            res = curRes

    for i in range(len(s) - 1): 
        curRes = getLongestEven(s, i)
        if len(curRes) > len(res): 
            res = curRes
    return res


s = "zyabayi"
s = "abaabcdzabbaz"
print(longestPalindrome(s))
