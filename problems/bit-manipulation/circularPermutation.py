# https://leetcode.com/problems/circular-permutation-in-binary-representation/description/?envType=problem-list-v2&envId=bit-manipulation
# 1238. Circular Permutation in Binary Representation

# Gray code
# https://cp-algorithms.com/algebra/gray-code.html



class Solution:
    def circularPermutation(self, n: int, start: int) -> list[int]:
        def grayCode(n): 
            return n ^ (n >> 1)
        res = []
        for i in range(2**n): 
            res.append(grayCode(i))
        idx = res.index(start)
        return res[idx:] + res[:idx]


s = Solution()
# print(grayCode(0))
# print(grayCode(1))

print(s.circularPermutation(3, 3))

# n = 3
# max = 2**3 - 1 = 7
# start with max 


# # how od i make sure i dont go over 7
# 1 xxx <-- will always be a bunch of 1's since it's 2*n - 1
# 2 yxx <-- flip the last means its smaller
# 3 yyx <-- flip the 2nd to last
# 4 yyy <-- 
# 5 yxy <-- flip 2nd
# 6 yxx <-- flip 
# 7 yxy <-- flip 1st 
# 8 xyx <-- flip 3rd


# divide and conquer 
# # not it
# 1# 000 
# 2# 001 2: flip 1
# 3# 011 3: flip 2
# 4# 111 4: flip 3
# 5# 101 5: flip 1
# 6# 100 4: flip 2 
# 7# 110 3: flip 3
# 8# 010 2: flip 2

# 1# 0000 
# 2# 0001 2: f1
# 3# 0011 3: f2
# 4# 0111 4: f3
# 5# 1111 5: f4
# 6# 1111 4: f3
# 7# 1011 3: f1
# 8# 1010 2: f2
# 1# 1111 x: f3
# 2# 1011 2: f2
# 3# 1001 3: f1
# 4# 1000 4: f2
# 5# 1010 5: f3
# 6# 1110 4: f4
# 7# 0110 3: f3
# 8# 0010 2: f2




# flip 
# 3 --> 9
# 0000 0001 0011 0111 1111 11111 10111 10011 10001


# you only need to change bits from 0 to n-1, 
# and that means you only shift from 0 to n-1
# len of p is 2^n


# candidates for 4: 

# 111
# 010
# 001

# 011 , 111 , 110, 100, 001 
# 3,    7,    6,    5,   1

# 3,   , 
# 0, 1, 2, 3, 4

# n = 3
