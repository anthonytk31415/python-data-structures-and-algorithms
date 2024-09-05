# https://leetcode.com/problems/longest-string-chain/
# 1048. Longest String Chain

from collections import defaultdict

# dp type questions with a dfs
# since longest word is 16, bucket words by length. each word has a chain of longer words. 
# so iterate from 16 to 1 inclusive, then over each word to find the largest chain from that word. 
# keep running maxLength

# O(n) time and space where you do things  26 times but constantly. 

def longestStrChain(words: list[str]) -> int:
    wordsByLength = [defaultdict(int) for _ in range(17)] # int length -> words
    for word in words: 
        i = len(word)
        wordsByLength[i][word] = 1

    def checkWord(word, wordsByLength):
        n = len(word)
        maxLength = 1
        for i in range(n+1):
            for char in "abcdefghijklmnopqrstuvwxyz":
                newWord = word[:i] + char + word[i:]
                if newWord in wordsByLength[n+1]: 
                    maxLength = max(maxLength, wordsByLength[n+1][newWord] + 1)        
        wordsByLength[n][word] = maxLength
        return maxLength

    maxLength = 1
    for i in range(15, 0, -1): 
        for word in wordsByLength[i]:              
            curMaxLength = checkWord(word, wordsByLength)
            maxLength = max(curMaxLength, maxLength)    
    
    return maxLength

words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
words = ["a","b","ba","bca","bda","bdca"]

print(longestStrChain(words))