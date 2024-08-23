def mergesort(a):
    if len(a) <= 1: return a
    mid = len(a) // 2
    left = mergesort(a[:mid])
    right = mergesort(a[mid:])
    merge(a, left, right)
    return a

def merge(a, left, right):
    i, j, k = 0, 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]: 
            a[k] = left[i]
            i += 1
        else: 
            a[k] = right[j]
            j += 1
        k += 1
    while i < len(left):
        a[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        a[k] = right[j]
        j += 1
        k += 1

a = [1,4,3,7,5,0,2,6]

mergesort(a)
print(a)

b = "anthony"
c = list(b)
print(c)
print(", ".join(c))