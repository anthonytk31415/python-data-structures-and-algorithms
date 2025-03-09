import math
# https://leetcode.com/problems/closest-prime-numbers-in-range/solutions/?envType=daily-question&envId=2025-03-08
# 2523. Closest Prime Numbers in Range

# Sieve of Eratosthenes and pairs
# O(nlog(logn)) time, O(n) space for primes storage

def find_primes(start, n): 
    primes = [True for _ in range(n + 1)]    
    primes[0] = primes[1] = False
    for i in range(2, math.ceil(math.sqrt(n))+1): 
        if primes[i] == True:             
            for j in range(i +i, len(primes), i): 
                primes[j] = False           
    return [i for i in range(start, len(primes)) if primes[i]]

def dist(i, primes):
    return primes[i] - primes[i-1]

class Solution:
    def closestPrimes(self, left: int, right: int) -> list[int]:
        primes = find_primes(left, right)
        min_pair = [-1, -1]
        min_dist = math.inf
        for i in range(len(primes) - 1, 0, -1): 
            cur_dist = dist(i, primes)
            if cur_dist <= min_dist:     
                min_dist = cur_dist
                min_pair = [primes[i-1], primes[i]]
        return min_pair
            

s = Solution()
# print(s.closestPrimes(10, 19))
# print(s.closestPrimes(4, 6))

# print(find_primes(10, 29))
print(find_primes(21, 25))
# print(s.closestPrimes(8, 11))