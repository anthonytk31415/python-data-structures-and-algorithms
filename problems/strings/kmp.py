

# We create the pi or LPS table so that when a prefix appears also as a suffix of the pattern, 
# when we do comparisons with the text and pattern, if we do not equal, we don't have 
# to backtrack - we just go back to where the prefix ended. 


# compute the longest prefix that's a suffix 
def computeLps(pattern):
    i, length, n = 1, 0, len(pattern) 
    lps =  [0]*n
    while i < n: 
        if pattern[i] == pattern[length]: 
            length += 1
            lps[i] = length
            i += 1
        else: 
            if length != 0: 
                length = lps[length - 1]        # backtrack to the last seen prefix that's a suffix
            else: 
                lps[i] = 0                  
                i += 1
    return lps

# return a list of all starting indices of when the pattern fully appears in the text
def kmp(text, pattern): 
    lps = computeLps(pattern)
    i, j = 0, 0
    res = []    
    while i < len(text): 
        if text[i] == pattern[j]: 
            i += 1
            j += 1
            if j >= len(pattern): 
                res.append(i - j)   # insert the starting index
                j = lps[j-1]        # reset to the last prefix
        else: 
            if j > 0: 
                j = lps[j-1]        # reset to the last prefix that's a suffix
            else: 
                i += 1
    return res


a = "abbaabc"

text = "abbaabc"
pattern = "aab"






def computeLps1(pattern): 
    n, i, length = len(pattern), 1, 0
    lps = [0]*n
    while i < len(pattern):
        if pattern[i] == pattern[length]: 
            length += 1
            lps[i] = length
            i += 1
        else: 
            if length > 0: 
                length = lps[length - 1]
            else: 
                # lps[i] = 0
                i += 1
    return lps

def kmp1(text, pattern): 
    lps = computeLps1(pattern)
    i, j = 0, 0
    res = []
    while i < len(text): 
        if text[i] == pattern[j]: 
            i += 1
            j += 1
            if j == len(pattern): 
                res.append(i - j)
                j = lps[j - 1]
        else: 
            if j > 0: 
                j = lps[j - 1]
            else: 
                i += 1
    return res

text = "abbaabc"
pattern = "aab"

print(kmp1(text, pattern))




def computeLps2(pattern): 
    i, length, n = 1, 0, len(pattern)
    lps = [0]*n
    while i  < len(pattern): 
        if pattern[i] == pattern[length]: 
            length += 1
            lps[i] = length
            i += 1
        else: 
            if length > 0: 
                length = lps[length - 1]
            else: 
                i += 1
    return lps


def kmp2(text, pattern): 
    lps = computeLps2(pattern)
    i = j = 0
    res = []
    while i < len(text): 
        if text[i] == pattern[j]: 
            i += 1
            j += 1
            if j == len(pattern):
                res.append(i - j)
                j = lps[j-1]
        else: 
            if j >0: 
                j = lps[j-1]
            else: 
                i += 1
    return res

print(kmp2(text, pattern))