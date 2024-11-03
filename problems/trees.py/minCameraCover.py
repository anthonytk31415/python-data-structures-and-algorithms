# https://leetcode.com/problems/binary-tree-cameras/description/
# 968. Binary Tree Cameras


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# We solve this recursively and use those results to decide our answer at the current node. 
# cameraCover works as follows: 
#  - returns (numNodesRequired, isMarked, isCovered)
#  - numNodesRequired is the number of nodes required in that given subtree 
#  - isMarked = True if the node contains a camera
#  - isCovered = True if it's covered by itself or a descendent
# Our base case is when we are at a leaf, in which case we return [0, F, F]
# We want to percolate our covered nodes up to the parent as much as possible. 
# At our current node, if we have a child, we call cameraCover on the child. 
# If the child is not covered, we cover it at the current node. 
# If the child is marked, then the current node is covered. 
# We then return the result for the next iteration to happen. 

# In our main function, we call Camera cover. If the result isn't covered, we add 1 to our 
# result. 

# Time: O(n) since we must traverse all nodes. 
# Space: O(n) since we have O(n) calls in the call stack. 

def isLeaf(root): 
    return not root.left and not root.right

# returns (numNodesRequired, isMarked, isCovered)
# isMarked = True if the node contains a camera
# isCovered = True if it's covered by itself or a descendent
def cameraCover(root): 
    if isLeaf(root): 
        return [0, False, False]
    nodesRequired = 0
    isMarked = isCovered = False
    for child in [root.left, root.right]: 
        if child: 
            childNodesRequired, childMarked, childCovered = cameraCover(child)
            nodesRequired += childNodesRequired            
            if not childCovered: 
                isMarked = isCovered = True
            if childMarked: isCovered = True
    if isMarked: nodesRequired += 1
    return [nodesRequired, isMarked, isCovered]
        
    
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        nodes, _, isCovered = cameraCover(root)
        if not isCovered: return nodes + 1
        return nodes