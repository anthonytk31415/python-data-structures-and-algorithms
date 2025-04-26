# twosum bst

# root of 2 bst
# target sum 
# is there a node in tree1 and tree2 where the sum of the values equals to 

# https://leetcode.com/problems/two-sum-bsts/description/
# 1214. Two Sum BSTs

# traverse A and memoize all of the values in a hash map/set. 
# traverse B. if the counterpart is in the hash, return True
# otherwise return recursive left or recursive right
# If not root, return False.


def twoSumBSTs(rootA, rootB, target): 

    def build_memo(root, memo): 
        if not root: 
            return False
        memo[root.val] = 1
        build_memo(root.left, memo)
        build_memo(root.right, memo)
        
    memo = {}
    build_memo(rootA, memo)

    def find_pair(root, memo, target): 
        if not root: 
            return False
        if target - root.val in memo: 
            return True
        return find_pair(root.left, memo, target) or find_pair(root.right, memo, target)

    return find_pair(rootB, memo, target)   
