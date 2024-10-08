def quicksort(a, p, r):
    if p < r: 
        q = partition(a, p, r)
        quicksort(a, p, q-1)
        quicksort(a, q+1, r)
    return 


def partition(a, p, r):
    pivot = a[r]
    i = p-1
    for j in range(p, r):
        if a[j] < pivot: 
            i+=1 
            a[i], a[j] =  a[j], a[i]
    a[i+1], a[r] = a[r], a[i+1]
    return i + 1

a = [1,4,3,7,5,0,2,6]

quicksort(a,0,7)
print(a)

