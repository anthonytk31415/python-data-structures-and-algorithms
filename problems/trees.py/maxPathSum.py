
class Solution:
    def maxPathSum(self, root):
    
        def helper(root):
    
            maxLeft, maxRight = -inf, -inf
            globalLeft, globalRight = -inf, -inf
            if root.left: 
                maxLeft, globalLeft = helper(root.left)
            
            if root.right:
                maxRight, globalRight = helper(root.right)

            globalMax = max([maxLeft, maxRight, root.val + max([maxLeft + maxRight, maxLeft, maxRight, 0]), globalLeft, globalRight])
            maxPathWithRoot = root.val + max([maxLeft, maxRight, 0]) 

            return maxPathWithRoot, globalMax
        return max(helper(root))