from math import inf

def sumDigits(num): 
    res = 0
    num = str(num)
    for digit in num: 
        res += int(digit)
    # print(res)
    return res

class Solution:
    def minElement(self, nums: list[int]) -> int:
        res = inf
        for num in nums: 
            res = min(sumDigits(num), res)
        return res


nums = [10,12,13,14]
nums = [999,19,199]
s = Solution()
print(s.minElement(nums))

# for x in ascii_uppercase: 
#     print(x)