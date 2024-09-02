## AND (&) OR (|) NOT (~) XOR (^)

# # ~x is -x - 1
# x = 156
# y = 18
# print("bit of x: {}, y: {}".format(bin(x), bin(y)))
# # print("x & y: ", bin(x&y))
# # print("x | y: ", bin(x |  y))
# print("not x: ", bin(~x))

# print(bin(-x-1))
# print(~x)
# print(~y)
# print("bit of not y: ", bin(~y))
# # print(bin(-y-1))

# # this is equivaent
# print(1 << y.bit_length(), 2**y.bit_length())

# # dshould this give actually the not y i.e. the bits inverted? 
# print("flip the switch: ", bin(~y & (2**y.bit_length() - 1)))

# print(y.bit_length())
# # why does this work? 2** bit length - 1 
# print(bin(2**y.bit_length() - 1))


# for NOT, you need to do ~x & 

def pb(n):
    print(bin(n))

# z = 5
# pb(z)
# pb(~z)
# bitmask = (1 << z.bit_length() )- 1
# pb(bitmask)
# pb(~z & bitmask)

# remember that ~x in python is really: 
# ~x & (1 << maxBits - 1)

# Why: in normal ~x, we just do bit flipping. But with python and most computers, which represent integers 
# as two's complement, to do the conversion from ~x in twos complement to 


# You must treat the NOT operation and flipping bits opreation differently. 


# Flip bits: ~x & (1 << max bits - 1)
# NOT: ~x, which flips bits in twos complement. So ~5 = -6 
# ~x = -x -1 

# z = 14
# pb(z)
# w = 1 << 2
# wComp = (~w) & ((1 << 8) - 1)
# pb(w)
# pb(wComp)
# pb(z & wComp)


# pb(5)
# pb(~5)


# Check if a bit is set: 
# y = 2
# pb((y >> 2 )& 1)


# is divisible by a power of two
# x & y == 0 where y = 1 << power of 2 - 1
# 12
# 4 ==> 2
# x = 12
# pTwo = 1 << 2
# pb(x & (pTwo - 1))
# pb(pTwo)


# 

# flip the xth bit
x = 3
a = 314
pb(a)