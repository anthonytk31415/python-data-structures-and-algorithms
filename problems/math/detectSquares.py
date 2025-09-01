from typing import List

# https://leetcode.com/problems/detect-squares/solutions/7142221/concise-12-line-python-solution-75ms-clean-efficient/

class DetectSquares:

    def __init__(self):
        self.grid = [[0]*1001 for _ in range(1001)]
        
    def add(self, point: List[int]) -> None:
        x, y = point 
        self.grid[x][y] +=1
    
    def remove(self, point): 
        x, y = point
        self.grid[x][y] -= 1

    def doCheck(self, point):
        self.add(point)
        x, y = point
        count = 0
        visited = set()
        
        def checkLeftAndRight(i):
            delta = abs(i - x)
            count = 0
            for yNew in [y - delta, y + delta]: 
                if 0 <= yNew <= 1001 and self.grid[i][yNew] and self.grid[x][yNew]: 
                    points = [(i, yNew), (x, yNew), (i, y)]
                    points.sort(key = lambda pt: (pt[0], pt[1]))
                    points = tuple(points)
                    if points not in visited: 
                        visited.add(points)
                        curProduct = 1
                        for u, v in points: 
                            curProduct *= self.grid[u][v]
                        count += curProduct                     
            return count
        
        for i in range(len(self.grid)):
            if i != x and self.grid[i][y]:                 
                count += checkLeftAndRight(i)

        self.remove(point)
        return count 

    def count(self, point: List[int]) -> int:
        return self.doCheck(point)