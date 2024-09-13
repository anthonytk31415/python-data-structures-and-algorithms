
# https://leetcode.com/problems/minimum-bit-flips-to-convert-number/
# 2220. Minimum Bit Flips to Convert Number


# try doing this with bit manipulation!
x = 209
print(bin(x & 0xFFFFFFFF))


x = 1076
print(bin(x & 0xFFFFFFFF))


def binary1(x, y): 
    if y > x:       # x >= y always 
        y, x = x, y
    binX =bin(x)[2:]
    binY= bin(y)[2:]
    while len(binY) < len(binX): 
        binY = "0" + binY

    count = 0
    for i in range(len(binX)): 
        if binX[i] != binY[i]: count += 1
    # print(binX)
    # print(binY)
    return count

def binary(x, y): 
    if y > x:       # x >= y always 
        y, x = x, y
    # binX =bin(x)[2:]
    # binY= bin(y)[2:]
    # print(binX)
    # print(binY)
    count = 0
    while x and y: 
        if x & 1 != y & 1: 
            # print(bin(x), bin(y))
            count += 1
        x >>= 1
        y >>= 1

    while x: 
        if x & 1 == 1: 
            # print(bin(x))
            count += 1
        x >>= 1

    return count


# x = 31
# print(bin(x))
# x = x >> 1
# print(bin(x))



print(binary(10, 3))
# print(binary(3, 4))