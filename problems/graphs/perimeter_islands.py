
# https://leetcode.com/problems/island-perimeter/description/

def perimeter_islands(matrix): 
    rows, cols = len(matrix), len(matrix[0])
    visited = set()    

    def count_water(i, j): 
        count_water = 0
        for u, v in [(i+1, j), (i-1, j), (i, j - 1), (i, j + 1)]:      
            if not (0 <= u < rows and 0 <= v < cols):
                count_water += 1
            else if matrix[u][v] == 0: 
        return count_water
    
    def dfs(i, j): 
        if not (0 <= u < rows and 0 <= v < cols) or matrix[i][jk]:             
            return 1
        
        visited.add((i, j))
        num_water = 0
        # num_water = count_water(i, j)
        for u, v in [(i+1, j), (i-1, j), (i, j - 1), (i, j + 1)]:             
            
            if matrix[u][v] == 0: num_water += 1
            
                num_water += dfs(u, v)
        return num_water
    
    
    
    for i in range(rows):
        for j in range(cols): 
            if matrix[i][j] == 1: 
                return dfs(i, j)
    