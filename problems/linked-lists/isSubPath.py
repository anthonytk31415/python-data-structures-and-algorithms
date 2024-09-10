# https://leetcode.com/problems/linked-list-in-binary-tree/description/?envType=company&envId=amazon&favoriteSlug=amazon-thirty-days
# 1367. Linked List in Binary Tree

# KMP kind of. if an element equals the first part of the list node, try going deeper. 
# If you didnt terminate earlier, you always want to "try" starting for each node. 
# O(n) Time, you have to traverse the n nodes twice. 
# Space: O(h) for the height of the tree

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSubPath(head, root):
    def progressNode(node, root):
        if not node: 
            return True
        if not root: return False
        if node.val == root.val: 
            if progressNode(node.next, root.left): return True
            if progressNode(node.next, root.right): return True
        return False

    def dfs(root): 
        if root.val == head.val: 
            if progressNode(head, root): return True
        if root.left and dfs(root.left): return True
        if root.right and dfs(root.right): return True
        return False

    return dfs(head, root)


# extremely suppressed 
def isSubPath(head, root):
    def progressNode(node, root):
        if not node: return True
        if not root: return False
        if node.val == root.val: 
            return progressNode(node.next, root.left) or progressNode(node.next, root.right)
        return False

    def dfs(root): 
        if not root: return False
        return (root.val == head.val and progressNode(head, root)) or dfs(root.left) or dfs(root.right)
    return dfs(root)