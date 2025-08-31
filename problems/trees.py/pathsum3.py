
from collections import Counter
def pathSum(root, sum):     
    # the "res" includes the node 
    def helper(node): 
        res = Counter()
        sumPath = 0
        if not node: 
            return sumPath, res            
        for child in [node.left, node.right]: 
            curSumPath, curRes = helper(child)
            sumPath += curSumPath
            res += {x + node.val: y for x, y in curRes.items()}          
        res[node.val] += 1        
        if sum in res:  
            sumPath += res[sum]                        
        return sumPath, res    
    return helper(root)[0]



x = {1: 2, 3: 4}
print(x.keys())
print(x.items())