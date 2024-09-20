# https://leetcode.com/problems/different-ways-to-add-parentheses/description/
# 241. Different Ways to Add Parentheses


# dp = {# ways to combine a window of i size starting at index j}
# i from 1 to length n - 1 inclusive, where n = length of numbers
# start at jth position, from 0 to n - i inclusive

# Time: O(n^3), Space: O(n^2)

# why is it O(n^3) and not O(n^4)? 
# the cross function follows the catalan numbers sequence. When you find the splits for inputs 
# of the cross function, the output is bounded by O(n), due to the catalan sequence. Lots of handwaviness. 


class Solution:
    def diffWaysToCompute(self, expression: str) -> list[int]:
        def splitString(expression): 
            nums = []
            operations = []
            cur = ""
            ops = set("+-*")
            for char in expression: 
                if char in ops: 
                    nums.append(cur)
                    cur = ""
                    operations.append(char)
                else: 
                    cur += char
            nums.append(cur)
            nums = [int(x) for x in nums]
            return nums, operations

        def applyOps(x, y, op): 
            if op == "+": return x + y 
            elif op == "-": return x - y
            else: return x * y

        def cross(arr1, arr2, j, operations): 
            res = []
            for x in arr1: 
                for y in arr2: 
                    curRes = applyOps(x, y, operations[j])
                    res.append(curRes)
            return res

        nums, operations = splitString(expression) 
        n = len(nums)
        dp = {}
        for i in range(1, n+1): 
            for j in range(0, n - i + 1): 
                curRes = []
                if i == 1: curRes.append(nums[j])
                else: 
                    for k in range(1, i): 
                        candidate = cross(dp[(k, j)], dp[(i-k, k + j)], k + j - 1, operations)
                        curRes += candidate
                dp[(i, j)] = curRes                   
        return dp[(n, 0)]
    

s = Solution()
expression = "2*3-4*5"
print(s.diffWaysToCompute(expression))