# https://leetcode.com/problems/number-of-good-leaf-nodes-pairs/solutions/?envType=problem-list-v2&envId=binary-tree
# 1530. Number of Good Leaf Nodes Pairs

from collections import Counter

# What information do you need to solve recursively this answer? 
# O(n) time; O(logn) space


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def countPairs(root: TreeNode, distance: int) -> int:

    counter = [0]

    # helper returns a hash: dist from current node: countLeaves
    def dfs(node): 
        res = Counter()
        if not node: return res
        if node.left == None and node.right == None: 
            res[0] += 1
            return res  
        leftCount, rightCount = dfs(node.left), dfs(node.right)
        # add leaves to res       
        for y in rightCount: 
            if y + 1 <= distance: res[y + 1] += rightCount[y]
        for x in leftCount: 
            if x + 1 <= distance: res[x + 1] += leftCount[x]
        # check condition if pairs are within distance, add to count
        for x in leftCount: 
            for y in rightCount:                     
                newCount = leftCount[x]*rightCount[y]                                        
                if x + y + 2 <= distance: 
                    counter[0] += newCount
        return res  
          
    dfs(root)
    return counter[0]