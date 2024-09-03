# https://leetcode.com/problems/sum-of-digits-of-string-after-convert/description/?envType=daily-question&envId=2024-09-03
# 1945. Sum of Digits of String After Convert

def getLucky(s: str, k: int) -> int:
    x = ""
    for c in s: 
        x += str(ord(c) - ord("a") + 1)
    for _ in range(k): 
        xNew = 0
        for c in x: 
            xNew += int(c)
        x = str(xNew)
    return int(x)