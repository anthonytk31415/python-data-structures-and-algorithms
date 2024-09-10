from collections import deque

# https://leetcode.com/problems/spiral-matrix-iv/
# 2326. Spiral Matrix IV

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def spiralMatrix(m: int, n: int, head):
    matrix = [[-1 for _ in range(n)] for _ in range(m)]
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    q = deque([n, m-1])     # iterate n times, then m-1 times,
    node = head
    dirsIndex, i, j = 0, 0, -1
    while q and node:     
        numIterations = q.popleft()
        for _ in range(numIterations): 
            if node: 
                i, j = i + dirs[dirsIndex][0], j + dirs[dirsIndex][1]         
                matrix[i][j] = node.val
                node = node.next
            else: break 
        q.append(numIterations-1)
        dirsIndex = (dirsIndex + 1)%4
    return matrix


m = 3
n = 5

headArr = [3,0,2,6,8,1,7,9,4,2,5,5,0]

dummy = ListNode()
node = dummy
for x in headArr: 
    # print(x)
    node.next = ListNode(x)
    node = node.next

node = dummy.next
# while node: 
#     print(node.val)
#     node = node.next

print(spiralMatrix(m, n, dummy.next))