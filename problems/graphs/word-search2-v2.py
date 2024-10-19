# https://leetcode.com/problems/word-search-ii/description/
# 212. Word Search II

# Build a trie, which is a tree with many children. 
# In this case, 26 of them (1 per lower-case letter). 
# We first build the trie and insert words in the trie in O(len(word))
# time for each word. 

# Then for each cell (i, j), we dfs if that letter is a valid next word
# in the trie in a backtracking fashion, never going back to a cell we
# visited in the current path. But we could visit the same cell twice 
# if we backtracked and arrived there again from a different route since
# that represents a potentially different word. If we find a word, 
# we return it. We only stop when we have exhausted our options (no more
# directions to go, no words in the dictionary, out of bounds).

# Complexity Analysis: 
# Time: O(mn*3^t), m= rows, n = cols, t = max length of each word in words. 
# Logic is we start at each mn, and we maximally traverse 3 directions (not
# from where we came from), and we go a length of t maximally. 
# Space: O(k) for k = sum of length of total words in the worst case, if 
# we have all unique words that do not overlap.


class TrieNode: 
    def __init__(self): 
        self.isWord = False
        self.children = {}


def insertWordIntoTrie(word, node): 
    for c in word: 
        if c not in node.children: 
            node.children[c] = TrieNode()
        node = node.children[c]
    node.isWord = True


def buildTrie(words): 
    tree = TrieNode()
    for word in words: 
        insertWordIntoTrie(word, tree)
    return tree

def dfs(i, j, node, curWord, visited, res, board): 
    visited.add((i, j))     # visit a node, but don't return to it on the trip
    if node.isWord: 
        res.add(curWord)        
    for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]: 
        u, v = i + di, j + dj
        if 0 <= u < len(board) and 0 <= v < len(board[0]) and (u, v) not in visited and board[u][v] in node.children: 
            dfs(u, v, node.children[board[u][v]], curWord + board[u][v], visited, res, board) 
    visited.remove((i, j))  # remove node so that you can visit again on a another distinct trip


def findWords(board: list[list[str]], words: list[str]) -> list[str]:
    trie = buildTrie(words)
    res = set()
    for i in range(len(board)): 
        for j in range(len(board[0])): 
            if board[i][j] in trie.children: 
                visited = set()
                dfs(i, j, trie.children[board[i][j]], board[i][j], visited, res, board)            
    return res

board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
words = ["oath","pea","eat","rain"]

# board = [["a","b"],["c","d"]]
# words = ["abd"]

print(findWords(board, words))