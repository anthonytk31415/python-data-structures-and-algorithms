# https://leetcode.com/problems/maximum-profitable-triplets-with-increasing-prices-ii/description/?envType=problem-list-v2&envId=segment-tree
# 2921. Maximum Profitable Triplets With Increasing Prices II

# creating a max Fenwick Tree
from math import inf


class FenwickTree: 
    def __init__(self, n): 
        self.n = n
        self.tree = [-inf]*(n+1)

    # given the i, update the 1-index and all its dependent nodes
    def update(self, i, val):
        i += 1
        while i <= self.n: 
            self.tree[i] = max(self.tree[i], val)
            i += i&-i        

    # given i, update to 1-indexed, and then return the query
    def query(self, i): 
        i += 1
        res = -inf 
        while i >= 1: 
            res = max(res, self.tree[i])
            i -= i&-i
        return res


def maxProfit(prices, profits):

    # build fenwick tree by prices
    maxPrice = max(prices)

    # left is max profit on left of i; 
    leftTree, rightTree = FenwickTree(maxPrice + 1), FenwickTree(maxPrice + 1)
    leftMaxProfit, rightMaxProfit = [-inf]*len(prices), [-inf]*len(prices)
    # for each i, price in prices, find the range (which will only have entries)

    # build left. query price - 1 so that you get prices[i] < prices[j]
    for i in range(len(prices)): 
        p = prices[i]
        leftMaxProfit[i] = leftTree.query(p-1)
        leftTree.update(p, profits[i])

    # print(leftMaxProfit)
    # print(leftTree.tree)

    # build right. query price - 1 so that you get prices[i] < prices[k]
    for i in range(len(prices)-1, -1, -1): 
        p = maxPrice + 1 - prices[i]
        rightMaxProfit[i] = rightTree.query(p-1)
        rightTree.update(p, profits[i])


    # print(rightMaxProfit)
    # print(rightTree.tree)

    # find answer
    res = -1
    for i in range(len(prices)):
        res = max(res, leftMaxProfit[i] + rightMaxProfit[i] + profits[i])

    return res


prices = [10,2,3,4]
profits = [100,2,7,10]
 


prices = [1,1,7]
profits = [84,46,6]
print(maxProfit(prices, profits))