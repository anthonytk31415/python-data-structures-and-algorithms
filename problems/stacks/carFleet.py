# https://leetcode.com/problems/car-fleet/description/?envType=problem-list-v2&envId=monotonic-stack
# 853. Car Fleet

# Calculate times to arrival for each car based on its position 
# and speed. Then build a list with the positions and times, 
# sorted by positions in descending order. 
# The stack keeps track of the order of arrival. 
# if a car collides with the one in front, don't push it. 
# Return the length of the stack. 

# Time: O(n), Space: O(n)

class Solution:
    def carFleet(self, target: int, positions: list[int], speeds: list[int]) -> int:
        times = []
        for pos, speed in zip(positions, speeds): 
            time = (target - pos)/speed
            times.append(time)
        combined = list(zip(positions, times))
        combined.sort(key = lambda x: (-x[0]))
        stack = []      # maintain order of arrival
        for pos, time in combined: 
            if not stack or stack[-1] < time:  
                stack.append(time)
        return len(stack)
    

target = 12
positions = [10,8,0,5,3]
speeds = [2,4,1,1,3]

# target = 10
# positions = [3]
# speed = [3]

# target = 100
# position = [0,2,4]
# speed = [4,2,1]

s = Solution()
print(s.carFleet(target, positions, speeds))