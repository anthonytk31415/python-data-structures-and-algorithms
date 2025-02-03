# Fibonacci Heap Pseudocode

def decreasePriority(x, key): 
    decrease x's key
    if heap property at x is violated: 
        promote(x)
        compare x to best root, change if better
    
def promote(x):
    if x is not already a root: 
        p = x.parent
        rearrange pointers to remove x from p's children, 
            add it x to the root list
        x.flag = False
        if p.flag: promote(p)
        elif p is not a root: 
            p.flag = True
            

# key invariat: in C, each root has a unique number of chidren. If we encounter
# a root with the same number of children, we merge them. 
def deleteMin(): 
    create a queue of all the root nodes
    create an array C of size m + 1 where m = log(n) 
        which will hold keys with the num of children
    create a queue Q and put all  the root nodes in there
    delete the min and put its children Q
    while Q: 
        v = dequeue(Q)
        mark v's num of children on the array in C. 
        If C is occupied, merge the two roots.  
            the two children with the smaller (higher priority)
            being the node. 
            enqueue that node in C
         
 