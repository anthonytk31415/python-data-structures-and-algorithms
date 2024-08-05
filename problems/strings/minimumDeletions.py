# https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/description/?envType=daily-question&envId=2024-07-30
# 1653. Minimum Deletions to Make String Balanced

def minimumDeletions(s: str) -> int:
    s = " " + s + " "
    a, b = [0]*len(s), [0]*len(s)
    # a counts max a's from and up to i
    # b counts max b's past i
    for i in range(1, len(s)):
        if s[i] == "a": a[i] = a[i-1] + 1
        else: a[i] = a[i-1]
    
    for i in range(len(b) - 2, -1, -1):
        if s[i] == "b": b[i] = b[i+1] + 1
        else: b[i] = b[i+1]

    res = 0
    for i in range(len(a)):
        res = max(res, a[i] + b[i])
    return len(s) - 2 - res

s = "aababbab"
s = "bbaaaaabb"
print(minimumDeletions(s))
# examples: 
    # aababbab 
    #     --> aaabbb (remove b, then a --> 2)
    #     --> aaabbb (remove 2*a)


    # bbaaaaabb --> remove 2b at front --> aaaaabb -- OK
    # bbaaaaabbaa
    #     --> remove all b's x 4'
    #     --> remove bb first, aa last --> 4 
    

    # aaaabb
    # bbbbbbb
    # aaaaaa
    # < any number of a's>
    # <any number of a's> + <any number of b's>
    # <any number of b's>