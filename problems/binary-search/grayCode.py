# https://leetcode.com/problems/gray-code/description/
# 89. Gray Code

class Solution1:
    def grayCode(self, n: int) -> list[int]:
        path = ["0", "1"]
        if n == 1: return [int(x, 2) for x in path]
        for _ in range(1, n): 
            path = ["0" + x for x in path] + ["1" + x for x in path[::-1]]
        return [int(x, 2) for x in path]
    

# DFS using some bit manipulation
def countBits(k): 
    count = 0
    while k: 
        k &= (k-1)
        count += 1
    return count

# print(bin(10))
# print(countBits(10))

# lets do a dfs solution
class Solution:
    def grayCode(self, n: int) -> list[int]:
    
        visited = set()
        def dfs(k):
            if len(visited) == 2**n and countBits(k) == 1: 
                return True
            for i in range(n): 
                z = k | 1 << i          # set ith bit,
                if z not in visited: 
                    path.append(z)
                    visited.add(z)
                    if dfs(z): return True
                    path.pop()
                    visited.remove(z)                
                y = k & ~(1<<i)              # clear ith bit
                if y not in visited:
                    path.append(y) 
                    visited.add(y)
                    if dfs(y): return True
                    path.pop()
                    visited.remove(y)

        path = [0]    
        visited.add(0)
        dfs(0)
        # print("res: ", path)
        return path

# binary solution

s = Solution()
# print(s.grayCode(2))

# print(bin(3))
# print(bin(3 & ~(1)))