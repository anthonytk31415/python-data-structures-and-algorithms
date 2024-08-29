# https://leetcode.com/problems/range-sum-query-mutable/description/
# 307. Range Sum Query - Mutable


# his is the Segment Tree Implementation
# O(n) initialization, O(logn) for update and range queries

class SegmentTree:

    def __init__(self, nums: list[int]):
        self.arr = [0]*len(nums)*2
        self.n = len(nums)

        for i in range(self.n):
            self.arr[i + self.n] = nums[i] 

        for i in range(self.n - 1, 0, -1): 
            self.arr[i] = self.arr[2*i] + self.arr[2*i + 1]

    def update(self, index: int, val: int) -> None:
        index += self.n
        delta = val - self.arr[index]
        while index >= 1: 
            self.arr[index] += delta
            index //=2

    def sumRange(self, left: int, right: int) -> int:
        res = 0
        left += self.n
        right += self.n
        while left <= right: 
            if left % 2 == 1: 
                res += self.arr[left]
                left += 1
            left //=2
            if right % 2 == 0: 
                res += self.arr[right]
                right -= 1
            right //=2
        return res
            

class NumArray(SegmentTree):
    pass


x = NumArray([1, 3, 5])

print("sum 0 1: ", x.sumRange(0,1))
print("sum 0 1: ", x.sumRange(0,2))


print("sum 0 1: ", x.sumRange(0,2))
x.update(1,2)
print(x.arr)
print("sum 0 1: ", x.sumRange(0,2))