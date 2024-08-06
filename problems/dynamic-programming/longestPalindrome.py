# https://leetcode.com/problems/longest-palindromic-substring/description/?envType=study-plan-v2&envId=top-interview-150
# 5. Longest Palindromic Substring

# Time: O(mn), Space: O(1) 

def longestPalindrome(s):
    if len(s) <= 1: return len(s)

    palindrome = s[0]
    # check middle
    for i in range(len(s)):
        curRes = s[i]
        for d in range(1, len(s) - i):
            if 0 <= i - d < len(s) and s[i - d] == s[i + d]: curRes = s[i - d] + curRes + s[i + d]
            else: break
        if len(curRes) > len(palindrome):
            palindrome = curRes

    for i in range(len(s)):
        curRes = ""
        for d in range(0, len(s) - i - 1):
            if 0 <= i - d < len(s) and s[i -    d] == s[i + 1 + d]: curRes = s[i - d] + curRes + s[i + 1 + d]
            else: break
        if len(curRes) > len(palindrome):
            palindrome = curRes 
            
    return palindrome

s = "aaaaaaaaab"
print(longestPalindrome(s))