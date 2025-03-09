# https://leetcode.com/problems/pour-water/submissions/1567517487/?envType=company&envId=airbnb&favoriteSlug=airbnb-six-months
# 755. Pour Water

# a good state machine diagram problem 



# move left until you can fall or yo uhit a wall, 
# if you hit a wall, return -1
# direction: -1 = left, 1 = right
def moveLateral(start, heights, direction): 
    end = start + direction
    while 0 <= end < len(heights): 
        if heights[end] > heights[start]: return start
        if heights[end] < heights[start]: return end 
        end += direction
    return start

def fall(k, heights): 
    for direction in [-1, 1]: 
        k_dir = moveLateral(k, heights, direction)    
        if k_dir != k: 
            if heights[k_dir] < heights[k]: 
                return fall(k_dir,heights)
            heights[k_dir] += 1
            return  
    heights[k] += 1 
    return 

class Solution:
    def pourWater(self, heights: list[int], volume: int, k: int) -> list[int]:
        for i in range(volume): 
            fall(k, heights)
        return heights