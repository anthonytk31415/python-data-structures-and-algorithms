
def f(x): 
    return x > 5
 
# Return the index of the earliest occurrence of when arr
# Invariant: 
#   f(left) = 0
#   f(right) = 1
#   right will be the first time f(x) = 1 
# - instantiate left and right outside the bounds of arr,  
# i.e. (-1 and n, respectively). 
# -1 and n never gets evaluated directly. 
# Key assumption: for arr, it's sorted in such a way that : 
# f(0) = 0, f(1) = 0, .... f(k-1) = 0, f(k) = 1, f(k+1) = 1, ...
# so we can then binary search the transition point k. 
def binary_search(arr): 
    n = len(arr)
    left = -1
    right = n
    while right - left > 1:         # right and left have to be 1 at least apart
        mid = (left + right)//2
        if f(mid): 
            right = mid    
        else: 
            left = mid
    return right


arr = [0,1,2,3,4,5,6,7]

print("binSearch answer: ", binary_search(arr))