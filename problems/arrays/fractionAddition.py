import math

def fractionAddition(expression: str) -> str:
    args = []
    ops = []
    cur = ""
    # consider the first sign of the entry
    # extract args, ops

    for i, c in enumerate(expression): 
        if i == 0: 
            if c == "-": 
                ops.append(c)
            else: 
                cur += c
                ops.append("+")        
        else: 
            if c in ["+", "-"]: 
                args.append(cur)
                ops.append(c)
                cur = ""
            else: 
                cur += c 

    args.append(cur)

    print(args, ops)

    # get num and denom
    numer, denom = [], []
    commonDenom = 1
    for num in args: 
        idxDiv = num.find("/")
        numer.append(int(num[:idxDiv]))
        denom.append(int(num[(idxDiv+1):]))
        commonDenom *= denom[-1]

    updatedNumer = [numer[i]*commonDenom//denom[i] for i in range(len(numer))]
    finalNumer = 0
    for i in range(len(updatedNumer)):
        if ops[i] == "+":
            finalNumer += updatedNumer[i]
        else: 
            finalNumer -= updatedNumer[i]

    gcd = math.gcd(finalNumer, commonDenom)
    finalNumer //= gcd
    commonDenom //= gcd

    return "{}/{}".format(finalNumer, commonDenom)

    # print(args)
    # print(ops)
    print(numer, denom)
    # print(commonDenom, updatedNumer)


expression = "-1/2+1/2"
expression = "-1/2+1/2-1/3"
# expression = "1/3-1/2"
expression = "7/3+5/2-3/10"

print(fractionAddition(expression))

# a = "anthony"
# print(a.find("t"))


a = 26
b = 46
gcd = math.gcd(a, b)
print(gcd)


from itertools import combinations, permutations
x = list(combinations([1,2,3], 2))
# [(1, 2), (1, 3), (2, 3)]

y = list(permutations((1,2,3), 2))
# [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]
print(x)
print(y)