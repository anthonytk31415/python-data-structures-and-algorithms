
# https://leetcode.com/problems/count-of-smaller-numbers-after-self/
# 315. Count of Smaller Numbers After Self



def countSmaller(nums: list[int]) -> list[int]:

    def mergesort(numsF): 
        if len(numsF) <= 1: return numsF
        mid = len(numsF) // 2
        left = mergesort(numsF[:mid])
        right = mergesort(numsF[mid:])
        merge(left, right, numsF)
        return numsF

    def merge(a, b, arr): 
        count, i, j, k = 0, 0, 0, 0
        # arr = [None]*(len(a) + len(b))
        while i < len(a) and j < len(b): 
            if a[i][0] <= b[j][0]: 
                arr[k] = [a[i][0], a[i][1] + count, a[i][2]]            
                i += 1
            else:             
                count += 1
                cur = [b[j][0], b[j][1], b[j][2]]
                arr[k] =  cur         
                j += 1
            k += 1

        while i < len(a): 
            arr[k] = [a[i][0], a[i][1] + count, a[i][2]]       
            i += 1
            k += 1
        while j < len(b): 
            arr[k] = [b[j][0], b[j][1], b[j][2]]            
            j += 1
            k += 1

    numsF = []      # numsF[i] = [num, count, idx]
    for i, num in enumerate(nums):
        numsF.append([num, 0, i])    

    mergesort(numsF)
    numsF.sort(key = lambda x: x[2])
    return [x[1] for x in numsF]



nums = [5,2,6,1]
print(countSmaller(nums))
    