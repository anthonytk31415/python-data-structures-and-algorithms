from math import sqrt

# 1954. Minimum Garden Perimeter to Collect Enough Apples
# https://leetcode.com/problems/minimum-garden-perimeter-to-collect-enough-apples/description/?envType=problem-list-v2&envId=binary-search

# Binary search the answer. 
# Use arithmetic series: sum of n terms from 1 to n = n*(n + 1) / 2


def getApples(r): 
    sigma = r*(r + 1)//2
    return 4*sigma*(1+2*r)

def getPerimeter(radius): 
    return radius*8

class Solution:
    def minimumPerimeter(self, neededApples: int) -> int:
        left = -1
        right = int(sqrt(neededApples))         # how to decide this? 
        while right - left > 1: 
            mid = (left + right)//2
            if getApples(mid) >= neededApples: 
                right = mid
            else: 
                left = mid
        return getPerimeter(right)
    

neededApples = 1
# neededApples = 13
neededApples = 1000000000
# neededApples = 215073301725407
s = Solution()
print(s.minimumPerimeter(neededApples))