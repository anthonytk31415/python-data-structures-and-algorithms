
def f(x): 
    return x > 5
 
# return the index of the earliest occurrance of when arr
# Invariant: 
# f(left) = 0
# f(right) = 1
# right will be 
# - instantiate left and right outside the boudns of arr. It never 
# gets evaluated directly
def binary_search(arr): 
    n = len(arr)
    left = -1
    right = n
    while right - left > 1:             # 
        mid = (left + right)//2
        if f(mid): 
            right = mid    
        else: 
            left = mid
    return right


arr = [0,1,2,3,4,5,6,7]

print("binSearch answer: ", binary_search(arr))