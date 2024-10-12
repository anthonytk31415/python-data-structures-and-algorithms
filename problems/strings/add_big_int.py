# take two infinite precision

# 
# 

# 1024
# 436

# positive integer


def getDigitAndRemainder(x, y, remainder): 
    curSum = x, y + remainder
    remainder = curSum // 10
    curSum = str(curSum)[-1]
    return curSum, remainder





def add_big_int(a, b): 

    # a is the smaller string
    a, b = str(a)[::-1], str(b)[::-1]
    if len(a) > len(b): 
        a, b = b, a
    res = ""
    remainder = 0
    # iterate the smaller string until the end. 
    
    for i in range(len(a)):
        # curSum = int(a[i]) + int(b[i]) + remainder
        curSum, r = getDigitAndRemainder(int(a[i]), int(b[i]), remainder)
        remainder = r
        # remainder = curSum //10
        # curSum = str(curSum % 10)
        res += curSum 

            
    # the longer string starts at end len(a) onward 
    for j in range(len(a), len(b)): 
        curSum = int(b[j]) + remainder
        remainder = curSum //10
        curSum = str(curSum % 10)
        res += curSum 

    return res[::-1] 

a = 123
b = 4128
print(add_big_int(a, b))