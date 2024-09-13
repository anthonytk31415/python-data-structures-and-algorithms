# https://leetcode.com/problems/count-subarrays-with-more-ones-than-zeros/
# 2031. Count Subarrays With More Ones Than Zeros


# Fenwick Tree implementation. Extremely tricky. 
# Define diff(i) = count(1's) - count(0's) up to ith index
# Key Observation: diff(i) - diff(j) = diff from j + 1 to i (like prefix sum)
# We create a diff(-1) = 0 for the empty string. 
# Then for each diff(i), we count the number of j < i for which diff[j] < diff[i]
# we can do this in a Fenwick Tree by each time we calculate diff[i], we perform 
# a range query on i -1, then update with the tree. 
# Make a Fenwick Tree with length = 2n+1 for the count of diff at some value. 

# Time: O(nlogn)
# Space: O(n)

class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0]*(n + 1)

    def update(self, k, val):
        k += 1
        while k <= self.n: 
            self.tree[k] += val
            k += k&-k

    def query(self, k): 
        k += 1
        res = 0
        while k >= 1: 
            res += self.tree[k]
            k -= k&-k
        return res

def subarraysWithMoreZerosThanOnes(nums):
    numOnes = 0
    countDiffs = [0]*(2*len(nums) + 1)
    tree = FenwickTree(len(countDiffs))
    res = 0
    tree.update(0 + len(nums), 1)
    for i, num in enumerate(nums): 
        if num == 1: numOnes += 1
        numZeroes = i + 1 - numOnes
        curDiff = numOnes - numZeroes
        res += tree.query(curDiff + len(nums) - 1)
        tree.update(curDiff + len(nums), 1)
    return res

nums = [0,1,1,0,1]

nums = [1]
print(subarraysWithMoreZerosThanOnes(nums))