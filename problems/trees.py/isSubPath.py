# https://leetcode.com/problems/linked-list-in-binary-tree/description/
# 1367. Linked List in Binary Tree


# For each node in the binary tree, we must call isPath to see if there's
# a valid path. We'll do this recursively so we can stop if our current
# node returns True. If not, we'll recursively call isBinaryPath on the 
# root's children, and traverse deeper into the Tree, calling isBinaryPath. 

# isPath will recursively check if the current node equals  
# the current node in the linked list, and if so, will recursively call 
# the left and right children of the root on the next node in the linked
# list until the linked List reaches the null pointer, at which point, 
# it should return True. If the values of the root and head don't match 
# ever, we return False. 

# Time: O(mn) for m nodes in the tree root, n nodes of the linked list
# you must traverse the linked list m times in the worst case
# Space: O(m) for m nodes in the tree, for the call stack of the recursive 
# output.

def isPath(root, head): 
    if not head: return True
    if not root: return False
    if root.val == head.val: return isPath(root.left, head.next) or isPath(root.right, head.next)
    return False

def isBinaryPath(root, head): 
    if not head: return True
    if not root: return False
    if isPath(root, head): return True
    return isBinaryPath(root.left, head) or isBinaryPath(root.right, head) 

class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        return isBinaryPath(root, head)
    
    
# Test cases: 
# root = [1]
# head = []
# True

# root = []
# head = [1]
# False

# root = []
# head = []
# True

# root = [1,2]
# head = [2]
# True

# root = [1,2,99,null, 2, 2, null, 3]
# head = [1,2,3]
# True