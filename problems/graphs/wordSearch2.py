# https://leetcode.com/problems/word-search-ii/description/
# 212. Word Search II

# build a trie
# then for each cell, dfs forward as long as you have a word in a trie
# if you hit a word, add it. 

from collections import defaultdict

def findWords(board: list[list[str]], words: list[str]) -> list[str]:
    class TrieNode: 
        def __init__(self): 
            self.isWord = False
            self.children = defaultdict(TrieNode) 

    def buildTrie(words): 
        tree = TrieNode()

        def dfsInsert(word, node): 
            for c in word: 
                node = node.children[c]
            node.isWord = True

        for word in words: 
            dfsInsert(word, tree)
        return tree

    def dfs(i,j, node, curWord): 
        visited.add((i, j))
        if node.isWord: 
            res.add(curWord)        
        for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]: 
            u, v = i + di, j + dj
            if 0 <= u < len(board) and 0 <= v < len(board[0]) and (u, v) not in visited and board[u][v] in node.children: 
                dfs(u, v, node.children[board[u][v]], curWord + board[u][v]  ) 
        visited.remove((i, j))

    trie = buildTrie(words)
    res = set()
    for i in range(len(board)): 
        for j in range(len(board[0])): 
            if board[i][j] in trie.children: 
                visited = set()
                dfs(i, j, trie.children[board[i][j]], board[i][j])            
    return list(res)

board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
words = ["oath","pea","eat","rain"]

# board = [["a","b"],["c","d"]]
# words = ["abd"]

print(findWords(board, words))