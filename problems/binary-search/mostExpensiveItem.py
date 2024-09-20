from math import inf 
# https://leetcode.com/problems/most-expensive-item-that-can-not-be-bought/description/?envType=company&envId=amazon&favoriteSlug=amazon-six-months
# 2979. Most Expensive Item That Can Not Be Bought


# ridiculous solution math problem
class Solution:
    def mostExpensiveItem(self, primeOne: int, primeTwo: int) -> int:
        return primeOne*primeTwo - primeOne - primeTwo

# a dp solution; can you recreate this? 
class Solution:
    def mostExpensiveItem(self, primeOne: int, primeTwo: int) -> int:
        j = primeOne * primeTwo

        dp = [False] * j
        dp[primeOne] = True
        dp[primeTwo] = True

        for i in range(j):
            dp[i] = dp[i] or dp[i - primeOne] or dp[i - primeTwo]
        
        for k in range(j - 1, -1, -1):
            if not dp[k]:
                return k
        
        return j - primeOne - primeTwo



# a sieve-like solution, but too slow. 
def crossOut(start, arr, p1, p2): 
    # print("crossout on {}".format(start))
    if not start or start % p1 != 0: 
        for i in range(0, len(arr)): 
            idx = start + p1*i
            if idx < len(arr): 
                arr[idx] = 0                 
            else:                     
                break 
    if not start or start % p2 != 0: 
        for i in range(0, len(arr)): 
            idx = start + p2*i
            if idx < len(arr):
                arr[idx] = 0                 
            else:                     
                break 

class Solution:
    def mostExpensiveItem(self, p1: int, p2: int) -> int:
        if p2 < p1: 
            p1, p2 = p2, p1
        arr = [1] * (p1*p2 + 1)
        crossOut(0, arr, p1, p2)
        for i in range(p1 - 1, len(arr)): 
            if arr[i] == 1 : continue
            crossOut(i, arr, p1, p2)
        maxI = 1
        for i, num in enumerate(arr): 
            if num == 1: 
                maxI = max(i, maxI)
        return maxI




class Solution1:
    def mostExpensiveItem(self, p1: int, p2: int) -> int:
        # create a bit the 0th bit represents 0, 1th bit is 1, etc.
        # p1 * p2 + 1 bits 
        maxLength = p1*p2 + 1
        x = (1 << maxLength) - 1        
        # print("starting x: ", bin(x))
        for i in range(0, p1*p2 + 1): 
            y = p1*i
            if y <= maxLength: 
                x = x & ~(1<<y)                 
            else:                     
                break 
        # find the largest set bit and return it
        for i in range(0, p1*p2 + 1): 
            y = p2*i
            if y <= maxLength: 
                x = x & ~(1<<y)                 
            else:                     
                break 
        # print("bin x after p1 and p2 applied: ", bin(x))
        i = 1
        iNum = 1<<i
        # z = x
        # print(bin(iNum))

        while i < maxLength:
            # print("starting x: ", bin(x))
            # seenOne = False 
            # print("i: ", i, bin(x << i))

            # find the next cleared bit
            while x & iNum != 0: 
                iNum <<=1
                i += 1
            # then do the & logic 
            # print("i       :", i)
            # print("bin x   : ", bin(x))
            # print("bin iNum: ", bin(iNum))
            y = x
            for _ in range(i): 
                y <<=1
                y += 1
            
            x = x & y
            # print("x: ", bin(x))
            # print("y: ", bin(y))
            # find the next one
            i += 1
            iNum <<= 1
        # return the number represented by most significant set bit
        # print("bit length of x: ", x.bit_length())
        # print("final x: ", bin(x))
        return x.bit_length() - 1
# 0b11111111111 

p1, p2 = 2, 5
p1, p2 = 3,5 
# p1, p2 = 5,7
# p1, p2 = 2,1871
# p1, p2 = 3, 1613
p1, p2 = 41, 239 # 9519
s = Solution()
print(s.mostExpensiveItem(p1, p2))

# x:    0b1000001010
# y:  0b101000101011


#    0b1000001010
# 0b1000001010111
