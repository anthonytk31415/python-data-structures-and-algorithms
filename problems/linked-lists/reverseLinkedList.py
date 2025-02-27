# recursive reverse linked list implementation

class ListNode: 
    def __init__(self, val = None):
        self.val = val
        self.next = None

def reverseLinkedList(node): 
    head = ListNode()    
    return helper(node, head)

# attah begining of node to 
def helper(node, head): 
    if not node: return head
    newNode = node.next
    node.next = head
    return helper(newNode, node)

dummy = ListNode()
node = dummy
for x in range(5): 
    node.next = ListNode(x)
    node = node.next
    


def printNode(root): 
    node = root
    while node: 
        print(node.val)
        node = node.next

printNode(dummy.next)
reversed = reverseLinkedList(dummy.next)
printNode(reversed)