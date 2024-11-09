# https://leetcode.com/problems/all-possible-full-binary-trees/description/
# 894. All Possible Full Binary Trees

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Approach: 
# We do a DP approach with memoization. Iterate k from 1 to n inclusive to create 
# the trees at each k. For each k, we realize that each valid tree has L left nodes
# and R right nodes where L + R = k - 1 and L or R must be odd. Further, each child
# subtree can take the form createTree(l). So for each ltree in L and for each rtree
# in R, we create a tree and add it to our result. Then we memoize our result for 
# each k. We then return memo[n]. 


# Base cases: 
#     k = 1: return a single tree node. 
#     k even: return the empty list of trees, since its impossible 
#     to create a full binary tree for even nodes. 

# Note: we create a createCopy(node) function to create deep copies of our trees to 
#     store them in our memo

# Time: O(2^n) since for each call, we'll match up 2^n pairs together. 
# Space: O(2^n) since we need to store 2^n subtrees for each k. 



def createCopy(node): 
    if not node: return None
    return TreeNode(node.val, createCopy(node.left), createCopy(node.right))
    
def createTrees(i, memo): 
    if i in memo: return memo[i]
    res = []
    if i == 1: res.append(TreeNode())
    else: 
        for k in range(1, i-1, 2): 
            left = memo[k]
            right = memo[i - k - 1]
            for lnode in left: 
                for rnode in right: 
                    newNode = TreeNode(0, createCopy(lnode), createCopy(rnode))
                    res.append(newNode)                    
    memo[i] = res
    return res

class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        memo = {}
        if n % 2 == 0: return []
        for i in range(1, n + 1): 
            createTrees(i, memo)
        return memo[n]        
