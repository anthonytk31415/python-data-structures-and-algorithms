def rabin_karp(T, P): 
    n, m = len(T), len(P)
    if m > n: return 
    
    B = 256
    M = 10**9 + 7
    
    power = 1
    for i in range(1, m): 
        power = (power * B) % M
    
    hashP, hashT = 0, 0
    for i in range(m): 
        hashP = (hashP * B + ord(P[i])) % M
        hashT = (hashT * B + ord(T[i])) % M
    
    for i in range(n - m + 1): 
        if hashT == hashP: 
            if T[i: (i + m)] == P: 
                return i
        if i < n - m: 
            left_val = (ord(T[i])*power) % M
            hashT = (hashT - left_val ) % M
            if hashT < 0:
                hashT += M
            hashT = (hashT * B + ord(T[i+m])) % M
    
    return -1

T = "abacab"
P = "cab"

# print(rabin_karp(T, P))

T = "mississippi"
P = "ippi"
print(rabin_karp(T, P))
