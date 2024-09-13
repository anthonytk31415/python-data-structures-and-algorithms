# given an array, turn it into a fenwick tree. 
# - for simplicity, tree is now 1-indexed
# 
class FenwickTree:
    def __init__(self, arr): 
        self.n = len(arr) 
        self.tree = [0]*(self.n + 1)
        self.update(arr)

    # for an index k, add  value and then update its dependencies 
    def add(self, k, val): 
        while (k <= self.n): 
            self.tree[k] += val
            k += k & -k
    
    def update(self, arr): 
        for i in range(len(arr)): 
            k = i + 1
            self.add(k, arr[i])

    # for kth index in arr, find the query wiht the fenwick tree
    def singleQuery(self, k):
        s = 0
        while k >= 1: 
            s += self.tree[k]
            k -= k&-k
        return s

    def rangeQuery(self, low, high): 
        low += 1
        high += 1
        if low == 1: 
            return self.singleQuery(high)

        return self.singleQuery(high) - self.singleQuery(low-1)


from math import inf

class FenwickTreeMin:
    def __init__(self, arr): 
        self.n = len(arr) 
        self.tree = [inf]*(self.n + 1)
        self.update(arr)

    # for an index k, add  value and then update its dependencies 
    def add(self, k, val): 
        while (k <= self.n): 
            self.tree[k] = min(self.tree[k], val)
            k += k & -k
    
    def update(self, arr): 
        for i in range(len(arr)): 
            k = i + 1
            self.add(k, arr[i])

    # for kth index in arr, find the query wiht the fenwick tree
    def singleQuery(self, k):
        s = inf
        while k >= 1: 
            s = min(s, self.tree[k])
            k -= k&-k
        return s

    def rangeQuery(self, low, high): 
        low += 1
        high += 1
        if low == 1: 
            return self.singleQuery(high)

        return min(self.singleQuery(high), self.singleQuery(low-1))


arr = [1,3,4,8,6,1,4,2]

# f = FenwickTreeMin(arr)
f = FenwickTree(arr)
print("arr: ", arr)
print(f.tree)

print(f.rangeQuery(0, 6))
print(f.rangeQuery(3, 5))
print(f.rangeQuery(3, 6))
