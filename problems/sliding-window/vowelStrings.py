# https://leetcode.com/problems/count-vowel-strings-in-ranges/
# 2559. Count Vowel Strings in Ranges


# prefix sum
# is prefix a sliding window implementation? 
# O(n) Time, Space: O(n)

def vowelStrings( words: list[str], queries: list[list[int]]) -> list[int]:
    vowels = "aeiou"
    prefix = [word[0] in vowels and word[-1] in vowels for word in words]
    prefix = [int(x) for x in prefix]
    for i in range(1, len(prefix)): 
        prefix[i] = prefix[i] + prefix[i-1]

    def getPrefix(start, end):
        if start == 0: return prefix[end]
        else: return prefix[end] - prefix[start - 1]

    res = []
    for start, end in queries: 
        curRes = getPrefix(start, end)
        res.append(curRes) 

    return res

words = ["aba","bcb","ece","aa","e"]
queries = [[0,2],[1,4],[1,1]]

print(vowelStrings(words, queries))