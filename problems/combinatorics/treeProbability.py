from nextPermutation import next_permutation
from printBST import print_bst

class TreeNode: 
    def __init__(self, val=None, left=None, right=None): 
        self.val = val
        self.left = left
        self.right = right

    
def insert(node, root): 
    if node.val < root.val:
        if root.left == None: 
            root.left = node
            return node
        else: 
            return insert(node, root.left)
    else: 
        if root.right == None: 
            root.right = node
            return node
        else: 
            return insert(node, root.right)        


# node = TreeNode(1)
# insert(TreeNode(2), node)
# insert(TreeNode(10), node)
# insert(TreeNode(4), node)
# insert(TreeNode(11), node)
# x = node
# while x: 
#     print(x.val)
#     x = x.right


def find(val, root): 
    if not root: return None
    if root.val == val: return root
    if val < root.val: 
        return find(val, root.left)
    else: 
        return find(val, root.right) 


# node11 = find(11, node)
# print(node11.val)
# print_bst(node)

def hasOneChild(val, root):
    target = find(val, root)
    return (target.left == None and target.right != None) or (target.right == None and target.left != None)

def createTree(perm): 
    root = None
    for i, num in enumerate(perm):
        if i == 0: 
            root = TreeNode(num)
        else: 
            insert(TreeNode(num), root)
    return root

# testRoot = createTree([1,2,3,4])
# testRoot = createTree([3,1,2,4])
# x = testRoot
# while x: 
#     print(x.val)
#     x = x.left

def buildAllTrees(firstPerm): 
    trees = []
    curPerm = [x for x in firstPerm]
    while True: 
        newTree = createTree(curPerm)
        trees.append(newTree)
        curPerm = next_permutation(curPerm)
        if curPerm == firstPerm: 
            break  
    return trees

# print(len())
# trees = buildAllTrees([1,2,3])
# for tree in trees: 
#     print_bst(tree)

def treeTest(k): 
    firstPerm = [x for x in range(k)]
    trees = buildAllTrees(firstPerm)
    res = {}
    for i in range(k): 
        numSingleTrees = 0
        for tree in trees: 
            if hasOneChild(i, tree): numSingleTrees += 1
        prob = numSingleTrees/len(trees)
        res[i] = (numSingleTrees, len(trees), prob)        
        print("for {}th value, singleChildTrees = {}, totalTrees = {}, prob = {}".format(i, numSingleTrees, len(trees), prob))    
    return res 

res = treeTest(9)

# a = [1,2,3]
# b = [1,2,4]
# print(a == b)

# print([] == [])