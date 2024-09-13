




def countSetBits1(n): 
    count = 0
    while n: 
        count += 1
        n -= n & ~(n-1)
    return count

def countSetBits(n): 
    count = 0
    while n: 
        count += 1
        n = n & (n-1)
    return count


n = 123
print(bin(n))
print(countSetBits(n))