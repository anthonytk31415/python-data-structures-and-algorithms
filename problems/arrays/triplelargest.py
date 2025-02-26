from math import inf 

# Prob from APS class
# Interesting trick wiht swapping; a bit tedious
# linear time for Time and Constant Time for space. 

def triple(nums): 
    x = y = a = b = c = None
    res = -inf
    for num in nums: 
        small = big = num
        if (a == None or big > a): 
            big, a = a, big
        if big != None and (b == None or big > b): 
            big, b = b, big
        if big != None and (c == None or big > c): 
            big, c = c, big

        if (x == None or small < x): 
            small, x = x, small
        if small != None and (y == None or small < y): 
            small, y = y, small

    res = max(res, max(a*b*c, a*x*y))    
    return res


def triple(nums): 
    minNums = [None, None]
    maxNums = [None, None, None]
    res = -inf
    for num in nums: 
        if (maxNums[2] == None or num > maxNums[2]): maxNums = maxNums[1:] + [num]
        elif (maxNums[1] == None or num > maxNums[1]): maxNums = [maxNums[1], num,  maxNums[2]]
        elif (maxNums[0] == None or num > maxNums[0]): maxNums = [num] + maxNums[1:]

        if (minNums[1] == None or num < minNums[1]): minNums = minNums[1:] + [num]
        elif (minNums[0] == None or num < minNums[0]): minNums = [num, minNums[1]] 
    
    c, b, a = maxNums
    y, x = minNums
    res = max(res, max(a*b*c, a*x*y))    
    return res



nums = [-1, -2, 3] # 6
nums = [9,1,3,2,10,2, -100, -100] # 100000
nums = [-1, -3, -1, 1] # 3
# nums = [1000, 1000, 1000, 1000] # 1000000000
# nums = [-1000, -100, -10, -1] # -1000

print(triple(nums))


