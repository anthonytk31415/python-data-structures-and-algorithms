# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iii/?envType=company&envId=amazon&favoriteSlug=amazon-three-months
# 1650. Lowest Common Ancestor of a Binary Tree III

# Amazon
# dfs downward on p to find q, and if found, return p. otherwise do again for q and p. 
# If not found, dfs upward twice. Once for p. Then again for q. When dfsUp on q, the 
# moment you find a common ancestor, return int

# Time: O(n) for n nodes in the tree...
# Space: O(n) 

def dfsDown(root, node): 
    if root == node: return True
    if not root: return False
    return dfsDown(root.left, node) or dfsDown(root.right, node)

def dfsUp(node, path): 
    if not node: return set(path)
    return dfsUp(node.parent, path + [node.val])

def dfsUpStopAtParent(node, setPath): 
    if node.val in setPath: return node
    return dfsUpStopAtParent(node.parent, setPath) 

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        if dfsDown(p, q): return p
        if dfsDown(q, p): return q        
        pathP = dfsUp(p, [])
        return dfsUpStopAtParent(q, pathP)
        