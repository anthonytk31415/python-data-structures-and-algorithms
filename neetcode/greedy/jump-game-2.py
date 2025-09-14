# https://neetcode.io/problems/jump-game-ii?list=neetcode150
#

def jump(nums): 
    end = len(nums) - 1
    
    def helper(i): 
        if i == end: 
            return 0
        next = i + 1
        if i + nums[i] >= end: 
            return 1
        for j in range(i + 2, i + nums[i] + 1):             
            if nums[j] > nums[next]: 
                next = j
        
        print(i, next)
                        
        return 1 + helper(next)
    
    return helper(0)
    
nums = [2,1,2,1,0]
nums = [2,4,1,1,1,1]
print(jump(nums))