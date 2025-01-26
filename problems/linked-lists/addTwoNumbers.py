# https://leetcode.com/problems/add-two-numbers/description/
# 2. Add Two Numbers
# sample for code practice

# Definition for singly-linked list. Add numbers using linked
# list and carry. 
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    dummy = ListNode()
    carry = 0
    node = dummy
    while l1 and l2: 
        curSum = l1.val + l2.val + carry
        carry = 0
        if curSum > 9: 
            carry = 1
            curSum = curSum % 10
        node.next = ListNode(curSum)
        node = node.next
        l1, l2 = l1.next, l2.next      
    if l2: l1 = l2  
    while l1: 
        curSum = l1.val + carry
        carry = 0 
        if curSum > 9: 
            carry = 1
            curSum = curSum %10
        node.next = ListNode(curSum)
        node = node.next
        l1 = l1.next
    if carry > 0: 
        node.next = ListNode(carry)
        node = node.next
    return dummy.next
