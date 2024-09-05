from math import inf 
from itertools import permutations

# https://leetcode.com/problems/last-stone-weight-ii/description/
# 1049. Last Stone Weight II

# The "smash" is basically this; partition the array into two pieces A and B, and take the difference: A - B. 
# Consider all the possible A, B sums and then we choose the one that minimizes the difference. 
# One thing to note: 
# (1) A + B = S (total sum)
# (2) B = S - A ==> diff = B - A = S - A - A 

# super brute force. Not scalable. 
def lastStoneWeightII(stones: list[int]) -> int:
    A = stones
    dp = {0}
    sumA = sum(A)
    for a in A: 
        dp |= {d + a for d in dp}           
    return min(sumA - 2*d for d in dp)


# can spave with this optimization
def lastStoneWeightII_2(stones: list[int]) -> int:
    A = stones
    dp = {0}
    sumA = sum(A)
    for a in A: 
        dp |= {d + a for d in dp if d+ a <= sumA/2}
    return min(sumA - 2*d for d in dp)



# super brute force. Not scalable. 
def lastStoneWeightII_1(stones: list[int]) -> int:
    def consume(stones): 
        res = stones[0]
        for num in stones[1:]: 
            res = abs(res - num)
        # print(stones, res)
        return res

    allPerms = list(permutations(stones, len(stones)))
    res = inf
    for perm in allPerms: 
        res = min(res, consume(perm))
    return res






stones = [2,3,5]
# stones = [31,26,33,21,40]
stones = [2,7,4,1,8,1]
stones = [31,26,33,21,40]
stones = [1,1,2,3,5,8,13,21,34,55,89,14,23,37,61,98]
print(lastStoneWeightII(stones))





            # arr = stones[i:]
            # arrComplete = [y] + arr
            # arrComplete.sort()
            # arrComplete = tuple(arrComplete)
            # curMin = inf
            # if not stones[i+1:]: 
            #     x = stones[i]
            #     curMin = min(curMin, collide(y, x))
            # else: 
            #     for j in range(len(arr)): 
            #         x = arr[j]
            #         newArr = arr[:j] + arr[j+1:]
            #         z = collide(x, arr[j])
            #         toDPArr = newArr   
            #         if z != 0: 
            #             toDPArr = [z] + toDPArr
            #         toDPArr.sort()
            #         toDPArr = tuple(toDPArr)
            #         curMin = min(curMin, dp[toDPArr])
            # dp[arrComplete] = curMin
