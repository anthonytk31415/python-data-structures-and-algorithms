class SegmentTree(): 
    def __init__(self, arr): 
        self.n = len(arr)
        self.tree = [0] * 2*self.n
        self.build(arr)

    def build(self, arr): 
        for i in range(self.n):
            self.tree[self.n + i] = arr[i]
        
        for i in range(self.n -1, 0, -1): 
            self.tree[i] = self.tree[2*i] + self.tree[2*i + 1]

    # given indexes of range [left, right] in 0-indexd array to begin with, get the sum
    def sum(self, left, right): 
        left += self.n
        right += self.n
        res = 0
        while left <= right: 
            if left % 2 == 1: 
                res += self.tree[left]
                left += 1
            if right % 2 == 0: 
                res += self.tree[right]
                right -= 1
            left //= 2
            right //= 2
        return res

    # add x to position k, 0-indexed
    # then iteratively update the parents
    def add(self, k, x): 
        k += self.n
        self.tree[k] += x
        k //= 2
        while k >= 1: 
            self.tree[k] = self.tree[2*k] + self.tree[2*k + 1]
            k //= 2
    
arr = [1,2,3,4,5,6,7,8]
st = SegmentTree(arr)
# print(st.tree)
# print(st.sum(6,7))

st.add(1, 3)
print(st.tree)
print(st.sum(1,1))