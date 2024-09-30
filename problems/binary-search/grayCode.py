# https://leetcode.com/problems/gray-code/description/
# 89. Gray Code

# Take the Gray code 0, 1. Write it forwards, then backwards: 0, 1, 1, 0. 
# Then prepend 0s to the first half and 1s to the second half: 00, 01, 11, 10. 
# Continuing, write 00, 01, 11, 10, 10, 11, 01, 00 to obtain: 000, 001, 011, 010, 110, 111, 101, 100, ... 
# Each iteration therefore doubles the number of codes.

class Solution1:
    def grayCode(self, n: int) -> list[int]:
        path = ["0", "1"]
        if n == 1: return [int(x, 2) for x in path]
        for _ in range(1, n): 
            path = ["0" + x for x in path] + ["1" + x for x in path[::-1]]
        return [int(x, 2) for x in path]
    

# DFS Backtracking using some bit manipulation



def countBits(k): 
    count = 0
    while k: 
        k &= (k-1)
        count += 1
    return count

class Solution:
    def grayCode(self, n: int) -> list[int]:    
        
        def doMove(z): 
            path.append(z)
            visited.add(z)

        def undoMove(z):
            path.pop()
            visited.remove(z)  

        def dfs(k):
            if len(visited) == 2**n and countBits(k) == 1: 
                return True
            for i in range(n): 
                z = k | (1 << i)               # set ith bit
                if z not in visited: 
                    doMove(z)   
                    if dfs(z): return True
                    undoMove(z)
                    
                z = k & ~(1<<i)              # clear ith bit
                if z not in visited:
                    doMove(z)   
                    if dfs(z): return True
                    undoMove(z) 

        visited = set()
        path = [0]    
        visited.add(0)
        dfs(0)
        return path

# binary solution

s = Solution()
print(s.grayCode(5))



# print(bin(10))
# print(countBits(10))

# lets do a dfs solution. 

# print(bin(3))
# print(bin(3 & ~(1)))