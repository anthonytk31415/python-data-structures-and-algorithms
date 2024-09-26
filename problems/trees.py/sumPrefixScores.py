# https://leetcode.com/problems/sum-of-prefix-scores-of-strings/description/
# 2416. Sum of Prefix Scores of Strings

# Trie Implementation. At each letter in a word, first, keep track of count of owrds at that letter. 
# Then for each word, traverse, and keep track of the count as you "dfs" the trie.

# O(mn) Time and Space


from collections import defaultdict

class TrieNode: 
    def __init__(self): 
        self.count = 0
        self.children = defaultdict(TrieNode)
        

def insertWord(node, word): 
    for w in word: 
        node = node.children[w] 
        node.count += 1

def getPrefixCount(node, word): 
    res = 0
    for w in word: 
        node = node.children[w] 
        res += node.count
    return res 

class Solution:
    def sumPrefixScores(self, words: list[str]) -> list[int]:
        trie = TrieNode()
        for word in words: 
            node = trie
            insertWord(node, word)
        res = []
        for word in words: 
            node = trie
            res.append(getPrefixCount(node, word))
        return res
    
words = ["abc","ab","bc","b"]
s = Solution()
print(s.sumPrefixScores(words))


z = ["/\\","\\/"]
for x in z: 
    print(x)