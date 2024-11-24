from math import inf

def success(i, arr):
    n = len(arr)
    if i == 0: 
        return arr[0] <= arr[1]
    elif i == n - 1: 
        return arr[n-2] >= arr[n-1]
    return  arr[i]<= arr[i+1] and arr[i-1] >= arr[i]

def descending(i, arr): 
    n = len(arr)
    if i == 0: 
        return arr[0] >= arr[1]
    elif i == n - 1: 
        return arr[n-2] >= arr[n-1]
    return  arr[i] >= arr[i+1] and arr[i-1] >= arr[i]

def find_local_maxima(arr): 
    n = len(arr)
    left = -1
    right = n
    while right - left > 1: 
        mid = (left + right) // 2
        if success(mid, arr): return mid
        elif descending(mid, arr): 
            left = mid
        else: 
            right = mid

    return right
    
arr = [10,23,17,20,1,2,3,4,-3,5]

print(find_local_maxima(arr))