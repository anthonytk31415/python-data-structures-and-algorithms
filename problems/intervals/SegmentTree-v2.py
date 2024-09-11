from math import inf

class SegmentTree:

    def __init__(self, nums):
        self.tree = [0]*len(nums)*2
        # print(self.tree)
        self.n = len(nums)
        self.buildSegmentTree(nums)

    def buildSegmentTree(self, nums): 
        tree = self.tree
        for i in range(self.n): 
            tree[i + self.n] = nums[i]
        for i in range(self.n - 1, 0, -1):
            tree[i] = min(tree[2*i], tree[2*i + 1])

    def rangeMin(self, left, right):
        res = inf
        left += self.n
        right += self.n
        while left <= right: 
            if left %2 == 1: 
                res = min(res, self.tree[left])
                left += 1
            left //= 2
            if right % 2 == 0: 
                res = min(res, self.tree[right]); 
                right -=1
            right //= 2 

        return res
    

nums = [1,5,2,7,3,6,4,0]
tree = SegmentTree(nums)

print(tree.rangeMin(0, 6))
