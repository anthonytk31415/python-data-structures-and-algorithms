from collections import Counter, defaultdict
from math import sqrt 

# https://leetcode.com/problems/largest-component-size-by-common-factor/description/
# 952. Largest Component Size by Common Factor

# An interesting union find problem. We decompose each number to its prime factorization. 
# Then create an adjacency list for each prime, where in the list is the num. 
# for each num in the prime list for a given prime p, we union adjacent numbers. 
# At the end, we return the length of the longest parent. 

# Time Complexity: O(n*sqrt(m)log(m)), dominated by the prime factorization of each num. So 
# for each of the num, we have sqrt(m) divisors, each with log(m) recursive calls of the 
# max number m in the worst case 
# Space Complexity: O(nlogm) for n numbers and m prime factors for each number in the worst case

def find(i, parent):
    if i != parent[i]:
        parent[i] = find(parent[i], parent)
    return parent[i]

def union(pu, pv, parent, rank):
    if rank[pu] < rank[pv]:
        pu, pv = pv, pu
    parent[pv] = pu
    rank[pu] += rank[pv]

# keep cutting down n by 
# runs in sqrt(n) log n time
def prime_decomposition(n): 
    for i in range(2, int(sqrt(n) + 1)): 
        if n % i == 0: 
            return prime_decomposition(n//i) | set([i])
    return set([n])

class Solution:
    def largestComponentSize(self, nums):
        n = len(nums)
        parent = [i for i in range(n)]
        rank = [1]*n
        primes = defaultdict(list)
        
        # do prime_decomp on each num. 
        # for each prime, add num to the adj list
        for i, num in enumerate(nums):
            i_prime_decomp = prime_decomposition(num)
            for q in i_prime_decomp: 
                primes[q].append(i)

        # for each i and i + 1 pair of nums in the prime adj list, union the num indices
        for primeList in primes.values():
            for i in range(len(primeList)-1):
                pu, pv = find(primeList[i], parent), find(primeList[i+1], parent)
                if pu != pv: 
                    union(pu, pv, parent, rank)

        # return the length of the largest parent node
        parentLength = Counter([find(i, parent) for i in range(n)])
        return max(parentLength.values())
        
s = Solution()
pset = s.prime_decomposition(24)
print(pset)