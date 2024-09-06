# https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array/description/
# 3217. Delete Nodes From Linked List Present in Array

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def modifiedList(nums: list[int], head): 

    nums = set(nums)
    dummy = ListNode
    dummy.next = nums
    node = dummy.next
    prev = dummy
    while node: 
        if node.val in nums: 
            prev.next = node.next            
            node.next = None
            node = prev.next                
        else: 
            prev = node
            node = node.next
    return dummy.next

