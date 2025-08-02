#https://leetcode.com/problems/merge-k-sorted-lists/description/

# Classic merge sort applied to k linked lists. 

# a and b are linked lists that are sorted

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge(a, b): 
    head = ListNode()
    c = head
    
    while a and b: 
        if a.val < b.val: 
            c.next = a
            a = a.next
        else: 
            c.next = b
            b = b.next
        c = c.next
    while a: 
        c.next = a
        a = a.next
        c = c.next
    while b: 
        c.next = b
        b = b.next
        c = c.next
    return head.next

def merge_cycle(lists): 
    new_lists = []
    for i in range(len(lists), 2): 
        if i + 1 >= len(lists): 
            new_lists.append(lists[i])
        else: 
            new_lists.append(merge(lists[i], lists[i+1]))
    return new_lists


# an iterative approach using merge_cycle
def mergeKLists(lists): 
    if not lists: 
        return None
    updated_list = [x for x in lists]
    while len(updated_list) > 1: 
        updated_list = merge_cycle(updated_list)
    return updated_list[0]



# recursive classical way to do mergesort
def mergesort(lists): 
    if not lists: 
        return None
    if len(lists) == 1: 
        return lists[0]
    mid = len(lists) // 2
    left = mergesort(lists[:mid])
    right = mergesort(lists[mid:])
    res = merge(left, right)
    return res


a_list = [1,4,6,7,10]
b_list = [2,3,5,8,11]

def build_linked_list(a_list): 
    dummy = ListNode()
    cur = dummy
    for val in a_list: 
        
        new_node = ListNode(val)
        cur.next = new_node
        cur = cur.next
    return dummy.next

def print_linked_list(node): 
    cur = node
    to_print = ""
    while cur: 
        to_print += str(cur.val) + ","
        cur = cur.next
    print(to_print)
    return 



        
    

    
# a_linked = build_linked_list(a_list)
# # print(a_linked.next.val)
# print_linked_list(a_linked)
# b_linked = build_linked_list(b_list)
# print_linked_list(b_linked)
# c_linked = merge(a_linked, b_linked)
# print_linked_list(c_linked)

lists = [1,3,4,5,6,7]


print([x for x in range(3, 10, 2)])

# print(list(range(len(lists), 2)))