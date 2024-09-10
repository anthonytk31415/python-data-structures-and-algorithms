# https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/?envType=daily-question&envId=2024-09-10
# 2807. Insert Greatest Common Divisors in Linked List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from numpy import gcd


print(gcd(18,6))

def insertGreatestCommonDivisors(head): 

    node = head
    while node: 
        if node.next: 
            next = node.next
            newNode = ListNode(gcd(node.val, next.va))
            node.next = newNode
            node = node.next
            node.next = next
        node = node.next
        
    return head