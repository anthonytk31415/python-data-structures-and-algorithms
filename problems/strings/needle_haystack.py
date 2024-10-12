def find(needle, haystack):
    for i in range(len(haystack)):
        if haystack[i] == haystack[0] and isMatch(needle, haystack, i): 
            return i
    return -1


def isMatch(needle, haystack, i): 
    for j in range(len(needle)): 
        if i + j >= len(haystack): return False
        if haystack[i + j] != needle[j]: return False
    return True

haystack = 'playpp'
needle = 'pen'
print(find(needle, haystack))
