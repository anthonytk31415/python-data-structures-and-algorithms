# https://leetcode.com/problems/xor-queries-of-a-subarray/submissions/1112322738/?envType=daily-question&envId=2024-09-13
# 1310. XOR Queries of a Subarray

# implement in nlogn Time with the segment tree


class SegmentTree: 
    def __init__(self, arr): 
        self.n = len(arr)
        self.tree = [0]*self.n*2
        self.build(arr)

    def build(self, arr): 
        for i in range(len(arr)):
            k = i + self.n
            self.tree[k] = arr[i]

        for i in range(self.n-1, 0, -1):
            self.tree[i] = self.tree[2*i]  ^ self.tree[2*i+1]
        
    def query(self, left, right): 
        res = 0
        left += self.n
        right += self.n
        while left <= right: 
            if left % 2 == 1: 
                res ^= self.tree[left]
                left += 1
            if right % 2 == 0: 
                res ^= self.tree[right]
                right -= 1
            right //= 2
            left //=2
        return res
    
    def update(self, i, val): 
        i += self.n
        self.tree[i] = val
        while i >= 1: 
            i //= 2
            self.tree[i] = self.tree[2*i] ^ self.tree[2*i + 1]


class Solution:
    def xorQueries(self, arr: list[int], queries: list[list[int]]) -> list[int]:
        tree = SegmentTree(arr)
        # print(tree.tree)
        res = []
        for left, right in queries: 
            res.append(tree.query(left, right))

        return res


        

arr = [0,3,4,8]
queries = [[0,1],[1,2],[0,3],[3,3]]

s  = Solution()
print(s.xorQueries(arr, queries))

# s.update(0, 1)
# print(s.xorQueries(arr, queries))

print(bin(4))