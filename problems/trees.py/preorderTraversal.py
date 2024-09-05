# binary treen preorder traversal 

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def preorderTraversal(root): 
    def helper(root): 
        res = []
        if not root: return res
        res.append(root.val)
        if root.left: 
            res += helper(root.left)
        if root.right: 
            res += helper(root.right)
        return res
    
    return helper(root)