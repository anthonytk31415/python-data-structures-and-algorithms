# https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/description/?envType=daily-question&envId=2024-08-04
# 1171. Remove Zero Sum Consecutive Nodes from Linked List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeZeroSumSublists(head):
    def helper(head):
        stack = []
        dummy = ListNode()
        dummy.next = head
        node = dummy.next
        curNode = 0
        prefix = {}
        while node: 
            if -node.val in prefix or node.val == 0: 
                if node.val != 0: 
                    for _ in range(curNode - prefix[-node.val]):
                        stack.pop()
                if stack: 
                    stack[-1].next = node.next
                else: 
                    dummy.next = node.next
                return dummy.next, True
            else: 
                newPrefix = {}
                for x in prefix: 
                    newPrefix[x + node.val] = prefix[x]
                newPrefix[node.val] = curNode
                prefix = newPrefix
                stack.append(node)
                node = node.next
                curNode += 1 
        return dummy.next, False
    
    node, check = helper(head) 
    while check:
        # print(node.val)
        node, check = helper(node)
    return node 

dummy = ListNode()
node = dummy
# for x in [1,2,-3,3,1]: 
# for x in [1,2,3,-3,-2]: 
for x in [0]: 
    node.next = ListNode(x)
    node = node.next


# node = dummy.next
# while node: 
#     print(node.val)
#     node = node.next

x = removeZeroSumSublists(dummy.next)

node = x
while node: 
    print(node.val)
    node = node.next
