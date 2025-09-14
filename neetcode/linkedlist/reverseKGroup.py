# https://neetcode.io/problems/reverse-nodes-in-k-group?list=neetcode150




# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# counts k, reverses and returns the head and the tail for you to attach
# if less than k, then just returns the head and tail unreversed. 

def hasKNodes(node, k): 
    curNode = node
    for _ in range(k):         
        if not curNode: 
            return False 
        curNode = curNode.next
    return True

def getNextK(node, k):
    
    if not hasKNodes(node, k): 
        return node, None, None
    
    
    dummy = ListNode()
    head = dummy
    
    nextNode = node

    for _ in range(k): 
        

     
    
    return dummy.next, head, nextNode, 

def reverseKGroup(head, k): 
    dummy = ListNode()
    tail = dummy
    node = head    
    # keep snipping off k, perform the op, then attach to
    while node: 
        curHead, curTail, nextHead = getNextK(node, k)
        tail.next = curHead
        tail = curTail
        node = nextHead                 
    
    return dummy.next