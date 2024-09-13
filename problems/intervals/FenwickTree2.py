
# build a fenwick tree for sum operations
class FenwickTree:
    
    # create the tree 1 indexed
    def __init__(self, n): 
        self.n = n
        self.tree = [0]*(n+1)

    # given the ith index, update; convert to 1-indexed
    # update each i for largest power of 2 iteratively
    def update(self, i, val): 
        i += 1
        while i <= self.n: 
            self.tree[i] += val
            i += i & -i
    
    # add all relavant; i is the tree index
    def singleRange(self, i):  
        res = 0
        while i >= 1: 
            res += self.tree[i]
            i -= i & -i
        return res
    
    # we assume left, right correspond to the original array, not the tree, so update left and righth
    # do the "prefix sum" trick of taking the sums of the intervals that matter
    def dualRange(self, left, right): 
        left += 1
        right += 1
        if left == 1: 
            return self.singleRange(right)
        return self.singleRange(right) - self.singleRange(left - 1)
    
arr = [0,1,2,3,4,5,6,7]
t = FenwickTree(len(arr))
for i, num in enumerate(arr): 
    t.update(i, num)

print("arr:  ", arr)
print("tree: ", t.tree)
print(t.dualRange(3, 6))