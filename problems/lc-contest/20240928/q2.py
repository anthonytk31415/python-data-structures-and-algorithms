# https://leetcode.com/problems/maximize-the-total-height-of-unique-towers/description/
# 3301. Maximize the Total Height of Unique Towers

class Solution:
    def maximumTotalSum(self, maxHeight: list[int]) -> int:
        n = len(maxHeight)
        maxHeight.sort()
        cur = None
        prev = maxHeight[n - 1]
        res = maxHeight[n - 1]

        check = [0]*n
        check[-1] = maxHeight[-1]
        for i in range(len(maxHeight) -2, -1, -1):
            if maxHeight[i] >= prev - 1: 
                cur = prev - 1
            else: 
                cur = maxHeight[i]
            check[i] = cur
            if cur <= 0: 
                # print(check)
                return -1
            res += cur
            prev, cur = cur, None

        # print(check)
        return res
    
# maxHeight = [2,3,4,3] # 10
# maxHeight = [15,10] # 25 
# maxHeight = [2,2,1] # -1
# maxHeight = [3, 3, 3, 3] # -1
maxHeight = [2,2] # 3

s = Solution()

print(s.maximumTotalSum(maxHeight))