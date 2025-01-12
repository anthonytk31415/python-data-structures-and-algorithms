from math import sqrt

# key iterations: 
# iterate from 2 to sqrt n + 1 
# if i prime, start from i**2 to n and mark not prime
# time is like less than O(n)

def sieve(n): 
    primes = [True]*(n+1)
    primes[1] = primes[0] = False
    for i in range(2, int(sqrt(n) + 1)): 
        if primes[i]: 
            for j in range(i**2, n+1, i): 
                primes[j] = False
    return primes


primes = sieve(100)
print(primes)