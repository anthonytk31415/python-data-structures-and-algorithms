# https://leetcode.com/problems/make-costs-of-paths-equal-in-a-binary-tree/
# 2673. Make Costs of Paths Equal in a Binary Tree

# Use Tree like recursion. 
# Time: O(n); Space: O(n) for the recursive calls

# adjust for 0 indexed 
def leftChild(i): 
    return 2*i + 1

def rightChild(i): 
    return 2*i + 2

# return the max path that has equal left and right children
def helper(i, cost, totalIncrements): 
    leftIdx, rightIdx = leftChild(i), rightChild(i)
    if min(leftIdx, rightIdx) >= len(cost): 
        return cost[i] 
    leftMax, rightMax = helper(leftIdx, cost, totalIncrements), helper(rightIdx, cost, totalIncrements)
    childMax , childMin = max(leftMax, rightMax), min(leftMax, rightMax)
    totalIncrements[0] += abs(childMax - childMin)          # delta
    return cost[i] + childMax                               # maxPath

class Solution:
    def minIncrements(self, n: int, cost: list[int]) -> int:
        totalIncrements = [0]
        helper(0, cost, totalIncrements)
        return totalIncrements[0]
