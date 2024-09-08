


def maxPossibleScore(start: list[int], d: int) -> int:
    start.sort()
    startD = [x + d for x in start]
    low = start[0]
    high = startD[-1] + 1

    def condition(mid): 
        cur = start[0]
        for i in range(1, len(start)):
            # print(cur + mid, start[i], startD[i])
            if start[i] <= cur + mid <= startD[i]: 
                cur += mid
            elif cur + mid > startD[i]: return False
            else:
                # print("entering this")
                check = False
                for x in range(start[i], startD[i] + 1): 
                    if x - cur >= mid: 
                        check = True 
                        break                    
                if not check: return False
                cur = x
        return True

    print(low, high)
    print(start)
    print(startD)

    while low < high : 
        mid = (high + low)// 2
        # print("low {}, mid {}, high {}".format(low, mid, high))
        if condition(mid): 
            low = mid + 1
            print(mid, "getting low")
        else: 
            print(mid, "getting high")
            high = mid
    return low - 1

start = [0, 10, 1,2,3]
d = 10
# 4

# start = [6,0,3]
# d = 2
# 4

# start = [1000000000,0]
# d = 1000000000

# start = [1000000000,1000000000]
# d = 1000000000

# start = [2,6,13,13]
# d = 5

# start = [6,0,3]
# d = 2


print(maxPossibleScore(start, d))
