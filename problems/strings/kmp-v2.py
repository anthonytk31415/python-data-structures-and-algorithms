# kmp

 
# aaaaba

def build_lps(pat): 
    lps = [0]*len(pat)
    length = 0
    i = 1
    while i < len(pat): 
        if pat[i] == pat[length]: 
            length += 1
            lps[i] = length
            i += 1
        else: 
            if length > 0: 
                length = lps[length - 1]
            else:                 
                i += 1
    return lps

def kmp(text, pat):
    lps = build_lps(pat)
    i = j = 0
    res = []
    while i < len(text): 
        if text[i] == pat[j]: 
            i += 1
            j += 1
            if j == len(pat): 
                res.append(i - j)
                j = lps[j - 1]
        else: 
            if j > 0: 
                j = lps[j - 1]
            else:                 
                i += 1
    return res

text = "xxxabababxxxababab"
pat = "abab"

print(kmp(text, pat))



