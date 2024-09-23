# binary search to find (1) the largest index that after jumps, is less than or equal to the target. 
# then consider: (1) jumps or (1) + 1 jumps. 
# delta * 2 = jumps

from math import sqrt , ceil

def applyJumps(k): 
    return k*(k+1)//2 + 0

def findMinJumps(target): 
    left = -1
    right = target
    while right - left > 1: 
        mid = (right + left)//2
        if applyJumps(mid) <= target: 
            left = mid
        else: 
            right = mid
    return left

target = -10
print(findMinJumps(target))

# 0>1>3>6>10

class Solution1:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        minJumps = findMinJumps(target)
        distMinJumps = applyJumps(minJumps)
        x = 2*abs(target - distMinJumps) + minJumps

        distMinJumpsPlusOne = applyJumps(minJumps +1)
        y = 2*abs(target - distMinJumpsPlusOne) + minJumps + 1

        return min(x, y) 
    



class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        k = ceil((sqrt(8*target+1)-1)/2)
        return k if (k-target) % 2 == 0 else k + 1 + k%2


s = Solution()
target = 4
# target = 10
print(s.reachNumber(target))