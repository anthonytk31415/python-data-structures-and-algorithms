# bit exercises


# Count the Number of Set Bits:
# Given an integer n, count the number of set bits (1s) in its binary representation.

# solution: x - 1 flips all bits up to the first rightmost set bit. 
def countSetBits(x): 
    count = 0
    while x: 
        count += 1
        x = x & (x-1)
    return count 


# Find the Bitwise AND of All Numbers in a Range:
# Given two integers m and n, find the bitwise AND of all integers in the range [m, n].

# Solution: Find the common prefix, shift, as you go, then shift back
def findBitwiseAndRange(m, n): 
    shift = 0
    while m > n: 
        m >> 1
        n >> 1
        shift += 1
    return m << shift


# Find the Single Non-Duplicate Element:
# Given an array where every element appears exactly twice except for one element that appears only once, find the single non-duplicate element using XOR.

# key property: a ^ a -> 0. 
def findNonDuplicateElement(arr): 
    x = 0
    for num in arr: 
        x ^= num
    return x
 

# Power of Two Check:
# Given an integer n, determine if it is a power of two using bit manipulation.



# Swap Two Numbers Using Bitwise XOR:
# Given two integers a and b, swap their values using XOR operations without using a temporary variable.

# Find the Rightmost Set Bit:
# Given an integer n, find the position of the rightmost set bit (1) in its binary representation.

# Convert Even Bit to 1 and Odd Bit to 0:
# Given an integer n, convert all even-indexed bits to 1 and all odd-indexed bits to 0.

# Number of Bits to Flip to Convert A to B:
# Given two integers a and b, determine the number of bits needed to flip to convert a to b.

# Reverse Bits of a 32-bit Integer:
# Given a 32-bit unsigned integer, reverse its bits.

# Generate All Subsets of a Set Using Bit Masking:

# Given a set of n elements, generate all possible subsets using bit manipulation.


print(1 << 1)

def flips(a, c): 
    if a < c: 
        c, a = a, c            
    n = 0
    print( a, c)
    while a and c: 
        if a & 1 != c & 1: 
            n += 1
        a >>= 1
        c >>= 1
        print(a)
    while a: 
        if a & 1 == 1: 
            n += 1
        a >>= 1
    return n

a = 10
c = 12




# while a: 
#     print(bin(a))
#     a >> 1

print(bin(a))
print(bin(c))
# print(103 >> 1 >> 1 >> 1 >> 1 >> 1 >> 1 >> 1)
print(flips(a, c))