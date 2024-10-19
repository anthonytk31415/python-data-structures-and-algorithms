# 1048. Longest String Chain
# https://leetcode.com/problems/longest-string-chain/description/


#O(N)
def putWordsIntoDictionary(words): 
    wordsByLength = {}
    for word in words: 
        if len(word) not in wordsByLength: 
            wordsByLength[len(word)] = {}
        wordsByLength[len(word)][word]=1
    return wordsByLength

# O(L^2)
def getMax(word, wordsByLength): 
    n = len(word)
    curMax = 0
    if n - 1 not in wordsByLength: return curMax 
    for i in range(0, len(word)): 
        prevWord = word[:i] + word[i+1:]
        if prevWord in wordsByLength[n-1]: 
            curMax = max(curMax, wordsByLength[n - 1][prevWord])
    return curMax

# O(n)
def longestStrChain(words: list[str]) -> int:
    wordsByLength = putWordsIntoDictionary(words)   
    res = 1
    for i in range(1, 17): 
        if i in wordsByLength: 
            wordList = wordsByLength[i]
            for word in wordList: 
                curRes = 1 + getMax(word, wordsByLength)
                wordsByLength[len(word)][word] = curRes
                res = max(res, curRes)
    return res

words = ["a","b","ba","bca","bda","bdca"]
words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
print(longestStrChain(words))

