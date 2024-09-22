from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.words = set()
        self.children = defaultdict(TrieNode)

class WordFilter:

    def __init__(self, words: list[str]):
        self.trie = TrieNode()
        self.words = words
        self.insertWordsIntoTrie(words)
        
    def insertWordIntoTrie(self, word): 
        node = self.trie
        self.trie.words.add(word)
        for w in word: 
            node = node.children[w]
            node.words.add(word)
            

    def insertWordsIntoTrie(self, words): 
        for word in words: 
            self.insertWordIntoTrie(word)
        return


    def f(self, pref: str, suff: str) -> int:
        res = -1
        # traverse to pref
        # 
        return res
    



