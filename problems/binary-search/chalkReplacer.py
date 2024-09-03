from bisect import bisect_left

def chalkReplacer(chalk: list[int], k: int) -> int:
    bounds = [x-1 for x in chalk]
    
    for i in range(1, len(bounds)): 
        bounds[i] = bounds[i-1] + chalk[i]
    target = k % sum(chalk) 
    res = bisect_left(bounds, target)
    return res


chalk = [5,1,5]
k = 22

chalk = [3,4,1,2]
k = 25
print(chalkReplacer(chalk, k))