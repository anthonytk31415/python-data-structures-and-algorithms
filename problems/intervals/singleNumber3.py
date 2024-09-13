
# https://leetcode.com/problems/single-number-iii/description/?envType=problem-list-v2&envId=bit-manipulation
# 260. Single Number III

# x =         10010
# x - 1 =     10001
# x & (x-1) = 10000
# x & -x gets you the rightmost bit

# x ^y for all y in nums gets you a ^ b
# in a ^b, there's at least 1 bit that differs from a to b. Get the first differing bit using z = x & -x. 
# for each num in nums, if a num mataches z, do aHat ^ z. else do bHat ^ z. 
# in the end, all of the pairs will cancel out to leave a in aHat and b in bHat, respectively. So return aHat, bHat. 

def singleNumber(nums: list[int]) -> list[int]:
    x = aHat = bHat = 0
    for num in nums: 
        x ^= num
    rightmost = x & -x
    for num in nums: 
        if num & rightmost == rightmost: 
            aHat ^= num
        else: 
            bHat ^= num
    return [aHat, bHat]


nums = [1,2,1,3,2,5]
print(singleNumber(nums))


x = 43
z = x - (x & (x-1)) == x & -x
print(z)