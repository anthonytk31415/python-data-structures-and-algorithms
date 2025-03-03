def cleanse(node, val):
    vals = set([val])
    if node.left: vals |= cleanse(node.left, 2*val + 1)
    if node.right: vals |= cleanse(node.right, 2*val + 2)
    return vals

# def findx(root, val): 
#     if not root: return False
#     print("val: {}, root.val: {}".format(val, root.val))
#     if root.val == val: return True
#     elif val < root.val: 
#         return findx(root.left, val)
#     else: 
#         return findx(root.right, val)

class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.vals = cleanse(root, 0)        
        
    def find(self, target: int) -> bool:
        return target in self.vals


a = set([1,2])
b = set([3,4])
print(a | b)