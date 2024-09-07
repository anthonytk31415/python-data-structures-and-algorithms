# https://leetcode.com/problems/palindromic-substrings/description/
# 647. Palindromic Substrings



def countSubstrings(s):

    count = 0
    for i in range(len(s)):        
        d = 1
        # check for free 1-middle
        while 0 <= i - d < len(s) and 0 <= i + d < len(s)  and  s[i + d] == s[i - d]: 
            # print(i-d, i, i+d, s[i-d:i+d], d)
            d += 1
        # add d + 1
        count += d 
        # print("count0: ", count)
        d = 0
        # check for no middle
        while 0 <= i - d - 1< len(s) and 0 <= i + d < len(s)  and  s[i - d - 1] == s[i + d]: 
            d += 1
            # print(i-d-1, i, i+d, s[i-d-1:i+d+1], d)
        # add d
        count += d 
        # print("count1: ", count)
    return count



s = "abcba"
print(countSubstrings(s))