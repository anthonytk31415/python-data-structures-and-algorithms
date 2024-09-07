# https://leetcode.com/problems/binary-tree-upside-down/description/
# 156. Binary Tree Upside Down


# https://interviewing.io/mocks/google-python-binary-tree-upside-down

# Given the root of a binary tree, turn the tree upside down and return the new root.
# You can turn a binary tree upside down with the following steps:

# The original left child becomes the new root.
# The original root becomes the new right child.
# The original right child becomes the new left child.

# The mentioned steps are done level by level. It is guaranteed that every right node has a sibling (a left node with the same parent) and has no children.

# Example 1:
# Input: root = [1,2,3,4,5]
# Output: [4,5,2,null,null,3,1]

# Example 2:
# Input: root = []
# Output: []

# Example 3:
# Input: root = [1]
# Output: [1]


# [1,2,3, 4, 5]

# newRoot = 4

#################
## sample call ##
# Call on 1: 
# oL = fn(2)
# oR = 3

# Call on 2: 
# root = 2
# oL = fn(4) = 4
# oR = 5
# oL.L = 5
# oL.R = 2
# 2.left = None, 2.right = None
# return 2

# Back to call on 1: 
# oL = 2 with no pointers
# 2.L = 3
# 2.R = 1
# 1.left = None, 1.right = None
# return 1





# traverse all the way to the left, then use helper to call on the left
def upsideDownBinaryTree(root):
    def helper(root): 
        if not root: return root
        if not root.left and not root.right: return root
        oldLeft = helper(root.left)
        oldRight = root.right
        oldLeft.left = oldRight
        oldLeft.right = root
        
        # the recursive call will set the return node's pointers, which will be the newLeft
        root.left = None
        root.right = None
        return root
                            
    # get to the left most node that iwll be our new root
    def getToLeft(root):
        node = root
        while node and node.left: 
            node = node.left        
        return node
                    
    newRoot = getToLeft(root)
    helper(root)
    return newRoot