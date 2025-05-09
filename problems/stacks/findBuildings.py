# https://leetcode.com/problems/buildings-with-an-ocean-view/description/

# monotonic stack implementation

class Solution:
    def findBuildings(self, heights: list[int]) -> list[int]:
        stack = []
        for i, h in enumerate(heights): 
            while stack and h >= heights[stack[-1]]:
                stack.pop()
            stack.append(i)
        return stack



