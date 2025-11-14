# https://leetcode.com/problems/increment-submatrices-by-one/?envType=daily-question&envId=2025-11-14
# Use index compression to reduce prefix sum overhead

from typing import List

class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        def increment(mat, query): 
            x1, y1, x2, y2 = query
            
            for x in range(x1, x2+1):
                mat[x][y1] += 1        
                if y2+1 < len(mat):  
                    mat[x][y2+1] -= 1
            return 

        def apply_cumulative(mat, res, n): 
            for i in range(n):
                cur_sum = 0
                for j in range(n): 
                    cur_sum += mat[i][j]
                    res[i][j] = cur_sum            
            return 

        mat = [[0]*n for _ in range(n)]
        
        for query in queries: 
            increment(mat, query)
                
        res = [[0]*n for _ in range(n)]        
        apply_cumulative(mat, res, n)
            
        return res
