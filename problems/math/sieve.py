from math import sqrt
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