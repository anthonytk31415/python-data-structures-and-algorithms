# https://leetcode.com/problems/reverse-nodes-in-k-group/description/
# 25. Reverse Nodes in k-Group

# 7:20pm 8:10pm

# keep two pointers: 
# - at the head (to return)
# - the end of an already reversed segment, so you can attack stuff to 

# iterate through the LL as follows: 
# - count k nodes
#   - if there's k nodes: 
#       - break of the ending node, 
#       - then reverse those nodes, 
#       - and attach the head to end's "next"; 
#       - then cycle define a new end
#   - else, 
#       - attach that head to the end's next
#       - return the head

# O(n) Time and Space implementation

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseListHelper(root, reversed):
    if not root: 
        return reversed
    headReversed = root
    newRoot = root.next
    headReversed.next = reversed
    return reverseListHelper(newRoot, headReversed) 

def reverseList(root): 
    return reverseListHelper(root, None)

# must have length >= k
def getKthNode(root, k): 
    node = root
    for _ in range(k): 
        node = node.next
    return node

# returns [bool, reversedNode, NextNode]; 
# if True, then it returns the head of the reversed, and the next node
# if False, then it returns None, and the rest of the nodes < k
def nextKNodes(root, k): 
    node = root
    for _ in range(k):  
        if node: 
            prev = node
            node = node.next
        else: 
            return [False, None, root]    
    prev.next = None    
    return [True, reverseList(root), node]

def reverseKHelper(head, k, reversedTail):
    hasNextK, reversedNode, nextNode = nextKNodes(head, k)
    if hasNextK: 
        reversedTail.next = reversedNode
        reverseKHelper(nextNode, k, getKthNode(reversedTail, k))
    else: 
        reversedTail.next = head        
        return  

def reverseK(head, k): 
    reversedHead = ListNode()
    reversedTail = reversedHead
    reverseKHelper(head, k, reversedTail)    
    return reversedHead.next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        return reverseK(head, k)
    
    
    